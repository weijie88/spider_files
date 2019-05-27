from bs4 import BeautifulSoup

#open方法默认打开编码是gbk 所以我们需要指定编码格式 encoding=‘utf-8’
soup = BeautifulSoup(open('first.html',encoding='utf-8'),'lxml')
#打印的是第一个满足条件的标签
# print(soup.a)
# a = soup.a
#name是打印的标签的名字而不是标签的name属性值<a name = 'fdf'
# print(a.name)
#attrs获取得是标签属性名和属性值 以字典形式返回
# print(a.attrs)
#----------------------find
#返回的是一个标签类型对象 返回也是第一个满足条件的标签 类似于soup。a
# a = soup.find('a')
# print(type(a))
# print(a)
# a = soup.find('a',title='fq')
# print(type(a))
# print(a)
#注意 当想获取class的值的标签的时候  需要在class后面加一个下划线
# li = soup.find('li',class_='hengheng1')
# print(type(li))
# print(li)
#=-----总结 soup.find方法返回的都是一个对象
#-----------------------------------findall
#查询所有a标签 返回的是一个列表
# a_list = soup.find_all('a')
# print(type(a_list))
# print(a_list)
# mix_list = soup.find_all(["a","li"])
# print(mix_list)
# limit_list = soup.find_all('li',limit=3)
# print(limit_list)
#返回的是一个列表 返回了所有的a标签
# a = soup.select('a')
# print(a)
#使用类选择器查询节点对象列表
# li = soup.select('.em')
# print(li)
#使用id选择器查询节点对象列表
# li = soup.select('#heihei')
# print(li)
#查询li标签中有class的标签对象  返回的也是一个列表
# li = soup.select('li[class]')
# print(li)
#查询li标签中有class的值为hengheng1的标签对象  返回的也是一个列表
# li = soup.select('li[class="hengheng1"]')
# print(li)
#空格代表的是第一级子标签以及第二极以下的标签
# li = soup.select('div ul')   //
# print(li)
#注意 在>的两边一定要有空格
# li = soup.select('div > ul')  /
# print(li)
#如果使用select查询一个组合标签 那么这些标签是放到一个字符串里的
# li = soup.select('a,li')
# print(li)

# a = soup.find('a')
# print(a)
# #如果标签中还有其他的标签  那么使用string这个方法 返回的是none 而get_text方法返回的是拼接之后的内容
# #我们推荐使用get_text()
# print(a.string)
# print(a.get_text())


# print(soup.body.contents)



# print(soup.body.descendants)
# for haha in soup.body.descendants:
#     print(haha)

# a = soup.find('a')
# print(a)
# b = a.attrs
# print(b.get('href'))

a = soup.a

print(a.string)
import bs4

if type(a.string) == bs4.element.Comment:
    print('i am zhushi')
else:
    print('i am not zhushi')




