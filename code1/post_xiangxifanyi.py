import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi'

headers = {
    # 'Host': 'fanyi.baidu.com',
    # 'Connection': 'keep-alive',
    #'Content-Length:': '120',
    # 'Accept': '*/*',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    #'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie':'to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; PSTM=1534421131; BIDUPSID=7B1981916885D051C494E1FDBF709563; BAIDUID=C4ACEC51409567FC59BF5A66D0A26B96:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=2; H_PS_PSSID=1435_21110_22158; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1534131258,1534313690,1536563704; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1536563704',
}

data = {
    'from':'en',
    'query':'BABY',
    'sign':'71628.390397',
    'simple_means_flag':'3',
    'to':'zh',
    'token':'6d30093135fffd0ecfc1c5744fabcfef',
    'transtype':'realtime',
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=post_url,headers=headers,data=data)

response = urllib.request.urlopen(request)

print(response.getcode())

# print(response.read().decode('utf-8'))
content = response.read().decode('utf-8')

print(content)