"""
2.2.1  Python 是弱类型语言
1. 无论使用什么语言编程，总要处理数据，处理数据就需要使用变量来保存数据。
2. 形象地看，变量就像一个个小容器，用于“盛装”程序中的数据。常量同样也用于“盛装”程序中的数据。
常量与变量的区别是：常量一旦保存某个数据之后，该数据就不能发生改变；
但变量保存的数据则可以多次发生改变，只要程序对变量重新赋值即可。
3. Python使用等号(=)作为赋值运算符，例如a= 20就是一条赋值语句，这条语句用于将20装入变量a 中
——这个过程就被称为赋值：将20赋值给变量a。
4. Python是弱类型语言，弱类型语言有两个典型特征。
(1)变量无须声明即可直接赋值：对一个不存在的变量赋值就相当于定义了一个新变量。
(2)变量的数据类型可以动态改变：同一个变量可以一会儿被赋值为整数值， 一会儿被赋值为字符串。
5. 形象地说，函数就相当于一个有魔法的“黑盒子”,你可以向这个“黑盒子”提供 一些数据，
这个“黑盒子”会对这些数据进行处理，这种处理包括转换和输出结果。
比如 print()也是一个函数，它的作用就是输出传入的数据。此处type(O)函数的作用则用于输出传入数据的类型。
"""
# 定义一个数值类型变量
a = 5
print(a)
# 重新将字符串值赋值给a变量
a = 'Hello, Charlie'
print(a)
# 如果想查看此时 a 的类型，可以使用Python的 type()函数。
print(type(a))
