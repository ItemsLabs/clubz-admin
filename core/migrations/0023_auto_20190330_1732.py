# Generated by Django 2.1.7 on 2019-03-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_matchplayer_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepick',
            name='minute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepick',
            name='second',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepowerup',
            name='minute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamepowerup',
            name='second',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='minute',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='second',
            field=models.IntegerField(default=0),
        ),
    ]
