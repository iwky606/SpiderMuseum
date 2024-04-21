import time

import requests

from SpiderBase import SpiderBase
from lxml import etree


class SpiderNjMuseum(SpiderBase):

    def fetch_item(self):
        page = 409 if not self.debug else 93
        cnt = 0
        while True:
            try:
                content = self.req_get(f'https://www.ahm.cn/Collection/CollectionSuperorderList/cpzm?page={page}').text
                tree = etree.HTML(content)
                rows = tree.xpath('//*[@id="articles"]/div[1]/div/table/tbody/tr[*]')
                result = []
                for row in rows:
                    title = row.xpath('./td[@class="title"]/text()')[0]
                    category = row.xpath('./td[2]/text()')[0]
                    if row.xpath('./td[3]/text()'):
                        period = row.xpath('./td[3]/text()')[0]
                    else:
                        sptitle = title.split(' ')
                        if len(sptitle) >= 2:
                            period = sptitle[0]
                        else:
                            period = None
                    image_url = row.xpath('./td[@class="img"]/a/@href')[0]
                    item = {
                        'museum': 'ahmuseum',
                        'title': title,
                        'ear': period,
                        'material': None,
                        'size': None,
                        'description': category,
                        'detail_url': None,
                        'image': image_url,
                        'download_link': image_url,
                        'geo': '中国'
                    }
                    result.append(tuple(item.values()))
                self.save_to_mysql(result)
                cnt += len(result)
                print(f'处理完{cnt}')
                if page > 1137 or (self.debug and page > 30):
                    break
                page += 1
            except:
                print(f'failed page:{page}')
                time.sleep(60)


if __name__ == '__main__':
    spider = SpiderNjMuseum()
    spider.fetch_item()
