import uuid
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from core.models import (
    GameWeek, DivisionReward, CustomUser,
    Transactions, Division,Match, Game,
    MatchLeaderboard, UserGameWeekHistory,
    Team, Season, Competition, UserDivision, GameSeason)

from .sync import (
    check_and_finish_week, get_season_users,
    get_global_leaderboards_without_divisions,
    create_history_data, create_new_week,
    assign_user_to_division, calculate_rewards,
    process_week_rewards, conclude_game_week, get_leaderboards_with_divisions
)
from .simulation import OrToolsDistributionStrategy, User, Division as SDivision


class BaseClassTest(TestCase):
    def setUp(self):
        DivisionReward.objects.all().delete()
        MatchLeaderboard.objects.all().delete()
        Game.objects.all().delete()
        Match.objects.all().delete()
        CustomUser.objects.all().delete()
        Division.objects.all().delete()
        GameWeek.objects.all().delete()
        Team.objects.all().delete()
        Season.objects.all().delete()
        Competition.objects.all().delete()


        divisions = [
            {'name': "Division 10", 'tier': 10, 'percentage': 0.08},
            {'name': "Division 9", 'tier': 9, 'percentage': 0.10},
            {'name': "Division 8", 'tier': 8, 'percentage': 0.15},
            {'name': "Division 7", 'tier': 7, 'percentage': 0.19},
            {'name': "Division 6", 'tier': 6, 'percentage': 0.15},
            {'name': "Division 5", 'tier': 5, 'percentage': 0.12},
            {'name': "Division 4", 'tier': 4, 'percentage': 0.09},
            {'name': "Division 3", 'tier': 3, 'percentage': 0.07},
            {'name': "Division 2", 'tier': 2, 'percentage': 0.04},
            {'name': "Division 1", 'tier': 1, 'percentage': 0.01},
        ]

        for division in divisions:
            Division.objects.create(name=division['name'], tier=division['tier'], percentage=division['percentage'])

        self.division = Division.objects.order_by('-tier').first()
        self.division2 = Division.objects.filter(tier=(self.division.tier - 1)).first()
        self.season = Season.objects.create(name="Test Season")
        self.game_season = GameSeason.objects.create(name="Test Game Season", start_at=(timezone.now() - timedelta(days=20)), end_at=(timezone.now() + timedelta(days=10)))

        self.game_week = GameWeek.objects.create(
            name="Week 1",
            start_at=timezone.now() - timedelta(days=7),
            end_at=timezone.now(),
            status=GameWeek.LIVE,
            season=self.game_season,
        )
        self.user1 = CustomUser.objects.create(name="user1")
        self.user2 = CustomUser.objects.create(name="user2", email='example@email.com')
        self.user3 = CustomUser.objects.create(name="user3", email='example2@email.com')

        self.team1 = Team.objects.create()
        self.team2 = Team.objects.create()
        self.competition = Competition.objects.create(name='Test Competition')

        self.match = Match.objects.create(
            match_time=timezone.now() - timedelta(days=1),
            match_end=timezone.now() - timedelta(minutes=1),
            competition=self.competition,
            season=self.season,
            home_team=self.team1,
            away_team=self.team2,
            match_type=Match.MATCH_TYPE_FREE,
            import_id='test-' + str(uuid.uuid4()),
        )

        self.game_user1 = Game.objects.create(
            user=self.user1,
            match=self.match,
            score=100

        )
        self.game_user2 = Game.objects.create(
            user=self.user2,
            match=self.match,
            score=80
        )

        self.old_match = Match.objects.create(
            season=self.season,
            match_time=timezone.now() - timezone.timedelta(days=19),
            match_end=timezone.now() - timezone.timedelta(days=18),
            competition=self.competition,
            home_team=self.team1,
            away_team=self.team2,
            match_type=Match.MATCH_TYPE_FREE,
            import_id='test-' + str(uuid.uuid4()),
        )

        # Create games for user3 outside the current game week
        self.old_game = Game.objects.create(
            user=self.user3,
            match=self.old_match,
            score=150
        )

        self.leaderboard1, created = MatchLeaderboard.objects.update_or_create(
            match=self.match,
            user=self.user1,
            defaults={
                'position': 1,
                'score': 100,
                'division': self.division
            }
        )

        self.leaderboard2, created = MatchLeaderboard.objects.update_or_create(
            match=self.match,
            user=self.user2,
            defaults={
                'position': 2,
                'score': 80,
                'division': self.division
            }
        )

        self.leaderboard3, created = MatchLeaderboard.objects.update_or_create(
            match=self.old_match,
            user=self.user3,
            defaults={
                'position': 1,
                'score': 150,
                'division': self.division2
            }
        )

        self.old_game_week = GameWeek.objects.create(
            name="Old Week",
            start_at=timezone.now() - timedelta(days=10),
            end_at=timezone.now() - timedelta(days=7),
            status=GameWeek.CLOSED,
            season=self.game_season,
        )
        self.user_division = UserDivision.objects.create(
            user=self.user3,
            division=self.division2,
            game_week=self.old_game_week
        )

        self.distributed_players = {
            self.user1.id: {
                'position': 1,
                'week_division_tier': None,
                'week_division_id': None,
                'points': self.leaderboard1.score,
                'coins': 0,
                'new_division_tier': self.division.tier,
                'new_division_id': self.division.id,
                'division_status': UserGameWeekHistory.PROMOTED,
            }, self.user2.id: {
                'position': 2,
                'week_division_tier': None,
                'week_division_id': None,
                'points': self.leaderboard2.score,
                'coins': 0,
                'new_division_tier': self.division.tier,
                'new_division_id': self.division.id,
                'division_status': UserGameWeekHistory.PROMOTED,
            }, self.user3.id: {
                'position': 1,
                'week_division_tier': self.division2.tier,
                'week_division_id': self.division2.id,
                'points': 0,
                'coins': 0,
                'new_division_tier': self.division2.tier,
                'new_division_id': self.division2.id,
                'division_status': UserGameWeekHistory.SAFE,

            }
        }

