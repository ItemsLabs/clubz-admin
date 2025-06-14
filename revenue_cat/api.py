import logging
import requests
from cachetools import TTLCache

logger = logging.getLogger()


class RevenueCatAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def _build_url(path):
        return 'https://api.revenuecat.com{}'.format(path)

    def get_subscriber(self, user_id):
        return self._process_request('/v1/subscribers/{}'.format(user_id))

    def _process_request(self, path, data=None):
        final_url = self._build_url(path)
        logger.info("Making request to {}".format(final_url))

        res = requests.get(final_url, data, headers={
            'Authorization': 'Bearer {}'.format(self.api_key)
        })

        if res.status_code != 200:
            raise Exception(
                'Received invalid status code {} for {}: {}'.format(res.status_code, final_url, res.content))
        return res.json()
