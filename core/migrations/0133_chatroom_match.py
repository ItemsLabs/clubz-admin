# Generated by Django 2.2 on 2024-06-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0132_update_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='chat_rooms', to='core.Match'),
        ),
    ]
