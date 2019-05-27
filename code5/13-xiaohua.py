import requests

get_url = 'http://www.jokeji.cn/user/c.asp?u=action&p=action123&t=big'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}

s = requests.session()
s.get(url=get_url,headers=headers)

get1_url = 'http://www.jokeji.cn/User/MemberCenter.asp'
res = s.get(url = get1_url,headers=headers)
res.encoding = 'gb2312'
print(res.text)

