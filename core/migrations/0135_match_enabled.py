# Generated by Django 2.2 on 2024-06-12 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0134_chatroom_import_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
