"""
2. 继承 Process 类创建子进程

继承 Process 类创建子进程的步骤如下。
①定义继承 Process 的子类,重写其 run()方法准备作为进程执行体。
②创建 Process 子类的实例。
③调用 Process 子类的实例的 start()方法来启动进程。

下面程序通过继承Process类来创建子进程。

"""
import multiprocessing
import os


class MyProcess(multiprocessing.Process):
    def __init__(self, max):
        self.max = max
        super().__init__()

    # 重写run()方法作为进程执行体
    def run(self):
        for i in range(self.max):
            print("(%s)子进程（父进程:(%s)）：%d" %
                  (os.getpid(), os.getppid(), i))


if __name__ == '__main__':
    # 下面是主程序（也就是主进程）
    for i in range(100):
        print("(%s)主进程: %d" % (os.getpid(), i))
        if i == 20:
            # 创建并启动第一个进程
            mp1 = MyProcess(100)
            mp1.start()
            # 创建并启动第一个进程
            mp2 = MyProcess(100)
            mp2.start()
            mp2.join()
    print('主进程执行完成!')
"""
该程序的运行结果与上一个程序的运行结果大致相同,它们只是创建进程的方式略有不同而已。

通常,推荐使用第一种方式来创建进程,因为这种方式不仅编程简单,而且进程直接包装target 函数,具有更清晰的逻辑结构。
"""
