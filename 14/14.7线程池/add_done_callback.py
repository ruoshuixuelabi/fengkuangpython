"""
14.7.2	获取执行结果

前面程序调用了 Future 的 result()方法来获取线程任务的返回值,但该方法会阻塞当前主线程,只有等到线程任务完成后,
result()方法的阻塞才会被解除。

如果程序不希望直接调用 result()方法阻塞线程,则可通过 Future 的 add_done_callback()方法来添加回调函数,该回调函数形如 fn(future)。
当线程任务完成后,程序会自动触发该回调函数,并将对应的Future对象作为参数传给该回调函数。

下面程序使用add done callback()方法来获取线程任务的返回值。
"""
from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含2条线程的线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池提交一个task,50会作为action()函数的参数
    future1 = pool.submit(action, 50)
    # 向线程池再提交一个task,100会作为action()函数的参数
    future2 = pool.submit(action, 100)


    def get_result(future):
        print(future.result())


    # 为future1添加线程完成的回调函数
    future1.add_done_callback(get_result)
    # 为future2添加线程完成的回调函数
    future2.add_done_callback(get_result)
    print('--------------')
"""
上面主程序中的两行粗体字代码分别为future1、future2 添加了同一个回调函数,该回调函数会在线程任务结束时获取其返回值。

主程序的最后一行代码打印了一条横线。由于程序并未直接调用future1、future2的 result()方法,
因此主线程不会被阻塞,可以立即看到输出主线程打印出的横线。
接下来将会看到两个新线程并发执行,当线程任务执行完成后, get_result()函数被触发,输出线程任务的返回值。

另外,由于线程池实现了上下文管理协议(Context Manage Protocol),因此,程序可以使用with语句来管理线程池,
这样即可避免手动关闭线程池,如上面的程序所示。
"""
