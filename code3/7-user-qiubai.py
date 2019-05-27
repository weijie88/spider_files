'''
https://www.qiushibaike.com/8hr/page/1/

//div[@id="content-left"]/div/div[starts-with(@class,"author")]//img/@src
//div[@id="content-left"]/div/div[starts-with(@class,"author")]//img/@alt
//div[@id="content-left"]/div/div/div/text()

'''
import urllib.request
from lxml import etree

def create_request(page):
    get_url = 'https://www.qiushibaike.com/8hr/page/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    url = get_url + str(page) + '/'
    request = urllib.request.Request(url = url,headers = headers)
    return request
def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    users = []
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]//img/@src')
    alt_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]//img/@alt')
    level_list = tree.xpath('//div[@id="content-left"]/div/div/div/text()')
    for i in range(len(src_list)):
        user = {}
        user["src"] = src_list[i]
        user['alt'] = alt_list[i]
        if alt_list[i] == '匿名用户':
            level_list.insert(i,'')
        user['level'] = level_list[i]
        users.append(user)
    with open('users.txt','w',encoding='utf-8')as fp:
        fp.write(str(users))
def main():
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = save_content(request)
        down_load(content)

if __name__ == '__main__':
    main()