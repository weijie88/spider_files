#需求  1 下载网页  2 下载图片  3 下载视频

import urllib.request

url = 'http://www.baidu.com/'
#使用urlretrieve方法来下载网页
urllib.request.urlretrieve(url = url,filename='baidu.html')

#下载图片
img_url = 'https://p99.pstatp.com/list/190x124/pgc-image/1536460411354f5b2854b56'
urllib.request.urlretrieve(url = img_url,filename='xiuren.jpg')

vedio_url = 'http://v11-tt.ixigua.com/e2d631f90c37b9ae37fe642737ac158f/5b95edca/video/m/22063ece14a138a40eaa0cb3d6dc402876b115b4d370000df170081607f/'
#下载视频
urllib.request.urlretrieve(url = vedio_url,filename='niuren.mp4')

