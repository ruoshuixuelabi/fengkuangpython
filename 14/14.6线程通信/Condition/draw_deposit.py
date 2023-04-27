"""
程序中的存款者线程循环100次重复存款,而取钱者线程则循环100次重复取钱,
存款者线程和取钱者线程分别调用Account 对象的deposit()、draw(方法来实现。
主程序可以启动任意多个"存款"线程和"取钱"线程,可以看到所有的"取钱"线程必须等"存款"线程存钱后才可以向下执行,
而"存款"线程也必须等"取钱"线程取钱后才可以向下执行。主程序代码如下。
"""
import threading
import Account


#  定义一个函数,模拟重复max次执行取钱操作
def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)


#  定义一个函数,模拟重复max次执行存款操作
def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)


# 创建一个账户
acct = Account.Account("1234567", 0)
# 创建、并启动一个"取钱"线程
threading.Thread(name="取钱者", target=draw_many, args=(acct, 800, 100)).start()
# 创建、并启动一个"存款"线程
threading.Thread(name="存款者甲", target=deposit_many, args=(acct, 800, 100)).start();
threading.Thread(name="存款者乙", target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name="存款者丙", target=deposit_many, args=(acct, 800, 100)).start()
"""
运行该程序,可以看到存款者线程、取钱者线程交替执行的情形,每当存款者向账户中存入800元之后,取钱者线程就立即从账户中取出这笔钱。
存款完成后账户余额总是800元,取钱结束后账户余额总是0元。运行该程序,将会看到如图14.8所示的结果。

从图14.8中可以看出,3个存款者线程随机地向账户中存钱,只有 1 个取钱者线程执行取钱操作。
只有当取钱者线程取钱后,存款者线程才可以存钱;同理,只有等存款者线程存钱后,取钱者线程才可以取钱。

图14.8显示程序最后被阻塞无法继续向下执行。
这是因为3个存款者线程共有300次尝试存钱操作,但1个取钱者线程只有100次尝试取钱操作,所以程序最后被阻塞!

注意：如图14.8所示的阻塞并不是死锁,对于这种情况,取钱者线程已经执行结束而存款者线程只是在等待其他线程来取钱而已,
并不是等待其他线程释放同步监视器。不要把死锁和程序阻塞等同起来!
"""