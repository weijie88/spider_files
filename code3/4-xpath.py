# pip install lxml
#xpath是爬虫中比较火一种解析方式
#使用xpath解析得文件有两种形式
                    # 1 解析本地文件   first.html  etree.parse(本地文件名字)
                    # 2 解析服务器响应文件（常用） response.read().deocde()
                        # etree.HTML(content)
from lxml import etree

tree = etree.parse('first.html')
#在xpath方法中写xpath语法
# li_list = tree.xpath('//li/text()')
# print(li_list)
# li_list = tree.xpath('div')
# print(li_list)

# list = tree.xpath('//div')
# print(list)
# list = tree.xpath('/div')
# print(list)
#查询有id得div标签
# div_list = tree.xpath('//div[@id]')
# # print(div_list)
#查询id值为hehe得div标签  注意 一定要加上“”
# haha = tree.xpath('//div[@id="haha"]')
# print(haha)
#查询li标签下有class得标签
# class_list = tree.xpath('//li[@class]')
# print(class_list)
#查询id为heihei和class为hengheng得li标签
# mix_list = tree.xpath('//li[@id="heihei" and @class="hengheng"]')
# print(mix_list)
#li标签中以he开头标签
# li_list = tree.xpath('//li[starts-with(@class,"he")]')
# print(li_list)





