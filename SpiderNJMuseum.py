from SpiderBase import SpiderBase


class SpiderNjMuseum(SpiderBase):

    @property
    def fetch_url(self):
        return "https://www.njmuseum.com/api/collection/select"

    def fetch_item(self):
        items = self.req_post(url=self.fetch_url, params={
            'pageNum': 1,
            'pageSize': 12,
        })
        print(items.text)
        with open('njmuseum.json', 'w') as f:
            f.write(items.text)


if __name__ == '__main__':
    spider = SpiderNjMuseum()
    spider.fetch_item()
