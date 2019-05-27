import requests
import threading
from queue import Queue
from lxml import etree
import json
# 糗事百科的网页获取到
url_base = 'https://www.qiushibaike.com/8hr/page/%d/'

# 任务队列
# 网络请求的队列
requestQueue = Queue()
# 解析的队列
parseQueue = Queue()
# 任务完成，退出线程，解析队列而言
exitParseFlag = False
# 数据解析的页码
parsePage = 1
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

# 多线程进行网络数据的获取
# 多线程进行网络数据的解析
class ThreadParse(threading.Thread):
    def __init__(self, queue,id,fp):
        super().__init__()
        self.queue = queue
        self.id = id
        self.fp = fp

    def run(self):
        super().run()
        print('解析线程：--------%d--------开始工作！'%(self.id))
        # 该方法，一直进行死循环，直到标志exitParseFlase变为True
        self.parseHtml()
        print('解析线程：--------%d--------完成工作！'%(self.id))

    def parseHtml(self):
        global exitParseFlag
        global parsePage
        while True:
            if exitParseFlag:
                break
            try:
                #获取队列中的元素
                html = self.queue.get(block = False)
                html_tree = etree.HTML(html)
                div_list = html_tree.xpath('//div[contains(@id,"qiushi_tag")]')
                print(len(div_list))
                for div in div_list:
                    header_img_url = div.xpath('.//div[@class="author clearfix"]//img/@src')[0]
                    nickname = div.xpath('.//div[@class="author clearfix"]//img/@alt')[0]
                    content = div.xpath('.//div[@class="content"]/span/text()')[0]
                    vote = div.xpath('.//div[@class="stats"]//i/text()')[0]
                    comment = div.xpath('.//div[@class="stats"]//i/text()')[1]
                    item = {}
                    item['header_img_url'] = header_img_url
                    item['nickname'] = nickname
                    item['content'] = content
                    item['vote'] = vote
                    item['comment'] = comment
                    str = json.dumps(item,ensure_ascii=False)
                    print(str)
            #         字典数据保存到文件中
                    self.fp.write(str+'\n')
                print('解析线程：------%d-------完成了页码：-------%d--------的数据解析工作'%(self.id,parsePage))
                parsePage += 1
                self.queue.task_done()
            except Exception as e:
                pass
        pass
# 这个是请求的线程  继承了Thread父类
class ThreadRequest(threading.Thread):
    #构造器
    def __init__(self, queue,id):
        super().__init__()
        self.queue = queue
        self.id = id

    def run(self):
        super().run()
        print('爬虫线程：--------%d--------开始工作！'%(self.id))
        #开始爬取数据
        self.getHtml()
        print('爬虫线程：--------%d--------结束工作！'%(self.id))

    def getHtml(self):
        # 该方法要一直执行，直到请求队列中为空
        while True:
            if self.queue.empty():
                break
            try:
                #获取队列中的数据  p代表的是页数
                p = self.queue.get(block = False)
            #     获得页码，进行网络请求  请求url已经获取
                url = url_base%(p)
                # 访问
                response = requests.get(url=url,headers = headers,verify = False)
                #获取响应的数据
                html = response.text
            #     将网络请求获取的数据保存另一个队列中 parseQueue
                parseQueue.put(html)
                self.queue.task_done()
                print('爬虫线程：-------%d-------下载页码：-------%d------的数据'%(self.id,p))
            except Exception as e:
                pass
        pass

if __name__ == '__main__':
    #爬取糗事百科前10页的数据
    # 现在使用多线程爬去前10页数据 url p = 1 p = 2
    # 任务
    for i in range(1,11):
        #队列中有10个数
        requestQueue.put(i)
    # 爬虫线程----把页数分别拼接成url 然后访问  把响应的数据存放到parse队列
    for i in range(1,4):
        #创建了一个请求线程
        threadRequest = ThreadRequest(requestQueue,i)
        #start方法是启动线程的意思  start方法会调用run方法
        threadRequest.start()
    # 解析线程
    fp = open('./糗事百科.txt','w',encoding='utf-8')
    for i in range(1,4):
        threadParese = ThreadParse(parseQueue,i,fp)
        threadParese.start()
    # 队列锁添加
    requestQueue.join()
    parseQueue.join()
    print('----------------------------------->','执行')
    # 解析线程可以退出
    exitParseFlag = True
    # 关闭文件
    fp.close()
