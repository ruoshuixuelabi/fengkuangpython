"""
接下来,在相同的路径下定义如下程序来使用该模块。

"""
import fk_module

print("================")
# 打印fk_module的类型
print(type(fk_module))
print(fk_module)
print(fk_module.name)
print(fk_module.hello)
"""
由于前面在 PYTHONPATH 环境变量中已经添加了点(.),因此 Python 程序总可以加载相同路径下的模块。
所以,上面程序可以导入相同路径下的 fk_module 模块。运行上面程序,可以看到如下输出结果。
this is fk_module
================
<class 'module'>
<module 'fk_module' from 'D:\\BaiduNetdiskDownload\\766841《疯狂Python讲义》PDF+源代码+习题\\fengkuangpython\\09\\9.2加载模块\\fk_module.py'>
fkit
<function hello at 0x000001F40CB392D0>

从上面的输出结果来看,当程序导入 fk_module 时,该模块中的输出语句会在import时自动执行。
该程序中还包含一个与模块同名的变量,该变量的类型是module。

使用"import fk_module"导入模块的本质就是：将 fk_module.py中的全部代码加载到内存并执行,
然后将整个模块内容赋值给与模块同名的变量,该变量的类型是 module, 而在该模块中定义的所有程序单元都相当于该 module 对象的成员。
"""
