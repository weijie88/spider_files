from selenium import webdriver
#这个是浏览器自带的  不需要我们再做额外的操作
from selenium.webdriver.chrome.options import Options

def share_browser():
	#初始化
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
    #下面这个路径是需要我们修改的  路径是你的chrome浏览器安装的路径
	path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
	chrome_options.binary_location = path

	browser = webdriver.Chrome(chrome_options=chrome_options)

	return  browser