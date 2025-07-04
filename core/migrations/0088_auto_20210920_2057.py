# Generated by Django 2.2 on 2021-09-20 20:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0087_customuser_last_name_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team_selection_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_selection_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='SelectionTeamPlayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('selection_id', models.CharField(max_length=10)),
                ('position', models.CharField(
                    choices=[('d', 'Defender'), ('m', 'Midfielder'), ('f', 'Forward'), ('g', 'Goalkeeper'),
                             ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True)),
                ('jersey_number', models.IntegerField(null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Team')),
            ],
            options={
                'db_table': 'selection_team_players',
                'unique_together': {('selection_id', 'team', 'player')},
                'index_together': {('selection_id', 'team', 'player')},
            },
        ),
    ]
