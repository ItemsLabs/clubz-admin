import logging
import pathlib
import uuid
import json
from datetime import datetime
from multiprocessing.pool import ThreadPool

import requests
from django.conf import settings
from django.db import transaction

from soccer_wiki.models import SoccerWikiPlayer
from util import gce

logger = logging.getLogger("soccerwiki")

def sync_players():
    print('sync_players')
    logger.info('downloading players from soccerwiki')
    r = requests.get(
        "https://en.soccerwiki.org/download-data.php?format=1&options%5B%5D=PlayerData&countryId=&submit=Download+Data")
    if r.status_code == 200:
        sync_players_from_json(r.json())

def sync_players_from_json(data):
    player_data = data.get('PlayerData', [])
    count = 0
    logger.info('syncing {} players'.format(len(player_data)))
    print('syncing {} players'.format(len(player_data)))
    for el in player_data:
        try:
            player_id = int(el.get("ID", "0"))
            first_name = el.get("Forename", "")
            second_name = el.get("Surname", "")
            birth_date = el.get("Birthdate", "")  # Assuming Birthdate field exists, correct if different
            height = int(el.get("Height", "0"))         # Assuming Height field exists, correct if different
            weight = int(el.get("Weight", "0"))         # Assuming Weight field exists, correct if different
            image = el.get("ImageURL", "")
        except ValueError:
            logger.error("Invalid data encountered for player with raw ID: {}".format(el.get("ID", "")))
            print("Invalid data encountered for player with raw ID: {}".format(el.get("ID", "")))
            continue


        try:
            birth_date_parsed = datetime.strptime(birth_date, "%Y-%m-%d") if birth_date else None
        except Exception:
            birth_date_parsed = None

        try:
            player = SoccerWikiPlayer.objects.get(import_id=player_id)
            update_fields = []
            if first_name != player.first_name:
                update_fields.append('first_name')
                player.first_name = first_name

            if second_name != player.second_name:
                update_fields.append('second_name')
                player.second_name = second_name

            if birth_date_parsed != player.birth_date:
                update_fields.append('birth_date')
                player.birth_date = birth_date_parsed

            if height != player.height:
                update_fields.append('height')
                player.height = height

            if weight != player.weight:
                update_fields.append('weight')
                player.weight = weight

            if image != player.image:
                update_fields += ['image', 'internal_image_status', 'internal_image_url']
                player.image = image
                player.internal_image_status = SoccerWikiPlayer.STATUS_UNKNOWN
                player.internal_image_url = image

            if len(update_fields) > 0:
                player.save(update_fields=update_fields)

        except SoccerWikiPlayer.DoesNotExist:
            SoccerWikiPlayer.objects.create(
                import_id=player_id,
                first_name=first_name,
                second_name=second_name,
                birth_date=birth_date_parsed,
                height=height,
                weight=weight,
                image=image,
            )

        count += 1

        if count % 1000 == 0:
            logger.info('processed {} out of {}'.format(count, len(player_data)))
    logger.info('synced {} players'.format(count))
    print('synced {} players'.format(count))
    return count
def process_soccer_wiki_player(player_id):
    bucket = settings.GCE_PLAYER_IMAGES_BUCKET

    # lock for processing
    with transaction.atomic():
        player = SoccerWikiPlayer.objects.select_for_update().get(pk=player_id)

        if player.internal_image_status != SoccerWikiPlayer.STATUS_UNKNOWN:
            return

        if not player.image:
            player.internal_image_status = SoccerWikiPlayer.STATUS_ERROR
            player.save(update_fields=['internal_image_status'])
            return

        # download image
        try:
            image_url = player.image
            res = requests.get(image_url, timeout=(3, 20))

            if res.status_code != 200:
                logger.info('cannot get image {}: {}'.format(image_url, res.status_code))
                player.internal_image_status = 4
                player.save(update_fields=['internal_image_status'])
                return
        except Exception:
            logger.error('cannot get image {}'.format(player.image))
            player.internal_image_status = 4
            player.save(update_fields=['internal_image_status'])
            return

        # get extension of file
        extension = pathlib.Path(player.image).suffix

        # upload image to gce
        new_filename = str(uuid.uuid4()) + extension

        try:
            new_image_url = gce.upload_file(bucket, new_filename, res.content, res.headers['content-type'])
            player.internal_image_status = SoccerWikiPlayer.STATUS_SUCCESS
            player.internal_image_url = new_image_url
            player.save(update_fields=['internal_image_status', 'internal_image_url'])
        except Exception:
            logger.exception("cannot upload image to gce")
            player.internal_image_status = 5
            player.save(update_fields=['internal_image_status'])

    logger.info("{} processed".format(player_id))
    print("{} processed".format(player_id))

def upload_soccer_wiki_photos():
    logger.info('uploading soccer wiki photos')
    print('uploading soccer wiki photos')
    player_ids = SoccerWikiPlayer.objects. \
        filter(internal_image_status=SoccerWikiPlayer.STATUS_UNKNOWN).values_list("id", flat=True)

    pool = ThreadPool(10)
    pool.map(process_soccer_wiki_player, player_ids)
    logger.info('uploaded {} photos'.format(len(player_ids)))
    return len(player_ids)

