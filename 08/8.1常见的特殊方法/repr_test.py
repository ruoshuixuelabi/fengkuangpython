"""
object 类提供的 __repr__()方法总是返回该对象实现类的"类名+object at+内存地址"值,
这个返回值并不能真正实现"自我描述"的功能,因此,如果用户需要自定义类能实现"自我描述"的功能,就必须重写 __repr__()方法。例如下面程序。
"""


class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    # 重写toString()方法,用于实现Apple对象的"自我描述"
    def __repr__(self):
        return "Apple[color=" + self.color + ", weight=" + str(self.weight) + "]"


a = Apple("红色", 5.68)
# 打印Apple对象
print(a)
"""
编译、运行上面程序,可以看到如下运行结果。
Apple[color=红色, weight=5.68]

从上面的运行结果可以看出,通过重写 Apple 类的 __repr__()方法,就可以让系统在打印 Apple 对象时打印出该对象的"自我描述"信息。

大部分时候,重写 __repr__()方法总是返回该对象的所有令人感兴趣的信息所组成的字符串。通常可返回如下格式的字符串：
类名[field1 = 值1 ,field2 = 值2, . . . ]
"""