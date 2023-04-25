"""
1.  如果程序需要在读取、设置属性之前进行某种拦截处理(比如检查数据是否合法之类的),
也可通过重写    __setattr__()或 __getattr__ 方法来实现。
2.  上面程序只重写了 __setattr__()方法,并在该方法中对 name、age 属性设置的属性值进行了限制。
比如程序中第一行粗体字代码限制了name 属性值的长度必须在2~8之间；第二行粗体字代码限制了age属性值必须在10~60之间,
只有在该范围内的属性值才能设置成功,否则程序会引发 ValueError 异常。
上面程序中最后两行代码设置的属性值不符合条件,它们将会引发 ValueError 异常。
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写__setattr__()方法对设置的属性值进行检查
    def __setattr__(self, name, value):
        # 如果正在设置name属性
        if name == 'name':
            if 2 < len(value) <= 8 or len(value) > 8:
                self.__dict__['name'] = value
            else:
                raise ValueError('name的长度必须在2～8之间')

        elif name == 'age':
            if 10 < value < 60:
                self.__dict__['age'] = value
            else:
                raise ValueError('age值必须在10～60之间')


u = User('fkit', 24)
print(u.name)
print(u.age)
# u.name = 'fk' # 引发异常
u.age = 2  # 引发异常
