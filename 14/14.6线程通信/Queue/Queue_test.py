"""
14.6.2	使用队列(Queue)控制线程通信

在 queue 模块下提供了几个阻塞队列,这些队列主要用于实现线程通信。

在 queue 模块下主要提供了三个类,分别代表三种队列,它们的主要区别就在于进队列、出队列的不同。关于这三个队列类的简单介绍如下。
(1)queue.Queue(maxsize = 0): 代表FIFO(先进先出)的常规队列,maxsize可以限制队列的大小。
如果队列的大小达到队列的上限,就会加锁,再次加入元素时就会被阻塞,直到队列中的元素被消费。
如果将maxsize 设置为0或负数,则该队列的大小就是无限制的
(2)queue.LifoQueue(maxsize=0):代表LIFO(后进先出)的队列,与Queue 的区别就是出队列的顺序不同。
(3)PriorityQueue(maxsize=0):代表优先级队列,优先级最小的元素先出队列。

这三个队列类的属性和方法基本相同,它们都提供了如下属性和方法。
(1)Queue.qsize():返回队列的实际大小,也就是该队列中包含几个元素。
(2)Queue.empty():判断队列是否为空。
(3)Queue.full():判断队列是否已满。
(4)Queue.put(item,block=True,timeout=None):向队列中放入元素。如果队列已满,且 block 参数为True(阻塞),
当前线程被阻塞,timeout指定阻塞时间,如果将timeout设置为None,则代表一直阻塞,直到该队列的元素被消费;
如果队列已满,且block参数为False(不阻塞),则直接引发queue.FULL异常。
(5)Queue.put_nowait(item):向队列中放入元素,不阻塞。相当于在上一个方法中将 block 参数设置为False。
(6)Queue.get(item,block=True,timeout=None):从队列中取出元素(消费元素)。
如果队列已满,且block参数为True (阻塞),当前线程被阻塞,timeout指定阻塞时间,
如果将timeout 设置为None,则代表一直阻塞,直到有元素被放入队列中;
如果队列已空,且block 参数为 False(不阻塞),则直接引发 queue.EMPTY异常。
(7)Queue.get_nowait(item):  从队列中取出元素,不阻塞。相当于在上一个方法中将block 参数设置为False。

下面以普通的Queue 为例介绍阻塞队列的功能和用法。首先用一个最简单的程序来测试Queue 的 put()和 get()方法。
"""
import queue

# 定义一个长度为2的阻塞队列
bq = queue.Queue(2)
bq.put("Python")
bq.put("Python")
print("1111111111")
bq.put("Python")  # ① 阻塞线程
print("2222222222")
"""
上面程序先定义了一个大小为2的Queue,程序先向该队列中放入两个元素,此时队列还没有满,两个元素都可以被放入。

当程序试图放入第三个元素时,如果使用 put()方法尝试放入元素将 会阻塞线程,如上面程序中①号代码所示。

与此类似的是,在 Queue 已空的情况下,程序使用 get() 方法尝试取出元素将会阻塞线程。
"""
