import urllib.request

# get_url = 'https://www.qiushibaike.com/8hr/page/3/'

def create_request(page):
    get_url = 'https://www.qiushibaike.com/8hr/page/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url = get_url + str(page) + '/'
    request = urllib.request.Request(url=url,headers=headers)
    return request

def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    filename = 'qiubai' + str(page) + '.html'
    with open(filename,'w',encoding='utf-8')as fp:
        fp.write(content)

def main():
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = save_content(request)
        down_load(content,page)

if __name__ == '__main__':
    main()