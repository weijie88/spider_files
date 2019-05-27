import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
}

data={
    'kw':'eye'
}

response = requests.post(url=url,data=data,headers=headers)

content = response.text

import json

obj = json.loads(content)

str1 = json.dumps(obj,ensure_ascii=False)

print(str1)
