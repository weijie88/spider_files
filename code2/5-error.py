import urllib.request
url = 'https://bfdsjfdjlfjsdlfjlsjflsddn.net/u012373815/article/details/792221211'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
try:
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print('您的请求后面多了一个1')
    print(e)
except urllib.error.URLError as e:
    print(1000)
    print(e)
except Exception:
    print(10000000)


# print(response.read().decode('utf-8'))