class RewardCalculationTest(BaseClassTest):
    def test_check_and_finish_week(self):
        result = check_and_finish_week(self.game_week)

        self.assertIsNone(result)
        self.assertEqual(self.game_week.status, GameWeek.FINISHED)

    def get_season_users(self):
        users = get_season_users(self.game_week)

        self.assertIn(User(id=self.user1.id, division_id=None, division_tier=None, verified=False), users)
        self.assertIn(User(id=self.user2.id, division_id=None, division_tier=None, verified=True), users)
        self.assertIn(User(id=self.user3.id, division_id=None, division_tier=None, verified=True), users)

    def test_get_global_leaderboards_without_divisions(self):
        leaderboard = get_global_leaderboards_without_divisions(self.game_week)

        self.assertEqual(leaderboard[self.user1.id], 100)
        self.assertEqual(leaderboard[self.user2.id], 80)
        self.assertEqual(leaderboard[self.user3.id], 0)

    def test_get_leaderboards_with_divisions(self):
        leaderboard = get_leaderboards_with_divisions(self.game_week)
        expected_result = {
            self.user1.id: {'division_tier': self.division.tier, 'total_score': 100.0, 'rank': 1},
            self.user2.id: {'division_tier': self.division.tier, 'total_score': 80.0, 'rank': 2},
            self.user3.id: {'division_tier': self.division2.tier, 'total_score': 0.0, 'rank': 1},
        }

        self.assertEqual(set(leaderboard.keys()), set(expected_result.keys()),
                         "The keys of the actual result do not match the expected keys.")

        for user_id, expected_data in expected_result.items():
            self.assertIn(user_id, leaderboard, f"User ID {user_id} not found in the actual result.")
            actual_data = leaderboard[user_id]

            self.assertEqual(actual_data['division_tier'], expected_data['division_tier'],
                             f"Division tier for user {user_id} does not match.")
            self.assertEqual(actual_data['total_score'], expected_data['total_score'],
                             f"Total score for user {user_id} does not match.")
            self.assertEqual(actual_data['rank'], expected_data['rank'], f"Rank for user {user_id} does not match.")

    def test_distribute_players(self):
        leaderboards = get_global_leaderboards_without_divisions(self.game_week)
        divisions = Division.objects.all()
        users = get_season_users(self.game_week)
        relegation_ranges = {i.tier: (0.2, 0.5) for i in divisions}
        promotion_ranges = {i.tier: (0.2, 0.5) for i in divisions}
        distribution_service = OrToolsDistributionStrategy(divisions, relegation_ranges, promotion_ranges, True)
        distribution_data = distribution_service.distribute(users, leaderboards)

        self.assertIsNotNone(distribution_data)

    def test_create_history_data(self):
        create_history_data(self.game_week, self.distributed_players)

        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user1, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user2, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user3, game_week=self.game_week).exists())


    def test_create_new_week(self):
        new_week = create_new_week(self.game_week)

        self.assertEqual(new_week.status, GameWeek.LIVE)
        self.assertEqual(new_week.season, self.game_season)


    def test_assign_user_to_division(self):
        new_week = create_new_week(self.game_week)
        assign_user_to_division(self.distributed_players, new_week.id)

        self.assertTrue(UserDivision.objects.filter(user=self.user1, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user2, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user3, game_week=new_week).exists())

    def test_calculate_rewards(self):
        rewards = DivisionReward.objects.filter(week=self.game_week)
        user_rewards, _players = calculate_rewards(rewards, self.distributed_players)

        self.assertEqual(user_rewards[0]['reward'], 600)
        self.assertEqual(user_rewards[1]['reward'], 300)
        self.assertEqual(user_rewards[2]['reward'], 666.6666666666667)

    def test_process_week_rewards(self):
        players = self.distributed_players
        self.game_week.status = GameWeek.FINISHED
        process_week_rewards(self.game_week, players)
        transactions = Transactions.objects.filter(week=self.game_week)

        self.assertEqual(len(list(transactions)), 3)
        self.assertEqual(transactions[0].user_id, self.user1.id)
        self.assertEqual(transactions[1].user_id, self.user2.id)
        self.assertEqual(transactions[2].user_id, self.user3.id)

