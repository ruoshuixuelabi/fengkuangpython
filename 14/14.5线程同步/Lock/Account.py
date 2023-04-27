"""
14.5.2	同步锁(Lock)

之所以出现如图14.5所示的错误结果,是因为run()方法的方法体不具有线程安全性——程序中有两个并发线程在修改Account 对象;
而且系统恰好在粗体字代码处执行线程切换,切换到另一个修改Account 对象的线程,所以就出现了问题。

为了解决这个问题, Python 的 threading模块引入了锁(Lock)。threading 模块提供了Lock 和 RLock 两个类,
它们都提供了如下两个方法来加锁和释放锁。
(1)acquire(blocking=True,timeout=-1): 请求对Lock 或 RLock 加锁,其中timeout参数指定加锁多少秒。
(2)release():释放锁。

Lock 和 RLock 的区别如下。
(1)threading.Lock:它是一个基本的锁对象,每次只能锁定一次,其余的锁请求,需等待锁释放后才能获取。
(2)threading.RLock:它代表可重入锁(Reentrant  Lock)。 对于可重入锁,在同一个线程中可以对它进行多次锁定,也可以多次释放。
如果使用RLock, 那么acquire()和 release()方法必须成对出现。如果调用了n 次 acquire()加锁,则必须调用n 次 release()才能释放锁。

由此可见, RLock 锁具有可重入性。也就是说,同一个线程可以对已被加锁的 RLock 锁再次加锁,
RLock 对象会维持一个计数器来追踪acquire()方法的嵌套调用,线程在每次调用acquire()加锁后,
都必须显式调用release()方法来释放锁。所以, 一段被锁保护的方法可以调用另一个被相同锁保护的方法。

Lock 是控制多个线程对共享资源进行访问的工具。通常,锁提供了对共享资源的独占访问,
每次只能有一个线程对Lock 对象加锁,线程在开始访问共享资源之前应先请求获得 Lock 对象。
当对共享资源访问完成后,程序释放对Lock 对象的锁定。

在实现线程安全的控制中,比较常用的是RLock。 通常使用RLock 的代码格式如下：
class X:
    #定义需要保证线程安全的方法
    def       m():
        #加锁
        self.lock.acquire()
        try:
            #需要保证线程安全的代码
            # . . . 方法体
            #使用finally 块来保证释放锁
        finally:
            #修改完成，释放锁
            self.lock.release()

使用 RLock 对象来控制线程安全,当加锁和释放锁出现在不同的作用范围内时,通常建议使用 finally 块来确保在必要时释放锁。

通过使用 Lock 对象可以非常方便地实现线程安全的类,线程安全的类具有如下特征。
(1)该类的对象可以被多个线程安全地访问。
(2)每个线程在调用该对象的任意方法之后,都将得到正确的结果。
(3)每个线程在调用该对象的任意方法之后,该对象都依然保持合理的状态。

总的来说,不可变类总是线程安全的,因为它的对象状态不可改变;但可变对象需要额外的方法来保证其线程安全。
例如,上面的 Account 就是一个可变类,它的self.account_no 和 self._balance(为了更好地封装,将balance改名为 _balance)
两个成员变量都可以被改变,当两个线程同时修改 Account 对象的self balance成员变量的值时,程序就出现了异常。
下面将Account 类 对self. balance 的访问设置成线程安全的,那么只需对修改self._balance 的方法增加线程安全的控制即可。

将Account 类改为如下形式,它就是线程安全的。
"""
import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()

    # 因为账户余额不允许随便修改,所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            # 修改完成,释放锁
            self.lock.release()
