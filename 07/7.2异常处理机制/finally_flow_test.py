"""
1.  在通常情况下,不要在finally块中使用如return或 raise等导致方法中止的语句(raise语句将 在后面介绍),
一旦在finally块中使用了retur 或 raise语句,将会导致try块 、except块中的return、 raise语句失效。看如下程序。
2.  上面程序在finally块中定义了一条return False语句,这将导致try块中的return True失去作用。
运行上面程序,将打印出False的结果。
3.  如果Python 程序在执行 try块 、except块时遇到了return或 raise语句,这两条语句都会导致该方法立即结束,
那么系统执行这两条语句并不会结束该方法,而是去寻找该异常处理流程中的 finally块,如果没有找到finally块,
程序立即执行return或 raise语句,方法中止；如果找到finally 块,系统立即开始执行finally块------
只有当finally块执行完成后,系统才会再次跳回来执行try块、 except块里的return或 raise语句；
如果在finally块里也使用了return或 raise等导致方法中止的语 句, finally块已经中止了方法,
系统将不会跳回去执行try块 、except块里的任何代码。
4.  注意：尽量避免在finally块里使用 return或 raise等导致方法中止的语句,否则可能出现一些很奇怪的情况。

7.2.7	异常处理嵌套

5.  正如 finally_test.py程序所示,在 finally块中也包含了一个完整的异常处理流程,这种在 try 块、except块或
finally块中包含完整的异常处理流程的情形被称为异常处理嵌套。
6.  异常处理流程代码可以被放在任何能放可执行代码的地方,因此完整的异常处理流程既可被放 在try块里,也可被放在except块里,
还可被放在finally块里。
7.  对异常处理嵌套的深度没有很明确的限制,但通常没有必要使用超过两层的嵌套异常处理,使用层次太深的嵌套异常处理没有太大必要,
而且容易导致程序的可读性降低。
"""


def test():
    try:
        # 因为finally块中包含了return语句,所以下面的return语句失去作用
        return True
    finally:
        return False


a = test()
print(a)
