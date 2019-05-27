'''
//tbody[@id="datalist"]/tr/td[1]
#datalist > tr >td[1]
接口：http://quote.stockstar.com/
思路  通过urlopen方法来获取服务器响应的数据 然后对数据进行解析
'''

import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
from Item import Stock
import json

get_url = 'http://quote.stockstar.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
request = urllib.request.Request(url=get_url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('gb2312')
soup = BeautifulSoup(content,'lxml')
tr_list = soup.select('#datalist > tr')
stocks = []
for tr in tr_list:
    code = tr.find_all('td')[0].string
    name = tr.find_all('td')[1].string
    price = tr.find_all('td')[2].string
    stock = Stock(code,name,price)
    stocks.append(stock.__dict__)
print(stocks)
sj = json.dumps(stocks,ensure_ascii=False)

with open('stock.json','w',encoding='utf-8')as fp:
    fp.write(sj)



# tree = etree.HTML(content)
# code_list = tree.xpath('//tbody[@id="datalist"]/tr/td[1]')
# print(code_list)