# //div[@class="thumb"]//img/@src

import urllib.request
from lxml import etree

def create_request(page):
    get_url = 'https://www.qiushibaike.com/8hr/page/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    url = get_url + str(page) + '/'
    request = urllib.request.Request(url=url,headers=headers)
    return request

def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def parse_content(content):
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[@class="thumb"]//img/@src')
    return src_list

def down_load(src_list):
    for src in src_list:
        print(src)

def main():
    start_page = int(input('爷们 请输入起始页面'))
    end_page = int(input('姐们 请输入结束页面'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = save_content(request)
        src_list = parse_content(content)
        down_load(src_list)

if __name__ == '__main__':
    main()