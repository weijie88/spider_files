from threading import Timer

def hello():
    print("hello, world")

t = Timer(1, hello)  # 等1秒，执行hello
t.start()