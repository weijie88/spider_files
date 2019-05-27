from selenium import webdriver
import time
path = 'chromedriver.exe'

url = 'http://www.baidu.com/'
#创建了一个浏览器
browser = webdriver.Chrome(path)

browser.get(url=url)
#找到了文本框的对象
text = browser.find_element_by_id('kw')

text.send_keys('刘诗诗')

time.sleep(2)

buttton = browser.find_element_by_id('su')

buttton.click()

time.sleep(2)

browser.back()

time.sleep(1)

browser.forward()

time.sleep(2)
#关闭浏览器
browser.quit()
