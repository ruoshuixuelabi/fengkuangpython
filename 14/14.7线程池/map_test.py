"""
此外,Exectuor还提供了一个map(func,*iterables, timeout=None,chunksize=1)方法,该方法的功能类似于全局函数map()
区别在于线程池的map()方法会为iterables的每个元素启动一个线程,以并发方式来执行func函数。
这种方式相当于启动len(iterables)个线程,并收集每个线程的执行结果。

例如,如下程序使用Executor的 map()方法来启动线程,并收集线程任务的返回值。
"""
import threading
from concurrent.futures import ThreadPoolExecutor


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含4条线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程执行map计算
    # 后面元组有3个元素,因此程序启动3条线程来执行action函数
    results = pool.map(action, (50, 100, 150))
    print('--------------')
    for r in results:
        print(r)
"""
上面程序中的粗体字代码使用map()方法来启动3个线程(该程序的线程池包含4个线程,如果继续使用只包含两个线程的线程池,
此时将有一个任务处于等待状态,必须等其中一个任务完成、 线程空闲出来才会获得执行的机会),
map() 方法的返回值将会收集每个线程任务的返回结果。

运行上面程序,同样可以看到3个线程并发执行的结果,最后通过results可以看到3个线程任务的返回结果。

通过上面程序可以看出,使用map (方法来启动线程,并收集线程的执行结果,不仅具有代码简单的优点,
而且虽然程序会以并发方式来执行action()函数,但最后收集的action()函数的执行结 果,依然与传入参数的结果保持一致。
也就是说,上面results的第一个元素是action(50)的结果,第二个元素是action(100)的结果,第三个元素是action(150)的结果。
"""