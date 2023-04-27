"""
上面程序中的第一行粗体字代码定义了一个 RLock 对象。
在程序中实现 draw()方法时,进入该方法开始执行后立即请求对 RLock 对象加锁,当执行完 draw()方法的取钱逻辑之后,
程序使用 finally块来确保释放锁。

程序中 RLock 对象作为同步锁,线程每次开始执行draw()方法修改self._balance时,都必须先对 RLock 对象加锁。
当该线程完成对self._balance的修改,将要退出draw()方法时,则释放对 RLock 对象的锁定。
这样的做法完全符合“加锁 →修改 →释放锁”的安全访问逻辑。

当一个线程在draw()方法中对RLock 对象加锁之后,其他线程由于无法获取对RLock 对象的锁定,
因此它们同时执行draw()方法对self._balance进行修改。
这意味着：并发线程在任意时刻只有一个线程可以进入修改共享资源的代码区(也被称为临界区),
所以在同一时刻最多只有一个线程处于临界区内,从而保证了线程安全。

为了保证Lock 对象能真正“锁定”它所管理的 Account 对象,程序会被编写成每个 Account 对象有一个对应的Lock——
就像一个房间有一个锁一样。

上面的Account 类增加了一个代表取钱的draw (方法,并使用Lock 对象保证该draw()方法的线程安全,
而且取消了setBalance()方法(避免程序直接修改 self._balance成员变量),
因此线程执行体只需调用 Account 对象的 draw()方法即可执行取钱操作。

下面程序创建并启动了两个取钱线程。
"""
import threading
import Account


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 直接调用account对象的draw()方法来执行取钱操作
    account.draw(draw_amount)


# 创建一个账户
acct = Account.Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()
"""
上面程序中代表线程执行体的draw()函数无须自己实现取钱操作,而是直接调用account的 draw() 方法来执行取钱操作。
由于 draw()方法已经使用 RLock 对象实现了线程安全,因此上面程序就不会导致线程安全问题。

多次重复运行上面程序,总可以看到如图14.6 所示的运行结果。
甲取钱成功！吐出钞票:800
余额为: 200
乙取钱失败！余额不足！

提示：在Account 中定义draw()方法,而不是直接在线程执行体函数中实现取钱逻辑,这种做法更符合面向对象的规则。
在面向对象中有一种流行的设计方式：Domain Driven Design(领域驱动设计,DDD),
这种方式认为每个类都应该是完备的领域对象,例如 Account 代表用户账户,应该提供用户账户的相关方法;
通过draw()方法来执行取钱操作(实际上还应该提供transfer()等方法来完成转账等操作),
而不是直接将setBalance()方法暴露出来任人操作,这样才可以更好地保证Account 对象的完整性和一致性。

可变类的线程安全是以降低程序的运行效率作为代价的,为了减少线程安全所带来的负面影响,程序可以采用如下策略。
(1)不要对线程安全类的所有方法都进行同步,只对那些会改变竞争资源(竞争资源也就是共享资源)的方法进行同步。
例如,上面Account 类中的 account_no 实例变量就无须同步, 所以程序只对 draw()方法进行了同步控制。
(2)如果可变类有两种运行环境：单线程环境和多线程环境,则应该为该可变类提供两种版本,即线程不安全版本和线程安全版本。
在单线程环境中使用线程不安全版本以保证性能,在多线程环境中使用线程安全版本。
"""