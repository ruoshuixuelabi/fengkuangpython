"""
即使是用户自行引发的异常,也可以使用try…except来捕获它。当然也可以不管它,让该异常向上(先调用者)传播,
如果该异常传到 Python 解释器,那么程序就会中止。下面示例示范了处 理用户引发异常的两种方式。
"""
import traceback


def main():
    try:
        # 使用try...except来捕捉异常
        # 此时即使程序出现异常,也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('程序出现异常:', e)
        #        help(e.with_traceback)
        traceback.print_exc()
    #        e.with_traceback(e)
    # 不使用try...except捕捉异常,异常会传播出来导致程序中止
    mtd(3)


def mtd(a):
    if a > 0:
        raise ValueError("a的值大于0,不符合要求")


main()
"""
从上面程序可以看到,程序既可在调用mtd(3)时使用try…except来捕获异常,这样该异常将会被 except 块捕获,不会传播给调用它的函数;
也可直接调用mtd(3),这样该函数的异常就会直接传播给它的调用函数,如果该函数也不处理该异常,就会导致程序中止。

运行上面程序，可以看到如下输出结果。
Traceback (most recent call last):
  File "D:\BaiduNetdiskDownload\766841《疯狂Python讲义》PDF+源代码+习题\fengkuangpython\07\7.3使用raise引发异常\raise_test.py", line 12, in main
    mtd(3)
  File "D:\BaiduNetdiskDownload\766841《疯狂Python讲义》PDF+源代码+习题\fengkuangpython\07\7.3使用raise引发异常\raise_test.py", line 24, in mtd
    raise ValueError("a的值大于0,不符合要求")
ValueError: a的值大于0,不符合要求
Traceback (most recent call last):
  File raise_test.py", line 24, in mtd
    raise ValueError("a的值大于0,不符合要求")
ValueError: a的值大于0,不符合要求
程序出现异常: a的值大于0,不符合要求

上面第一行输出是第一次调用 mtd(3)的结果,该方法引发的异常被 except 块捕获并处理。
后面的大段输出则是第二次调用 mtd(3)的结果,由于该异常没有被except 块捕获,因此该异常一直向上传播,
直到传给Python 解释器导致程序中止。

第二次调用mtd(3)引发的以"File"开头的三行输出,其实显示的就是异常的传播轨迹信息。
也就是说,如果程序不对异常进行处理, Python 默认会在控制台输出异常 的传播轨迹信息。
"""