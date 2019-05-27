'''
需求  爬取性感美女的图片以及图片名字
方案：1 找接口  观察接口的变化
        http://sc.chinaz.com/tupian/xingganmeinvtupian.html
        http://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
        http://sc.chinaz.com/tupian/rentisheying.html
     2 xpath
        //div[@id="container"]/div/div/a/img/@alt
        //div[@id="container"]/div/div/a/img/@src
'''
import urllib.request
from lxml import etree

def create_request(pic_type,page):
    get_url = 'http://sc.chinaz.com/tupian/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    if page == 1:
        url = get_url + pic_type+'.html'
    else:
        url = get_url + pic_type + '_' + str(page) + '.html'
    request = urllib.request.Request(url = url,headers=headers)
    return request

def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    alt_list = tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
    # print(len(src_list))
    # print(len(alt_list))
    if len(src_list) == len(alt_list):
        for i in range(len(src_list)):
            src = src_list[i]
            alt = alt_list[i]
            filename = './meinv/'+alt
            urllib.request.urlretrieve(url=src,filename=filename)
        # print('下载完成。。。。。')
    else:
        print('数据不匹配。。。。。')
def main():
    pic_type = input('请输入你喜欢的图片类型')
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = create_request(pic_type,page)
        content = save_content(request)
        down_load(content)

if __name__ == '__main__':
    main()
