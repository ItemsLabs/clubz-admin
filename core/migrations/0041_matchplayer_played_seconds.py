# Generated by Django 2.1.7 on 2019-04-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20190423_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='played_seconds',
            field=models.IntegerField(null=True),
        ),
    ]
