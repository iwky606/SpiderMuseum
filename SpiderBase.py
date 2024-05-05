import sys

import requests
import pymysql

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tmt.v20180321 import tmt_client, models
import time
import config
from config import MySQLConfig


def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_time_called = [0.0]

        def rate_limited_function(*args, **kwargs):
            elapsed = time.perf_counter() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_time_called[0] = time.perf_counter()
            return ret

        return rate_limited_function

    return decorate


class SpiderBase:

    def __init__(self):
        self.db = self.get_db()
        self.cursor = self.db.cursor()
        self._tmt_client = None
        print(f"当前是debugmode:{self.debug}")

    def get_db(self):
        return pymysql.connect(
            host=MySQLConfig.host, port=MySQLConfig.port, user=MySQLConfig.user, password=MySQLConfig.password,
            database=MySQLConfig.database, charset='utf8'
        )

    def reload_db(self):
        self.db = self.get_db()
        self.cursor = self.db.cursor()

    def req_post(self, url, json=None, params=None, data=None):
        return requests.post(url, json=json, params=params, data=data, headers=self.headers)

    def req_get(self, url, params=None):
        return requests.get(url, data=params, headers=self.headers)

    @property
    def headers(self):
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39'
        ]
        import random
        return {"User-Agent": random.choice(user_agents)}

    @property
    def debug(self):
        for i in sys.argv:
            if i == '1':
                return False
        return True

    def save_to_mysql(self, items):
        print("[+] 开始写入数据库")
        print('\n'.join([str(i) for i in items]))
        sql = f'''
            INSERT INTO {'museum_items_of_china_v2' if not self.debug else 'test_museum_crawl'}
            (museum, title, era, material, size, description, detail_url, image, download_link, geo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
        self.cursor.executemany(sql, items)
        self.db.commit()
        print("[-] 写入完成")

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

    @rate_limited(5)
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

    def translate_item(self, source, item):
        try:
            texts = []
            for key in item.keys():
                if key not in self.need_translate:
                    continue
                texts.append(str(item[key]))
            res = self.batch_translate(texts, source, 'zh') if texts else None
            index = 0
            for key in item.keys():
                if key not in self.need_translate:
                    continue
                item[key] = res[index] if item[key] else None
                index += 1
        except Exception:
            print(item)
            texts = []
            for key in item.keys():
                if key not in self.need_translate or key == 'description':
                    continue
                texts.append(str(item[key]))
            res = self.batch_translate(texts, source, 'zh') if texts else None

            index = 0
            for key in item.keys():
                if key not in self.need_translate or key == 'description':
                    continue
                item[key] = res[index] if item[key] else None
                index += 1

            res = self.batch_translate([item['description'][:5000]], source, 'zh') if texts else None
            item['description'] = res[0]

    @property
    def need_translate(self):
        return ['title', 'ear', 'material', 'description', 'size', 'geo']


if __name__ == "__main__":
    t = SpiderBase()
    print(t.debug)
