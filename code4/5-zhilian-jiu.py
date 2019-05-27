'''
https://sou.zhaopin.com/jobs/searchresult.ashx?jl=上海
&kw=爬虫工程师&sm=0&p=1

//div[@id="newlist_list_content_table"]/table/tbody/tr/td/div/a
#newlist_list_content_table > table > tbody > tr > td > div > a
//td[@class="gsmc"]
.gsmc
//td[@class="zwyx"]
.zwyx
//td[@class="gzdd"]
.gzdd


bug:
    1 cookie
    2 bs4路径
    3 类型转换
            写进json文件的数据类型一定是json字符串
            python对象转换成json字符串的方法是dumps
            python对象是列表的情况下  列表中的元素一定是一个字典
                       为什么是字典？
                       因为json文件就是以字典格式显示的
                       将python对象转换为字典的方法是对象.__dict__
'''

import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from Item1 import Zhiwei

get_url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': 'ZP-ENV-FLAG=gray; adfbid2=0; sts_deviceid=164a0bd42d0c96-087b28d667f285-47e1039-1296000-164a0bd42d2b17; dywea=95841923.2852643098294665000.1536823481.1536823481.1536823481.1; dywec=95841923; dywez=95841923.1536823481.1.1.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; __utma=269921210.1290550856.1536823482.1536823482.1536823482.1; __utmc=269921210; __utmz=269921210.1536823482.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; sts_sg=1; sts_sid=165d1d161ed93e-0959b3e32a26bb-9393265-1296000-165d1d161ee729; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DfTEUNAFOwzYXwFQSieeMNUFBk30190SZOwEQCuiU4JlqsBdUESZgoOZ0EEsdncnv%26wd%3D%26eqid%3Dc48e3d520003f9bd000000025b9a10b4; ZP-ENV-FLAG=gray; GUID=df0b9a420e87459eb846da1eccfea8e0; Hm_lvt_d838d7d6abb840b6c1a339ec5aee915d=1536823486; Hm_lpvt_d838d7d6abb840b6c1a339ec5aee915d=1536823486; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1536823487; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1536823487; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%2293fe89a4-54bd-4d7a-a01b-781761494d69-sou%22%2C%22funczone%22:%22smart_matching%22}}; ZP_OLD_FLAG=true; _jzqa=1.2566278383055240700.1536823492.1536823492.1536823492.1; _jzqc=1; _jzqx=1.1536823492.1536823492.1.jzqsr=sou%2Ezhaopin%2Ecom|jzqct=/.-; _jzqckmp=1; _qzjc=1; JSSearchModel=0; BLACKSTRIP=yes; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%91%a8%e6%9c%ab%e5%8f%8c%e4%bc%91%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e9%a4%90%e8%a1%a5%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e6%af%8f%e5%b9%b4%e5%a4%9a%e6%ac%a1%e8%b0%83%e8%96%aa%7c%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%8c%85%e5%90%83%7c14%e8%96%aa%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e5%8c%85%e4%bd%8f%7c%e5%81%a5%e8%ba%ab%e4%bf%b1%e4%b9%90%e9%83%a8%7c%e4%b8%8d%e5%8a%a0%e7%8f%ad%7c%e6%88%bf%e8%a1%a5%7c%e4%bd%8f%e6%88%bf%e8%a1%a5%e8%b4%b4%7c%e6%97%a0%e8%af%95%e7%94%a8%e6%9c%9f%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4%7c%e5%85%8d%e6%81%af%e6%88%bf%e8%b4%b7; lastchannelurl=https%3A//passport.zhaopin.com/account/login%3FbkUrl%3Dhttps%253A%252F%252Fsou.zhaopin.com%252Fjobs%252Fsearchresult.ashx%253Fjl%253D%2525E4%2525B8%25258A%2525E6%2525B5%2525B7%2526kw%253Dpython%2525E5%2525BC%252580%2525E5%25258F%252591%2526sm%253D0%2526p%253D1%2526isadv%253D0; __utmt=1; qrcodekey=79a50f22542a4dc587c6d04283defbc2; firstchannelurl=https%3A//passport.zhaopin.com/account/login%3FbkUrl%3Dhttps%253A//sou.zhaopin.com/jobs/searchresult.ashx%253Fjl%253D%2525E4%2525B8%25258A%2525E6%2525B5%2525B7%2526kw%253Dpython%2525E5%2525BC%252580%2525E5%25258F%252591%2526sm%253D0%2526p%253D1%2526isadv%253D0%26y7bRbP%3DdpoIrmwUYTwUYTwUzGB9xu36y.gRHeRVbELBl_nJZYQ; JsNewlogin=1849791356; JSloginnamecookie=18642820892; JSShowname=%E6%9D%8E%E6%99%B6; at=52ee666fdb554253a4365476ccc7ae65; Token=52ee666fdb554253a4365476ccc7ae65; rt=765b12a58645415194725c17899c7127; JSsUserInfo=3d753d6857645e7548685c645d7540685d645975486852645375356824645575486852645e754d68586450754b685a6450754068586453752c6824645575370f1c0253753c68276455754c6853645d7548685c645d754a685f64507539681b641975576809640775146851643b752d6857645a7542682b643c754468526445754d684a6459754c6850645d7548685164297535685764587542683f64297544682064257548685c645d7540685d645975486852645a7542683f643c7544685b6453752a6823645575496851643d75296824645575486852645e754d68586450754b685a6450754068586453753; uiioit=3b622a6459640e644664416a5d6e5b6e5364553855775c7751682c622a64596408644c646; sts_evtseq=6; LastSearchHistory=%7b%22Id%22%3a%22059e1d1e-e255-43ce-bf77-847ef5df4fa2%22%2c%22Name%22%3a%22python%e5%bc%80%e5%8f%91+%2b+%e4%b8%8a%e6%b5%b7%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e4%25b8%258a%25e6%25b5%25b7%26kw%3dpython%25e5%25bc%2580%25e5%258f%2591%26sm%3d0%26p%3d1%26isadv%3d0%22%2c%22SaveTime%22%3a%22%5c%2fDate(1536825083091%2b0800)%5c%2f%22%7d; SubscibeCaptcha=CFA654C7E1BFD4EB37E3AFD5EB3A8E6D; dywem=95841923.y; dyweb=95841923.10.9.1536825054607; __utmb=269921210.10.9.1536825054611; _qzja=1.334852622.1536823491631.1536823491631.1536823491632.1536824312831.1536825078202.0.0.0.6.1; _qzjb=1.1536823491631.6.0.0.0; _qzjto=6.1.0; _jzqb=1.7.10.1536823492.1; loginreleased=1'
}
data = {
    'jl':'上海',
    'kw':'python开发',
    'sm':'0',
    'p':'1',
}
data = urllib.parse.urlencode(data)
url = get_url + data
request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)
#此页面返回的是登陆页面  那么登陆页面中是没有bs4定位信息的 所以我们需要添加cookie
content = response.read().decode('utf-8')
# print(content)
soup = BeautifulSoup(content,'lxml')
table_list = soup.select('#newlist_list_content_table > table')
Zs = []
#使用切片的原因是因为table_list把表头的信息table也算作一行  所以需要使用切片
for table in table_list[1:]:
    ##newlist_list_content_table > table > tbody > tr > td > div > a
    zwmc = table.select('tr > td > div > a')[0].get_text()
    '''
    //td[@class="gsmc"]
    .gsmc
    //td[@class="zwyx"]
    .zwyx
    //td[@class="gzdd"]
    .gzdd
    '''
    gsmc = table.select('td[class="gsmc"] > a')[0].get_text()
    zwyx = table.select('td[class="zwyx"]')[0].get_text()
    gzdd = table.select('td[class="gzdd"]')[0].get_text()
    zhiwei = Zhiwei(zwmc,gsmc,zwyx,gzdd)
    Zs.append(zhiwei.__dict__)
#因为Zs是一个python对象 是不可以保存json文件中  所以我们需要把python对象
#转换成json字符串  使用的方法是json.dumps
import json
obj = json.dumps(Zs,ensure_ascii=False)
with open('zhiwei.json','w',encoding='utf-8')as fp:
    fp.write(obj)





