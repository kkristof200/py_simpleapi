from typing import Optional, Dict
import json

from ksimpleapi import Api


class RandomApi(Api):

    def __init__(self, user_agent: str):
        super().__init__(user_agent=user_agent)


    @classmethod
    def extra_headers(self) -> Optional[Dict[str, any]]:
        return {
            'Accept': 'json'
        }

    def random_get_request(self):
        return self._get('https://www.google.com')

    @classmethod
    def random_get_request_cls(cls, user_agent: str):
        return cls._get_cls('https://www.google.com', user_agent=user_agent)


some_random_ua = 'Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36 Avast/81.0.3737.69'
api = RandomApi(some_random_ua)
response1 = api.random_get_request()
response2 = RandomApi.random_get_request_cls(some_random_ua)

print(response1, json.dumps(dict(response1.request.headers), indent=4))
print(response2, json.dumps(dict(response2.request.headers), indent=4))