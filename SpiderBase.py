import requests
import pymysql

from config import MySQLConfig


class SpiderBase:
    def __init__(self):
        self.db = pymysql.connect(
            host=MySQLConfig.host, port=MySQLConfig.port, user=MySQLConfig.user, password=MySQLConfig.password,
            database=MySQLConfig.database, charset='utf8'
        )
        self.cursor = self.db.cursor()

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
        sql = '''
        INSERT INTO museum_items_of_china
        (museum, title, era, material, size, description, detail_url, image, download_link)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.cursor.executemany(sql, items)
        self.db.commit()
