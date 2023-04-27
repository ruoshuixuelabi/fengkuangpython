"""
14.2.2	继承Thread类创建线程类

通过继承Thread类来创建并启动线程的步骤如下。
① 定义 Thread 类的子类,并重写该类的 run() 方法。run() 方法的方法体就代表了线程需要完成的任务,因此把run()方法称为线程执行体。
② 创建Thread 子类的实例,即创建线程对象。
③ 调用线程对象的start()方法来启动线程。

下面程序示范了通过继承Thread类来创建并启动线程。
"""
import threading


# 通过继承threading.Thread类来创建线程类
class FkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写run()方法作为线程执行体
    def run(self):
        while self.i < 100:
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().name + " " + str(self.i))
            self.i += 1


# 下面是主程序(也就是主线程的执行体)
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        ft1 = FkThread()
        ft1.start()
        # 创建并启动第二个线程
        ft2 = FkThread()
        ft2.start()
print('主线程执行完成!')
"""
上面程序中的 FkThread 类继承了threading.Thread 类,如第一行粗体字代码所示,并实现了run()方法,如第二段粗体字代码所示。
run()方法中的代码执行流就是该线程所需要完成的任务。

运行上面程序,将会看到如图14.2所示的界面。

从图14.2可以看到,此时程序中同样有主线程、Thread-1和 Thread-2三个线程,它们以快速轮换的方式在执行,这就是三个线程并发执行的效果。

通常来说,推荐使用第一种方式来创建线程,因为这种方式不仅编程简单,而且线程直接包装 target函数,具有更清晰的逻辑结构。
"""
