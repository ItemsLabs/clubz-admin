# Generated by Django 2.2 on 2024-04-19 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0113_update_position_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroommember',
            name='mod',
            field=models.BooleanField(default=False),
        ),
    ]
