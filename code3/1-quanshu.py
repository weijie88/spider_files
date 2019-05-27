'''
当遇到动态cookie的时候 那么我们直接定位写死的cookie的时候 那么就不会
进入到藏书架
假设 全书网是一个动态cookie 那么解决方案：
 1 获取登陆cookie
 2 把cookie给藏书家

 动态获取cookie的使用步骤：
  1 import http.cookiejar
  2 cookie = http.cookiejar.CookieJar()
  3 handler
  4 opener
  5 open
'''

import urllib.request
import urllib.parse
import http.cookiejar

post_url = 'http://www.quanshuwang.com/login.php?do=submit'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
data = {
    'username': 'action',
    'password': 'action',
    'action': 'login',
}
data = urllib.parse.urlencode(data).encode('gbk')
request = urllib.request.Request(url=post_url,headers=headers,data=data)

cookie = http.cookiejar.CookieJar()
#hangler  opener open
handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open(request)
#如果说opener中包含了登陆的cookie 那么我再次通过opener。open（藏书家）
#是不是就可以访问藏书家了呢
get_url = 'http://www.quanshuwang.com/modules/article/bookcase.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
request1 = urllib.request.Request(url=get_url,headers=headers)

response1 = opener.open(request1)

print(response1.read().decode('gbk'))








