'''
http://tieba.baidu.com/f?kw=python&pn=200
http://tieba.baidu.com/f?kw=python&pn=250
'''
import urllib.request
import urllib.parse

def create_request(kw,page):
    get_url = 'http://tieba.baidu.com/f?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    data = {
        'kw':kw,
        'pn':(page-1)*50,
    }
    data = urllib.parse.urlencode(data)

    url = get_url + data

    request = urllib.request.Request(url = url,headers = headers)
    return request

def save_content(request):
    repsonse = urllib.request.urlopen(request)
    content = repsonse.read().decode('utf-8')
    return content

def down_load(content,page):
    filename = 'tieba' + str(page) + '.html'
    with open(filename, 'w',encoding='utf-8')as fp:
        fp.write(content)

def main():
    kw = input('请输入你要查询的贴吧的名字')
    start_page = int(input('请输入你要查询的起始页码'))
    end_page = int(input('请输入你要查询的结束页码'))
    print('请开始你的表演')
    for page in range(start_page,end_page+1):
        request = create_request(kw,page)
        content = save_content(request)
        down_load(content,page)

if __name__ == '__main__':
    main()