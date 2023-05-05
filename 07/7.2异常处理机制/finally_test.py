"""
7.2.6 使用finally回收资源

有些时候,程序在try块里打开了一些物理资源(例如数据库连接、网络连接和磁盘文件等),这些物理资源都必须被显式回收。

提示：Python 的垃圾回收机制不会回收任何物理资源,只能回收堆内存中对象所占用的内存。

那么在哪里回收这些物理资源呢?在try块里回收,还是在except块中进行回收?假设程序在try块里进行资源回收,
根据图7.1所示的异常捕获流程——如果try块的某条语句引发了异常,该语句后的其他语句通常不会获得执行的机会,
这将导致位于该语句之后的资源回收语句得不到执行。如果在except块里进行资源回收,因为except 块完全有可能得不到执行,
这将导致不能及时回收这些物理资源。

为了保证一定能回收在try块中打开的物理资源,异常处理机制提供了finally块。不管try块中的代码是否出现异常,
也不管哪一个 except 块被执行,甚至在 try 块或 except 块中执行了 return 语句,finally块总会被执行。
Python 完整的异常处理语法结构如下：
try:
    #业务实现代码
except    SubException    as    e:
    #异常处理块1
except     SubException2     as     e:
    #异常处理块2
else:
    #正常处理块
finally:
    #资源回收块

在异常处理语法结构中,只有 try 块是必需的,也就是说,如果没有try块,则不能有后面的 except块和finally块：
except 块和 finally块都是可选的,但except块和finally块至少出现其中之一,也可以同时出现;可以有多个 except 块,
但捕获父类异常的 except 块应该位于捕获子类异常的 except块的后面;不能只有 try 块,既没有 except 块,也没有 finally 块;
多个 except 块必须位于 try 块之后,finally 块必须位于所有的 except 块之后。看如下程序。
"""
import os


def test():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e:
        print(e.strerror)
        # return语句强制方法返回
        #        return        # ①
        os._exit(1)  # ②
    finally:
        # 关闭磁盘文件,回收资源
        if fis is not None:
            try:
                # 关闭资源
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行finally块里的资源回收!")


test()
"""
上面程序在try块后增加了finally块,用于回收在try块中打开的物理资源。
注意在程序的 except 块中①处有一条 return语句,该语句强制方法返回。在通常情况下,一旦在方法里执行到return语句,程序将立即结束该方法；
现在不会了,虽然return语句也强制方法结束,但一定会先执行finally块的代码。运行上面程序,将看到如下运行结果。

No such file or directory
执行finally块里的资源回收!

上面的运行结果表明在方法返回之前执行了finally块的代码。将①处的return语句注释掉,取消②处代码的注释,
即在异常处理的except块中使用 os._exit(1) 语句来退出 Python 解释器。运行上面代码,将看到如下运行结果。

No such file or directory

上面的运行结果表明 finally 块没有被执行。如果在异常处理代码中使用 os._exit(1) 语句来退出Python解释器,则finally块将失去执行的机会。

注意：除非在try块 、except块中调用了退出 Python 解释器的方法,否则不管在 try 块、except块中执行怎样的代码,出现怎样的情况,
异常处理的finally块总会被执行。调用 os.exit() 方法退出程序不能阻止finally块的执行,
这是因为sys.exit()方法本身就是通过引发SystemExit异常来退出程序的。
"""