import threading
import time

NUM = 10
def func(lock):
    global NUM
    # 上锁
    lock.acquire()
    NUM -= 1 #NUM = NUM-1
    time.sleep(1)
    print(NUM)
    # 开锁
    lock.release()
# Lock = threading.Lock()   # 不支持嵌套锁，一般不用
RLock = threading.RLock()   # 一般用RLock，支持嵌套锁。
for i in range(10):
    t = threading.Thread(target=func,args=(RLock,))
    t.start()

'''
死锁：
就是你也抢资源，我也抢资源，谁也抢不走就是死锁。
如果是python，就是Lock，弄成嵌套锁，不支持，则变成死锁。
解决办法：
用RLock，支持嵌套锁
'''