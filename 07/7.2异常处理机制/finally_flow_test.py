"""
在通常情况下,不要在finally块中使用如 return 或 raise 等导致方法中止的语句(raise语句将在后面介绍),
一旦在 finally 块中使用了 return 或 raise 语句,将会导致try块、except块中的return、raise语句失效。看如下程序。
"""


def test():
    try:
        # 因为finally块中包含了 return 语句,所以下面的return语句失去作用
        return True
    finally:
        return False


a = test()
print(a)
"""
上面程序在 finally 块中定义了一条 return False 语句,这将导致 try 块中的 return True 失去作用。
运行上面程序,将打印出False的结果。

如果 Python 程序在执行 try块 、except块时遇到了 return 或 raise 语句,这两条语句都会导致该方法立即结束,
那么系统执行这两条语句并不会结束该方法,而是去寻找该异常处理流程中的 finally 块,如果没有找到 finally 块,
程序立即执行 return 或 raise 语句,方法中止;如果找到 finally 块,系统立即开始执行finally块------
只有当 finally 块执行完成后,系统才会再次跳回来执行 try 块、except 块里的 return 或 raise 语句;
如果在 finally 块里也使用了 return 或 raise 等导致方法中止的语句,finally 块已经中止了方法,
系统将不会跳回去执行try块 、except块里的任何代码。

注意：尽量避免在finally块里使用 return或 raise等导致方法中止的语句,否则可能出现一些很奇怪的情况。

7.2.7 异常处理嵌套

正如 finally_test.py程序所示,在 finally块中也包含了一个完整的异常处理流程,这种在 try 块、except块或
finally块中包含完整的异常处理流程的情形被称为异常处理嵌套。

异常处理流程代码可以被放在任何能放可执行代码的地方,因此完整的异常处理流程既可被放在try块里,也可被放在except块里,
还可被放在finally块里。

对异常处理嵌套的深度没有很明确的限制,但通常没有必要使用超过两层的嵌套异常处理,使用层次太深的嵌套异常处理没有太大必要,
而且容易导致程序的可读性降低。
"""