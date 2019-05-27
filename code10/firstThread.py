import threading
import time
#创建线程
  # 1 导入threading
  # 2 threading.Thread()
def worker(num):
    time.sleep(1)
    print("The num is  %d" % num)
    return

for i in range(20):
    t = threading.Thread(target=worker, args=(i,))
    #启动线程的方法是？ start（）方法
    t.start()

