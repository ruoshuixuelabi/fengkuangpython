"""
9.2.2	默认的模块加载路径
1.  如果要安装某些通用性模块,比如复数功能支持的模块、矩阵计算支持的模块、图形界面支持的模块等,
这些都属于对Python本身进行扩展的模块,这种模块应该直接安装在Python内部,
以便被所有程序共享,此时就可借助于Python 默认的模块加载路径。
2.  Python 默认的模块加载路径由sys.path变量代表,因此可通过在交互式解释器中执行如下命令来查看Python 默认的模块加载路径。
3.  上面的运行结果列出的路径都是Python 默认的模块加载路径,但通常来说,
我们应该将Python 的扩展模块添加在liblsite-packages路径下,它专门用于存放Python 的扩展模块和包。
4.  下面编写一个Python 模块文件,并将该文件复制在lib\site-packages路径下。
5.  上面模块文件中定义了一个print triangle()函数,把该模块文件拷贝到lib\site-packages路径下,
就相当于为Python 扩展了一个print shape模块,这样任何Python 程序都可使用该模块。
下面可直接在Python 交互式解释器中测试该模块。在Python 交互式解释器中输入如下命令。
"""
"""
简单的模块,该模块包含以下内容
my_list：保存列表的变量
print_triangle: 使用星号打印三角形的函数
"""
my_list = ['Python', 'Kotlin', 'Swift']


def print_triangle(n):
    """使用星号打印一个三角形"""
    if n <= 0:
        raise ValueError('n必须大于0')
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1), end='')
        print('')


# ====以下是测试代码====
def test_print_triangle():
    print_triangle(3)
    print_triangle(4)
    print_triangle(7)


if __name__ == '__main__': test_print_triangle()
