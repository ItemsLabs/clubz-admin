# Generated by Django 2.2 on 2024-08-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0173_appinbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinbox',
            name='user_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
