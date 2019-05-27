import queue
#from queue import Queue
#队列

#q = queue.Queue()如果没有参数的话，就是可以放无限多的数据。
q = queue.Queue(2)
print(q.empty())    # 返回队列是否为空，空则为True，此处为True
q.put(11)
q.put(22)
print(q.empty())    # 此处为False
print(q.qsize())    # 返回队列中现在有多少元素
# q.put(22)
# 如果队列最大能放2个元素，这时候放了第三个，默认是阻塞的，block=False，
# 如果就会报错：queue.Full
# q.put(33,block=False)
# 设置为阻塞，如果timeout设置的时间之内，还没有人来取，则就会报错：queue.Full
# q.put(33,block=True,timeout=2)
print(q.get())
print(q.get())
# # 队列里的数据已经取完了，如果再取就会阻塞，这里timeout时间2秒，就是等待2秒，
# 队列里还没有数据就报错：queue.Empty
print(q.get(timeout=2))