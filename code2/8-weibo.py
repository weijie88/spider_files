import urllib.request

get_url = 'https://weibo.cn/6451491586/info'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie':
'SCF=Ahi2Sm3XHpcYIJvIsbJd8AnqkyO8t5RFmHXn8yHeTOMYgumvEqFGsgNbZbD6BmzlV7GA-B8sNWcbTcHeVmF3eNc.; _T_WM=b5c6289fde8a60d64446f59e63a81ce0; SUB=_2A252kx7hDeRhGeBK7lMV-S_JwzqIHXVSf6KprDV6PUJbkdAKLUnmkW1NR6e0UBMZmMMWdmpeEQCuS9uS7HZHOrH7; SUHB=0u5hypmo3fwlim; SSOLoginState=1536650929',
}

request = urllib.request.Request(url = get_url,headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)