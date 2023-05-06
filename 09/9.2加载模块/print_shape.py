"""
9.2.2 默认的模块加载路径

如果要安装某些通用性模块,比如复数功能支持的模块、矩阵计算支持的模块、图形界面支持的模块等,
这些都属于对Python本身进行扩展的模块,这种模块应该直接安装在Python内部,
以便被所有程序共享,此时就可借助于Python 默认的模块加载路径。

Python 默认的模块加载路径由 sys.path 变量代表,因此可通过在交互式解释器中执行如下命令来查看Python 默认的模块加载路径。
import sys,pprint
pprint.pprint(sys.path)

上面代码使用 pprint 模块下的 pprint() 函数代替普通的 print() 函数,这是因为如果要打印的内容很多,使用pprint可以显示更友好的打印结果。

上面的运行结果就是 Python 3.x 默认的模块加载路径,这是因为作者将 Python 安装在了d:\Python路径下。
如果将 Python 安装在其他路径下,上面的运行结果应该略有差异。

上面的运行结果列出的路径都是Python 默认的模块加载路径,但通常来说,
我们应该将Python 的扩展模块添加在 lib\site-packages路径下,它专门用于存放 Python 的扩展模块和包。

下面编写一个Python 模块文件,并将该文件复制在lib\site-packages路径下。

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
"""
上面模块文件中定义了一个 print_triangle()函数,把该模块文件拷贝到 lib\site-packages路径下,
就相当于为 Python 扩展了一个 print_triangle 模块,这样任何 Python 程序都可使用该模块。
下面可直接在 Python 交互式解释器中测试该模块。在Python 交互式解释器中输入如下命令。
import  print_shape
print(print_shape.__doc__)

上面第一行代码用于导入 print_shape 模块;第二行代码用于查看 print_shape 模块的文档,
交互式解释器输出了该模块开始定义的文档内容;第三行代码用于查看 print_shape 模块下 print_triangle 函数的文档,
交互式解释器会输出该函数定义后的文档说明。

接下来测试该模块中的 my_list 变量和 print_shape()函数。在交互式解释器中输入如下命令。
print_shape.my_list[1]
print_shape.print_triangle(4)

从上面的运行结果可以看到,程序通过模块前缀访问 my_list 变量,输出了该变量的第二个元素;
程序也通过模块前缀调用了 print_triangle 函数,打印出由星号组成的三角形,这表明该模块完全正常。
"""