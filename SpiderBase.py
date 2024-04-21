import requests
import pymysql

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tmt.v20180321 import tmt_client, models

import config
from config import MySQLConfig


class SpiderBase:

    def __init__(self):
        self.db = pymysql.connect(
            host=MySQLConfig.host, port=MySQLConfig.port, user=MySQLConfig.user, password=MySQLConfig.password,
            database=MySQLConfig.database, charset='utf8'
        )
        self.cursor = self.db.cursor()
        self._tmt_client = None

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
        sql = f'''
        INSERT INTO {'museum_items_of_china' if not config.DEBUG else 'test_museum_crawl'}
        (museum, title, era, material, size, description, detail_url, image, download_link, geo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.cursor.executemany(sql, items)
        self.db.commit()

    @property
    def qcloud_client(self):
        if self._tmt_client:
            return self._tmt_client
        cred = credential.Credential(config.TencentSecretKey.secretId, config.TencentSecretKey.secretKey)
        http_profile = HttpProfile()
        http_profile.endpoint = "tmt.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile

        self._tmt_client = tmt_client.TmtClient(cred, "ap-beijing", client_profile)
        return self._tmt_client

    def batch_translate(self, texts, source, target):
        req = models.TextTranslateBatchRequest()
        params = {
            "Source": source,
            "Target": target,
            "ProjectId": 0,
            "SourceTextList": texts
        }
        req.from_json_string(json.dumps(params))

        resp = self.qcloud_client.TextTranslateBatch(req)
        return resp.TargetTextList
