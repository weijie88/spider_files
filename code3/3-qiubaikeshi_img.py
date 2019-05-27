#需求   在控制台上输入起始页码  输入结束页码  然后下页面中的所有图片下载到qiushibaike
#的文件夹中
'''
1 main()
  start_page
  end_page
  for page in range(s...+1)
      request = create_request
      content = save_content  content中包含了每一页完整数据
      parse_content
      down_load
      https://www.qiushibaike.com/8hr/page/3/
'''

import urllib.request
import re

def create_request(page):
    get_url = 'https://www.qiushibaike.com/8hr/page/'+str(page)+'/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    request = urllib.request.Request(url=get_url,headers=headers)
    return request
def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def parse_content(content):
    p = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=".*?"',re.S)
    src_list = p.findall(content)
    return src_list

def down_load(src_list):
    for i in range(len(src_list)):
        name = src_list[i].split('/')[-1]
        src = src_list[i]
        url = 'https:' + src
        filename = './qiushibaike/' + name
        urllib.request.urlretrieve(url=url,filename=filename)
        print('下载结束。。。。')
def main():
    start_page = int(input('爷们 请输入起始页码'))
    end_page = int(input('姐妹 请输入结束页码'))
    print('下载开始。。。。')
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = save_content(request)
        src_list = parse_content(content)
        down_load(src_list)



if __name__ == '__main__':
    main()