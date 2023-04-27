"""
1.  下面再定义一个更加复杂的包,在该包下将会包含多个模块,并使用  __init__.py文件来加载这些模块。
2.  新建一个 fk_package 包,并在该包下包含三个模块文件。
(1)print_shape.py
(2)billing.py
(3)arithmetic_chart.py

3.  fk_package 的文件结构如下：
fk_package
    arithmetic  chart.py
    billing.py
    print_shape.py
    __init__.py
其中, arithmetic chart.py模块文件的内容如下。
"""


def print_multiple_chart(n):
    """打印乘法口角表的函数"""
    for i in range(n):
        for j in range(i + 1):
            print('%d * %d = %2d' % ((j + 1), (i + 1), (j + 1) * (i + 1)), end='  ')
        print('')
