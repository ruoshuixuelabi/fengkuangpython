"""
上面的 __all__ 变量指定该模块默认只被导入hello和world 两个程序单元。下面程序示范了模块中  __all__ 变量的用处。
"""
# 导入all_module模块内所有成员
from all_module import *
hello()
world()
test() # 会提示找不到test()函数

"""
上面第一行粗体字代码使用"from all_module import *"导入了 all_module 模块下所有的程序单元。
由于该模块包含了 __all__ 变量,因此该语句只导入 __all__ 变量所列出的程序单元。

运行上面程序,可以看到如下输出结果。
Hello, Python
Pyhton World is funny
Traceback (most recent call last):
  File "D:all_module_test.py", line 8, in <module>
    test() # 会提示找不到test()函数
NameError: name 'test' is not defined

从上面的输出结果可以看到,通过"from all_module import *"语句确实只能导入 __all__ 变量所列出的全部程序单元,
没有列出的test就没有被导入进来。

事实上,__all__ 变量的意义在于为模块定义了一个开放的公共接口。通常来说,只有 __all__ 变量列出的程序单元,
才是希望该模块被外界使用的程序单元。因此,为模块设置  __all__ 变量还是比较有用的。
比如一个实际的大模块可能包含了大量其他程序不需要使用的变量、函数和类,那么通过 __all__ 变量即可把它们自动过滤掉,这还是非常酷的。

如果确实希望程序使用模块内  __all__ 列表之外的程序单元,有两种解决方法。
(1)第一种是使用"import 模块名"来导入模块。在通过这种方式导入模块之后,
总可以通过模块名前缀(如果为模块指定了别名,则可以使用模块的别名作为前缀)来调用模块内的成员。
(2)第二种是使用"from 模块名 import 程序单元"来导入指定程序单元。
在这种方式下,即使想导入的程序单元没有位于 __all__ 列表中,也依然可以导入。
"""
