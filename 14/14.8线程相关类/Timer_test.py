"""
14.8.2	定时器

Thread类有 一 个Timer 子类,该子类可用于控制指定函数在特定时间内执行一次。例如如下程序。
"""
from threading import Timer


def hello():
    print("hello, world")


# 指定10秒后执行hello函数
t = Timer(10.0, hello)
t.start()
"""
上面程序中粗体字代码使用Timer 控制10s 后执行hello函数。

需要说明的是,Timer 只能控制函数在指定时间内执行一次,
如果要使用Timer 控制函数多次重复执行,则需要再执行下一次调度。
"""
