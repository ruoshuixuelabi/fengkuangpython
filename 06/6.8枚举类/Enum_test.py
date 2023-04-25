"""
6.8 枚举类

1.  在某些情况下, 一个类的对象是有限且固定的,比如季节类,它只有4个对象；
再比如行星类, 目前只有8个对象。这种实例有限且固定的类,在Python 中被称为枚举类。

6.8.1	枚举入门

2.  程序有两种方式来定义枚举类。
(1)直 接 使 用Enum 列出多个枚举值来创建枚举类。
(2)通 过 继 承Enum 基类来派生枚举类。
3.  如下程序示范了直接使用Enum 列出多个枚举值来创建枚举类。
4.  上面程序使用Enum() 函数(就是Enum  的构造方法)来创建枚举类,该构造方法的第一个参数是枚举类的类名；
第二个参数是一个元组,用于列出所有枚举值。
5.  在定义了上面的 Season 枚举类之后,程序可直接通过枚举值进行访问,这些枚举值都是该枚举的成员,
每个成员都有 name、value 两个属性,其中 name 属性值为该枚举值的变量名, value代表该枚举值的序号(序号通常从1开始)。
6.  程序除可直接使用枚举之外,还可通过枚举变量名或枚举值来访问指定枚举对象。例如如下代码(程序清单同上)。
7.  此外, Python 还为枚举提供了一个 __members__ 属性,,该属性返回一个dict字典,字典包含了该枚举的所有枚举实例。
程序可通过遍历 __members__ 属性来访问枚举的所有实例。例如如下代码
"""
import enum
# 定义Season枚举类
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
# 直接访问指定枚举
print(Season.SPRING)
# 访问枚举成员的变量名
print(Season.SPRING.name)
# 访问枚举成员的值
print(Season.SPRING.value)

# 根据枚举变量名访问枚举对象
print(Season['SUMMER']) # Season.SUMMER
# 根据枚举值访问枚举对象
print(Season(3)) # Season.FALL

# 遍历Season枚举的所有成员
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)