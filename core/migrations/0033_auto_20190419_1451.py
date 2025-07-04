# Generated by Django 2.1.7 on 2019-04-19 14:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20190416_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptaFeedItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unique_id', models.BigIntegerField()),
                ('event_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'opta_feed_items',
            },
        ),
        migrations.CreateModel(
            name='OptaFeedItemVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'No Diff'), (3, 'Partial Cancel'), (4, 'Full Cancel')])),
                ('version', models.BigIntegerField()),
                ('last_modified_at', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.OptaFeedItem')),
            ],
            options={
                'db_table': 'opta_feed_item_versions',
            },
        ),
        migrations.AddField(
            model_name='gameevent',
            name='match_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.MatchEvent'),
        ),
        migrations.AddField(
            model_name='optafeeditem',
            name='current_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.OptaFeedItemVersion'),
        ),
        migrations.AddField(
            model_name='optafeeditem',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Match'),
        ),
        migrations.AddField(
            model_name='matchevent',
            name='opta_feed_item_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.OptaFeedItemVersion'),
        ),
        migrations.AlterUniqueTogether(
            name='optafeeditem',
            unique_together={('unique_id', 'event_id')},
        ),
    ]
