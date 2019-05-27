from selenium import webdriver

import time

url = 'http://www.baidu.com/'

browser = webdriver.Chrome('chromedriver.exe')

browser.get(url=url)

time.sleep(1)

text = browser.find_element_by_id('kw')

text.send_keys('刘诗诗')

time.sleep(1)

button = browser.find_element_by_id('su')

button.click()

time.sleep(1)

browser.back()

time.sleep(1)

browser.forward()

browser.quit()

