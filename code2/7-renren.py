'''
如果我把进入到个人中心  然后把cookie删除掉 那么刷新页面
就会跳转到登陆页面
---》推论：个人中心中如果有cookie（登陆的cookie） 刷新之后还是到个人中心

登陆接口的寻找：
           1 使用fiddler抓包工具
           2 使用google浏览器 输入一个错误用户名字或者密码
'''

import urllib.request

get_url = 'http://www.renren.com/305523888/profile'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': 'anonymid=jix3nuu4-498h3n; _r01_=1; _de=BF83005E46A2ACDF72FFEFECAA50653A696BF75400CE19CC; ln_uact=595165358@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20170509/0940/main_5crY_aee9000088781986.jpg; depovince=SH; jebe_key=10d644cd-d571-414c-b5c5-e87b99e851ca%7Cdca572dcc866b00768c874af75fd79ec%7C1536587424981%7C1%7C1536587425676; wp_fold=0; jebecookies=4a5f19bf-848d-4538-9d4e-04bb53071472|||||; JSESSIONID=abc6KJGKqwRWTdJ6Lxhxw; ick_login=4bba2fbc-6344-4524-a650-5153bd9a02e2; p=561978f3b33d6d15f8c63cf8757873538; first_login_flag=1; t=35a56fc80278735fda53cff37ca82a428; societyguester=35a56fc80278735fda53cff37ca82a428; id=305523888; xnsid=389fdbac; ver=7.0; loginfrom=null'
}

request = urllib.request.Request(url=get_url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

