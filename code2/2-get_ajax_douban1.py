'''
需求：在控制台上输入你要下载的起始页 和 结束页 然后开始下载
     封装：下载豆瓣   1 请求对象的定制
                   2 获取响应的数据
                   3 保存页面
'''
import urllib.request
import urllib.parse

def create_request(page):
    get_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    data = {
        'start':(page-1)*20,
        'limit':'20',
    }
    data = urllib.parse.urlencode(data)
    url = get_url + data
    request = urllib.request.Request(url = url,headers = headers)
    return request

def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    filename = 'douban' + str(page) + '.html'
    with open(filename,'w',encoding='utf-8')as fp:
        fp.write(content)
        print(filename + '已下载完成！！！')



def main():
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    print('下载开始。。。。')
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = save_content(request)
        down_load(content,page)
        print('第' + str(page)+'正在下载思密达。。。。')

if __name__ == '__main__':
    main()