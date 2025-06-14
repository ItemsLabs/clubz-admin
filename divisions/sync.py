import json
import os
from urllib import request
import uuid
from datetime import timedelta
from typing import Dict, Any

from celery import shared_task
from django.utils import timezone
from django.db import transaction, connection

from core.models import AppInbox, GameWeek, MatchLeaderboard, Rewards, UserGameWeekHistory, Division, CustomUser, UserDivision, \
    Transactions, DivisionReward, Game, Match, GameWeekDivision, AssignedCardPack
from core.notifications import send_push_to_users
from .simulation import OrToolsDistributionStrategy, User, Division as SDivision

from django.db.models import Sum, Case, When, Value, IntegerField, Window, F, Q
from django.db.models.functions import Rank
from web3 import Web3
from blockchain_web3.services import CryptoTransactionService

DB_FMT = '%Y-%m-%d %H:%M:%SZ'

def check_and_finish_week(week):
    if not week.already_ended or week.status == GameWeek.FINISHED:
        return

    week.status = GameWeek.FINISHED
    week.save(update_fields=['status'])


def get_season_users(week):
    season_s = week.season.start_at.strftime('%Y-%m-%d %H:%M:%SZ')
    season_e = week.season.end_at.strftime('%Y-%m-%d %H:%M:%SZ')

    users_with_games = (CustomUser.objects
                        .filter(
        Q(matchleaderboard__match__match_time__gte=season_s) & Q(matchleaderboard__match__match_end__lte=season_e))
                        .distinct('id')
                        .prefetch_related('divisions'))

    users = []
    for user in users_with_games:
        division = user.last_division()
        division_tier = division.tier if division else None
        division_id = division.id if division else None
        verified = user.email_verified
        users.append(User(id=user.id, division_id=division_id, division_tier=division_tier, verified=verified))

    return users


def get_global_leaderboards_without_divisions(week):
    query = """
    with all_week_matches as (
        select ml.user_id,
               ml.score,
               row_number() over(partition by ml.user_id order by ml.score desc nulls last) as match_rank
          from match_leaderboard ml
         where ml.match_id in (
               select id 
                 from matches
                where match_time >= %s and match_time <= %s
               )
    ),
    top_week_matches as (
        select *
          from all_week_matches
         where match_rank <= 5
    ),
    season_users as (
        select u.id as user_id
          from users u
         where exists(
               select null
                 from match_leaderboard ml,
                      matches m
                where ml.match_id = m.id
                  and ml.user_id = u.id
                  and m.match_time >= %s and m.match_time <= %s
               )
    )
    select su.user_id,
           sum(coalesce(rm.score,0)) total_score
      from season_users su
      left join top_week_matches rm on su.user_id=rm.user_id
     group by su.user_id
     order by total_score desc
    """

    season_start = week.season.start_at.strftime(DB_FMT)
    season_end = week.season.end_at.strftime(DB_FMT)
    week_start = week.start_at.strftime(DB_FMT)
    week_end = week.end_at.strftime(DB_FMT)

    with connection.cursor() as cursor:
        cursor.execute(query, [week_start, week_end, season_start, season_end])
        leaderboard = dict(cursor.fetchall())

    return leaderboard


def get_divisions():
    divisions_from_db = Division.objects.all().order_by('-tier')
    divisions = []
    for division in divisions_from_db:
        divisions.append(SDivision(id=division.id, tier=division.tier, percentage=division.percentage))
    return divisions


