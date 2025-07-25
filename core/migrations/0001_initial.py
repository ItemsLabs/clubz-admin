# Generated by Django 2.1.7 on 2019-03-09 17:34

from django.db import migrations, models
import django.db.models.deletion
import uuid

def create_third_party_extension(apps, schema_editor):
    schema_editor.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")


def drop_third_party_extension(apps, schema_editor):
    schema_editor.execute("DROP EXTENSION IF EXISTS pg_trgm;")


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_third_party_extension, reverse_code=drop_third_party_extension, atomic=True),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'competitions',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
                ('iso', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('device_id', models.CharField(max_length=400, unique=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='w', max_length=1)),
                ('version', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='GamePick',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ended_at', models.DateTimeField(null=True)),
                ('position', models.IntegerField()),
                ('score', models.FloatField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='picks', to='core.Game')),
            ],
            options={
                'db_table': 'game_picks',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('match_time', models.DateTimeField()),
                ('last_processed_id', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'matches',
            },
        ),
        migrations.CreateModel(
            name='MatchEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField()),
                ('type', models.IntegerField()),
                ('points', models.FloatField(null=True)),
                ('payload', models.TextField(null=True)),
                ('minute', models.IntegerField()),
                ('second', models.IntegerField()),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
                ('match_event_id', models.IntegerField()),
                ('provider_id', models.CharField(max_length=30)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'match_events',
            },
        ),
        migrations.CreateModel(
            name='MatchEventProcessor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(1, 'scores')])),
                ('last_processed_id', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match')),
            ],
            options={
                'db_table': 'match_event_processors',
            },
        ),
        migrations.CreateModel(
            name='OptaFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('processing_started', models.DateTimeField(null=True)),
                ('processing_ended', models.DateTimeField(null=True)),
                ('feed_object_id', models.CharField(max_length=50, unique=True)),
                ('feed_hash', models.TextField(null=True)),
                ('feed_type', models.CharField(choices=[('F1', 'F1'), ('F24', 'F24'), ('F40', 'F40')], max_length=3)),
                ('status', models.IntegerField(choices=[(1, 'Received'), (2, 'Processing'), (3, 'Processed'), (4, 'Error')], default=1)),
                ('headers', models.TextField()),
            ],
            options={
                'db_table': 'opta_feeds',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('first_name', models.TextField(null=True)),
                ('last_name', models.TextField(null=True)),
                ('full_name', models.TextField(null=True)),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='SeasonCompetitionMember',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Competition')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season')),
            ],
            options={
                'db_table': 'season_competition_members',
            },
        ),
        migrations.CreateModel(
            name='SeasonTeamPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season')),
            ],
            options={
                'db_table': 'season_team_players',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('import_id', models.CharField(max_length=15, unique=True)),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Country')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Region')),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team')),
            ],
            options={
                'db_table': 'team_players',
            },
        ),
        migrations.AddField(
            model_name='seasonteamplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
        migrations.AddField(
            model_name='seasoncompetitionmember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
        migrations.AddField(
            model_name='matchevent',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player'),
        ),
        migrations.AddField(
            model_name='matchevent',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='away_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Competition'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='home_team', to='core.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Season'),
        ),
        migrations.AddField(
            model_name='gamepick',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.AlterUniqueTogether(
            name='seasonteamplayer',
            unique_together={('player', 'team', 'season')},
        ),
        migrations.AlterIndexTogether(
            name='seasonteamplayer',
            index_together={('player', 'team', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='seasoncompetitionmember',
            unique_together={('competition', 'team', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='matcheventprocessor',
            unique_together={('match', 'type')},
        ),
        migrations.AlterUniqueTogether(
            name='matchevent',
            unique_together={('match', 'match_event_id')},
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('match', 'user')},
        ),
    ]
