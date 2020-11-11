from typing import Optional, Dict
import json

from ksimpleapi import Api


class RandomApi(Api):

    def __init__(
        self,
        user_agent: str
    ):
        super().__init__(user_agent=user_agent)


    @property
    def extra_headers(self) -> Optional[Dict[str, any]]:
        return {
            'Accept': 'json'
        }

    def random_get_request(self):
        return self._get('https://www.google.com')


some_random_ua = 'Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36 Avast/81.0.3737.69'
api = RandomApi(some_random_ua)
response = api.random_get_request()

print(json.dumps(dict(response.request.headers), indent=4))