"""
2.2 变量

无论使用什么语言编程,总要处理数据,处理数据就需要使用变量来保存数据。

形象地看,变量就像一个个小容器,用于"盛装"程序中的数据。常量同样也用于"盛装"程序中的数据。常量与变量的区别是：
常量一旦保存某个数据之后,该数据就不能发生改变;但变量保存的数据则可以多次发生改变,只要程序对变量重新赋值即可。

Python使用等号(=)作为赋值运算符,例如a = 20就是一条赋值语句,这条语句用于将 20 装入变量 a 中——
这个过程就被称为赋值：将20赋值给变量a。

Python是弱类型语言,弱类型语言有两个典型特征。
(1)变量无须声明即可直接赋值：对一个不存在的变量赋值就相当于定义了一个新变量。
(2)变量的数据类型可以动态改变：同一个变量可以一会儿被赋值为整数值,一会儿被赋值为字符串。

2.2.1   Python是弱类型语言

对于没有编程基础的读者(甚至是小孩子,比如我儿子也在学习这本书),可以先不编写真正的 Python 程序,
而是先打开Python的交互式解释器,在这个交互式解释器中"试验"Python。

下面先在Python解释器中输入如下内容。
a = 5

上面代码没有生成任何输出,只是向交互式解释器中存入了一个变量 a, 该变量 a 的值为5。

如果我们想看到某个变量的值,可以直接在交互式解释器中输入该变量。例如,此处想看到变量 a 的值,可以直接输入 a。
a

从上面的交互式过程可以看到,交互式解释器输出变量 a 的值：5。

接下来,如果改变变量 a 的值,只要将新的值赋给(装入)变量 a 即可,新赋的值会覆盖原来的值。例如：
a ='Hello,Charlie'

此时变量 a 的值就不再是5了,而是字符串"Hello,Charlie",a的类型也变成了字符串。下面再次输入a, 让交互式解释器显示a 的值。
a
'Hello,Charlie'

如果想查看此时 a 的类型,可以使用Python的 type()函数。
在交互式解释器中输入：
type(a)
此时可以看到a 的类型是str。

提示：形象地说,函数就相当于一个有魔法的"黑盒子",你可以向这个"黑盒子"提供一些数据,
这个"黑盒子"会对这些数据进行处理,这种处理包括转换和输出结果。
比如 print() 也是一个函数,它的作用就是输出传入的数据。此处type()函数的作用则用于输出传入数据的类型。

将上面的交互过程转换成真正的Python 程序——只要将交互式过程中输入的每行代码放在一 个文件中,
并使用print()函数来输出变量(在交互式解释器中只要输入变量名,交互式解释器就会输出变量的值;
但在 Python 程序中则必须使用 print() 函数来输出变量),将该文件保存为以 .py 结尾的源文件即可。上面的交互过程对应的程序如下。
"""
# 定义一个数值类型变量
a = 5
print(a)
# 重新将字符串值赋值给a变量
a = 'Hello, Charlie'
print(a)
# 如果想查看此时 a 的类型,可以使用Python的 type()函数。
print(type(a))
