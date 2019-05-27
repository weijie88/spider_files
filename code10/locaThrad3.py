'''
Lock,RLock是多个用户同时修改一份数据，可能会出现脏数据，数据就会乱，
就加互斥锁，一次只能让一个人修改数据，就能解决。
condition，使用场景：
如果写了个爬虫，在建立数据库连接，线程就等着，什么能数据库能用了，就开通线程，
再爬虫。
notify维护一个队列，传几个，就只能出去几次。
'''
import threading
def func(i, con):
    print(i)
    con.acquire()
    con.wait()#线程休眠
    print(i + 100)
    con.release()
    #暂时不知道condition对象的作用
c = threading.Condition()
for i in range(10):
    #创建一个线程
    t = threading.Thread(target=func, args=(i, c,))
    #开启一个线程
    t.start()
while True:
    inp = input(">>>")
    if inp == 'q':
        break
    c.acquire()
    c.notify(int(inp))#唤醒
    c.release()