#需求： 带参数怎么爬取
#难点：请求资源路径怎么定义  参数怎么传输
#解决方法：1 观察浏览器地址栏 （get请求方式）2 使用抓包工具
#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#浏览器会自动编解码  而pycharm不会给我们自动编解码
import urllib.request
#因为pycharm不会自动编解码  所以不能识别韩红  所以报错
# url = 'http://www.baidu.com/s?wd=韩红'
# response = urllib.request.urlopen(url = url)
# print(response.getcode())

#1使用quote方法
import urllib.parse

# url = 'http://www.baidu.com/s?wd='
#
# data = '韩红'
# #data是韩红进行编码之后的字节码
# #我们不能把整个字符串都进行编码  因为会把一些符号也进行编码 那么这个url路径就不是完整路径
# data = urllib.parse.quote(data)
# url = url + data
# # print(url)
# response = urllib.request.urlopen(url = url)
#
# print(response.getcode())
#2 如果是2个参数的时候  那么我们怎么办？ 我们使用urlencode方法来操纵
#quote方法只适用于一个参数的时候  当然也可以适用于多个参数 但是比较麻烦 需要拼接很多次

#此时有2个参数 还有中文  所以我们需要进行编码
#如果有两个及两个以上参数的时候 那么我们就需要使用urlencode方法
url1 = 'http://www.baidu.com/s?'

data1 = {
    'wd':'刘强东',
    'sex':'n',
}

data1 = urllib.parse.urlencode(data1)

url1 = url1 + data1

print(url1)
response = urllib.request.urlopen(url=url1)
print(response.getcode())

