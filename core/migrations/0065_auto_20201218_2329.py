# Generated by Django 2.1.7 on 2020-12-18 23:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0064_auto_20201218_2200'),
    ]

    operations = [
        migrations.RunSQL(
            """CREATE INDEX IF NOT EXISTS soccer_wiki_player_gin_idx 
                ON soccer_wiki_players USING gin ((first_name||' '||second_name) gin_trgm_ops);""",
            """DROP INDEX soccer_wiki_player_gin_idx;""",
        ),
    ]
