from selenium import webdriver

path = 'chromedriver.exe'

url = 'http://www.baidu.com/'

browser = webdriver.Chrome(path)

browser.get(url = url)
#获取响应源代码  和使用真实浏览器响应的数据一致
content = browser.page_source

# print(content)
#name是标签的属性值
# name = browser.find_elements_by_name('wd')
# print(name)
# #标签的对象
# tag_name = browser.find_elements_by_tag_name('input')
# print(tag_name)

# map = browser.find_elements_by_link_text('地图')
#
# print(map)
# xx = browser.find_elements_by_xpath('//input[@id="kw"]')
# print(xx)
# dd = browser.find_elements_by_css_selector('#kw')
# # print(dd)
# su = browser.find_element_by_id('su')
# print(su)
# #获取标签中的属性值
# print(su.get_attribute('id'))
# print(su.text)

su_button = browser.find_elements_by_css_selector('#su')[0]
print(su_button.get_attribute("class"))

print(su_button.tag_name)

print(su_button.text)

print(su_button.id)







browser.quit()