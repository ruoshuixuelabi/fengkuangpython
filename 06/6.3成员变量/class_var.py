"""
6.3	成员变量
1.  在类体内定义的变量,默认属于类本身。如果把类当成类命名空间,那么该类变量其实就是定义在类命名空间内的变量

6.3.1   类变量和实例变量

2.  在类命名空间内定义的变量就属于类变量, Python可以使用类来读取、修改类变量。 
例如,下面代码定义了一个Address类,并为该类定义了多个类变量。
3.  下面两行粗体字代码为Address 定义了两个类变量。
4.  对于类变量而言,它们就是属于在类命名空间内定义的变量,因此程序不能直接访问这些变量, 程序必须使用类名来调用类变量。
不管是在全局范围内还是函数内访问这些类变量,都必须使用类 名进行访问。
5.  当程序第一次调用 Address 对象的 info()方法输出两个类变量时,将会输出这两个类变量的初始值。
接下来程序通过 Address 类修改了两个类变量的值,因此当程序第二次通过 info()方法输出两个类变量时,将会输出这两个类变量修改之后的值。
"""


class Address:
    detail = '广州'
    post_code = '510660'

    def info(self):
        # 尝试直接访问类变量
        #        print(detail) # 报错
        # 通过类来访问类变量
        print(Address.detail)  # 输出 广州
        print(Address.post_code)  # 输出 510660


# 通过类来访问Address类的类变量
print(Address.detail)
addr = Address()
addr.info()
# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()
