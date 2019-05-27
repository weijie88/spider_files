'''
  提交表单的时候 多了2个数据 一个是formhash  一个是referer
  所以我们需要观察原始页面中form的参数
  当我们使用普通的请求的时候  显示的数据量不足  那么我们就要驱动真实的
  浏览器也就是selenium来操纵  browser.page_source

  http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes
  先执行这个请求的原因是因为登陆表单中需要formhash和referer  那么这两个值
  是在登陆页面中获取的
  那么怎么去获取这两个值的内容呢？
  答我们可以获取页面数据之后 然后使用bs4或者xpath进行解析
'''

import requests
from bs4 import BeautifulSoup

get_url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}

response = requests.get(url=get_url,headers=headers)
#服务器响应的页面
content = response.text
soup = BeautifulSoup(content,'lxml')
#也可以使用
# input = soup.select('.form > input')[0]
# print(input.attrs.get('value'))
formhash = soup.select('input[name="formhash"]')[0].attrs.get('value')
referer = soup.select('input[name=referer]')[0].attrs.get('value')

post_url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LjoKO'

data = {
    'formhash': formhash,
    'referer': referer,
    'username': 'action123321',
    'password': 'action123',
    'loginsubmit': 'true',
    'return_type': '',
}
res = requests.post(url=post_url,headers=headers,data=data)

print(res.text)
