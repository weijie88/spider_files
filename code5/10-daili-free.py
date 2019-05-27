import requests

url = 'http://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
data = {
    'wd':'ip'
}

proxy = {
    'http':'222.221.11.119:3128'
}

response = requests.get(url=url,headers=headers,params=data,
                        proxies=proxy)

with open('baidu.html','w',encoding='utf-8')as fp:
    fp.write(response.text)