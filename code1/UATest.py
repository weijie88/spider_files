import urllib.request
#咱们现在做的都是模拟一个浏览器去向服务器发送请求 并不是真是的浏览器
#如果是真是的浏览器的话  那么必定会携带UA  所以如果我们想让我们的程序
#更加的健壮  那么我们就需要寻找UA 并且添加到请求对象中
#上面这段话  总结就是 请求对象的定制 ---》代码  urllib.request.Request(url,headers,data)
url = 'http://www.baidu.com/'

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
#定义了UA  然后UA是不能放再urlopen方法中的  因为这个方法没有该参数
#所以我们需要 请求对象的定制
#请求对象的定制---》当原始的urlopen中的数据满足不了请求参数的时候 我们就需要请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))