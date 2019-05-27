'''
threading.RLock和threading.Lock 的区别
RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
如果使用RLock，那么acquire和release必须成对出现，
即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。
'''
import threading

lock = threading.Lock()    #Lock对象
lock.acquire()
lock.acquire()  #产生了死琐。
lock.release()
#lock.release()　

# import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire()    #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()