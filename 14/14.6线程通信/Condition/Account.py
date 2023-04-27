"""
当线程在系统中运行时,线程的调度具有一定的透明性,通常程序无法准确控制线程的轮换执行,如果有需要,
Python 可通过线程通信来保证线程协调运行。

14.6.1	使用Condition实现线程通信

假设系统中有两个线程,这两个线程分别代表存款者和取钱者——
现在假设系统有一种特殊的要求,即要求存款者和取钱者不断地重复存款、取钱的动作,
而且要求每当存款者将钱存入指定账 户后,取钱者就立即取出该笔钱。不允许存款者连续两次存钱,也不允许取钱者连续两次取钱。

为了实现这种功能,可以借助于Condition对象来保持协调。
使用Condition可以让那些已经得到 Lock 对象却无法继续执行的线程释放Lock 对象,Condition对象也可以唤醒其他处于等待状态的线程。

将 Condition对象与 Lock 对象组合使用,可以为每个对象提供多个等待集(wait-set)。
因此, Condition对象总是需要有对应的Lock 对象。从 Condition 的构造器 __init__(self, lock=None):
可以看出,程序在创建Condition时可通过lock 参数传入要绑定的Lock 对象;
如果不指定lock 参数,在创建 Condition 时它会自动创建一个与之绑定的 Lock 对象。

Condition类提供了如下几个方法。
(1)acquire([timeout])/release(): 调用Condition关联的Lock 的 acquire()或 release()方法。
(2)wait([timeout]):导致当前线程进入Condition的等待池等待通知并释放锁,
直到其他线程调用该Condition的 notify()或 notify all()方法来唤醒该线程。
在调用该wait()方法时可传入一个timeout参数,指定该线程最多等待多少秒。
(3)notify():唤醒在该Condition 等待池中的单个线程并通知它,收到通知的线程将自动调用 acquire()方法尝试加锁。
如果所有线程都在该Condition等待池中等待,则会选择唤醒其中一个线程,选择是任意性的。
(4)notify_all(): 唤醒在该Condition等待池中等待的所有线程并通知它们。

在本例程序中,可以通过一个旗标来标识账户中是否已有存款,当旗标为False时,表明账户中没有存款,
存款者线程可以向下执行,当存款者把钱存入账户中后,将旗标设为 True, 并调用 Condition 的 notify()或 notify all(方法来唤醒其他线程;
当存款者线程进入线程体后,如果旗标为 True, 就调用Condition的 wait()方法让该线程等待。

当旗标为True 时,表明账户中已经存入了钱,取钱者线程可以向下执行,当取钱者把钱从账户中取出后,将旗标设为False,
并调用Condition的 notify()或 notify all()方法来唤醒其他线程;当取钱者线程进入线程体后,如果旗标为False,就调用wait()方法让该线程等待。

本程序为Account 类提供了draw()和 deposit()两个方法,分别对应于该账户的取钱和存款操作。
因为这两个方法可能需要并发修改Account 类 的self. balance成员变量的值,所以它们都使用Lock 来控制线程安全。
除此之外,这两个方法还使用了Condition的 wait()和 notify_all()来控制线程通信。
"""
import threading


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        # 定义代表是否已经存钱的旗标
        self._flag = False

    # 因为账户余额不允许随便修改,所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁,相当于调用Condition绑定的Lock的acquire()
        self.cond.acquire()
        try:
            # 如果self._flag为假,表明账户中还没有人存钱进去,取钱方法阻塞
            if not self._flag:
                self.cond.wait()
            else:
                # 执行取钱操作
                print(threading.current_thread().name
                      + " 取钱:" + str(draw_amount))
                self._balance -= draw_amount
                print("账户余额为：" + str(self._balance))
                # 将标识账户是否已有存款的旗标设为False
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用finally块来释放锁
        finally:
            self.cond.release()

    def deposit(self, deposit_amount):
        # 加锁,相当于调用Condition绑定的Lock的acquire()
        self.cond.acquire()
        try:
            # 如果self._flag为真,表明账户中已有人存钱进去,存钱方法阻塞
            if self._flag:  # ①
                self.cond.wait()
            else:
                # 执行存款操作
                print(threading.current_thread().name \
                      + " 存款:" + str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为：" + str(self._balance))
                # 将表示账户是否已有存款的旗标设为True
                self._flag = True
                # 唤醒其他线程
                self.cond.notify_all()
        # 使用finally块来释放锁
        finally:
            self.cond.release()


"""
上面程序中的粗体字代码使用Condition 的 wait()和 notify all()方法进行控制,对存款者线程而言,
当程序进入deposit()方法后,如果self._flag 为True,则表明账户中已有存款,程序调用Condition 的 wait()方法被阻塞;
否则,程序向下执行存款操作,当存款操作执行完成后,系统将self._flag 设为 True,然后调用notify_all()来唤醒其他被阻塞的线程 — —
如果系统中有存款者线程,存款者线程 也会被唤醒,但该存款者线程执行到①号粗体字代码处时再次进入阻塞状态,
只有执行draw()方法 的取钱者线程才可以向下执行。同理,取钱者线程的运行流程也是如此。

"""
