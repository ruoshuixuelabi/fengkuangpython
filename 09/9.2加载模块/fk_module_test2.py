"""
1.  使用"import fk module"导入模块的本质就是：将fk module.py中的全部代码加载到内存并执行,
然后将整个模块内容赋值给与模块同名的变量,该变量的类型是 module, 而在该模块中定义的所有程序单元都相当于该module对象的成员。
2.  下面再试试使用from…import语句来执行导入,例如使用如下程序来测试该模块。
3.  从上面的输出结果可以看出,即使使用from…import只导入模块中部分成员,该模块中的输出语句也会在import时自动执行,
这说明Python依然会加载并执行模块中的代码。
4.  使用"from fk module import name, hello"导入模块中成员的本质就是：
将fk module.py中的全部代码加载到内存并执行,然后只导入指定变量、函数等成员单元,并不会将整个模块导入,
因此上面程序在输出fk module 时将看到错误提示： name 'fk module'is not defined。
5.  在导入模块后,可以在模块文件所在目录下看到一个名为"pycache"的文件夹,打开该文件夹,
可以看到Python为每个模块都生成一个*.cpython-36.pyc文件,比如Python为 fk_module 模块生成
一个fk_module.cpython-36.pyc文件,该文件其实是Python为模块编译生成的字节码,用于提升该模块的运行效率。
"""
from fk_module import name, hello

print("================")
print(name)
print(hello)
# 打印fk_module
print(fk_module)
