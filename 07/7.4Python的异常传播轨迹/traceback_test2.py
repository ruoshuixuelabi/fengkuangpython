"""
1.  借助于traceback模块的帮助,我们可以使用except块捕获异常,并在其中打印异常传播信息, 包括把它输出到文件中。例如如下程序。
2.  上面程序第一行先导入了 traceback 模块,接下来程序使用 except 捕获程序的异常,并使用 traceback的 print_exc()方法输出异常传播信息,
分别将它输出到控制台和指定文件中。运行上面程序,同样可以看到在控制台输出异常传播信息,而且在程序目录下生成了一个 log.txt 文件,
该文件中同样记录了异常传播信息。
"""
# 导入trackback模块
import traceback


class SelfException(Exception): pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常信息")


try:
    main()
except:
    # 捕捉异常,并将异常传播信息输出控制台
    traceback.print_exc()
    # 捕捉异常,并将异常传播信息输出指定文件中
    traceback.print_exc(file=open('log.txt', 'a'))
