import requests
import json
import jsonpath
from handless import share_browser
from lxml import etree
import urllib.request
get_url = 'https://www.ixigua.com/api/pc/feed/?max_behot_time=1537147688&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A1351B39AFF11D3&cp=5B9F8161CD135E1&_signature=KplxhBAYcQ2AtjEEnp8MviqZcZ'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
response = requests.get(url=get_url,headers=headers)
content = response.text
obj = json.loads(content)
str1 = json.dumps(obj,ensure_ascii=False)
with open('xigua.json','w',encoding='utf-8')as fp:
    fp.write(str1)
obj1 = json.load(open('xigua.json','r',encoding='utf-8'))
url_list = jsonpath.jsonpath(obj1,'$..source_url')
for url1 in url_list:
    #url /group/6601704002692317699/
    url2 = url1.split('/')[2]
    url = 'https://www.ixigua.com/a' + url2
    # url = 'https://www.ixigua.com/a6601394640610394631'
    # response1 = requests.get(url = url,headers = headers)
    # print(response1.text)
    browser = share_browser()
    browser.get(url=url)
    response2 = browser.page_source
    tree = etree.HTML(response2)
    src = tree.xpath('//video/@src')[0]
    name = tree.xpath('//h2/text()')[0] + '.mp4'
    print(src)
    print(name)
    urllib.request.urlretrieve(url=src,filename=name)

