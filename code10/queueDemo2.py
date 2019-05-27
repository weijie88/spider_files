'''
# join：实际上意味着等到队列为空，再执行别的操作，否则就一直阻塞，
不是说get取完了，就不阻塞了，而是每次get之后，
# 要执行：task_done 告诉一声已经取过了，等队列为空，join才不阻塞。
'''
import queue
q = queue.Queue(2)
q.put(123)
q.put(456)
q.get()
q.task_done()
q.get()
# 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
q.task_done()
q.join()