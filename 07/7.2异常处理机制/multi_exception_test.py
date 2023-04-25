"""
7.2.3	多异常捕获
1.  Python 的一个except块可以捕获多种类型的异常。
2.  在使用一个except 块捕获多种类型的异常时,只要将多个异常类用圆括号括起来,中间用逗号隔开即可------其实就是构建多个异常类的元组。
3.  下面程序示范了Python 的多异常捕获。
4.  上面程序中第一行粗体字代码使用了(IndexError,ValueError,ArithmeticError)来指定所捕获的异常类型,
这就表明该except块可以同时捕获这三种类型的异常。
5.  读者看上面程序中第二行粗体字代码,这行代码只有except 关键字,并未指定具体要捕获的异常类型,
这种省略异常类的 except 语句也是合法的,它表示可捕获所有类型的异常, 一般会作为异常捕获的最后一个except块。
"""
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except (IndexError, ValueError, ArithmeticError):
    print("程序发生了数组越界、数字格式异常、算术异常之一")
except:
    print("未知异常")
