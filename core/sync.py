import logging
import uuid

import requests
from django.conf import settings
from django.db import transaction

from core.models import Team, Player
from util import gce


def update_avg_score():
    players_qs = Player.objects.all()[:9999999]
    len_players = len(players_qs)

    count = 0
    for player in players_qs:
        player.avg_score = player.calculate_avg_score()
        player.save(update_fields=['avg_score'])
        count += 1
        if count % 100 == 0:
            print('processed {} out of {} records'.format(count, len_players))


def sync_missing_team_crests():
    for team in Team.objects.filter(crest_url__isnull=True):
        import_id = team.import_id.replace('t', '')
        image_url = 'https://ufl-crests.s3.amazonaws.com/{}.png'.format(import_id)
        res = requests.get(image_url)
        if res.status_code != 200:
            logging.error("cannot get image by url {}".format(image_url))
            continue

        new_filename = str(uuid.uuid4()) + ".png"

        # upload image to gce
        bucket = settings.GCE_TEAM_CRESTS_BUCKET
        try:
            gce.upload_file(bucket, new_filename, res.content, res.headers['content-type'])
            new_image_url = gce.get_file_url(bucket, new_filename)
        except Exception:
            logging.exception("cannot upload file to gce")
            continue

        # update in db
        team.crest_url = new_image_url
        team.save(update_fields=['crest_url'])

        logging.info("team {} synced".format(team.pk))

def normalize_and_check_all_names():
    with transaction.atomic():
        players = Player.objects.iterator()  # for large dataset
        to_update = []

        for player in players:
            current_normalized_name = player.normalized_name
            new_normalized_name = player.calculate_normalized_name()
            if new_normalized_name != current_normalized_name:
                player.normalized_name = new_normalized_name
                to_update.append(player)

        # Bulk update all changed records
        if to_update:
            Player.objects.bulk_update(to_update, ['normalized_name'])
        
        print(f"Updated {len(to_update)} players with new normalized names.")