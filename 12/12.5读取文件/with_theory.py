"""
下面我们自定义一个实现上下文管理协议的类,并使用with语句来管理它。
"""


class FkResource:
    def __init__(self, tag):
        self.tag = tag
        print('构造器,初始化资源: %s' % tag)

    # 定义__enter__方法,with体之前的执行的方法
    def __enter__(self):
        print('[__enter__ %s]: ' % self.tag)
        # 该返回值将作为as子句中变量的值
        return 'fkit'  # 可以返回任意类型的值

    # 定义__exit__方法,with体之后的执行的方法
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('[__exit__ %s]: ' % self.tag)
        # exc_traceback为None,代表没有异常
        if exc_traceback is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False  # 可以省略,默认返回None也被看做是False


with FkResource('孙悟空') as dr:
    print(dr)
    print('[with代码块] 没有异常')
print('------------------------------')
with FkResource('白骨精'):
    print('[with代码块] 异常之前的代码')
    raise Exception
    print('[with代码块] ~~~~~~~~异常之后的代码')
"""
上面程序定义了一个 FkResource 类,该类定义了 __enter__()和 __exit__()两个方法,因此该类的对象可以被 with 语句管理。
(1)程序在执行 with 代码块之前,会执行 __enter__()方法,并将该方法的返回值赋值给 as 子句后的变量。
(2)程序在执行 with 代码块之后,会执行 __exit__()方法,可以根据该方法的参数来判断 with 代码块是否有异常。

程序两次使用 with 语句管理 FkResource 对象：第一次,with 代码块没有出现异常;第二次,with代码块出现了异常。
大家可以看到,使用 with 语句两次对 FkResource 的管理略有差异——主要是在 __exit__() 方法中略有差异。

运行上面的程序,可以看到如下输出结果。

从上面的输出结果来看,使用 with 语句管理资源,程序总可以在进入 with 代码块之前自动执行 __enter__()方法,
无论with代码块是否有异常,这个部分都是一样的,而且 __enter__()方法的返回值被赋值给了as 子句后的变量,如上面的①号输出信息所示。

对于 with 代码块有异常和无异常这两种情况,此时主要通过 __exit__()方法的参数进行判断,
程序可针对with代码块是否有异常分别进行处理,如上面的两行粗体字输出信息所示。

"""