# Generated by Django 2.1.7 on 2019-04-05 21:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0029_competition_short_name'),
    ]

    operations = [
        migrations.RunSQL(
            '''create unique index idx_game_picks_position_uk on game_picks(game_id, position) where ended_at is null;''',
            '''drop index idx_game_picks_position_uk;''',
        ),
        migrations.RunSQL(
            '''create unique index idx_game_picks_player_uk on game_picks(game_id, player_id) where ended_at is null;''',
            '''drop index idx_game_picks_player_uk;''',
        ),
    ]
