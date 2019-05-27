'''
# queue.Queue，先进先出队列
# queue.LifoQueue，后进先出队列
# queue.PriorityQueue，优先级队列
# queue.deque，双向对队

python的队列是在内存里创建的，python的进程退出了，则队列也清空了。
'''
import queue
q = queue.LifoQueue()
q.put(123)
q.put(456)
# 打印；456
# 优先级最小的拿出来
'''
首先根据前面参数的优先级判断 优先级大的输出 
如果第一个参数的优先级一致 那么根据第二个参数的ascii码判断 
如果2个参数一致  会输出第二个存放到队列的数据
'''
q = queue.PriorityQueue()
q.put((2,'alex2'))
q.put((2,'alex2'))
# q.put((1,'abaaalex3'))
# q.put((3,'alex3'))
# q.put((1, 'aalex21'))
# print(q.get())

q = queue.deque()
q.append(123)
q.append(333)
q.appendleft(456)
# deque([456, 123, 333])
print(q)
# 打印：456
print(q[0])
q.pop()     # 从右边删除
# # deque([456, 123])
print(q)
q.popleft() # 从左边删除