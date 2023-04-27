"""
9.2.4	模块的__all__ 变量

1.  在默认情况下,如果使用"from 模块名 import *"这样的语句来导入模块,程序会导入该模块中所有不以下画线开头的程序单元,
这是很容易想到的结果。
2.  有时候模块中虽然包含很多成员,但并不希望每个成员都被暴露出来供外界使用,此时可借助于模块的 __all__ 变量,
将变量的值设置成一个列表,只有该列表中的程序单元才会被暴露出来。
3.  例如,下面程序定义了一个包含 __all__ 变量的模块。
"""
'测试__all__变量的模块'


def hello():
    print("Hello, Python")


def world():
    print("Pyhton World is funny")


def test():
    print('--test--')


# 定义__all__变量,指定默认只导入hello和world两个程序单元
__all__ = ['hello', 'world']
