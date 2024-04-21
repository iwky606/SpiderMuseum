from SpiderBase import SpiderBase
import config


class SpiderNjMuseum(SpiderBase):

    @property
    def fetch_url(self):
        return "https://www.njmuseum.com/api/collection/select"

    def fetch_item(self):
        page = 1
        page_size = 50 if not config.DEBUG else 3
        cnt = 0
        while True:
            res = self.req_post(url=self.fetch_url, params={
                'pageNum': page,
                'pageSize': page_size,
            }).json()
            data = res['data']
            total = res['total']
            self.parse_item(data['list'])
            cnt += len(data['list'])
            print(f'处理完{cnt}条数据，总共{total}')
            if page_size * page >= total:
                break
            if config.DEBUG and page > 2:
                break
            page += 1

    def parse_item(self, items):
        parse_items = []
        for item in items:
            pass


if __name__ == '__main__':
    spider = SpiderNjMuseum()
    spider.fetch_item()
