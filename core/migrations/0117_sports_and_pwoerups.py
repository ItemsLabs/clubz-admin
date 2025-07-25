# Generated by Django 2.2 on 2024-05-14 12:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0116_competition_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sports',
            },
        ),
        migrations.AddField(
            model_name='powerup',
            name='cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='powerup',
            name='type',
            field=models.IntegerField(choices=[(1, 'event'), (2, 'game')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
        migrations.AddField(
            model_name='powerup',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sport'),
        ),
    ]
