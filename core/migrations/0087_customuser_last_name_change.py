# Generated by Django 2.2 on 2021-06-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_customuser_avg_rank_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_name_change',
            field=models.DateTimeField(null=True),
        ),
    ]
