import requests

url = 'http://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
data = {
    'wd':'李大钊'
}
#请求资源路径后面可以不加？ 参数自动编解码  get方法中params代表的是参数
#也不需要请求对象的定制
response = requests.get(url=url,params=data,headers=headers)

# print(type(response))
# response.encoding = 'utf-8'
#获取的网站源码
# print(response.text)
#获取字节码
# print(response.content)
#获取请求资源路径
print(response.url)
print(response.status_code)
print(response.headers)

# print(response)