class ConcludeGameWeekTest(BaseClassTest):
    def test_conclude_game_week(self):
        distribution_data = conclude_game_week(self.game_week)
        self.distributed_players[self.user1.id]['coins'] = 600
        self.distributed_players[self.user2.id]['coins'] = 300
        self.distributed_players[self.user3.id]['coins'] = 666.6666666666667
        self.distributed_players[self.user1.id]['new_division_id'] = self.division.id
        self.distributed_players[self.user2.id]['new_division_id'] = self.division.id
        self.distributed_players[self.user3.id]['new_division_id'] = self.division2.id
        self.distributed_players[self.user1.id]['new_division_tier'] = self.division.tier
        self.distributed_players[self.user2.id]['new_division_tier'] = self.division.tier
        self.distributed_players[self.user3.id]['new_division_tier'] = self.division2.tier

        self.assertEqual(set(distribution_data.keys()), set(self.distributed_players.keys()),
                         "The keys of the actual result do not match the expected keys.")

        for user_id, expected_data in self.distributed_players.items():
            self.assertIn(user_id, distribution_data, f"User ID {user_id} not found in the actual result.")
            actual_data = distribution_data[user_id]

            self.assertEqual(actual_data['new_division_id'], expected_data['new_division_id'],
                             f"new_division_id tier for user {user_id} does not match.")
            self.assertEqual(actual_data['week_division_id'], expected_data['week_division_id'],
                             f"week_division_id tier for user {user_id} does not match.")
            self.assertEqual(actual_data['division_status'], expected_data['division_status'],
                             f"division_status tier for user {user_id} does not match.")
            self.assertEqual(actual_data['new_division_tier'], expected_data['new_division_tier'],
                             f"Division tier for user {user_id} does not match.")
            self.assertEqual(actual_data['coins'], expected_data['coins'],
                             f"Coins for user {user_id} does not match.")
            self.assertEqual(actual_data['points'], expected_data['points'],
                             f"Total points for user {user_id} does not match.")
            self.assertEqual(actual_data['week_division_tier'], expected_data['week_division_tier'],
                             f"Week_division_tier for user {user_id} does not match.")
            self.assertEqual(actual_data['position'], expected_data['position'], f"Rank for user {user_id} does not match.")

        self.game_week.refresh_from_db()
        self.assertEqual(self.game_week.status, GameWeek.CLOSED)

        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user1, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user2, game_week=self.game_week).exists())
        self.assertTrue(UserGameWeekHistory.objects.filter(user=self.user3, game_week=self.game_week).exists())

        transactions = list(Transactions.objects.filter(week=self.game_week).order_by('user_id'))
        self.assertEqual(len(transactions), 3)
        user_ids = sorted([self.user1.id, self.user2.id, self.user3.id])
        transaction_user_ids = [transaction.user_id for transaction in transactions]

        self.assertEqual(transaction_user_ids, user_ids)

        new_week = GameWeek.objects.get(status=GameWeek.LIVE)
        start_at = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_at = start_at + timedelta(days=6, hours=23, minutes=59, seconds=59)

        self.assertEqual(new_week.status, GameWeek.LIVE)
        self.assertEqual(new_week.start_at, start_at)
        self.assertEqual(new_week.end_at, end_at)
        self.assertEqual(new_week.season, self.game_season)

        self.assertTrue(UserDivision.objects.filter(user=self.user1, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user2, game_week=new_week).exists())
        self.assertTrue(UserDivision.objects.filter(user=self.user3, game_week=new_week).exists())

class TestDistribution(BaseClassTest):
    def test_ortools_distributor(self):
        divisions = Division.objects.all()
        s = OrToolsDistributionStrategy(
            [SDivision(div.id, div.tier, div.percentage) for div in divisions],
            {div.tier: (div.relegation_min_range, div.relegation_max_range) for div in divisions},
            {div.tier: (div.promotion_min_range, div.promotion_max_range) for div in divisions},
            True,
        )
        population = {}
        for division in divisions:
            population[division.id] = division.tier * 100
        print(s.calculate_capacity(population))