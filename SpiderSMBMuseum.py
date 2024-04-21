# Berlin
import config
from SpiderBase import SpiderBase
import re


class SpiderSMBMuseum(SpiderBase):

    def api_url(self, offset, limit):
        return f'https://api.smb.museum/search/?lang=de&limit={limit}&offset={offset}&sort=-_score%2C-attachments%2C-%40lastSynced'

    def fetch_item(self):
        page = 1
        page_size = 50 if not self.debug else 3
        cnt = 0
        while True:
            items = self.req_post(url=self.api_url((page - 1) * page_size, page_size), params={
                "q_advanced": [{"field": "geographicalReferences", "operator": "AND", "q": "China"}]
            })
            result = items.json()
            total = result['total']
            items = result['objects']
            self.parse_item(items)
            cnt += len(items)
            print(f'处理完{cnt}条数据，总共{total}')
            if page_size * page >= total:
                break
            if self.debug and page > 2:
                break
            page += 1

    def get_geo(self, id):
        res = self.req_get(url=f"https://api.smb.museum/search/{id}/?projection=full").json()
        res = dict(res)
        if not 'geographicalReferences' in res:
            return None
        geos = res['geographicalReferences']
        item = []
        for i in geos:
            if not 'location' in i:
                continue
            item.append(i['location'])
        return ','.join(item)

    def parse_item(self, items):

        parsed_items = []
        for item in items:
            image_url = f'https://recherche.smb.museum/images/{item['assets'][0]}_300x300.jpg' if len(
                item['assets']) > 0 else None

            parsed_item = {
                'museum': 'Staatliche Museen zu Berlin',
                'title': item.get('title', None),
                'ear': '-'.join(item['dating']) if 'dating' in item else None,
                'material': item['materialAndTechnique'][0] if 'materialAndTechnique' in item else None,
                'size': item['dimensionsAndWeight'][0] if 'dimensionsAndWeight' in item else None,
                'description': item.get('description', None),
                'detail_url': item.get('permalink', None),
                'image': image_url,
                'download_link': image_url,
                'geo': self.get_geo(item['id'])
            }

            texts = []
            for key in parsed_item.keys():
                if key not in self.need_translate:
                    continue
                texts.append(str(parsed_item[key]))

            res = self.batch_translate(texts, 'de', 'zh') if texts else None
            index = 0
            for key in parsed_item.keys():
                if key not in self.need_translate:
                    continue
                parsed_item[key] = res[index] if parsed_item[key] else None
                index += 1
            parsed_items.append(tuple(parsed_item.values()))

        self.save_to_mysql(parsed_items)

    @property
    def need_translate(self):
        return ['title', 'ear', 'material', 'size', 'description', 'geo']


if __name__ == '__main__':
    spider = SpiderSMBMuseum()
    spider.fetch_item()
