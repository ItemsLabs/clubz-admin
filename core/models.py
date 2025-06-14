import math
import os
import traceback
import uuid
from datetime import timedelta
from functools import lru_cache
from math import floor, ceil
from typing import Optional

from django.conf import settings
from django.db import models, transaction, connection, IntegrityError
from django.db.models import DO_NOTHING, Q
from django.utils import timezone
from django.db.models import Avg
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.serializers.json import DjangoJSONEncoder

from core import const
from core.const import TIER_CHOICES, TIER_NONE
from util.calc import get_rank_dict

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImportModel(BaseModel):
    import_id = models.CharField(unique=True, null=True, max_length=15)

    class Meta:
        abstract = True


class V2ImportModel(BaseModel):
    import_id = models.CharField(unique=True, null=True, max_length=128)

    class Meta:
        abstract = True


class CustomUser(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=True, blank=True)
    password_hash = models.TextField(null=True, blank=True)
    email_verified = models.BooleanField(null=False, default=False)
    token_expiration = models.DateTimeField(null=True, blank=True)
    verification_token = models.CharField(null=True, blank=True, max_length=100)
    name = models.CharField(max_length=255, unique=True)
    firebase_id = models.CharField(max_length=50, null=True, blank=True)
    avatar_url = models.TextField(null=True, blank=True)
    balance = models.FloatField(default=0)
    paypal_email = models.CharField(null=True, blank=True, max_length=255)
    verified = models.BooleanField(null=False, default=False)
    referral_code = models.CharField(null=True, blank=True, max_length=10, unique=True)
    referrer = models.ForeignKey('CustomUser', null=True, on_delete=DO_NOTHING, blank=True)
    referral_bonus_used = models.BooleanField(null=True, blank=True, default=False)
    bonus_powerups = models.IntegerField(null=False, default=0, blank=True)
    follower_count = models.IntegerField(null=True, blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    games_played = models.IntegerField(null=True, blank=True)
    avg_points = models.IntegerField(null=True, blank=True)
    avg_rank = models.IntegerField(null=True, blank=True)
    avg_rank_percent = models.IntegerField(null=True, blank=True)
    name_changed = models.BooleanField(null=False, default=False)
    last_name_change = models.DateTimeField(null=True, blank=False)
    moderator = models.BooleanField(null=False, default=False)
    premium = models.BooleanField(null=False, default=False)
    influencer = models.BooleanField(null=False, default=False)
    subscription = models.ForeignKey('Subscription', null=True, blank=True, on_delete=DO_NOTHING)
    subscription_tier = models.IntegerField(null=False, blank=False, choices=TIER_CHOICES, default=TIER_NONE)
    wallet_address = models.CharField(null=True, blank=True, max_length=255, unique=True)
    finished_games = models.TextField(null=True, blank=True)
    divisions = models.ManyToManyField('Division', through='UserDivision')
    sequence_session_id = models.CharField(null=True, blank=True, max_length=255)
    real_name = models.CharField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        # empty name
        if not self.name:
            # get next sequence value
            self.name = 'Guest#{}'.format(self.get_next_user_index())
        super(CustomUser, self).save(*args, **kwargs)

    @staticmethod
    def get_next_user_index():
        query = """select nextval('user_guest_index');"""
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        return res[0]

    def is_authenticated(self):
        return True

    def calculate_stats(self):
        sql = """
select round(avg(match_leaderboard.position)) avg_rank,
       round(avg(match_leaderboard.score)) avg_points,
       ceil(avg(100 * match_leaderboard.position /
       (select count(*) from match_leaderboard ml2 where ml2.match_id = match_leaderboard.match_id))),
       count(1) games_played
  from match_leaderboard,
       games
 where match_leaderboard.game_id = games.id
   and games.user_id = %s
 group by games.user_id
        """

        with connection.cursor() as c:
            c.execute(sql, [self.pk])
            row = c.fetchone()

            if not row:
                return

            self.avg_rank = row[0]
            self.avg_points = row[1]
            self.avg_rank_percent = row[2]
            self.games_played = row[3]
            self.save(update_fields=['avg_rank', 'avg_points', 'avg_rank_percent', 'games_played'])

    def calculate_avg_rank(self):
        rank = MatchLeaderboard.objects.exclude(position__isnull=True). \
            filter(game__user=self).aggregate(Avg('position'))
        self.avg_rank = round(rank)
        self.save(update_fields=['avg_points'])

    def calculate_avg_rank_percent(self):
        query = """
select ml.position / (select count(*) from match_leaderboard ml2 where ml2.match_id = ml.match_id)
  from match_leaderboard ml
 where ml.user_id"""
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        self.avg_rank_percent = math.ceil(res[0] * 100)
        self.save(update_fields=['avg_rank_percent'])

    def update_premium(self):
        has_premium, subscription_tier = False, TIER_NONE
        try:
            # find manual subscription first
            ms = ManualSubscription.objects.filter(user=self, expires_at__gt=timezone.now()).get()
            has_premium = True
            subscription_tier = ms.tier
        except ManualSubscription.DoesNotExist:
            if self.subscription is not None and self.subscription.active:
                has_premium = True
                subscription_tier = self.subscription.tier

        if self.premium != has_premium or self.subscription_tier != subscription_tier:
            self.premium = has_premium
            self.subscription_tier = subscription_tier
            self.save(update_fields=['premium', 'subscription_tier', 'updated_at'])

    def subscribe_to_leaderboard(self, leaderboard):
        UserLeaderboardSubscription.objects.get_or_create(user=self, leaderboard=leaderboard)

    def unsubscribe_from_leaderboard(self, leaderboard):
        UserLeaderboardSubscription.objects.filter(user=self, leaderboard=leaderboard).delete()

    def get_subscribed_leaderboards(self):
        return Leaderboard.objects.filter(user_subscriptions__user=self)

    def division_in_game_week(self, game_week):
        return Division.objects.filter(
            Q(userdivision__user=self) & Q(userdivision__game_week=game_week)
        ).distinct().first()

    def last_division(self):
        return Division.objects.filter(
            Q(userdivision__user=self)
        ).order_by('-userdivision__join_date').first()


    def __str__(self):
        return '{} ({})'.format(self.name, self.pk)

    class Meta:
        db_table = 'users'


class Transactions(BaseModel):
    VIRTUAL = 'v'  # virtual currency
    CRYPTO = 'c'  # crypto currency
    NFT = 'n'  # NFT token
    GAME = 'g'  # game currency
    LAPT = 'l'  # Lapt token
    EVENT_TICKET = 'e'  # Event ticket
    MERCH = 'm'  # Merchandise
    BALL = 'b'  # Ball
    SIGNED_BALL = 'a'  # Signed Ball
    SHIRT = 's'  # Shirt
    SIGNED_SHIRT = 'h'  # Signed Shirt
    KICKOFF_PACK_1 = '1'  # Kickoff Pack 1
    KICKOFF_PACK_2 = '2'  # Kickoff Pack 1
    KICKOFF_PACK_3 = '3'  # Kickoff Pack 1
    SEASON_PACK_1 = '4'  # Season Pack 1
    SEASON_PACK_2 = '5'  # Season Pack 2
    SEASON_PACK_3 = '6'  # Season Pack 3

    OBJECT_TYPE = (
        (VIRTUAL, 'virtual'),
        (CRYPTO, 'crypto'),
        (NFT, 'nft'),
        (GAME, 'game'),
        (LAPT, 'lapt'),
        (EVENT_TICKET, 'event_ticket'),
        (MERCH, 'merch'),
        (BALL, 'ball'),
        (SIGNED_BALL, 'signed_ball'),
        (SHIRT, 'shirt'),
        (SIGNED_SHIRT, 'signed_shirt'),
        (KICKOFF_PACK_1, 'kickoff_pack_1'),
        (KICKOFF_PACK_2, 'kickoff_pack_2'),
        (KICKOFF_PACK_3, 'kickoff_pack_3'),
        (SEASON_PACK_1, 'season_pack_1'),
        (SEASON_PACK_2, 'season_pack_2'),
        (SEASON_PACK_3, 'season_pack_3'),
    )
    user = models.ForeignKey(CustomUser, on_delete=DO_NOTHING)
    amount = models.FloatField(default=0)
    quantity = models.BigIntegerField(null=False, blank=False, default=0)
    object_type = models.CharField(choices=OBJECT_TYPE, max_length=1, default=VIRTUAL)
    blockchain_uuid = models.TextField(null=True, blank=True)
    order = models.ForeignKey('Order', null=True, blank=True, on_delete=DO_NOTHING)
    match = models.ForeignKey('Match', null=True, blank=True, on_delete=DO_NOTHING)
    week = models.ForeignKey('GameWeek', null=True, blank=True, on_delete=DO_NOTHING)
    text = models.TextField(null=True, blank=True)
    delivered = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    class Meta:
        db_table = 'transactions'


class OptaFeed(models.Model):
    STATUS_RECEIVED = 1
    STATUS_PROCESSING = 2
    STATUS_PROCESSED = 3
    STATUS_ERROR = 4

    STATUSES = (
        (STATUS_RECEIVED, 'Received'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_PROCESSED, 'Processed'),
        (STATUS_ERROR, 'Error'),
    )

    FEED_TYPE_F1 = 'F1'
    FEED_TYPE_F24 = 'F24'
    FEED_TYPE_F40 = 'F40'

    FEED_TYPES = (
        (FEED_TYPE_F1, 'F1'),
        (FEED_TYPE_F24, 'F24'),
        (FEED_TYPE_F40, 'F40'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    processing_started = models.DateTimeField(null=True)
    processing_ended = models.DateTimeField(null=True)
    feed_object_id = models.CharField(unique=True, max_length=50)
    feed_hash = models.TextField(null=True)
    feed_type = models.CharField(choices=FEED_TYPES, max_length=3)
    status = models.IntegerField(choices=STATUSES, default=STATUS_RECEIVED)
    headers = models.TextField()
    match = models.ForeignKey('Match', null=True, on_delete=DO_NOTHING)

    class Meta:
        db_table = 'opta_feeds'


class OptaFeedItem(BaseModel):
    match = models.ForeignKey('Match', on_delete=DO_NOTHING)
    unique_id = models.CharField(max_length=50)
    event_id = models.CharField(max_length=50)
    current_version = models.ForeignKey('OptaFeedItemVersion', null=True, on_delete=DO_NOTHING)

    class Meta:
        db_table = 'opta_feed_items'
        unique_together = ('match', 'unique_id', 'event_id',)


class OptaFeedItemVersion(BaseModel):
    ACTIVE = 1
    NO_DIFF = 2
    PARTIAL_CANCEL = 3
    FULL_CANCEL = 4

    STATUSES = (
        (ACTIVE, 'Active'),
        (NO_DIFF, 'No Diff'),
        (PARTIAL_CANCEL, 'Partial Cancel'),
        (FULL_CANCEL, 'Full Cancel'),
    )

    item = models.ForeignKey('OptaFeedItem', on_delete=DO_NOTHING)
    status = models.IntegerField(choices=STATUSES)
    version = models.TextField()
    last_modified_at = models.DateTimeField()

    class Meta:
        db_table = 'opta_feed_item_versions'


class Country(V2ImportModel):
    name = models.TextField()
    iso = models.CharField(max_length=10, null=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.iso)

    class Meta:
        db_table = 'countries'


class Region(V2ImportModel):
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'


class Sport(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        db_table = 'sports'


class Team(V2ImportModel):
    name = models.TextField(blank=True)
    short_name = models.TextField(null=True, blank=True)
    abbr = models.CharField(max_length=5, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=DO_NOTHING)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=DO_NOTHING)
    crest_url = models.TextField(null=True, blank=True)
    ortec_selection_id = models.CharField(max_length=30, null=True, blank=True)
    opta_selection_id = models.CharField(max_length=30, null=True, blank=True)

    def get_display_name(self):
        if self.short_name:
            return self.short_name
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teams'


class Season(V2ImportModel):
    name = models.TextField()
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    # @classmethod
    # def current_season(cls):
    #     try:
    #         return cls.objects.filter(import_id=2024).get()
    #     except Season.DoesNotExist:
    #         return cls.objects.create(
    #             import_id=2024,
    #             name="2024"
    #         )

    class Meta:
        db_table = 'seasons'

class GameSeason(V2ImportModel):
    name = models.TextField()
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'game_seasons'


class CompetitionConfig(V2ImportModel):
    name = models.TextField()
    filter = models.TextField()  # in case of opta, is comeptitionCode
    enabled = models.BooleanField(default=False)
    related_competition = models.ForeignKey('Competition', null=True, on_delete=DO_NOTHING)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competition_config'


class Competition(V2ImportModel):
    name = models.TextField()
    code = models.CharField(max_length=50)
    short_name = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=True)
    config = models.ForeignKey('CompetitionConfig', null=True, on_delete=DO_NOTHING)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    # editions = HAVE RELATED EDITIONS HERE

    def get_display_name(self):
        if self.short_name:
            return self.short_name
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competitions'


class CompetitionEdition(V2ImportModel):
    name = models.TextField()
    competition = models.ForeignKey('Competition', on_delete=DO_NOTHING)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'competition_editions'


class CompetitionPhase(V2ImportModel):
    name = models.TextField()
    competition_edition = models.ForeignKey('CompetitionEdition', on_delete=DO_NOTHING)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'competition_phases'


class SeasonCompetitionMember(BaseModel):
    competition = models.ForeignKey(Competition, null=False, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    season = models.ForeignKey(Season, null=False, on_delete=DO_NOTHING)

    class Meta:
        unique_together = ('competition', 'team', 'season')
        db_table = 'season_competition_members'


class Player(V2ImportModel):
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    full_name = models.TextField(null=True, blank=True)
    nick_name = models.TextField(null=True, blank=True)
    avg_score = models.FloatField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    normalized_name = models.TextField(null=True, blank=True)
    soccer_wiki_player = models.ForeignKey('soccer_wiki.SoccerWikiPlayer', null=True, blank=True, on_delete=DO_NOTHING)

    def calculate_normalized_name(self):
        # Calculate full_name
        full_name = ('' if not self.first_name else self.first_name) + ' ' + \
                    ('' if not self.last_name else self.last_name)

        # Set the normalized_name based on nick_name or use full_name if nick_name contains abbreviation
        if self.nick_name and not any(char + '.' in self.nick_name for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            return self.nick_name
        else:
            return full_name.strip()

    def update_avg_score(self):
        self.avg_score = self.calculate_avg_score()
        self.save(update_fields=['avg_score'])

    def calculate_avg_score(self):
        # select match players for this player
        total_time, total_score, match_cnt = 0, 0, 0

        mp_qs = MatchPlayer.objects.filter(player=self, match__match_time__gt=timezone.now() - timedelta(days=180)). \
            exclude(Q(played_seconds__isnull=True) | Q(score__isnull=True)). \
            order_by('-match__match_time')

        for mp in mp_qs[:50]:
            if mp.played_seconds:
                total_time += mp.played_seconds
                total_score += mp.score
                match_cnt += 1

                # reach required amount of points
                if total_time >= (450 * 60):
                    # calculate avg score, and then normalize it to 90 min
                    avg_score = total_score / match_cnt
                    norm_avg_score = avg_score / ((total_time / match_cnt) / (90 * 60))

                    return round(norm_avg_score, 1)

        # goal is not reached
        return None

    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return ""

    def save(self, *args, **kwargs):
            # Calculate and set the full_name if not already set
            if not self.full_name:
                self.full_name = ('' if not self.first_name else self.first_name) + ' ' + \
                                ('' if not self.last_name else self.last_name)

            # Set the normalized_name
            self.normalized_name = self.calculate_normalized_name()

            super(Player, self).save(*args, **kwargs)

    class Meta:
        db_table = 'players'


class SeasonTeamPlayer(BaseModel):
    season = models.ForeignKey(Season, null=False, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.CharField(choices=const.POSITIONS, max_length=1, null=True)
    jersey_number = models.IntegerField(null=True)

    class Meta:
        unique_together = ('player', 'team', 'season')
        index_together = [
            ('player', 'team', 'season'),
        ]
        db_table = 'season_team_players'


class SelectionTeamPlayer(BaseModel):
    selection_id = models.CharField(max_length=30, null=False, blank=False)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.CharField(choices=const.POSITIONS, max_length=1, null=True)
    jersey_number = models.IntegerField(null=True)

    class Meta:
        unique_together = ('selection_id', 'player',)
        index_together = ('selection_id', 'player',)
        db_table = 'selection_team_players'


class MatchDay(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'match_days'


class Match(V2ImportModel):
    MATCH_TYPE_UNKNOWN = 0
    MATCH_TYPE_FREE = 1
    MATCH_TYPE_CASH = 2
    MATCH_TYPE_CASH_PLUS = 3

    MATCH_TYPES = (
        (MATCH_TYPE_UNKNOWN, 'Unknown'),
        (MATCH_TYPE_FREE, 'Free'),
        (MATCH_TYPE_CASH, 'Cash'),
        (MATCH_TYPE_CASH_PLUS, 'Cash Plus'),
    )

    competition = models.ForeignKey(Competition, null=False, on_delete=DO_NOTHING)
    edition = models.ForeignKey(CompetitionEdition, null=True, on_delete=DO_NOTHING)
    season = models.ForeignKey(Season, null=False, on_delete=DO_NOTHING)
    status = models.CharField(choices=const.MATCH_STATUSES, null=False, default=const.MATCH_STATUS_WAITING, max_length=1)
    period = models.CharField(choices=const.MATCH_PERIODS, null=False, default=const.MATCH_PERIOD_PREGAME, max_length=3)
    match_type = models.IntegerField(choices=MATCH_TYPES, default=MATCH_TYPE_UNKNOWN, db_index=True)
    has_lineups = models.BooleanField(default=False)
    home_team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING, related_name='home_team')
    away_team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING, related_name='away_team')
    home_team_selection_id = models.CharField(max_length=30, null=True, blank=True)
    away_team_selection_id = models.CharField(max_length=30, null=True, blank=True)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    last_processed_id = models.CharField(null=True, blank=True, max_length=15)
    match_time = models.DateTimeField(null=False)
    match_end = models.DateTimeField(null=True, blank=True)
    f_start = models.DateTimeField(null=True, blank=True)
    f_end = models.DateTimeField(null=True, blank=True)
    s_start = models.DateTimeField(null=True, blank=True)
    s_end = models.DateTimeField(null=True, blank=True)
    x1_start = models.DateTimeField(null=True, blank=True)
    x1_end = models.DateTimeField(null=True, blank=True)
    x2_start = models.DateTimeField(null=True, blank=True)
    x2_end = models.DateTimeField(null=True, blank=True)
    p_start = models.DateTimeField(null=True, blank=True)
    p_end = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    simulation_from_match = models.ForeignKey('self', null=True, blank=True, on_delete=DO_NOTHING)
    rewarded = models.BooleanField(null=False, blank=True, default=False)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    match_day = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.CASCADE, related_name='matches')
    week = models.IntegerField(default=0)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    enabled = models.BooleanField(default=True)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        super(Match, self).save(*args, **kwargs)
        self.set_up_default_rewards()

    def set_up_default_rewards(self):
        if not MatchReward.objects.filter(match=self).exists():
            rewards_instances = [
                MatchReward(min_position=1, max_position=1, amount=600, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0,match=self),
                MatchReward(min_position=2, max_position=2, amount=300, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=3, max_position=3, amount=200, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=4, max_position=10, amount=100, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=11, max_position=20, amount=50, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
                MatchReward(min_position=21, max_position=None, amount=30, game=0, lapt=0, event=0, balls=0, signed_balls=0, shirts=0, signed_shirts=0, kickoff_pack_1=0,kickoff_pack_2=0,kickoff_pack_3=0,season_pack_1=0,season_pack_2=0,season_pack_3=0, match=self),
            ]
            MatchReward.objects.bulk_create(rewards_instances)


    def create_simulation(self, duration):
        events = MatchEvent.objects.filter(match=self).order_by('match_event_id')

        base_inc = duration.total_seconds() / len(events) if len(events) > 0 else 0

        with transaction.atomic():
            now = timezone.now()
            simulation = Match.objects.create(
                competition=self.competition,
                season=self.season,
                home_team=self.home_team,
                away_team=self.away_team,
                match_time=now,
                simulation_from_match=self,
                match_type=Match.MATCH_TYPE_FREE,
                import_id='simulation-' + str(uuid.uuid4()) + "-" + self.import_id,
                home_team_selection_id=self.home_team.import_id,
                away_team_selection_id=self.away_team.import_id,
                sport_id=self.sport_id
            )

            # init match players
            simulation.sync_match_players(True)

            delay_time = timedelta(seconds=60)

            # insert simulation plan
            for i in range(len(events)):
                # calculate new timestamp
                new_timestamp = now + delay_time + timedelta(seconds=base_inc * i)
                MatchEventSimulation.objects.create(
                    match_event=events[i],
                    match=simulation,
                    timestamp=new_timestamp,
                )

        return simulation

    def get_team_id_by_selection_id(self, selection_id):
        if str(selection_id) == str(self.home_team_selection_id):
            return self.home_team_id
        elif str(selection_id) == str(self.away_team_selection_id):
            return self.away_team_id
        else:
            raise Exception("cannot find team {}, home_team is {} - {}, away_team is {} - {}.".format(
                selection_id,
                self.home_team_selection_id,
                self.home_team_id,
                self.away_team_selection_id,
                self.away_team_id,
            ))

    def insert_missing_match_players(self):
        team_players = SelectionTeamPlayer.objects.select_related('player').filter(
            Q(selection_id=self.home_team_selection_id) | Q(selection_id=self.away_team_selection_id)
        )
        for tp in team_players:
            team_id = self.get_team_id_by_selection_id(tp.selection_id)
            try:
                mp = MatchPlayer.objects.filter(
                    match_id=self.id,
                    player_id=tp.player.id,
                    team_id=team_id,
                ).get()
                mp.position = tp.position
                mp.jersey_number = tp.jersey_number
                mp.save(update_fields=['position', 'jersey_number'])
            except MatchPlayer.DoesNotExist:
                try:
                    MatchPlayer.objects.create(
                        match_id=self.pk,
                        player_id=tp.player.id,
                        team_id=team_id,
                        position=tp.position,
                        jersey_number=tp.jersey_number,
                        from_lineups=False
                    )
                except IntegrityError:
                    print(f"[ERR] [insert_missing_match_players] cannot create match player: {traceback.format_exc}")
                    pass

    def update_match_players_score(self, sync_avg_score=False):
        match_players = MatchPlayer.objects.select_related('player').filter(match=self)

        if sync_avg_score:
            # update avg scores for all players
            for mp in match_players:
                mp.player.update_avg_score()

        for mp in match_players:
            # propagate value from player
            mp.avg_score = mp.player.avg_score
            mp.save(update_fields=['avg_score'])

    def update_match_players_star_flag(self):
        match_players = MatchPlayer.objects.filter(match=self)
        score_ranks = get_rank_dict([mp.avg_score for mp in match_players if mp.avg_score])

        for mp in match_players:
            rank = score_ranks.get(mp.avg_score, 0)

            # only top N of players are star players
            is_star = rank <= settings.STAR_PLAYERS_TOP if rank > 0 else False

            # propagate value from player
            mp.is_star = is_star
            mp.save(update_fields=['is_star'])

    def sync_match_players(self, sync_avg_score=False):
        with transaction.atomic():
            # lock match
            m = Match.objects.select_for_update().get(pk=self.pk)

            # ignore matches in other than 'waiting' and 'unknown' states
            if m.status not in (const.MATCH_STATUS_WAITING, const.MATCH_STATUS_UNKNOWN, const.MATCH_STATUS_EMPTY):
                return

            should_update_star = True

            # we shouldn't update `is_star` flag if less than 3 days left
            # and is_star flag is already set
            if (m.match_time - timedelta(days=3)) < timezone.now() and \
                    MatchPlayer.objects.filter(match=m.pk, is_star=True).count() > 0:
                should_update_star = False

            self.insert_missing_match_players()
            self.update_match_players_score(sync_avg_score)

            if should_update_star:
                self.update_match_players_star_flag()

    def is_opta_selection_from_match(self, value):
        return self.is_opta_home_selection_from_match(value) or self.is_opta_away_selection_from_match(value)

    def is_opta_home_selection_from_match(self, value):
        return str(value) == self.home_team_selection_id

    def is_opta_away_selection_from_match(self, value):
        return str(value) == self.away_team_selection_id

    def get_import_id(self) -> str:
        if self.simulation_from_match is not None:
            return self.simulation_from_match.get_import_id()
        return self.import_id

    def __str__(self):
        return f"{'[SIM] ' if self.simulation_from_match else ''}{self.home_team} vs {self.away_team} on {self.match_time.strftime('%Y-%m-%d %H:%M:%S')} - import_id: {self.get_import_id()} - id: {self.id}"

    class Meta:
        db_table = 'matches'
        verbose_name_plural = 'Matches'


class MatchReward(models.Model):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    position = models.IntegerField(null=True, blank=True)  # deprecated
    min_position = models.IntegerField(default=1)
    max_position = models.IntegerField(null=True, blank=True)
    amount = models.FloatField()
    game = models.FloatField(default=0)
    lapt = models.FloatField(default=0)
    event = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)  # For merchandise
    signed_balls = models.IntegerField(default=0)  # For merchandise
    shirts = models.IntegerField(default=0)  # For merchandise
    signed_shirts = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_1 = models.IntegerField(default=0)
    kickoff_pack_2 = models.IntegerField(default=0)
    kickoff_pack_3 = models.IntegerField(default=0)
    season_pack_1 = models.IntegerField(default=0)
    season_pack_2 = models.IntegerField(default=0)
    season_pack_3 = models.IntegerField(default=0)

    class Meta:
        db_table = 'match_rewards'
        unique_together = ('match', 'min_position', 'max_position')


class MatchEvent(models.Model):
    ACTIVE = 1
    CANCELLED = 2
    IGNORED = 3

    STATUSES = (
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
        (IGNORED, 'Ignored'),
    )

    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(null=False)
    team = models.ForeignKey(Team, null=True, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=True, on_delete=DO_NOTHING)
    type = models.IntegerField(null=False)
    points = models.FloatField(null=True)
    payload = models.TextField(null=True)
    minute = models.IntegerField(null=False)
    second = models.IntegerField(null=False)
    x = models.FloatField(null=False, default=0)
    y = models.FloatField(null=False, default=0)
    match_event_id = models.IntegerField(null=False)
    provider_id = models.CharField(max_length=30)
    opta_feed_item_version = models.ForeignKey(OptaFeedItemVersion, null=True, on_delete=DO_NOTHING)
    status = models.IntegerField(choices=STATUSES, default=ACTIVE)
    period = models.IntegerField(default=None, null=True, blank=True)
    has_real_timestamp = models.BooleanField(default=False)

    class Meta:
        db_table = 'match_events'
        unique_together = ('match', 'match_event_id')


class MatchEventSimulation(models.Model):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    match_event = models.ForeignKey(MatchEvent, null=False, on_delete=DO_NOTHING)
    timestamp = models.DateTimeField(null=False, db_index=True)
    simulated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'match_event_simulations'
        unique_together = ('match', 'match_event')


class MatchPlayer(BaseModel):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.CharField(choices=const.POSITIONS, max_length=1, null=True)
    jersey_number = models.IntegerField(null=True)
    from_lineups = models.BooleanField(default=False)
    is_star = models.BooleanField(default=False)
    score = models.FloatField(null=True)
    played_seconds = models.IntegerField(null=True)
    avg_score = models.FloatField(null=True)

    class Meta:
        db_table = 'match_players'
        unique_together = ('match', 'player',)


class MatchHeadline(models.Model):
    SCREEN_TYPE_LOBBY = 1
    SCREEN_TYPE_GAMEPLAY = 2
    SCREEN_TYPE_FULLTIME = 3

    SCREEN_TYPES = (
        (SCREEN_TYPE_LOBBY, 'lobby'),
        (SCREEN_TYPE_GAMEPLAY, 'gameplay'),
        (SCREEN_TYPE_FULLTIME, 'fulltime'),
    )

    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.TextField()
    type = models.CharField(max_length=30)
    screen_type = models.IntegerField(choices=SCREEN_TYPES)
    image_type = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'match_headlines'


class Game(BaseModel):
    STATUS_WAITING = 'w'
    STATUS_GAMEPLAY = 'g'
    STATUS_FINISHED = 'f'

    STATUS_CHOICES = (
        (STATUS_WAITING, 'w'),
        (STATUS_GAMEPLAY, 'g'),
        (STATUS_FINISHED, 'f'),
    )

    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING)
    status = models.CharField(max_length=1, default=STATUS_WAITING)
    version = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    premium = models.BooleanField(default=False)
    subscription_tier = models.IntegerField(null=False, blank=False, choices=TIER_CHOICES, default=TIER_NONE)
    num = models.IntegerField(null=True, blank=True)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    notified = models.BooleanField(default=False)

    class Meta:
        db_table = 'games'
        unique_together = (('match', 'user'), ('user', 'num'))


class GamePick(BaseModel):
    ended_at = models.DateTimeField(null=True)
    game = models.ForeignKey(Game, null=False, on_delete=DO_NOTHING, related_name='picks')
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    position = models.IntegerField(null=False)
    version = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    ended_minute = models.IntegerField(null=True)
    ended_second = models.IntegerField(null=True)
    user_swapped = models.BooleanField(default=True)
    assigned_player = models.ForeignKey('AssignedPlayer', null=True, on_delete=DO_NOTHING, related_name='assigned_player')

    class Meta:
        db_table = 'game_picks'


class GameEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game, null=False, on_delete=DO_NOTHING)
    player = models.ForeignKey(Player, null=False, on_delete=DO_NOTHING)
    game_pick = models.ForeignKey(GamePick, null=False, on_delete=DO_NOTHING)
    powerup = models.ForeignKey('GamePowerUp', null=True, on_delete=DO_NOTHING)
    team = models.ForeignKey(Team, null=False, on_delete=DO_NOTHING)
    minute = models.IntegerField(null=False)
    second = models.IntegerField(null=False)
    type = models.IntegerField(null=False)
    score = models.FloatField(default=0)
    initial_score = models.FloatField(default=0)
    match_event = models.ForeignKey(MatchEvent, null=True, on_delete=DO_NOTHING)
    nft_multiplier = models.FloatField(default=1.0)
    boost_multiplier = models.FloatField(default=1.0)
    nft_image = models.TextField(null=True)

    class Meta:
        db_table = 'game_events'


class GamePowerUp(BaseModel):
    ended_at = models.DateTimeField(null=True)
    powerup = models.ForeignKey('PowerUp', on_delete=DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=DO_NOTHING)
    position = models.IntegerField()
    duration = models.IntegerField()
    multiplier = models.FloatField()
    minute = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    bonus = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'game_powerups'


class LeaderboardType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'leaderboard_types'

class Division(BaseModel):
    name = models.CharField(max_length=255)
    tier = models.IntegerField()
    percentage = models.FloatField(default=0.01)
    relegation_min_range = models.FloatField(default=0.2)
    relegation_max_range = models.FloatField(default=0.3)
    promotion_min_range = models.FloatField(default=0.2)
    promotion_max_range = models.FloatField(default=0.3)

    def __str__(self):
        return f"Division {self.tier}"

    class Meta:
        db_table = 'divisions'



class MatchLeaderboard(models.Model):
    match = models.ForeignKey(Match, on_delete=DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=DO_NOTHING)
    score = models.FloatField(null=True)
    position = models.IntegerField(null=True)
    division = models.ForeignKey(Division, null=True, blank=True, on_delete=models.DO_NOTHING)
    leaderboard_type = models.ForeignKey(LeaderboardType, null=True, blank=True, on_delete=models.DO_NOTHING)
    transaction = models.ForeignKey('Transactions', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'match_leaderboard'


class MatchEventProcessor(models.Model):
    TYPE_POINTS = 1
    TYPE_SYSTEM = 2

    TYPES = (
        (TYPE_POINTS, 'points'),
        (TYPE_SYSTEM, 'system'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    type = models.IntegerField(choices=TYPES)
    last_processed_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'match_event_processors'
        unique_together = ('match', 'type',)


class Action(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    score = models.FloatField(null=False)
    ordering = models.IntegerField()
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    category = models.TextField(null=True)
    nft_category = models.TextField(null=True, blank=True, choices=const.NFT_CATEGORIES)
    icon = models.TextField(null=True)

    @staticmethod
    @lru_cache()
    def get_name_by_id(action_id):
        try:
            action = Action.objects.get(pk=action_id)
            return action.name
        except Action.DoesNotExist:
            return ""

    @staticmethod
    @lru_cache()
    def get_score_by_id(action_id):
        try:
            action = Action.objects.get(pk=action_id)
            return action.score
        except Action.DoesNotExist:
            return 0

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'actions'


class PowerUp(models.Model):
    TYPE_EVENT = 1
    TYPE_GAME = 2
    TYPES = (
        (TYPE_EVENT, 'event'),
        (TYPE_GAME, 'game'), # Means that it's applied to the whole game/match
    )
    name = models.TextField(null=False)
    description = models.TextField(null=True)
    icon_url = models.TextField(null=True)
    duration = models.IntegerField(null=False, help_text='duration in seconds')
    multiplier = models.FloatField(null=False)
    cost = models.FloatField(null=False, default=0.0)
    type = models.IntegerField(choices=TYPES, null=True, default=TYPE_EVENT)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.DO_NOTHING)
    enabled = models.BooleanField(null=False, blank=False, default=False)
    conditions = JSONField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powerups'


class PowerUpAction(models.Model):
    action = models.ForeignKey(Action, null=False, on_delete=DO_NOTHING)
    powerup = models.ForeignKey(PowerUp, null=False, on_delete=DO_NOTHING)
    ordering = models.IntegerField()

    class Meta:
        db_table = 'powerup_actions'


class MatchNotification(BaseModel):
    match = models.ForeignKey(Match, null=False, on_delete=DO_NOTHING)
    user = models.ForeignKey(CustomUser, null=True, on_delete=DO_NOTHING)
    type = models.IntegerField()

    class Meta:
        db_table = 'match_notifications'


class Follower(models.Model):
    from_user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING, related_name='followers')
    to_user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING, related_name='followings')

    class Meta:
        db_table = 'followers'
        unique_together = ('from_user', 'to_user',)


class BanPenalty(models.Model):
    user = models.ForeignKey(CustomUser, null=False, on_delete=DO_NOTHING, related_name='penalties')
    start_time = models.DateTimeField(null=False, blank=False, default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True, help_text='Empty end time means permanent ban')
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.end_time:
            return 'Ban at period {} - {}'.format(self.start_time, self.end_time)
        else:
            return 'Permanent ban from {}'.format(self.start_time)

    class Meta:
        db_table = 'ban_penalties'


class Subscription(models.Model):
    user_id = models.TextField(null=False, blank=False, unique=True)
    last_billing_update = models.DateTimeField(null=False, blank=False)
    raw_data = models.TextField(null=False, blank=False)
    expiration_time = models.DateTimeField(null=False, blank=False)
    active = models.BooleanField(null=False, blank=False)
    tier = models.IntegerField(null=True, blank=False, choices=TIER_CHOICES)

    class Meta:
        db_table = 'subscriptions'


class SubscriptionHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    subscription = models.ForeignKey(Subscription, null=False, blank=False, on_delete=DO_NOTHING)
    last_billing_update = models.DateTimeField(null=False, blank=False)
    raw_data = models.TextField(null=False, blank=False)
    expiration_time = models.DateTimeField(null=False, blank=False)
    active = models.BooleanField(null=False, blank=False)

    class Meta:
        db_table = 'subscription_history'


class SubscriptionRequest(models.Model):
    user_id = models.TextField(null=False, blank=False)
    last_billing_update = models.DateTimeField(null=False, blank=False)
    app_user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=DO_NOTHING)

    class Meta:
        db_table = 'subscription_requests'


class ManualSubscription(BaseModel):
    user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=DO_NOTHING)
    tier = models.IntegerField(choices=TIER_CHOICES)
    expires_at = models.DateTimeField(null=False, blank=False)

    class Meta:
        db_table = 'manual_subscriptions'


