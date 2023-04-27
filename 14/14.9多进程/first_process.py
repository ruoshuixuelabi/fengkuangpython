"""
14.9.2	使用 multiprocessing.Process创建新进程

虽然使用 os.fork()方法可以启动多个进程,但这种方式显然不适合 Windows,而 Python 是跨平台的语言,
所以 Python 绝不能仅仅局限于 Windows 系统,因此 Python 也提供了其他方式在 Windows 下创建新进程。

Python在 multiprocessing 模块下提供了 Process 来创建新进程。与Thread类似的是,使用 Process 创建新进程也有两种方式。
(1)以指定函数作为target,创建Process对象即可创建新进程。
(2)继承Process类,并重写它的run()方法来创建进程类,程序创建Process子类的实例作为进程。

Process类也有如下类似的方法和属性。
(1)run():重写该方法可实现进程的执行体。
(2)start():该方法用于启动进程。
(3)join([timeout]):该方法类似于线程的join()方法,当前进程必须等待被join的进程执行完成才能向下执行。
(4)name:该属性用于设置或访问进程的名字。
(5)is_alive():判断进程是否还活着。
(6)daemon:该属性用于判断或设置进程的后台状态。
(7)pid:返回进程的ID。
(8)authkey:返回进程的授权key。
(9)terminate():中断该进程。

1. 以指定函数作为target创建新进程

下面先介绍以指定函数作为target来创建新进程。
"""
import multiprocessing
import os


# 定义一个普通的action函数,该函数准备作为进程执行体
def action(max):
    for i in range(max):
        print("(%s)子进程（父进程:(%s)）：%d" %
              (os.getpid(), os.getppid(), i))


if __name__ == '__main__':
    # 下面是主程序（也就是主进程）
    for i in range(100):
        print("(%s)主进程: %d" % (os.getpid(), i))
        if i == 20:
            # 创建并启动第一个进程
            mp1 = multiprocessing.Process(target=action, args=(100,))
            mp1.start()
            # 创建并启动第一个进程
            mp2 = multiprocessing.Process(target=action, args=(100,))
            mp2.start()
            mp2.join()
    print('主进程执行完成!')
"""
上面程序中两行粗体字代码就是程序创建并启动新进程的关键代码,不难发现这两行代码和创建并启动新线程的代码几乎一样,
只是此处创建的是 multiprocessing.Process 对象。

需要说明的是,通过 multiprocessing.Process 来创建并启动进程时,程序必须先判断 if __name__ == '__main__':,否则可能引发异常。

运行上面程序,可以看到程序中运行了三个进程：一个主进程和程序启动的两个子进程, 如图14.13所示。

由于上面程序调用了mp2.join(), 因此主进程必须等mp2 进程完成后才能向下执行。
"""
