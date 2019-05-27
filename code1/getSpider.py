#需求： 在控制台上输入一个你想要查询的人名  然后就会给我们响应

import urllib.request
import urllib.parse
name = input('请输入你要查询的人名')

get_url = 'http://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
}

data = {
    'wd':name,
    'sex':'nv'
}
#由于可能输入的是汉语  pycharm不会给我们自动编解码  所以我们需要手动操作
data = urllib.parse.urlencode(data)
#拼接url和参数
url = get_url + data
#请求对象的定制  --》urlopen中只能填写url 所以我们需要请求对象的定制
request = urllib.request.Request(url = url, headers = headers)
#向服务器发送请求
response = urllib.request.urlopen(request)

print(response.getcode())

# print(response.read().decode('utf-8'))
#获取响应的数据
content = response.read().decode('utf-8')
#将响应的数据保存起来
with open('long.html','w',encoding='utf-8')as fp:
    fp.write(content)




