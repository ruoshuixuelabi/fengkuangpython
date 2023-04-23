"""
 2.3.3  复数
1. Python甚至可以支持复数，复数的虚部用 j 或 J 来表示。
2. 如果需要在程序中对复数进行计算，可导入Python的 cmath 模块 (c 代表complex), 在该模块下包含了各种支持复数运算的函数。
3. 模块就是一个Python程序，Python正是通过模块提高了自身的可扩展性的；
Python 本身内置了大量模块，此外还有大量第三方模块，导入这些模块即可直接使用这些程序中定义的函数。
关于模块的详细介绍请参考本书第9章。

"""
ac1 = 3 + 0.2j
print(ac1)
print(type(ac1))  # 输出 complex类型
ac2 = 4 - 0.1j
print(ac2)
# 复数运行
print(ac1 + ac2)  # 输出 (7+0.1j)
# 导入cmatch模块
import cmath

# sqrt()是 cmath 模块下的函数，用于计算平方根
ac3 = cmath.sqrt(-1)
print(ac3)  # 输出 1j
