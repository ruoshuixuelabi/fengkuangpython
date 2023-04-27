"""
14.9.5	进程通信

Python 为进程通信提供了两种机制。
(1)Queue:一个进程向 Queue 中放入数据,另一个进程从 Queue 中读取数据。
(2)Pipe:Pipe 代表连接两个进程的管道。程序在调用 Pipe() 函数时会产生两个连接端,分别交给通信的两个进程,
接下来进程既可从该连接端读取数据,也可向该连接端写入数据。

1. 使用Queue  实现进程通信

下面先看使用Queue 来实现进程通信。multiprocessing模块下的Queue 和 queue 模块下的Queue 基本类似,
它们都提供了qsize()、empty()、full()、put()、put_nowait()、get()、get nowait()等方法。
区别只是 multiprocessing 模块下的 Queue 为进程提供服务,而 queue 模块下的 Queue 为线程提供服务。

下面程序使用Queue 来实现进程之间的通信。
"""
import multiprocessing


def f(q):
    print('(%s) 进程开始放入数据...' % multiprocessing.current_process().pid)
    q.put('Python')


if __name__ == '__main__':
    # 创建进程通信的Queue
    q = multiprocessing.Queue()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(q,))
    # 启动子进程
    p.start()
    print('(%s) 进程开始取出数据...' % multiprocessing.current_process().pid)
    # 取出数据
    print(q.get())  # Python
    p.join()
"""
上面程序中第一行粗体字代码(子进程)负责向 Queue 中放入一个数据,第二行粗体字代码 (父进程)负责从Queue 中读取一个数据,这样就实现了父、子两个进程之间的通信。
运行上面程序,可以看到如下输出结果。
"""
