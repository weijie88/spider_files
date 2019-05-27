'''
1 找到登陆的接口 千万不误以为主页面就是代表着登陆
'''
import requests

post_url = 'http://www.quanshuwang.com/login.php?do=submit'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
data = {
    'username': 'action',
    'password': 'action',
    'action': 'login',
}
s = requests.session()
res = s.post(url = post_url,headers = headers,data=data)

# print(res.text)

get_url = 'http://www.quanshuwang.com/modules/article/bookcase.php'

res1 = s.get(url=get_url,headers=headers)
res1.encoding = 'gbk'
print(res1.text)

