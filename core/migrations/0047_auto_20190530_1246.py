# Generated by Django 2.1.7 on 2019-05-30 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_matchplayer_avg_score'),
    ]

    operations = [
        migrations.RunSQL(
            '''create index idx_matches_time_and_type on matches(match_time) where match_type != 0;''',
            '''drop index idx_matches_time_and_type;'''
        )
    ]
