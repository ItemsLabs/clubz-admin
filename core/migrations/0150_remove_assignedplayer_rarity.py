# Generated by Django 2.2 on 2024-07-18 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0149_auto_20240717_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedplayer',
            name='rarity',
        ),
    ]
