"""
7.2.2 异常类的继承体系

当 Python 解释器接收到异常对象时,如何为该异常对象寻找 except 块呢?注意上面 gobang.py 程序中except块的except Exception:
这意味着每个 except 块都是专门用于处理该异常类及其子类的异常实例。

当 Python 解释器接收到异常对象后,会依次判断该异常对象是否是 except 块后的异常类或其子类的实例,如果是,
Python 解释器将调用该 except 块来处理该异常;否则,再次拿该异常对象和下一个 except 块里的异常类进行比较。
Python 异常捕获流程示意图如图7.1所示。

从图7.1中可以看出,在 try 块后可以有多个 except 块,这是为了针对不同的异常类提供不同的异常处理方式。当程序发生不同的意外情况时,
系统会生成不同的异常对象,Python 解释器就会根据该异常对象所属的异常类来决定使用哪个except块来处理该异常。

通过在try块后提供多个 except 块可以无须在异常处理块中使用if判断异常类型,但依然可以针对不同的异常类型提供相应的处理逻辑,
从而提供更细致、更有条理的异常处理逻辑。

从图7.1中可以看出,在通常情况下,如果 try 块被执行一次,则 try 块后只有一个except 块会被执行,不可能有多个 except 块被执行。
除非在循环中使用了continue开始下一次循环,下一次循环又重新运行了try块,这才可能导致多个except块被执行。

Python的所有异常类都从 BaseException 派生而来,提供了丰富的异常类,这些异常类之间有严格的继承关系,
图7.2显示了Python 的常见异常类之间的继承关系。

从图7.2中可以看出,Python 的所有异常类的基类是 BaseException,但如果用户要实现自定义异常,则不应该继承这个基类,
而是应该继承Exception类。

BaseException 的主要子类就是 Exception,不管是系统的异常类,还是用户自定义的异常类,都应该从Exception派生。

下面看几个简单的异常捕获的例子。
"""
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except IndexError:
    print("索引错误：运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误：程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知异常")
"""
上面程序导入了sys模块,并通过sys模块的 argv 列表来获取运行 Python 程序时提供的参数。
其中sys.argv[0]通常代表正在运行的 Python 程序名,sys.argv[1]代表运行程序所提供的第一个参数,
sys.argv[2]代表运行程序所提供的第二个参数……依此类推。

Python 使用 import 语句来导入模块,关于模块和导入模块在本书第9章中进行详细讲解。

上面程序针对IndexError、ValueError、ArithmeticError类型的异常,提供了专门的异常处理逻辑。
该程序运行时的异常处理逻辑可能有如下几种情形。
(1)如果在运行该程序时输入的参数不够,将会发生索引错误,Python 将调用IndexError对应的except块处理该异常。
(2)如果在运行该程序时输入的参数不是数字,而是字母,将发生数值错误,Python 将调用 ValueError 对应的 except 块处理该异常。
(3)如果在运行该程序时输入的第二个参数是0,将发生除0异常,Python 将调用 ArithmeticError 对应的 except 块处理该异常。
(4)如果在程序运行时出现其他异常,该异常对象总是 Exception 类或其子类的实例,Python 将调用Exception对应的except块处理该异常。

上面程序中的三种异常,都是非常常见的运行时异常,读者应该记住这些异常,并掌握在哪些情况下可能出现这些异常。

正如在前面程序中所看到的,程序总是把对应Exception类的except块放在最后,这是为什么呢?
想一下图7.1所示的 Python 异常捕获流程,读者可能明白原因：如果把Exception 类对应的 except块排在其他except块的前面,
Python 解释器将直接进入该except块(因为所有的异常对象都是Exception或其子类的实例),
而排在它后面的except块将永远也不会获得执行的机会。

实际上,在进行异常捕获时不仅应该把Exception类对应的except块放在最后,
而且所有父类异常的except块都应该排在子类异常的except块的后面(即：先处理小异常,再处理大异常)。

虽然 Python 语法没有要求,但在实际编程时一定要记住先捕获小异常,再捕获大异常。
"""
