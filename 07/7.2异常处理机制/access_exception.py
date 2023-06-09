"""
7.2.4 访问异常信息

如果程序需要在 except 块中访问异常对象的相关信息,则可通过为异常对象声明变量来实现。
当 Python 解释器决定调用某个 except 块来处理该异常对象时,会将异常对象赋值给 except 块后的异常变量,
程序即可通过该变量来获得异常对象的相关信息。

所有的异常对象都包含了如下几个常用属性和方法。
(1)args:该属性返回异常的错误编号和描述字符串。
(2)errno:该属性返回异常的错误编号。
(3)strerror:该属性返回异常的描述字符串。
(4)with_traceback():通过该方法可处理异常的传播轨迹信息。

下面例子演示了程序如何访问异常信息。

"""


def foo():
    try:
        fis = open("a.txt")
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        # 访问异常的错误编号
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)


foo()
"""
从上面程序可以看出,如果要访问异常对象,只要在单个异常类或异常类元组(多异常捕获)之后使用as再加上异常变量即可

在 Python 2.x的早期版本中,直接在单个异常类或异常类元组(多异常捕获)之后添加异常变量,中间用逗号隔开即可

上面程序调用了 Exception 对象的 args 属性(该属性相当于同时返回ermno属性和strerror属性)访问异常的错误编号和详细信息。
运行上面程序,会看到如下运行结果。

(2, 'No such file or directory')
2
No such file or directory

从上面的运行结果可以看到,由于程序尝试打开的文件不存在,因此引发的异常错误编号为2,异常详细信息为：No such file or directory。

关于如何处理异常的传播轨迹信息,本章后面还有更详细的介绍,此处暂不详细讲解。

提示：上面程序中使用 open()方法来打开一个文件,用于读取磁盘文件的内容。关于该open()方法的详细介绍请参考本书第12章的内容
"""