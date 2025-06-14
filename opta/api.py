import logging
import requests
from django.conf import settings

logger = logging.getLogger()


class OptaAPI:
    def __init__(self, outletAuthKey, mode, dataformat):
        self.outletAuthKey = outletAuthKey
        self.mode = mode
        self.dataformat = dataformat

    def get_proxies(self):
        proxy_url = settings.OPTA_PROXY
        if proxy_url is None or proxy_url == "":
            return None
        return {
            'http': proxy_url,
            'https': proxy_url,
        }

    def get_competitions(self):
        return self._process_request("/tournamentcalendar", "/active/authorized")

    def get_competition_phases(self, tournamentCalendarUuid):
        return self._process_request(f"/standings", "", f"tmcl={tournamentCalendarUuid}")

    def get_schedule(self, tournamentCalendarUuid):
        return self._process_request(f"/tournamentschedule", f"/{tournamentCalendarUuid}")

    def get_selection_persons(self, tournamentCalendarUuid, contestantUUID):
        # with stats info for the players, currently not needed
        # return self._process_request(f"/squads", "", f"tmcl={tournamentCalendarUuid}&ctst={contestantUUID}&detailed=yes")
        return self._process_request(f"/squads", "", f"tmcl={tournamentCalendarUuid}&ctst={contestantUUID}&detailed=no")

    def get_match_events(self, match_id):
        return self._process_request(f"/matchevent", f"", f"fx={match_id}")

    def get_match_stats(self, match_id, detailed="yes"):
        return self._process_request(f"/matchstats", f"/{match_id}", f"detailed={detailed}")

    @staticmethod
    def _build_url(self, path, extraPath="", extraQuery=""):
        if extraQuery and extraQuery != "" and extraQuery != None:
            extraQuery = "&" + extraQuery
        q = f"?_rt={self.mode}&_fmt={self.dataformat}" + extraQuery
        url = f"https://api.performfeeds.com/soccerdata{path}/{self.outletAuthKey}{extraPath}" + q
        # print(url)
        return url

    def _process_request(self, path, extraPath="", extraQueryString="", data=None):
        final_url = self._build_url(self, path, extraPath, extraQueryString)
        # logger.info("Making request to {}".format(final_url))
        # print("Making request to {}".format(final_url))

        res = requests.get(
            final_url,
            data,
            proxies=self.get_proxies(),
            # headers={"Authorization": "Session {}".format(self.get_token())},
        )

        if res.status_code != 200:
            raise Exception(
                "Received invalid status code {} for {}: {}".format(
                    res.status_code, final_url, res.content
                )
            )
        return res.json()
