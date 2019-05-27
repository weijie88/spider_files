#安装jsonpath pip install jsonpath
import jsonpath
import json

obj = json.load(open(r'./code4/book.json','r',encoding='utf-8'))
 print(type(obj))
 print(obj)
jsonpath(1个参数（解析的对象），2个参数（解析的语法）)
书点所有书的作者
 ret = jsonpath.jsonpath(obj,'$.store.book[*].author')
所有的作者
 ret = jsonpath.jsonpath(obj,'$...author')
 ret = jsonpath.jsonpath(obj,'$.store.*')
 ret = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')

ret = jsonpath.jsonpath(obj,'$..book[?(@.isbn)')
print(ret)

