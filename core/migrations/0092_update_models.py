# Generated by Django 2.2 on 2024-02-03 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
