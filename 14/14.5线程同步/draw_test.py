"""
接下来程序会定义一个模拟取钱的函数,该函数根据执行账户、取钱数量进行取钱操作,
取钱的逻辑是当账户余额不足时无法提取现金,当余额足够时系统吐出钞票,余额减少。

程序的主程序非常简单,仅仅是创建一个账户,并启动两个线程从该账户中取钱。程序如下。
"""
import threading
import time
import Account


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name \
              + "取钱成功！吐出钞票:" + str(draw_amount))
        #        time.sleep(0.001)
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name \
              + "取钱失败！余额不足！")


# 创建一个账户
acct = Account.Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()
"""
先不要管程序中那行被注释掉的粗体字代码,上面程序是一个非常简单的取钱逻辑,这个取钱逻辑与实际的取钱操作也很相似。

多次运行上面程序,很有可能都会看到如图14.5所示的错误结果。
甲取钱成功！吐出钞票:800
乙取钱成功！吐出钞票:800
	余额为: 200
	余额为: -600

如图14.5所示的运行结果并不是银行所期望的结果(不过有可能看到正确的运行结果),这正是多线程编程突然出现的"偶然"错误——
因为线程调度的不确定性。假设系统线程调度器在粗体字代码处暂停,让另一个线程执行——
为了强制暂停,只要取消上面程序中粗体字代码的注释即可。取消注释后,再次运行draw test.py程序,将总可以看到如图14.5所示的错误结果。

问题出现了：账户余额只有1000元时取出了1600元,而且账户余额出现了负值,这不是银行所期望的结果。
虽然上面程序是人为地使用 time.sleep(0.001)来强制线程调度切换,但这种切换也是完全可能发生的——
100000次操作只要有1次出现了错误,那就是由编程错误引起的。
"""