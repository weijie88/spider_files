from selenium import webdriver
import time
path = 'chromedriver.exe'

url = 'https://www.qiushibaike.com/'

browser = webdriver.Chrome(path)

browser.get(url=url)
time.sleep(3)
next = browser.find_elements_by_css_selector('.next')[0]

next.click()

time.sleep(5)
browser.quit()



