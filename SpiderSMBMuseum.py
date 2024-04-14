# Berlin
from SpiderBase import SpiderBase


class SpiderSMBMuseum(SpiderBase):

    def api_url(self, offset, limit):
        return f'https://api.smb.museum/search/?lang=de&limit={limit}&offset={offset}&sort=-_score%2C-attachments%2C-%40lastSynced'

    def fetch_item(self):
        page = 1
        page_size = 50
        while True:
            items = self.req_post(url=self.api_url((page - 1) * page_size, page_size), params={
                "q_advanced": [{"field": "geographicalReferences", "operator": "AND", "q": "China"}]
            })
            result = items.json()
            total = result['total']
            items = result['objects']
            self.parse_item(items)
            if page_size * page >= total:
                break
            if self.is_debug and page > 2:
                break
            page += 1

    def parse_item(self, items):
        parsed_items = []
        for item in items:
            image_url = f'https://recherche.smb.museum/images/{item['assets'][0]}_300x300.jpg'
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
            }
            parsed_items.append(parsed_item)
        print(parsed_items)
        print(len(parsed_items))


if __name__ == '__main__':
    spider = SpiderSMBMuseum()
    spider.fetch_item()