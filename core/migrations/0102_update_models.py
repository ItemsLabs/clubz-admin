# Generated by Django 2.2 on 2024-02-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0101_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verification_token',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
