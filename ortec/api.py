import logging
import requests
from cachetools import TTLCache

logger = logging.getLogger()


class OrtecAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # 30 minutes cache
        self.token_cache = TTLCache(maxsize=10, ttl=60 * 30)

    @staticmethod
    def _build_url(path):
        return 'https://sports.ortec-hosting.com/EIADataFeedApi{}'.format(path)

    def get_token(self):
        try:
            return self.token_cache['token']
        except KeyError:
            token = self.generate_new_token()
            self.token_cache['token'] = token
            return token

    def generate_new_token(self):
        url = self._build_url('/api/token')
        res = requests.post(url, json={"username": self.username, "password": self.password})
        return res.json()

    def get_competitions(self):
        return self._process_request('/api/Competition')

    def get_competition_editions(self, competition_id):
        return self._process_request('/api/Competition/competitioneditions/{}'.format(competition_id))

    def get_competition_phases(self, competition_edition_id):
        return self._process_request('/api/Competition/competitionphases/{}'.format(competition_edition_id))

    def get_registrations(self, competition_phase_id):
        return self._process_request('/api/Competition/competitionphases/{}/registrations'.format(competition_phase_id))

    def get_registration(self, registration_id):
        return self._process_request('/api/RegistrationData/{}'.format(registration_id))

    def get_selection_persons(self, selection_id):
        return self._process_request('/api/selections/persons/{}'.format(selection_id))

    def _process_request(self, path, data=None):
        final_url = self._build_url(path)
        logger.info("Making request to {}".format(final_url))

        res = requests.get(final_url, data, headers={
            'Authorization': 'Session {}'.format(self.get_token())
        })

        if res.status_code != 200:
            raise Exception(
                'Received invalid status code {} for {}: {}'.format(res.status_code, final_url, res.content))
        return res.json()