def get_leaderboards_with_divisions(week):
    result = {}
    season_start = week.season.start_at.strftime(DB_FMT)
    season_end = week.season.end_at.strftime(DB_FMT)
    week_start = week.start_at.strftime(DB_FMT)
    week_end = week.end_at.strftime(DB_FMT)

    params = [week_start, week_end, season_start, season_end]
    query = '''
with latest_user_divisions AS (
    select user_id,
           division_id
      from (
        select ud.user_id,
               ud.division_id,
               ROW_NUMBER() OVER (PARTITION BY ud.user_id ORDER BY ud.join_date DESC) AS rn
          from user_divisions ud
      ) t
     where t.rn = 1
),
all_week_matches as (
    select ml.user_id,
           ml.score,
           ml.position,
           row_number() over(partition by ml.user_id order by ml.score desc nulls last) as match_rank
      from match_leaderboard ml
     where ml.match_id in (
           select id 
             from matches
            where match_time >= %s and match_time <= %s
           )
),
top_week_matches as (
    select *
      from all_week_matches
     where match_rank <= 5
),
season_users as (
    select u.id as user_id
      from users u
     where exists(
           select null
             from match_leaderboard ml,
                  matches m
            where ml.match_id = m.id
              and ml.user_id = u.id
              and m.match_time >= %s and m.match_time <= %s
           )
),
ranked_leaderboard as (
    select season_users.user_id,
           divisions.id as division_id,
           coalesce(divisions.tier, 0) as division_tier,
           sum(coalesce(top_week_matches.score,0)) total_score
      from season_users
      left join top_week_matches on top_week_matches.user_id = season_users.user_id
      left join latest_user_divisions on latest_user_divisions.user_id = season_users.user_id
      left join divisions on divisions.id = latest_user_divisions.division_id
     group by season_users.user_id,
              divisions.id,
              divisions.tier
     order by divisions.tier nulls last,
              total_score desc
)
select user_id,
       total_score,
       RANK() OVER (PARTITION BY division_tier ORDER BY total_score DESC nulls last) AS rank,
       division_tier,
       division_id,
       (select avg(t.position)
          from all_week_matches t
         where t.user_id = ranked_leaderboard.user_id
       ) as week_average_rank,
       (select count(*)
          from all_week_matches t
         where t.user_id = ranked_leaderboard.user_id
       ) as week_matches_played
  from ranked_leaderboard;
    '''

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        returned_result = cursor.fetchall()

    for entry in returned_result:
        d_tier = entry[3]
        if d_tier is None or d_tier == 0:
            d_tier = 'genesis'
        if entry[0] not in result:
            result[entry[0]] = {}
        user_data = {
            'division_tier': d_tier,
            'total_score': entry[1],
            'rank': entry[2],
            'week_average_rank': entry[5],
            'week_matches_played': entry[6],
        }
        result[entry[0]] = user_data

    return result


def get_division_ranges():
    divisions = Division.objects.all()

    relegation_ranges = {
        division.tier: (division.relegation_min_range, division.relegation_max_range)
        for division in divisions
    }

    promotion_ranges = {
        division.tier: (division.promotion_min_range, division.promotion_max_range)
        for division in divisions
    }

    return relegation_ranges, promotion_ranges


def distribute_players(week):
    leaderboards = get_global_leaderboards_without_divisions(week)  # {user_uuid: score_int}
    divisions = get_divisions()
    relegation_ranges, promotion_ranges = get_division_ranges()
    print(f"relegation_ranges: {relegation_ranges}, promotion_ranges: {promotion_ranges}")
    users_with_games = get_season_users(week)
    distribution_service = OrToolsDistributionStrategy(divisions, relegation_ranges, promotion_ranges, True)
    distribution_data = distribution_service.distribute(users_with_games, leaderboards,week)

    def division_cache():
        cache = {}
        divs = Division.objects.all()

        for division in divs:
            cache[division.tier] = division.id

        return cache

    def update_dict_of_users(data: Dict[uuid.UUID, Dict[str, Any]]):
        cache = division_cache()

        leaderboard = get_leaderboards_with_divisions(week)
        for user_id, user_info in data.items():
            data[user_id]['week_division_id'] = cache[user_info['week_division_tier']] if user_info[
                                                                                              'week_division_tier'] is not None else None
            data[user_id]['new_division_id'] = cache[user_info['new_division_tier']] if user_info[
                                                                                            'new_division_tier'] is not None else None
            data[user_id]['position'] = leaderboard[user_id]['rank']  # Update position from leaderboard
            data[user_id]['week_matches_played'] = leaderboard[user_id]['week_matches_played']
            data[user_id]['week_average_rank'] = leaderboard[user_id]['week_average_rank']
            print(
                f"user_id: {user_id}, old_division: {user_info['week_division_tier']}, new_division: {user_info['new_division_tier']}, points: {user_info['points']}, position: {user_info['position']}"
            )
        return data

    return update_dict_of_users(distribution_data)


def set_concluded_status(week):
    week.status = GameWeek.CLOSED
    week.scored_at = timezone.now()
    week.save(update_fields=['status', 'scored_at'])


