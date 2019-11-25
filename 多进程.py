from multiprocessing import Pool, Process
import time
import os

name = "tom"


def P1(name):
    time.sleep(2)
    print("你好,%s先生!\nP1 child process ID: %s\nP2 parent process ID: %s" %
          (name, os.getpid(), os.getppid()))


def P2():
    time.sleep(2)
    global name
    name = "jerry"
    print("P2 child process ID: %s\nP2 parent process ID: %s" %
          (os.getpid(), os.getppid()))
    print("P2 -> name: " + name)


if __name__ == "__main__":
    print("Main -> name: " + name)
    ppool = Pool(3)
    for name in ["A","B","C"]:
        ppool.apply_async(P1,args=(name,))
    p1 = Process(target=P1, args=("harry",))
    p2 = Process(target=P2)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    ppool.close()
    ppool.join()
    time.sleep(2)
    print("main process ID: %s" % (os.getpid()))
    print("程序执行完毕 name = %s" % (name))
