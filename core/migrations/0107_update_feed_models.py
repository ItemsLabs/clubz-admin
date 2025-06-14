from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0106_update_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='ortec_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='opta_selection_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='competitionedition',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='competitionphase',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='import_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='selectionteamplayer',
            name='selection_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='match',
            name='edition',
            field=models.ForeignKey(null=True, on_delete=models.deletion.DO_NOTHING, to='core.CompetitionEdition'),
        ),
    ]
