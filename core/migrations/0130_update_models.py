# Generated by Django 2.2 on 2024-06-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0129_update_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='finished_games',
            field=models.TextField(blank=True, null=True),
        ),
    ]
