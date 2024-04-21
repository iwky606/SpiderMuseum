from SpiderBase import SpiderBase


class SpiderNjMuseum(SpiderBase):

    @property
    def fetch_url(self):
        return "https://www.njmuseum.com/api/collection/select"

    def fetch_item(self):
        page = 1
        page_size = 50 if not self.debug else 12
        cnt = 0
        while True:
            res = self.req_post(url=self.fetch_url, params={
                'pageNum': page,
                'pageSize': page_size,
            }).json()
            data = res['data']
            total = data['total']
            self.parse_item(data['list'])
            cnt += len(data['list'])
            print(f'处理完{cnt}条数据，总共{total}')
            if page_size * page >= total:
                break
            if self.debug and page > 2:
                break
            page += 1

    def parse_item(self, items):
        parsed_items = []
        for item in items:
            imgs = item['imgSrc']
            img_url = ''
            if len(imgs) > 0:
                img_url = 'www.njmuseum.com' + imgs[0]
            parsed_item = {
                'museum': 'njmuseum',
                'title': item.get('title', None),
                'ear': None,
                'material': None,
                'size': item['size'] if 'size' in item else None,
                'description': item.get('describe', None),
                'detail_url': f'https://www.njmuseum.com/zh/collectionDetails?id={item["id"]}',
                'image': img_url,
                'download_link': img_url,
                'geo': '中国',
            }
            parsed_items.append(parsed_item)

        db_items = []
        for item in parsed_items:
            db_items.append(tuple(item.values()))
        self.save_to_mysql(db_items)


if __name__ == '__main__':
    spider = SpiderNjMuseum()
    spider.fetch_item()
