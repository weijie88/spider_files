import urllib.request
import urllib.parse

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
#cname: 上海
# pid:
# pageIndex: 4
# pageSize: 10
#需求  根据输入的城市  起始页 结束页码  下载数据

def create_request(cname,page):
    post_url ='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    data = {
        'cname':cname,
        'pid':'',
        'pageIndex':page,
        'pageSize':'10',
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url = post_url,headers = headers, data = data)
    return request

def save_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    filename = 'KFC' + str(page)+'.html'
    with open(filename,'w',encoding='utf-8')as fp:
        fp.write(content)
        print('竣工了。。。')
import time
def main():
    cname = input('请输入你要查询的城市名称')
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    print('请开始你的下载')
    for page in range(start_page,end_page+1):
        request = create_request(cname,page)
        content = save_content(request)
        down_load(page,content)
        time.sleep(1)
        print('第'+str(page)+'页正在下载。。。')
if __name__ == '__main__':
    main()