class Item(models.Model):
    CREDIT_TOKEN = 1
    CARDPACK = 2

    TYPES = (
        (CREDIT_TOKEN, 'CreditToken'),
        (CARDPACK, 'CardPack'),
    )

    price = models.FloatField(default=0)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    page_url = models.TextField(null=True, blank=True)
    purchase_img_url = models.TextField(null=True, blank=True)
    contract_abbr = models.TextField(null=False, blank=False)
    contract_address = models.TextField(null=False, blank=False)
    token_id = models.TextField(null=True, blank=True)
    stripe_price_id = models.TextField(null=True, blank=True)
    min_quantity = models.IntegerField(null=True, blank=True)
    default_quantity = models.IntegerField(null=True, blank=True)
    max_quantity = models.IntegerField(null=True, blank=True)
    whitelist_required = models.BooleanField(default=False)
    start_date_at = models.DateTimeField(null=False, blank=False)
    close_date_at = models.DateTimeField(null=False, blank=False)
    bonus_quantity = JSONField()
    type = models.IntegerField(choices=TYPES, default=CREDIT_TOKEN)

    class Meta:
        db_table = 'items'


class Order(BaseModel):
    PROCESSING = 0
    FAILED = 1
    COMPLETED = 2
    EXPIRED = 3

    MINT_NOT_STARTED = 0
    MINT_IN_PROGRESS = 1
    MINT_FAILED = 2
    MINT_SUCCEEDED = 3
    MINT_TIMEOUT = 4

    # payment_platform_types
    STRIPE = 1
    INTERNAL = 2

    STATUSES = (
        (PROCESSING, 'Processing'),
        (FAILED, 'Failed'),
        (COMPLETED, 'Completed'),
        (EXPIRED, 'Expired'),
    )

    BC_STATUSES = (
        (MINT_NOT_STARTED, 'Mint not started'),
        (MINT_IN_PROGRESS, 'Mint in progress'),
        (MINT_FAILED, 'Mint Failed'),
        (MINT_SUCCEEDED, 'Mint Succeeded'),
        (MINT_TIMEOUT, 'Mint Timeout'),
    )

    TYPES = (
        (STRIPE, 'Stripe'),
        (INTERNAL, 'INTERNAL')
    )

    user = models.ForeignKey('CustomUser', null=False, on_delete=DO_NOTHING)
    item = models.ForeignKey('Item', null=True, on_delete=DO_NOTHING)
    quantity = models.BigIntegerField(null=False, blank=False, default=0)
    amount = models.FloatField(default=0)
    contract = models.TextField(null=True, blank=True)
    token_id = models.TextField(null=True, blank=True)
    delivered = models.BooleanField(null=False, blank=False, default=False)
    purchased_at = models.DateTimeField(null=True, blank=True)
    blockchain_uuid = models.TextField(null=True, blank=True)

    payment_platform_uuid = models.TextField(null=True, blank=True)
    blockchain_order_status = models.IntegerField(choices=BC_STATUSES, default=MINT_NOT_STARTED)
    payment_platform_status = models.IntegerField(choices=STATUSES, default=PROCESSING)
    payment_platform_type = models.IntegerField(choices=TYPES, default=STRIPE)

    cancel_url = models.TextField(null=True, blank=True)
    success_url = models.TextField(null=True, blank=True)
    payment_platform_url = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'orders'


