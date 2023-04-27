"""
还有一种设置进程启动方式的方法,就是利用 get_context()方法来获取 Context 对象,
调用该方法时可传入spawn、fork 或 forkserver字符串。
Context拥有和 multiprocessing 相同的API,因此程序可通过Context来创建并启动进程。例如如下程序。
"""
import multiprocessing
import os


def foo(q):
    print('被启动的新进程: (%s)' % os.getpid())
    q.put('Python')


if __name__ == '__main__':
    # 设置使用fork方式启动进程,并获取Context对象
    ctx = multiprocessing.get_context('fork')
    # 接下来就可用Context对象来代替mutliprocessing模块了
    q = ctx.Queue()
    # 创建进程
    mp = ctx.Process(target=foo, args=(q,))
    # 启动进程
    mp.start()
    # 获取队列中的消息 
    print(q.get())
    mp.join()
"""
上面程序中粗体字代码设置以fork方式启动进程,并获取Context对象,这样程序后面就可以使用Context对象来代替multiprocessing模块了。

"""