def create_history_data(week, distributed_players):
    for user_id, user_data in distributed_players.items():
        UserGameWeekHistory.objects.create(
            user_id=user_id,
            game_week=week,
            week_division_id=user_data['week_division_id'],
            week_division_position=user_data['position'],
            week_division_tier=user_data['week_division_tier'],
            week_points=user_data['points'],
            week_coins=user_data['coins'],
            week_matches_played=user_data['week_matches_played'],
            week_average_rank=user_data['week_average_rank'],

            # store results of promoted/safe/relegated/ from finished week to new week
            new_division_id=user_data['new_division_id'],
            new_division_tier=user_data['new_division_tier'],
            status=user_data['division_status'],

        )


def create_new_week(week):
    start_at = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end_at = start_at + timedelta(days=6, hours=23, minutes=59, seconds=59)

    season_start_at = week.season.start_at
    season_end_at = week.season.end_at

    # Check if the new week falls outside the season's start and end dates
    if season_start_at is None or season_end_at is None:
        # Handle cases where the season's start or end dates are not set
        return None

    if start_at < season_start_at or end_at > season_end_at:
        return None

    game_week = GameWeek.objects.create(
        name=f"Week of {start_at.strftime('%Y-%m-%d')} - {end_at.strftime('%Y-%m-%d')}",
        start_at=start_at,
        end_at=end_at,
        status=GameWeek.LIVE,
        season=week.season
    )
    return game_week


def assign_user_to_division(distribution_data, new_game_week_id):
    new_user_divisions = []

    for user_id, user_info in distribution_data.items():
        user_division = UserDivision(
            user_id=user_id,
            division_id=user_info['new_division_id'],
            game_week_id=new_game_week_id,

        )
        new_user_divisions.append(user_division)

    UserDivision.objects.bulk_create(new_user_divisions)


def calculate_rewards(division_rewards, players: Dict[uuid.UUID, Dict[str, Any]]):
    result = []

    def binary_search(ranges, target):
        left, right = 0, len(ranges) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if ranges[mid].min_position <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right  # return high index

    def find_rewards(position, division_id):
        division_rewards_list = [r for r in division_rewards if r.division_id == division_id]
        division_rewards_list.sort(key=lambda r: r.min_position)
        idx = binary_search(division_rewards_list, position)
        if idx >= 0:
            r = division_rewards_list[idx]
            if not r.max_position or position <= r.max_position:
                return {
                    'virtual': r.reward.credits,
                    'game': r.reward.game_token,
                    'lapt': r.reward.lapt_token,
                    'tickets': r.reward.event_tickets,
                    'balls': r.reward.ball,
                    'signed_balls': r.reward.signed_ball,
                    'shirts': r.reward.shirt,
                    'signed_shirts': r.reward.signed_shirt,
                    'kickoff_pack_1': r.reward.kickoff_pack_1,
                    'kickoff_pack_2': r.reward.kickoff_pack_2,
                    'kickoff_pack_3': r.reward.kickoff_pack_3,
                    'season_pack_1': r.reward.season_pack_1,
                    'season_pack_2': r.reward.season_pack_2,
                    'season_pack_3': r.reward.season_pack_3,
                }
        return {
            'virtual': 0,
            'game': 0,
            'lapt': 0,
            'tickets': 0,
            'balls': 0,
            'signed_balls': 0,
            'shirts': 0,
            'signed_shirts': 0,
            'kickoff_pack_1': 0,
            'kickoff_pack_2': 0,
            'kickoff_pack_3': 0,
            'season_pack_1': 0,
            'season_pack_2': 0,
            'season_pack_3': 0,
        }

    for player_id, player in players.items():
        rewards = find_rewards(player['position'], player['week_division_id'])
        player['coins'] = rewards['virtual']
        player['game'] = rewards['game']
        player['lapt'] = rewards['lapt']
        player['tickets'] = rewards['tickets']
        player['balls'] = rewards['balls']
        player['signed_balls'] = rewards['signed_balls']
        player['shirts'] = rewards['shirts']
        player['signed_shirts'] = rewards['signed_shirts']
        player['kickoff_pack_1'] = rewards['kickoff_pack_1']
        player['kickoff_pack_2'] = rewards['kickoff_pack_2']
        player['kickoff_pack_3'] = rewards['kickoff_pack_3']
        player['season_pack_1'] = rewards['season_pack_1']
        player['season_pack_2'] = rewards['season_pack_2']
        player['season_pack_3'] = rewards['season_pack_3']
        result.append(
            {
                'user_id': player_id,
                **rewards,
                'position': player['position'],
                'division_id': player['week_division_id']
            }
        )

    return result, players


