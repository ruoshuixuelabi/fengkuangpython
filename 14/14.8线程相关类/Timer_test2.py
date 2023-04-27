"""
如果程序想取消Timer 的调度,则可调用Timer 对象的cancel()函数。例如,如下程序每1s 输出一次当前时间。

"""
from threading import Timer
import time

# 定义总共输出几次的计数器
count = 0


def print_time():
    print("当前时间：%s" % time.ctime())
    global t, count
    count += 1
    # 如果count小于10,开始下一次调度
    if count < 10:
        t = Timer(1, print_time)
        t.start()


# 指定1秒后执行print_time函数
t = Timer(1, print_time)
t.start()
"""
上面程序开始运行后,程序控制 1s 后执行 print_time()函数。print time()函数中的粗体字代码判断：
如果count 小于10,程序再次使用 Timer 调度 1s 后执行print time()函数,这样就可以控制 print_time()函数多次重复执行。

在上面程序中,由于只有当count 小于10时才会使用Timer 调度 1s 后执行 print_time()函数, 因此该函数只会重复执行10次。
"""