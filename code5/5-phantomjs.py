from selenium import webdriver

path = 'phantomjs.exe'

url = 'http://www.baidu.com/'

browser = webdriver.PhantomJS(path)

browser.get(url=url)

browser.save_screenshot('1.jpg')

text = browser.find_element_by_id('kw')

text.send_keys('陈独秀')

browser.save_screenshot('2.jpg')

button = browser.find_element_by_id('su')

button.click()

browser.save_screenshot('3.jpg')