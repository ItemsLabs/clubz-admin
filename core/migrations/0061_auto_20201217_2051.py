# Generated by Django 2.1.7 on 2020-12-17 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_auto_20201217_2051'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchplayer',
            unique_together={('match', 'player', 'team')},
        ),
    ]
