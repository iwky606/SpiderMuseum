# Berlin
from SpiderBase import SpiderBase


class SpiderSMBMuseum(SpiderBase):

    def api_url(self, offset, limit):
        return f'https://api.smb.museum/search/?lang=de&limit={limit}&offset={offset}&sort=-_score%2C-attachments%2C-%40lastSynced'

    def fetch_item(self):
        items = self.req_post(url=self.api_url(0, 12), params={
            "q_advanced": [{"field": "geographicalReferences", "operator": "AND", "q": "China"}]
        })
        with open('smbmuseum.json', 'w') as f:
            f.write(items.text)


if __name__ == '__main__':
    spider = SpiderSMBMuseum()
    spider.fetch_item()
