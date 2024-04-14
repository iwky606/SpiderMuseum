import requests
import pymysql

class SpiderBase:
    def __init__(self):
        # pymysql.connect('')
        pass

    @property
    def is_debug(self):
        return True

    def req_post(self, url, params):
        return requests.post(url, json=params, headers=self.headers)

    def req_get(self, url, params=None):
        return requests.get(url, data=params, headers=self.headers)

    @property
    def headers(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

    def save_to_mysql(self, items):
        pass
