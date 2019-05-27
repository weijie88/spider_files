'''
1 获取页面中的a标签中的href属性值
2 把href的值当作请求发送给服务器
3 跳转到视频页面之后 找到video的src值
4 下载 urllib.request.urlretrieve(url=url,filename=filename)
'''
import requests
from lxml import etree
from handless import share_browser
get_url = 'https://www.365yg.com/api/pc/feed/?max_behot_time=1537147244&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A125CB29CF803E5&cp=5B9F6053AEC52E1&_signature=OsZI8xAZYV-Q6QhzfSUUBDrGSO'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

response = requests.get(url=get_url,headers=headers,verify=False)

import json

obj = json.loads(response.text)

str1 = json.dumps(obj,ensure_ascii=False)
with open('movie.json','w',encoding='utf-8')as fp:
    fp.write(str1)

import jsonpath

obj1 = json.load(open('movie.json','r',encoding='utf-8'))

url_list = jsonpath.jsonpath(obj1,'$..source_url')
for url in url_list:
    #/group/6598948265230598669/
    #https://www.365yg.com/a6599600694703948291
    url1 = url.split('/')[2]
    url2 = 'https://www.365yg.com/a'+url1
    # url2 = 'https://www.365yg.com/a6599790861595181572'
    # res1 = requests.get(url=url2,headers=headers,verify=False)
    # print(res1.text)
    browser = share_browser()
    browser.get(url=url2)
    res3 = browser.page_source
    #现在想获取的是res1.text页面中video标签中的src属性
    #所以我们需要对res1.text进行解析
    tree = etree.HTML(res3)
    src = tree.xpath('//video/@src')[0]
    print(src)



