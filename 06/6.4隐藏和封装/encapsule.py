"""
1.  封装(Encapsulation)是面向对象的三大特征之一(另外两个是继承和多态),
它指的是将对象的状态信息隐藏在对象内部,不允许外部程序直接访问对象内部信息,
而是通过该类所提供的方 法来实现对内部信息的操作和访问。
2.  封装是面向对象编程语言对客观世界的模拟,在客观世界里,对象的状态信息都被隐藏在对象内部,外界无法直接操作和修改。
对一个类或对象实现良好的封装,可以达到以下目的。
(1)隐藏类的实现细节 。
(2)让使用者只能通过事先预定的方法来访问数据,从而可以在该方法里加入控制逻辑,限制对属性的不合理访问。
(3)可进行数据检查,从而有利于保证对象信息的完整性。
(4)便于修改,提高代码的可维护性。
3.  为了实现良好的封装,需要从两个方面来考虑。
(1)将对象的属性和实现细节隐藏起来,不允许外部直接访问。
(2)把方法暴露出来,让方法来控制对这些属性进行安全的访问和操作。
4.  因此,实际上封装有两个方面的含义：把该隐藏的隐藏起来,把该暴露的暴露出来。
5.  Python并没有提供类似于其他语言的private等修饰符,因此Python 并不能真正支持隐藏。
6.  为了隐藏类中的成员, Python 玩了一个小技巧：只要将Python类的成员命名为以双下画线开头的, Python 就会把它们隐藏起来。
7.  例如,如下程序示范了Python 的封装机制。
8.  下面程序将 User 的两个实例变量分别命名为 __name  和 __age, 这两个实例变量就会被隐藏起来,
这样程序就无法直接访问 __name、__age 变量,只能通过setname()、getname()、setage()、getage()
这些访问器方法进行访问,而setname()、setage()会对用户设置的name、age 进行控制,只有符合条件的name、age 才允许设置。
9.  下面程序用到了raise关键字来抛出异常。关于raise 关键字和异常的相关信息,请参考本书第7章。
10. 从该程序可以看出封装的好处,程序可以将User对象的实现细节隐藏起来,程序只能通过暴露出来的setname()、setage()方法
来改变User 对象的状态,而这两个方法可以添加自己的逻辑控制,这种控制对User 的修改始终是安全的。
11. 最后需要说明的是, Python 其实没有真正的隐藏机制,双下画线只是Python的一个小技巧：
Python 会"偷偷"地改变以双下画线开头的方法名,会在这些方法名前添加单下画线和类名。
12. 类似的是,程序也可通过为隐藏的实例变量添加下画线和类名的方式来访问或修改对象的实例变量。
13. 总结：Python 并没有提供真正的隐藏机制,所以 Python 类定义的所有成员默认都是公开的;如果程序希望将 Python 类中
的某些成员隐藏起来,那么只要让该成员的名字以双下画线开头即可。 即使通过这种机制实现了隐藏,其实也依然可以绕过去。
"""


class User:
    def __hide(self):
        print('示范隐藏的hide方法')

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3～8之间')
        self.__name = name

    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户名年龄必须在18在70之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


# 创建User对象
u = User()
# 对name属性赋值,实际上调用setname()方法
# u.name = 'fk' # 引发 ValueError: 用户名长度必须在3～8之间
u.name = 'fkit'
u.age = 25
print(u.name)  # fkit
print(u.age)  # 25

# 尝试调用隐藏的__hide()方法
# u.__hide()

# 调用隐藏的__hide()方法
u._User__hide()
# 对隐藏的__name属性赋值
u._User__name = 'fk'
# 访问User对象的name属性（实际上访问__name实例变量）
print(u.name)
