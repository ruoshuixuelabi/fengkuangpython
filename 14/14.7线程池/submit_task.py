"""
系统启动一个新线程的成本是比较高的,因为它涉及与操作系统的交互。在这种情形下,使用线程池可以很好地提升性能,
尤其是当程序中需要创建大量生存期很短暂的线程时,更应该考虑使用线程池。

线程池在系统启动时即创建大量空闲的线程,程序只要将一个函数提交给线程池,线程池就会启动一个空闲的线程来执行它。
当该函数执行结束后,该线程并不会死亡,而是再次返回到线程池中变成空闲状态,等待执行下一个函数。

此外,使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时,会导致系统性能急剧下降,
甚至导致 Python 解释器崩溃,而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。

14.7.1	使用线程池

线程池的基类是 concurrent.futures 模块中的 Executor,Executor 提供了两个子类,即 ThreadPoolExecutor 和 ProcessPoolExecutor,
其中 ThreadPoolExecutor 用于创建线程池,而 ProcessPoolExecutor用于创建进程池。

如果使用线程池/进程池来管理并发编程,那么只要将相应的 task 函数提交给线程池/进程池, 剩下的事情就由线程池/进程池来搞定。

Exectuor提供了如下常用方法。
(1)submit(fn,*args,**kwargs):将 fn函数提交给线程池。*args代表传给fn函数的参数,*kwargs代表以关键字参数的形式为fn函数传入参数。
(2)map(func,*iterables,timeout=None,chunksize=1): 该函数类似于全局函数 map(func,*iterables),只是该函数将会启动多个线程,
以异步方式立即对iterables执行 map 处理。
(3)shutdown(wait=True): 关闭线程池。

程序将task函数提交(submit)给线程池后, submit方法会返回一个Future对象,Future类主要用于获取线程任务函数的返回值。
由于线程任务会在新线程中以异步方式执行,因此,线程执行 的函数相当于一个"将来完成"的任务,所以 Python 使用 Future 来代表。

提示：实际上,在Java的多线程编程中同样有Future, 此处的Future与 Java的 Future大同小异。

Future提供了如下方法。
(1)cancel(): 取消该Future代表的线程任务。如果该任务正在执行,不可取消,则该方法返回False; 否则,程序会取消该任务,并返回True。
(2)cancelled(): 返回Future代表的线程任务是否被成功取消。
(3)running(): 如果该Future代表的线程任务正在执行、不可被取消,该方法返回True。
(4)done():  如果该Future代表的线程任务被成功取消或执行完成,则该方法返回True。
(5)result(timeout=None): 获取该Future代表的线程任务最后返回的结果。
如果Future代表的 线程任务还未完成,该方法将会阻塞当前线程,其中timeout参数指定最多阻塞多少秒。
(6)exception(timeout=None):获取该Future代表的线程任务所引发的异常。如果该任务成功完成,没有异常,则该方法返回None。
(7)add_done_callback(fn): 为该Future代表的线程任务注册一个"回调函数",当该任务成功完成时,程序会自动触发该fn 函数。

在用完一个线程池后,应该调用该线程池的shutdown()方法,该方法将启动线程池的关闭序列。
调用shutdown()方法后的线程池不再接收新任务,但会将以前所有的已提交任务执行完成。
当线程池中的所有任务都执行完成后,该线程池中的所有线程都会死亡。

使用线程池来执行线程任务的步骤如下。

①调用 ThreadPoolExecutor 类的构造器创建一个线程池。
②定义一个普通函数作为线程任务。
③调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务。
④当不想提交任何任务时,调用 ThreadPoolExecutor 对象的 shutdown() 方法来关闭线程池。

下面程序示范了如何使用线程池来执行线程任务。
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
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 50)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 100)
# 判断future1代表的任务是否结束
print(future1.done())
time.sleep(3)
# 判断future2代表的任务是否结束
print(future2.done())
# 查看future1代表的任务返回的结果
print(future1.result())
# 查看future2代表的任务返回的结果
print(future2.result())
# 关闭线程池
pool.shutdown()
"""
上面程序中第一行粗体字代码创建了一个包含两个线程的线程池,接下来的两行粗体字代码只要将action()函数提交(submit)给线程池,
该线程池就会负责启动线程来执行action()函数。这种启动线程的方法既优雅,又具有更高的效率。

当程序把action()函数提交给线程池时,submit()方法会返回该任务所对应的Future对象,
程序立即判断futurel的 done()方法,该方法将会返回False——表明此时该任务还未完成。
接下来主程 序暂停3秒,然后判断future2的 done()方法,如果此时该任务已经完成,那么该方法将会返回True。

程序最后通过 Future的 result()方法来获取两个异步任务返回的结果。运行上面程序,在程序开始执行时可以看到如图14.10所示的输出信息。
当程序执行完成后,可以看到如图14.11所示的输出信息。

当程序使用Future的 result()方法来获取结果时,该方法会阻塞当前线程,如果没有指定timeout参数,
当前线程将一直处于阻塞状态,直到Future代表的任务返回。
"""
