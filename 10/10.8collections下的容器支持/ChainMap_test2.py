"""
1.  掌握了 ChainMap 的用法之后,接下来介绍的示例程序借鉴了Python 库文档中的一个例子,
该例子将局部范围的定义、全局范围的定义、Python 内置定义链成一个ChainMap,
当程序通过该 ChainMap 获取变量时,将会按照局部定义、全局定义、内置定义的顺序执行搜索
"""
from collections import ChainMap
import builtins

my_name = '孙悟空'


def test():
    my_name = 'yeeku'
    # 将locals、globals、buliltins的变量链接成ChainMap
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    # 访问my_name对应的value,优先使用局部范围的定义
    print(pylookup['my_name'])  # 'yeeku'
    # 访问len对应的value,由于局部范围、全区范围都找不到,因此访问内置定义的len函数
    print(pylookup['len'])  # <built-in function len>


test()
