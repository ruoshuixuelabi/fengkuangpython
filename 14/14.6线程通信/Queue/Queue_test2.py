"""
在掌握了 Queue 阻塞队列的特性之后,在下面程序中就可以利用 Queue 来实现线程通信了。

"""
import threading
import time
import queue


def product(bq):
    str_tuple = ("Python", "Kotlin", "Swift")
    for i in range(99999):
        print(threading.current_thread().name + "生产者准备生产元组元素！")
        time.sleep(0.2);
        # 尝试放入元素,如果队列已满,则线程被阻塞
        bq.put(str_tuple[i % 3])
        print(threading.current_thread().name \
              + "生产者生产元组元素完成！")


def consume(bq):
    while True:
        print(threading.current_thread().name + "消费者准备消费元组元素！")
        time.sleep(0.2)
        # 尝试取出元素,如果队列已空,则线程被阻塞
        t = bq.get()
        print(threading.current_thread().name \
              + "消费者消费[ %s ]元素完成！" % t)


# 创建一个容量为1的Queue
bq = queue.Queue(maxsize=1)
# 启动3个生产者线程
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
# 启动一个消费者线程
threading.Thread(target=consume, args=(bq,)).start()
"""
上面程序启动了三个生产者线程向 Queue 队列中放入元素,启动了三个消费者线程从 Queue 队列中取出元素。
本程序中 Queue 队列的大小为1,因此三个生产者线程无法连续放入元素,必须等待消费者线程取出一个元素后,
其中的一个生产者线程才能放入一个元素。运行该程序,将会看到如图14.9所示的结果。

从图14.9可以看出,三个生产者线程都想向 Queue 中放入元素,但只要其中一个生产者线程向该队列中放入元素之后,
其他生产者线程就必须等待,等待消费者线程取出Queue 队列中的元素。
"""