'''
新版的智联的接口返回的是一个json文件  所以我们需要使用jsonpath方法来解析数据
找接口：只能通过接口去观察response（建议使用fiddler）
jsonpath的解析路径

'''
import urllib.request
import jsonpath
import json

get_url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22538%22,%22kt%22:%223%22%7D'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
request = urllib.request.Request(url=get_url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open('zhilian.json','w',encoding='utf-8')as fp:
    fp.write(content)


obj = json.load(open('zhilian.json','r',encoding='utf-8'))

ret = jsonpath.jsonpath(obj,'$.data.results[*].company.name')

for r in ret:
    print(r)
