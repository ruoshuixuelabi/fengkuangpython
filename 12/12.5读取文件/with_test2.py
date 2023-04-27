"""
程序也可以使用 with 语句来处理通过 fileinput.input 合并的多个文件,例如如下程序。
"""
import fileinput

# 使用with语句打开文件,该语句会负责关闭文件
with fileinput.input(files=('test.txt', 'info.txt')) as f:
    for line in f:
        print(line, end='')
"""
上面两个程序中的粗体字代码都使用了 with 语句来管理资源,因此它们都不需要显式关闭文件。

那么,with 语句的实现原理是什么?其实很简单,使用 with 语句管理的资源必须是一个实现上下文管理协议(context manage protocol)的类,
这个类的对象可被称为上下文管理器。要实现上下文管理协议,必须实现如下两个方法。
(1)context_manager.__enter__():进入上下文管理器自动调用的方法。
该方法会在 with 代码块执行之前执行。如果 with 语句有 as 子句,那么该方法的返回值会被赋值给as子句后的变量：
该方法可以返回多个值,因此,在 as 子句后面也可以指定多个变量(多个变量必须由"()"括起来组成元组)。
(2)context_manager.__exit_(exc_type,exc_value,exc_traceback): 退出上下文管理器自动调用的方法。
该方法会在 with 代码块执行之后执行。如果 with 代码块成功执行结束,程序自动调用该方法,调用该方法的三个参数都为None;
如果 with 代码块因为异常而中止,程序也自动调用该方法,使用 sys.exc_info 得到的异常信息将作为调用该方法的参数。

通过上面的介绍不难发现,只要一个类实现了__enter__()和 __exit_(exc_type,exc_value,exc_traceback) 方法,
程序就可以使用with语句来管理它;通过 __exit__() 方法的参数,即可判断出 with 代码块执行时是否遇到了异常。

换而言之,上面程序所用的文件对象、FileInput对象,其实都实现了这两个方法,因此它们都可以接受 with 语句的管理。
"""