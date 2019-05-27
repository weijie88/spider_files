from selenium import webdriver
import time
path = 'chromedriver.exe'

url = 'https://www.qiushibaike.com/'

browser = webdriver.Chrome(path)

browser.get(url=url)

time.sleep(2)

# js='document.body.scrollTop=100000'
# browser.execute_script(js)
js='document.documentElement.scrollTop=100000'
browser.execute_script(js)

time.sleep(2)

next = browser.find_elements_by_css_selector('.next')[0]

next.click()

time.sleep(1)

browser.quit()

