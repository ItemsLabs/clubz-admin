# Generated by Django 2.2 on 2024-10-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0190_pushnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpacktype',
            name='collection',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
