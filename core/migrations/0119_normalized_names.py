from django.db import migrations

def fill_normalized_name(apps, schema_editor):
    Player = apps.get_model('core', 'Player')
    db_alias = schema_editor.connection.alias
    players = Player.objects.using(db_alias).all()
    for player in players:
        if player.nick_name and not any(char + '.' in player.nick_name for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            player.normalized_name = player.nick_name
        else:
            player.normalized_name = player.full_name
        player.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_player_normalized_name'), 
    ]

    operations = [
        migrations.RunPython(fill_normalized_name),
    ]
