# Generated by Django 2.2 on 2024-04-04 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0108_update_feed_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchleaderboard',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Transactions'),
        ),
    ]
