#需求  爬取百度首页

import urllib.request
url = 'http://www.baidu.com/'
#通过程序模拟一个浏览器去访问服务器
response = urllib.request.urlopen(url = url)

#判断类型 以及6个方法的使用
#之所以判断response的类型是为了和requests（只属于python的第三方库）做一个对比
# print(type(response))
#获取响应的状态码 如果是200了代码响应数据成功
# print(response.getcode())
#获取的响应头
# print(response.getheaders())
#获取请求url
# print(response.geturl())
#编码    对象---》字节码   encode（）方法   码---马赛克
#解码    字节码---》对象   decode（）方法
print(response.read().decode('utf-8'))#常用

# print(response.readline())
#
# print(response.readlines())
