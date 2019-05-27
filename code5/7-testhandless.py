from handless import share_browser

browser = share_browser()

browser.get('http://www.baidu.com/')

browser.save_screenshot('handless1.png')
