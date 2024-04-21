# Berlin
from SpiderBase import SpiderBase


class SpiderSMBMuseum(SpiderBase):

    def api_url(self, offset, limit):
        return f'https://api.smb.museum/search/?lang=de&limit={limit}&offset={offset}&sort=-_score%2C-attachments%2C-%40lastSynced'

    def fetch_item(self):
        page = 1 if not self.debug else 28
        page_size = 50 if not self.debug else 50
        cnt = 0
        while True:
            items = self.req_post(url=self.api_url((page - 1) * page_size, page_size), json={
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

    def get_geo(self, item):
        if 'geographicalReferences' not in item:
            return None
        geos = item['geographicalReferences']
        res = []
        for i in geos:
            if not 'location' in i:
                continue
            res.append(i['location'])
        return ','.join(res)

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
                'geo': self.get_geo(item)
            }
            self.translate_item('de',parsed_item)
            parsed_items.append(parsed_item)

        db_items = []
        for item in parsed_items:
            db_items.append(tuple(item.values()))
        self.save_to_mysql(db_items)


if __name__ == '__main__':
    spider = SpiderSMBMuseum()
    spider.fetch_item()
