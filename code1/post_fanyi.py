#需求 ： 输入要翻译的单词 然后获取内容
#准备工作  url（接口）   headers  data（参数名字）
#找接口   我不能通过接口的名字来确定接口  因为接口的命名没有规范
#如果说接口的参数是我们查询的那个baby  我们就可以确定是那个接口

import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
data = {
    'kw':'baby'
}
#get请求方式和post请求方式的区别？
#1 post请求在编码之后还需要掉用encode方法 而get请求则不用
data = urllib.parse.urlencode(data).encode('utf-8')
#2 post请求的data参数是放在Request里面的 而 get请求方式需要进行拼接
request = urllib.request.Request(url = post_url,headers=headers,data=data)
response = urllib.request.urlopen(request)
print(response.getcode())
content = response.read().decode('utf-8')

import json
obj = json.loads(content)
string = json.dumps(obj,ensure_ascii=False)
with open('fanyi.json','w',encoding='utf-8')as fp:
    fp.write(string)



