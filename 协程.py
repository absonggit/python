def yield_test(n):  
    for i in range(n):  
        yield call(i)  
        print(i)
def call(i):  
    return i*2  
  
#使用for循环  
for i in yield_test(5):  
    pass


def producer(c):
    c.send(None)
    for i in range(5):
        print("生产%d" % i)
        c.send(str(i))
    c.close()

def consumer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费%s" % n)
c = consumer()
producer(c)
