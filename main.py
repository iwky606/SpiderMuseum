import json

import requests

# res = requests.get(url="https://api.smb.museum/search/885911/?projection=full").json()
# res=dict(res)
# with open("geo.json", "w") as fp:
#     json.dump(res,fp)

import re

url = "https://id.smb.museum/object/1908454/kampfe-bei-dabulin-schlachtenbild"
match = re.search(r'/object/(\d+)/', url)

if match:
    print(match.group(1))  # 输出：885911

res={'id': 2722390, '@id': '2722390', '@initialImport': '2023-03-27T20:21:56.157361+00:00',
 '@lastSynced': '2024-04-16T13:22:01.488627+00:00', 'acquisition': ['Schenkung, 2019'], 'assets': [
    {'thumbnail': 'https://recherche.smb.museum/images/62/6246338_480x480.jpg', 'filename': '6246338.jpg',
     'markup': '<span><a href="https://recherche.smb.museum/images/62/6246338_480x480.jpg" data-link-type="external" target="_blank">2722390_6246338.jpg</a></span>',
     'formatted': '6246338', 'linkTemplate': 'https://recherche.smb.museum/images/62/6246338_{width}x{height}.jpg',
     'id': 6246338}], 'attachments': True, 'collection': 'Ethnologisches Museum', 'collectionKey': 'EMMusikethnologie',
 'compilation': 'Musikethnologie', 'description': {
    'markup': '<div>Charakteristisch für die So-na (Suona) sind der profilierte Korpus aus dunkel gefärbtem Holz, bei sich dem jedes Griffloch in einer ausgedrehten Vertiefung befindet, und der aus Aluminium oder Messing gefertigte Schalltrichter. Ein mit zwei Kugeln (die auch durchbrochen sein können) und zwei Scheiben versehener Aufsatz trägt das kleine Rohrblatt. Das Instrument weist sieben frontale Tonlöcher und ein Daumenloch auf. Dieser Typus wird auch in Japan und Vietnam gespielt.\xa0</div><div>Diese alte So-na weist noch Druckspuren von Metallreifen zwischen den Klappen auf.Die Metallreifen wurden entfernt, der Korpus in Stoff (?) gewickelt und mit schwarzem Lack bemalt. Das Instrument hat nun sieben frontale ovale Tonlöcher und kein Daumenloch. Der Trichter wurde aus Kupfer gefertigt. Der Rohrträger besitz zwischen zwei Scheiben die üblichen zwei Zierkugeln und ein Strohmundstück.\xa0\xa0\xa0\xa0\xa0\xa0 \xa0<br><p class="MsoNoSpacing"><br><span style="font-size:13.0pt;\nfont-family:" times="" new="" roman",serif;mso-fareast-font-family:"times="" roman";="" mso-bidi-font-family:"lohit="" hindi";color:gray;mso-themecolor:background1;="" mso-themeshade:128;mso-ansi-language:de;mso-fareast-language:de;mso-bidi-language:="" ar-sa"=""><span style="mso-tab-count:1">\xa0</span><span style="mso-spacerun:yes">\xa0\xa0\xa0\xa0 </span></span></p></div>',
    'formatted': 'Charakteristisch für die So-na (Suona) sind der profilierte Korpus aus dunkel gefärbtem Holz, bei sich dem jedes Griffloch in einer ausgedrehten Vertiefung befindet, und der aus Aluminium oder Messing gefertigte Schalltrichter. Ein mit zwei Kugeln (die auch durchbrochen sein können) und zwei Scheiben versehener Aufsatz trägt das kleine Rohrblatt. Das Instrument weist sieben frontale Tonlöcher und ein Daumenloch auf. Dieser Typus wird auch in Japan und Vietnam gespielt.&nbsp;Diese alte So-na weist noch Druckspuren von Metallreifen zwischen den Klappen auf.Die Metallreifen wurden entfernt, der Korpus in Stoff (?) gewickelt und mit schwarzem Lack bemalt. Das Instrument hat nun sieben frontale ovale Tonlöcher und kein Daumenloch. Der Trichter wurde aus Kupfer gefertigt. Der Rohrträger besitz zwischen zwei Scheiben die üblichen zwei Zierkugeln und ein Strohmundstück.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'},
 'dimensionsAndWeight': ['Objektmaß: 47,5 x 11 x 11 cm', 'Länge: 475 mm'], 'exhibit': False, 'geographicalReferences': [
    {'search': 'https://api.smb.museum/search/?q=geographicalReferences.id:39362',
     'markup': '<div><span><a href="https://api.smb.museum/search/?q=geographicalReferences.id:39362" data-link-type="internal">Asien</a></span> <span>(Asien)</span> <span>(Kontinent)</span></div>',
     'denominationId': 467, 'formatted': 'Asien (Asien) (Kontinent)', 'location': 'Asien', 'id': 39362},
    {'search': 'https://api.smb.museum/search/?q=geographicalReferences.id:191',
     'markup': '<div><span><a href="https://api.smb.museum/search/?q=geographicalReferences.id:191" data-link-type="internal">China</a></span> <span>(Land)</span></div>',
     'denominationId': 22, 'formatted': 'China (Land)', 'location': 'China', 'id': 191}, {
        'search': 'https://api.smb.museum/search/?q=geographicalReferences.details:"Schanghai+%28Shanghai%29+%28%E4%B8%8A%E6%B5%B7%29"',
        'markup': '<div><span><a href="https://api.smb.museum/search/?q=geographicalReferences.details:"Schanghai+%28Shanghai%29+%28%E4%B8%8A%E6%B5%B7%29"" data-link-type="internal">Schanghai (Shanghai) (上海)</a></span> <span>(Stadt)</span></div>',
        'denominationId': 107, 'formatted': 'Schanghai (Shanghai) (上海) (Stadt)',
        'details': 'Schanghai (Shanghai) (上海)'}], 'highlight': False, 'identNumber': 'VII c 1075',
 'materialAndTechnique': [{
                              'search': 'https://api.smb.museum/search/?q=materialAndTechnique.name:"Holz%2C+Metall%2C+Stoff%2C+Lack%2C+Stroh%2C+Pflanzenfaser"',
                              'markup': '<div><span><a href="https://api.smb.museum/search/?q=materialAndTechnique.name:"Holz%2C+Metall%2C+Stoff%2C+Lack%2C+Stroh%2C+Pflanzenfaser"" data-link-type="internal">Holz, Metall, Stoff, Lack, Stroh, Pflanzenfaser</a></span></div>',
                              'formatted': 'Holz, Metall, Stoff, Lack, Stroh, Pflanzenfaser',
                              'name': 'Holz, Metall, Stoff, Lack, Stroh, Pflanzenfaser', 'typeId': 4}],
 'technicalTerm': {'search': 'https://api.smb.museum/search/?q=technicalTerm:Oboe',
                   'markup': '<div><span><a href="https://api.smb.museum/search/?q=technicalTerm:Oboe" data-link-type="internal">Oboe</a></span></div>',
                   'formatted': 'Oboe'}, 'title': 'So-na',
 'permalink': {'formatted': 'https://id.smb.museum/object/2722390/so-na',
               'markup': '<div><span><a href="https://id.smb.museum/object/2722390/so-na" data-link-type="permalink">https://id.smb.museum/object/2722390</a></span></div>'}}

with open('test.json','w') as fp:
    fp.write(json.dumps(res))