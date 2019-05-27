import urllib.request
import random

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

proxiesPool = [

]
proxy = random.choice(proxiesPool)

handler = urllib.request.ProxyHandler(proxies=proxy)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('baidu.html','w',encoding='utf-8')as fp:
    fp.write(content)
