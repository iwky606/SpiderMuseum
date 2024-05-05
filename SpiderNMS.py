import time

from SpiderBase import SpiderBase
from lxml import etree
from playwright.sync_api import sync_playwright
import traceback

TIME_OUT_MS = 60000


class SpiderNMS(SpiderBase):

    def __init__(self):
        super().__init__()
        self.default_img = 'https://www.nms.ac.uk/images/no_image.gif'

    def fetch_item(self):
        cnt = 0
        go_page = 1
        time_out_extra = 0
        while True:
            try:
                with sync_playwright() as p:
                    print(f"start crawl page:{go_page}")
                    browser = p.chromium.launch(headless=False)
                    context = browser.new_context()
                    context.set_default_timeout(TIME_OUT_MS)
                    page = browser.new_page()
                    page.set_extra_http_headers(self.headers)
                    page.goto("https://www.nms.ac.uk/explore-our-collections/collection-search-results/")
                    page.wait_for_selector("#searchTerm")
                    accept_all_cookies_button = page.query_selector('#ccc-notify-accept')
                    # 如果该按钮存在,则点击
                    if accept_all_cookies_button:
                        accept_all_cookies_button.click()
                    page.fill('input[name="searchTerm"]', 'china')
                    page.click('#btnCollectionsSearch')
                    page.wait_for_load_state("networkidle", timeout=TIME_OUT_MS + time_out_extra)  # 等待网络空闲
                    if go_page:
                        page.wait_for_selector("#page")
                        page.fill('input[name="page"]', str(go_page))
                        page.press("#page", 'Enter')

                        while True and (not self.debug or cnt < 2):
                            print(f"now page:{go_page}")
                            page.wait_for_load_state("networkidle", timeout=TIME_OUT_MS + time_out_extra)  # 等待网络空闲
                            tree = etree.HTML(page.content())

                            rows = tree.xpath('//*[@id="SiteMain"]/div/div[2]/div/div[2]/div[*]')
                            items = []
                            for row in rows:
                                detail_url = 'https://www.nms.ac.uk' + row.xpath('.//a/@href')[0]
                                title = row.xpath('.//a[@class="itemTitle"]/text()')[0]
                                img_urls = row.xpath('.//a[@class="itemThumb"]/img/@src')
                                img_url = None
                                if img_urls and len(img_urls) > 0:
                                    img_url = img_urls[0]
                                    if img_url == '/images/no_image.gif':
                                        img_url = self.default_img
                                    else:
                                        img_url = 'https://www.nms.ac.uk/' + img_url

                                items.append((detail_url, title, img_url))

                            self.parse_items(items)
                            cnt += 1
                            print(f'处理完{cnt}页')
                            if len(items) < 16:
                                break

                            # page.wait_for_selector("#btnSearchNext")
                            page.click("#btnSearchNext")
                            go_page += 1
                            print("next page")

                # 未出现异常且爬取完成，推出循环
                break
            except Exception as e:
                time.sleep(10 + time_out_extra)
                time_out_extra += 10000
                print(traceback.format_exc())
                print(f"page:{go_page} failed, retrying...")
                self.reload_db()
                print("reload db success")

    def parse_items(self, items):
        parsed_items = []
        for url, title, img_url in items:
            while True:
                try:
                    content = self.req_get(url).text
                    tree = etree.HTML(content)
                    rows = tree.xpath('//*[@id="SiteMain"]/div/div[2]/div/div[2]')[0].xpath('.//h1|.//h2|.//h3')
                    parsed_item = {
                        'museum': 'National Museum of Scotland',
                        'title': title,
                        'ear': None,
                        'material': None,
                        'size': None,
                        'description': None,
                        'detail_url': url,
                        'image': img_url,
                        'download_link': img_url,
                        'geo': "中国"
                    }
                    try:
                        for row in rows:
                            text = row.text
                            if text == 'Description':
                                parsed_item['description'] = row.xpath('following-sibling::p/text()')[0][:255]
                            if text == 'Physical description':
                                parsed_item['material'] = row.xpath('following-sibling::p/text()')[0][:255]
                            if text == 'Style / Culture':
                                parsed_item['ear'] = row.xpath('following-sibling::p/text()')[0][:255]
                            if text == 'Materials':
                                parsed_item['material'] = row.xpath('following-sibling::p/text()')[0][:255]
                    except Exception as e:
                        pass
                    self.translate_item('en', parsed_item)
                    parsed_items.append(parsed_item)
                    break
                except Exception as e:
                    print(traceback.format_exc())
                    print(f"url:{url} failed, retrying...")
                    time.sleep(20)

        db_items = []
        for item in parsed_items:
            db_items.append(tuple(item.values()))
        self.save_to_mysql(db_items)


if __name__ == '__main__':
    spider = SpiderNMS()

    spider.fetch_item()
