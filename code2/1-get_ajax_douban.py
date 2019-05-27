'''
需求： 爬取豆瓣电影   根据输入的页码 爬取响应的页面
难点： ajax寻找接口   向下划  观察是get还是post

https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

page = int(input('请输入页码'))

page  1 2 3
      0 20 40
      (page-1)*20
'''

import urllib.request
import urllib.parse

get_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

page = int(input('请输入你要下载的页码'))

data = {
    'start':(page-1)*20,
    'limit':'20',
}

data = urllib.parse.urlencode(data)

url = get_url + data

print(url)

request = urllib.request.Request(url = url,headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

import json

obj = json.loads(content)

string = json.dumps(obj,ensure_ascii=False)

filename = 'douban'+str(page)+'.json'

with open(filename,'w',encoding='utf-8')as fp:
    fp.write(string)