class CardPackType(BaseModel):
    name = models.CharField(max_length=255)
    card_pack_code = models.CharField(max_length=255, null=True) # has to be equal to the card_pack_code in card_pack
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    tier1 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier2 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier3 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier4 = JSONField(default=list, encoder=DjangoJSONEncoder)
    tier5 = JSONField(default=list, encoder=DjangoJSONEncoder)
    pack_limits = models.IntegerField(null=True, blank=True)
    star_ratings = JSONField(default=list, encoder=DjangoJSONEncoder,null=True, blank=True)
    rarities = JSONField(default=list, encoder=DjangoJSONEncoder,null=True, blank=True)
    collection = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'card_pack_types'


class AssignedCardPack(BaseModel):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    card_pack_type = models.ForeignKey('CardPackType', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)
    revealed_at = models.DateTimeField(null=True, blank=True)
    revealed = models.BooleanField(default=False)
    card_ids = JSONField(default=list, encoder=DjangoJSONEncoder, null=True, blank=True)
    store_transaction = models.ForeignKey('StoreProductTransactions', on_delete=models.DO_NOTHING, null=True, blank=True)
    refunded = models.BooleanField(default=False)

    class Meta:
        db_table = 'assigned_card_packs'


class PlayerBucket(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    game_position = models.CharField(max_length=255, null=True, blank=True)
    real_popularity = models.IntegerField(default=0)
    usable_popularity = models.IntegerField(default=0)
    bronze = models.BooleanField(null=True, blank=True)
    silver = models.BooleanField(null=True, blank=True)
    gold = models.BooleanField(null=True, blank=True)
    platinum = models.BooleanField(null=True, blank=True)
    diamond = models.BooleanField(null=True, blank=True)
    common = models.IntegerField(default=0)
    uncommon = models.IntegerField(default=0)
    rare = models.IntegerField(default=0)
    ultra_rare = models.IntegerField(default=0)
    legendary = models.IntegerField(default=0)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'player_bucket'


class AssignedPlayer(BaseModel):
    player_nft = models.ForeignKey('NftBucket', on_delete=models.CASCADE, null=True, blank=True, default=None)
    nft_id = models.CharField(max_length=255, null=True, blank=True, default=None)
    rarity = models.CharField(max_length=255, null=True, blank=True, default=None)

    class Meta:
        db_table = 'assigned_players'


class Leaderboard(BaseModel):
    TYPE_CHOICES = [
        ('season', 'Season'),
        ('country', 'Country'),
        ('team', 'Team'),
        ('matchday', 'Matchday'),
        # Add new types here
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True, related_name='leaderboards')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='leaderboards')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='leaderboards')  # New field

    class Meta:
        db_table = 'leaderboards'


