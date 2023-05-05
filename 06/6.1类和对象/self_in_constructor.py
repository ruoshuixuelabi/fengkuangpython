"""
此外,在构造方法中,self参数(第一个参数)代表该构造方法正在初始化的对象。例如如下代码。

在 InConstructor 的构造方法中,self参数总是引用该构造方法正在初始化的对象。
程序中粗体字代码将正在执行初始化的InConstructor对象的foo实例变量设为6,这意味着该构造方法返回的所有对象的foo实例变量都等于6。
"""


class InConstructor:
    def __init__(self):
        # 在构造方法里定义一个foo变量(局部变量)
        foo = 0
        # 使用self代表该构造方法正在初始化的对象
        # 下面的代码将会把该构造方法正在初始化的对象的foo实例变量设为6
        self.foo = 6


# 所有使用InConstructor创建的对象的foo实例变量将被设为6
print(InConstructor().foo)  # 输出6
