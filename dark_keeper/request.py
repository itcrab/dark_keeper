import random
import time

import requests

from .cache import from_cache, to_cache, get_cache_dir
from .exceptions import DarkKeeperRequestResponseError


class Request(object):
    def __init__(self, delay, base_url, user_agent=None):
        self.delay = delay if isinstance(delay, list) and len(delay) == 2 else [1, 2]
        self.cache_dir = get_cache_dir(base_url)

        self.headers = None
        if user_agent:
            self.headers = {
                'User-Agent': user_agent
            }

    def receive_html(self, url):
        html = from_cache(url, self.cache_dir)
        if not html:
            self._delay()

            html = self._from_url(url)

            to_cache(url, self.cache_dir, html)

        return html

    def _delay(self):
        time.sleep(random.uniform(self.delay[0], self.delay[1]))

    def _from_url(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise DarkKeeperRequestResponseError(e)

        html = response.content

        return html