class UserLeaderboardSubscription(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    leaderboard = models.ForeignKey(Leaderboard, on_delete=models.CASCADE)
    subscription_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_leaderboard_subscriptions'
        unique_together = ('user', 'leaderboard')


class ChatRoom(V2ImportModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(CustomUser, through='ChatRoomMember')
    match = models.ForeignKey(Match, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='chat_rooms')

    class Meta:
        db_table = 'chat_rooms'


class ChatMessage(BaseModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        db_table = 'chat_messages'


class ChatRoomMember(models.Model):
    room = models.OneToOneField(ChatRoom, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    muted = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    banned_at = models.DateTimeField(null=True, blank=True)
    mod = models.BooleanField(default=False)

    class Meta:
        db_table = 'chat_room_members'
        unique_together = ('room', 'user')

class DataFeedSimModel(models.Model):
    match = models.ForeignKey(Match, null=True, blank=True, on_delete=DO_NOTHING)
    import_id = models.CharField(max_length=50, null=True, blank=True)
    json_events = JSONField(blank=True, null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'data_feed_sim'

class EventThrottler(models.Model):
    exchange = models.CharField(max_length=32, null=False, blank=False)
    event_type = models.CharField(max_length=32, null=False, blank=False, db_column='type')
    data = models.TextField(null=False, blank=True)
    processing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'event_throttler'

class StoreProduct(BaseModel):
    PRODUCT_TYPES = [
        ('consumable', 'Consumable'),
        ('nonconsumable', 'Non-Consumable'),
        ('subscription', 'Subscription'),
        ('nft', 'NFT'),
    ]
    store_product_id = models.CharField(max_length=255)
    apple_product_id = models.CharField(max_length=255, null=True, blank=True)
    google_product_id = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')
    active = models.BooleanField(default=True)
    product_type = models.CharField(max_length=255, null=True, blank=True, default=PRODUCT_TYPES[0][0], choices=PRODUCT_TYPES)
    class Meta:
        db_table = 'store_products'

class StoreProductTransactions(BaseModel):
    transaction = models.ForeignKey(Transactions, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True)
    product = models.ForeignKey(StoreProduct, on_delete=models.PROTECT)
    external_transaction_id = models.CharField(max_length=255, null=True, blank=True)
    initiated = models.BooleanField(default=False)
    initiated_at = models.DateTimeField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    origin_store = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'store_product_transactions'

class NftBucket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    team_id = models.UUIDField(null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)
    game_position = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    common_claiming = models.FloatField(null=True, blank=True, default=0.0)
    common_defence = models.FloatField(null=True, blank=True, default=0.0)
    common_distribution = models.FloatField(null=True, blank=True, default=0.0)
    common_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    common_passing = models.FloatField(null=True, blank=True, default=0.0)
    common_shooting = models.FloatField(null=True, blank=True, default=0.0)
    common_stopping = models.FloatField(null=True, blank=True, default=0.0)
    legendary_claiming = models.FloatField(null=True, blank=True, default=0.0)
    legendary_defence = models.FloatField(null=True, blank=True, default=0.0)
    legendary_distribution = models.FloatField(null=True, blank=True, default=0.0)
    legendary_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    legendary_passing = models.FloatField(null=True, blank=True, default=0.0)
    legendary_shooting = models.FloatField(null=True, blank=True, default=0.0)
    legendary_stopping = models.FloatField(null=True, blank=True, default=0.0)
    nationality = models.CharField(max_length=255, null=True, blank=True, default='')
    rare_claiming = models.FloatField(null=True, blank=True, default=0.0)
    rare_defence = models.FloatField(null=True, blank=True, default=0.0)
    rare_distribution = models.FloatField(null=True, blank=True, default=0.0)
    rare_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    rare_passing = models.FloatField(null=True, blank=True, default=0.0)
    rare_shooting = models.FloatField(null=True, blank=True, default=0.0)
    rare_stopping = models.FloatField(null=True, blank=True, default=0.0)
    star_rating = models.FloatField(default=0.0)
    ultra_rare_claiming = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_defence = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_distribution = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_passing = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_shooting = models.FloatField(null=True, blank=True, default=0.0)
    ultra_rare_stopping = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_claiming = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_defence = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_distribution = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_dribbling = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_passing = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_shooting = models.FloatField(null=True, blank=True, default=0.0)
    uncommon_stopping = models.FloatField(null=True, blank=True, default=0.0)
    common_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    common_image = models.CharField(max_length=255, null=True, blank=True, default='')
    uncommon_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    uncommon_image = models.CharField(max_length=255, null=True, blank=True, default='')
    legendary_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    legendary_image = models.CharField(max_length=255, null=True, blank=True, default='')
    rare_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    rare_image = models.CharField(max_length=255, null=True, blank=True, default='')
    ultra_rare_metadata = models.CharField(max_length=255, null=True, blank=True, default='')
    ultra_rare_image = models.CharField(max_length=255, null=True, blank=True, default='')
    common_limit = models.IntegerField(null=True, blank=True, default=0)
    uncommon_limit = models.IntegerField(null=True, blank=True, default=0)
    rare_limit = models.IntegerField(null=True, blank=True, default=0)
    ultra_rare_limit = models.IntegerField(null=True, blank=True, default=0)
    legendary_limit = models.IntegerField(null=True, blank=True, default=0)
    players_group = models.CharField(max_length=255, null=True, blank=True, default='')
    opta_id = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'nft_bucket'

class GameWeek(BaseModel):
    SCHEDULED = 's'  # Game week is planned but hasn't started yet
    LIVE = 'l'  # Game week is currently ongoing
    FINISHED = 'f'  # Game week has ended but not yet processed
    CLOSED = 'c'  # Game week has been processed and concluded

    STATUSES = (
        (SCHEDULED, 'New'),
        (LIVE, 'Live'),
        (FINISHED, 'Not_processed'),
        (CLOSED, 'Concluded'),
    )

    name = models.CharField(max_length=255)
    start_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)
    scored_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUSES, null=False, default=SCHEDULED, max_length=1)
    leaderboards = models.ForeignKey('MatchLeaderboard', null=True, blank=True, on_delete=models.DO_NOTHING)
    season = models.ForeignKey('GameSeason', null=True, blank=True, on_delete=models.DO_NOTHING)

    def already_ended(self):
        return timezone.now() > self.end_at

    @transaction.atomic()
    def save(self, *args, **kwargs):
        super(GameWeek, self).save(*args, **kwargs)

        self.set_up_default_rewards()

    def set_up_default_rewards(self):
        if not DivisionReward.objects.filter(week=self).exists():
            divisions = Division.objects.all()
            for division in divisions:
                self.set_up_division_rewards(division)
            # genesis
            self.set_up_division_rewards(None)

    def set_up_division_rewards(self, division: Optional[Division]):
        reward_configurations = {
            1: [
                    (1,1, {'credits': 1575, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 875, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 600, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 375, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                2: [
                    (1,1, {'credits': 1425, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 775, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 525, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 325, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                3: [
                    (1,1, {'credits': 1275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 700, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 475, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                4: [
                    (1,1, {'credits': 1150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 625, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 425, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 175, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                5: [
                    (1,1, {'credits': 1025, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 550, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 375, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 175, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                6: [
                    (1,1, {'credits': 925, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 500, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 325, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                7: [
                    (1,1, {'credits': 825, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 450, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 275, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 175, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                8: [
                    (1,1, {'credits': 750, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 400, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 250, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 150, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                9: [
                    (1,1, {'credits': 675, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 350, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 225, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 50, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                10: [
                    (1,1, {'credits': 600, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 300, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
                0: [
                    (1,1, {'credits': 600, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (2,2, {'credits': 300, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (3,3, {'credits': 200, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (4,10, {'credits': 125, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (11,20, {'credits': 100, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                    (21,1000, {'credits': 75, 'game_token': 0, 'lapt_token': 0, 'event_tickets': 0, 'ball': 0, 'signed_ball': 0, 'shirt': 0, 'signed_shirt': 0,'kickoff_pack_1': 0, 'kickoff_pack_2': 0, 'kickoff_pack_3': 0, 'season_pack_1': 0, 'season_pack_2': 0, 'season_pack_3': 0}),
                ],
        }

        tier = division.tier if division is not None else 0
        positions = reward_configurations.get(tier, [])

        qs = DivisionReward.objects
        if division is None:
            qs = qs.filter(week=self, division__isnull=True)
        else:
            qs = qs.filter(week=self, division=division)
        existing_rewards = qs.values_list('min_position', 'max_position')

        rewards_instances = []
        for min_position, max_position, reward_data in positions:
            if (min_position, max_position) not in existing_rewards:
                reward = Rewards.objects.create(
                    name=f"Division {tier} Position {min_position} to {max_position}",
                    **reward_data
                )
                rewards_instances.append(DivisionReward(
                    min_position=min_position,
                    max_position=max_position,
                    reward=reward,
                    week=self,
                    division=division
                ))

        if rewards_instances:
            DivisionReward.objects.bulk_create(rewards_instances)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'game_weeks'

class UserGameWeekHistory(BaseModel):
    SAFE = 's'
    PROMOTED = 'p'
    DEMOTED = 'd'

    STATUSES = (
        (SAFE, 'Safe'),
        (PROMOTED, 'Promoted'),
        (DEMOTED, 'Demoted'),
    )

    user = models.ForeignKey('CustomUser', on_delete=DO_NOTHING)
    game_week = models.ForeignKey('GameWeek', on_delete=DO_NOTHING)
    week_division = models.ForeignKey('Division', on_delete=DO_NOTHING, null=True, blank=True)
    week_division_position = models.IntegerField(default=0)
    week_division_tier = models.IntegerField(null=True, blank=True)
    week_points = models.IntegerField(default=0)
    week_coins = models.IntegerField(default=0)
    new_division = models.ForeignKey('Division', on_delete=DO_NOTHING, null=True, blank=True, related_name='new_divisions')
    new_division_tier = models.IntegerField(null=True, blank=True)
    week_average_rank = models.FloatField(null=True, blank=True)
    week_matches_played = models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES, null=False, default=SAFE, max_length=1)

    def __str__(self):
        return f"User history for week {self.game_week.name}, {self.user.name}({self.user.id})"
    class Meta:
        db_table = 'user_game_week_histories'


class UserDivision(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    game_week = models.ForeignKey(GameWeek, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_or_initiate(cls, user_id, division_id, game_week_id, points):
        try:
            user_division = cls.objects.get(
                user_id=user_id,
                division_id=division_id,
                game_week_id=game_week_id,
            )
            user_division.points = points
            user_division.join_date = timezone.now()
        except cls.DoesNotExist:
            user_division = cls(
                user_id=user_id,
                division_id=division_id,
                game_week_id=game_week_id,
                join_date=timezone.now()
            )
        return user_division

    def __str__(self):
        return f"User Division for week: {self.game_week.name}, tier:{self.division.tier} {self.user.name}({self.user.id})"


    class Meta:
        unique_together = ('user', 'division', 'game_week')
        db_table = 'user_divisions'


class DivisionReward(BaseModel):
    week = models.ForeignKey(GameWeek, null=False, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)
    min_position = models.IntegerField(default=1)
    max_position = models.IntegerField(null=True, blank=True)
    reward = models.ForeignKey('Rewards', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'division_rewards'
        unique_together = ('week', 'division', 'min_position', 'max_position')

class AppInbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)  # Example values: 'Active', 'Inactive'
    priority = models.CharField(max_length=50)  # Example values: 'Low', 'Medium', 'High'
    category = models.CharField(max_length=50)  # Example categories: 'Update', 'Reward'
    image_url = models.URLField(null=True, blank=True)
    link_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)  # New field to track if the notification is read
    claimed = models.BooleanField(default=False)  # New field to track if the notification is claimed
    clamed_at = models.DateTimeField(null=True, blank=True)  # New field to track when the notification is claimed
    reward = models.ForeignKey('Rewards', null=True, blank=True, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, null=True, blank=True, on_delete=models.CASCADE)
    game_week_id = models.ForeignKey(GameWeek, null=True, blank=True, on_delete=models.CASCADE)
    clear = models.BooleanField(default=False)  # New field to track if the notification is cleared
    game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_inbox'

    def __str__(self):
        return self.title

class GameWeekDivision(models.Model):
    week = models.ForeignKey(GameWeek, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    promotion_count = models.FloatField()
    relegation_count = models.FloatField()

    class Meta:
        db_table = 'game_week_divisions'
    
class Rewards(BaseModel):
    name = models.CharField(max_length=255)
    credits = models.FloatField(default=0)  # For virtual currency
    game_token = models.FloatField(default=0)  # For cryptocurrency
    lapt_token = models.FloatField(default=0)  # For first token
    event_tickets = models.IntegerField(default=0)  # For event tickets
    ball = models.IntegerField(default=0)  # For merchandise
    signed_ball = models.IntegerField(default=0)  # For merchandise
    shirt = models.IntegerField(default=0)  # For merchandise
    signed_shirt = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_1 = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_2 = models.IntegerField(default=0)  # For merchandise
    kickoff_pack_3 = models.IntegerField(default=0)  # For merchandise
    season_pack_1 = models.IntegerField(default=0)  # For merchandise
    season_pack_2 = models.IntegerField(default=0)  # For merchandise
    season_pack_3 = models.IntegerField(default=0)  # For merchandise

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rewards'

class PushNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, max_length=255,null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    payload = JSONField(null=True, blank=True)
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification to {self.user} - {self.title}"
    
    class Meta:
        db_table = 'push_notifications'

class Badges(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.URLField()
    points = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'badges'
        

class UserBadges(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badges, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Badge {self.badge.name} to {self.user.name}"
    
    class Meta:
        db_table = 'user_badges'
        
class Frames(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.URLField()
    points = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'frames'
        
class UserFrames(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    frame = models.ForeignKey(Frames, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Frame {self.frame.name} to {self.user.name}"
    
    class Meta:
        db_table = 'user_frames'
        
class Banner(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.URLField()
    points = models.IntegerField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'banners'
        
class UserBanners(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Banner {self.banner.name} to {self.user.name}"
    
    class Meta:
        db_table = 'user_banners'