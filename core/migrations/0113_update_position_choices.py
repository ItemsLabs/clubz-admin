# Generated by Django 2.2 on 2024-04-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0112_update_import_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Wing Back'), ('d', 'Defender'), ('m', 'Defensive Midfielder'), ('m', 'Midfielder'), ('m', 'Attacking Midfielder'), ('f', 'Striker'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='seasonteamplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Wing Back'), ('d', 'Defender'), ('m', 'Defensive Midfielder'), ('m', 'Midfielder'), ('m', 'Attacking Midfielder'), ('f', 'Striker'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='selectionteamplayer',
            name='position',
            field=models.CharField(choices=[('d', 'Wing Back'), ('d', 'Defender'), ('m', 'Defensive Midfielder'), ('m', 'Midfielder'), ('m', 'Attacking Midfielder'), ('f', 'Striker'), ('g', 'Goalkeeper'), ('s', 'Substitute'), ('u', 'Unknown')], max_length=1, null=True),
        ),
    ]
