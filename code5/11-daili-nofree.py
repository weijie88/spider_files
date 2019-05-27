import requests
#执行这个连接 那么就会返回一个ip以及端口号
daili_url = 'http://kps.kdlapi.com/api/getkps/?orderid=963689621512832&num=1&pt=1&sep=1'

response = requests.get(url=daili_url)

url = 'http://www.baidu.com/s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
data = {
    'wd':'ip'
}

proxy = {
    'http':response.text
}

res = requests.get(url = url,headers =headers,params=data,proxies=proxy)

with open('kuai.html','w',encoding='utf-8')as fp:
    fp.write(res.text)