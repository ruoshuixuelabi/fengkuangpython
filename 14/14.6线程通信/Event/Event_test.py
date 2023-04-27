"""
14.6.3	使用Event控制线程通信

Event 是一种非常简单的线程通信机制：一个线程发出一个 Event,另一个线程可通过该 Event 被触发。

Event 本身管理一个内部旗标,程序可以通过 Event 的 set()方法将该旗标设置为True,
也可以调用 clear()方法将该旗标设置为False。程序可以调用wait()方法来阻塞当前线程,直到Event 的内部旗标被设置为True

Event 提供了如下方法。
(1)is_set(): 该方法返回 Event 的内部旗标是否为True。
(2)set(): 该方法将会把 Event 的内部旗标设置为True, 并唤醒所有处于等待状态的线程。
(3)clear(): 该方法将 Event 的内部旗标设置为False,通常接下来会调用wait()方法来阻塞当前 线程。
(4)wait(timeout=None):该方法会阻塞当前线程。

下面程序示范了Event 最简单的用法。
"""
import threading
import time

event = threading.Event()


def cal(name):
    # 等待事件,进入等待阻塞状态
    print('%s 启动' % threading.current_thread().name)
    print('%s 准备开始计算状态' % name)
    event.wait()  # ①
    # 收到事件后进入运行状态
    print('%s 收到通知了.' % threading.current_thread().name)
    print('%s 正式开始计算！' % name)


# 创建并启动两条,它们都会①号代码处等待
threading.Thread(target=cal, args=('甲',)).start()
threading.Thread(target=cal, args=("乙",)).start()
time.sleep(2)  # ②
print('------------------')
# 发出事件
print('主线程发出事件')
event.set()
"""
上面程序以 cal()函数为 target,创建并启动了两个线程。由于 cal()函数在①号代码处调用了 Event 的 wait(),
因此两个线程执行到①号代码处都会进入阻塞状态;即使主线程在②号代码处被阻塞,两个子线程也不会向下执行。

直到主程序执行到最后一行：程序调用了 Event 的 set()方法将Event 的内部旗标设置为True, 并唤醒所有等待的线程,这两个线程才能向下执行。

运行上面程序,将看到如下输出结果。

Thread-1 (cal) 启动
甲 准备开始计算状态
Thread-2 (cal) 启动
乙 准备开始计算状态
------------------
主线程发出事件
Thread-1 (cal) 收到通知了.Thread-2 (cal) 收到通知了.
甲 正式开始计算！
乙 正式开始计算！

上面程序还没有使用 Event 的内部旗标,如果结合 Event 的内部旗标,同样可实现前面的Account 的生产者-消费者效果：
存钱线程(生产者)存钱之后,必须等取钱线程(消费者)取钱之 后才能继续向下执行。
提示：Event 实际上有点类似于Condition和旗标的结合体,但 Event 本身并不带Lock 对象,
因此,如果要实现线程同步,还需要额外的Lock 对象。
"""
