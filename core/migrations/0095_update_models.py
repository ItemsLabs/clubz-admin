# Generated by Django 2.2 on 2024-02-07 00:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0094_update_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('season', 'Season'), ('country', 'Country'), ('team', 'Team')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaderboards', to='core.Season')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaderboards', to='core.Team')),
            ],
            options={
                'db_table': 'leaderboards',
            },
        ),
        migrations.CreateModel(
            name='MatchDay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'match_days',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='match_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='core.MatchDay'),
        ),
        migrations.CreateModel(
            name='UserLeaderboardSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscription_date', models.DateTimeField(auto_now_add=True)),
                ('leaderboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Leaderboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
            ],
            options={
                'db_table': 'user_leaderboard_subscriptions',
                'unique_together': {('user', 'leaderboard')},
            },
        ),
    ]
