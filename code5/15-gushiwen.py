'''
字母
计算
汉字
图片
手机验证码
邮箱验证
流程： 首先获取登陆页面源代码 然后对图片进行解析 获取验证码图片
保存到本地 然后观察 输入到控制台 然后把这个值复制给登陆的参数
'''
import requests
from bs4 import BeautifulSoup
import urllib.request

#登陆页面的接口
get_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}
#向服务器发送请求 获取响应
response = requests.get(url = get_url,headers = headers)
#获取响应的数据
content = response.text
soup = BeautifulSoup(content,'lxml')
#对登陆页面进行解析 获取验证码的路径
RandCode = soup.select('#imgCode')[0].attrs.get('src')
#/RandCode.ashx 返回的是这样的一个路径 但是这个路径并不能直接访问 所以要观察验证码实际路径
#进行实际路径的拼接
img_url = 'https://so.gushiwen.org' + RandCode
#因为urlretrieve发送了第二次请求  并且提交的时候还应该是第一次的验证码
#所以不能使用urlretrieve方法
# urllib.request.urlretrieve(url = url,filename='RandCode.jpg')
s = requests.session()
res2 = s.get(img_url)
with open('RandCode.png','wb')as fp:
    #需要注意 获取的是字节码
    fp.write(res2.content)

code = input('请输入你的验证码')
post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
#__VIEWSTATE  __VIEWSTATEGENERATOR  from
#由于页面中有2个隐藏域  所以需要使用bs4进行解析  然后赋值给表单的参数
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstatefenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
print(viewstate)
print(viewstatefenerator)
data={
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstatefenerator,
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': code,
    'denglu': '登录',
}

res1 = s.post(url=post_url,headers=headers,data=data)

print(res1.text)



