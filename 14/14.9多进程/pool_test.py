"""
14.9.4	使用进程池管理进程

与线程池类似的是,如果程序需要启动多个进程,也可以使用进程池来管理进程。
程序可以通过 multiprocessing 模块的 Pool()函数创建进程池,进程池实际上是multiprocessing.pool.Pool类。

进程池具有如下常用方法。
(1)apply(func[,args[,kwds]]):将 func 函数提交给进程池处理。其中args代表传给func 的位置参数,
kwds 代表传给func的关键字参数。该方法会被阻塞直到 func 函数执行完成。
(2)apply_async(func[,args[, kwds[,callback[,error_callback]]]]): 这是apply()方法的异步版本, 该方法不会被阻塞。
其中callback指定func 函数完成后的回调函数,error_callback指定 func 函数出错后的回调函数。
(3)map(func,iterable[,chunksize]): 类似于Python 的 map() 全局函数,只不过此处使用新进程对 iterable的每一个元素执行 func 函数。
(4)map_async(func,iterable[,chunksize[,callback[,error_callback]]]): 这是map()方法的异步版本,该方法不会被阻塞。
其中 callback 指定 func 函数完成后的回调函数, error_callback 指定 func 函数出错后的回调函数。
(5)imap(func,iterable[,chunksize]): 这 是map()方法的延迟版本。
(6)imap_unordered(func,iterable[,chunksize]):功能类似于imap()方法,
但该方法不能保证所生成的结果(包含多个元素)与原iterable 中的元素顺序一致。
(7)starmap(func,iterable[,chunksize]):功能类似于map()方法,但该方法要求iterable的元素也是 iterable对象,
程序会将每一个元素解包之后作为func 函数的参数。
(8)close(): 关闭进程池。在调用该方法之后,该进程池不能再接收新任务,它会把当前进程池中的所有任务执行完成后再关闭自己。
(9)terminate():  立即中止进程池。
(10)join(): 等待所有进程完成。

从上面介绍不难看出,如果程序只是想将任务提交给进程池执行,则可调用 apply()或 apply async()方法;
如果程序需要使用指定函数将iterable转换成其他iterable, 则可使用 map()或 imap()方法。

下面程序示范了使用apply async()方法启动进程。
"""
import multiprocessing
import time
import os


def action(name='default'):
    print('(%s)进程正在执行,参数为: %s' % (os.getpid(), name))
    time.sleep(3)


if __name__ == '__main__':
    # 创建包含4条进程的进程池
    pool = multiprocessing.Pool(processes=4)
    # 将action分3次提交给进程池
    pool.apply_async(action)
    pool.apply_async(action, args=('位置参数',))
    pool.apply_async(action, kwds={'name': '关键字参数'})
    pool.close()
    pool.join()
"""
上面程序中第一行粗体字代码创建了一个进程池,接下来3行粗体字都负责将action提交给进程池,只是每次提交时指定参数的方式不同。

运行上面程序,可以看到如下输出结果。

从上面的输出结果可以看到,程序分别使用3个进程来执行action任务。

从上面程序可以看出,进程池同样实现了上下文管理协议,因此程序可以使用 with 子句来管理进程池,这样就可以避免程序主动关闭进程池。
"""