def process_week_rewards(week, players: Dict[uuid.UUID, Dict[str, Any]]):
    if week.status == GameWeek.FINISHED:
        division_rewards = DivisionReward.objects.filter(week_id=week.id).select_related('reward')

        user_rewards, players = calculate_rewards(division_rewards, players)

        transactions = []
        reward_inboxes = []
        
        for r in user_rewards:
            user = CustomUser.objects.get(id=r['user_id'])
            # Check for virtual currency rewards (credits)
            if r['virtual'] > 0:
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    amount=r['virtual'],
                    text=f"Virtual reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.VIRTUAL,
                    delivered=True
                ))
            # Check for game token rewards
            if r['game'] > 0:
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    amount=r['game'],
                    text=f"GAME reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.GAME,
                    delivered=False
                ))
            # Check for LAPT token rewards
            if r['lapt'] > 0:
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    amount=r['lapt'],
                    text=f"LAPT reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.LAPT,
                    delivered=False
                ))
            # Check for event tickets rewards
            if r['tickets'] > 0:
                reward = Rewards(event_tickets=r['tickets'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['tickets'],
                    text=f"Event tickets reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.EVENT_TICKET,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['tickets']} Event Tickets",
                    description=f"Congratulations! You have received {r['tickets']} Event Tickets for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Tickets.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['tickets']} Event Tickets for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )

                # Send the Slack alert
                send_slack_alert(slack_message)            # Check for ball rewards
            if r['balls'] > 0:
                reward = Rewards(balls=r['balls'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['balls'],
                    text=f"Ball reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.BALL,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['balls']} Balls",
                    description=f"Congratulations! You have received {r['balls']} Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Frame.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['balls']} Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message) 
            # Check for signed ball rewards
            if r['signed_balls'] > 0:
                reward = Rewards(signed_balls=r['signed_balls'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['signed_balls'],
                    text=f"Signed Ball reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.SIGNED_BALL,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['signed_balls']} Signed Balls",
                    description=f"Congratulations! You have received {r['signed_balls']} Signed Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Frame.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['signed_balls']} Signed Balls for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message) 
            # Check for shirt rewards
            if r['shirts'] > 0:
                reward = Rewards(shirts=r['shirts'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['shirts'],
                    text=f"Shirt reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.SHIRT,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['shirts']} Shirts",
                    description=f"Congratulations! You have received {r['shirts']} Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    category='claim_prize',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Shirt.png",
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['shirts']} Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message)
            # Check for signed shirt rewards
            if r['signed_shirts'] > 0:
                reward = Rewards(signed_shirts=r['signed_shirts'])
                reward.save()  # Save individual reward
                transactions.append(Transactions(
                    user_id=r['user_id'],
                    quantity=r['signed_shirts'],
                    text=f"Signed Shirt reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                    week_id=week.id,
                    object_type=Transactions.SIGNED_SHIRT,
                    delivered=False
                ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['signed_shirts']} Signed Shirts",
                    description=f"Congratulations! You have received {r['signed_shirts']} Signed Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.digitaloceanspaces.com/notification-icons/Shirt.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                slack_message = (
                    f"User ID: {r['user_id']}\n"
                    f"Name: {user['name']}\n"
                    f"Email: {user['email']}\n"
                    f"Real Name: {user['real_name']}\n"
                    f"Has earned {r['signed_shirts']} Signed Shirts for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard."
                )
                send_slack_alert(slack_message)
            # Check for kickoff pack rewards
            if r['season_pack_1'] > 0:
                reward = Rewards(season_pack_1=r['season_pack_1'])
                reward.save()  # Save individual reward
                for i in range(r['season_pack_1']):
                    transactions.append(Transactions(
                        user_id=r['user_id'],
                        quantity=1,
                        text=f"Card pack reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                        week_id=week.id,
                        object_type=Transactions.SEASON_PACK_1,
                        delivered=False
                    ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['season_pack_1']} Card Packs",
                    description=f"Congratulations! You have received {r['season_pack_1']} Card Packs for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.cdn.digitaloceanspaces.com/notification-icons/Packs.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))

            if r['season_pack_2'] > 0:
                reward = Rewards(season_pack_2=r['season_pack_2'])
                reward.save()  # Save individual reward
                for i in range(r['season_pack_2']):
                    transactions.append(Transactions(
                        user_id=r['user_id'],
                        quantity=1,
                        text=f"Card pack reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                        week_id=week.id,
                        object_type=Transactions.SEASON_PACK_2,
                        delivered=False
                    ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['season_pack_2']} Card Packs",
                    description=f"Congratulations! You have received {r['season_pack_2']} Card Packs for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.cdn.digitaloceanspaces.com/notification-icons/Packs.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))
                
            if r['season_pack_3'] > 0:
                reward = Rewards(season_pack_3=r['season_pack_3'])
                reward.save()  # Save individual reward
                for i in range(r['season_pack_3']):
                    transactions.append(Transactions(
                        user_id=r['user_id'],
                        quantity=1,
                        text=f"Card pack reward for {r['position']} position in {players[r['user_id']]['week_division_tier']} division leaderboard",
                        week_id=week.id,
                        object_type=Transactions.SEASON_PACK_3,
                        delivered=False
                    ))
                reward_inboxes.append(AppInbox(
                    user_id=r['user_id'],
                    title=f"You earned {r['season_pack_3']} Card Packs",
                    description=f"Congratulations! You have received {r['season_pack_3']} Card Packs for securing {r['position']} position in the {players[r['user_id']]['week_division_tier']} division leaderboard.",
                    status='Active',
                    priority='High',
                    image_url="https://laliga.ams3.cdn.digitaloceanspaces.com/notification-icons/Packs.png",
                    category='claim_prize',
                    created_at=timezone.now(),
                    updated_at=timezone.now(),
                    read=False,
                    claimed=False,
                    game_week_id=week,
                    clear=False,
                    reward_id=reward.id
                ))

        # After processing, bulk create the transactions and inbox entries
        Transactions.objects.bulk_create(transactions)
        AppInbox.objects.bulk_create(reward_inboxes)

        return players


@shared_task
def conclude_game_week(week):
    if week.season:
        with transaction.atomic():
            # Step 1: Check and finish the current game week
            check_and_finish_week(week)
            # Step 2: Distribute players based on their performance
            distributed_players = distribute_players(week)
            if distributed_players:
                # Step 3: Process rewards for the distributed players
                modified_distributed_players = process_week_rewards(week, distributed_players)
            else:
                modified_distributed_players = None
            # Step 4: Set the current game week's status to 'concluded'
            set_concluded_status(week)
            # Step 5: Create a new game week
            new_week = create_new_week(week)
            if modified_distributed_players:
                # Step 6: Assign users to their new divisions for the new week
                assign_user_to_division(modified_distributed_players, new_week.id)
                # Step 7: Create history data for the concluded game week
                create_history_data(week, modified_distributed_players)
            # Step 8: Recalculate new week
            calculate_promotion_and_relegation(new_week)

    # Notify players that the week has been concluded
    if modified_distributed_players:
        send_push_to_users.delay(list(modified_distributed_players.keys()), week.id)
    return modified_distributed_players


@shared_task
def calculate_promotion_and_relegation(week):
    divisions = get_divisions()
    relegation_ranges, promotion_ranges = get_division_ranges()
    users_with_games = get_season_users(week)
    division_population = {}
    for user in users_with_games:
        if user.division_id is None:
            continue
        if user.division_id not in division_population:
            division_population[user.division_id] = 0
        division_population[user.division_id] += 1

    distribution_service = OrToolsDistributionStrategy(divisions, relegation_ranges, promotion_ranges, True)
    distribution_data = distribution_service.calculate_capacity(division_population)

    for div_id, data in distribution_data.items():
        GameWeekDivision.objects.get_or_create(week=week, division_id=div_id, defaults={
            'capacity': data.capacity,
            'promotion_count': data.promotion_count,
            'relegation_count': data.relegation_count,
        })

# Slack webhook URL
slack_webhook_url = 'https://hooks.slack.com/services/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'

def send_slack_alert(message):
    payload = {
        "text": message  # Message that will be sent to the Slack channel
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = request.post(slack_webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request to Slack returned error {response.status_code}, the response is:\n{response.text}")
