"""
现在问题来了,如果使用类调用实例方法,那么该方法的第一个参数(self)怎么自动绑定呢? 例如如下程序。

class User:
    def walk(self):
        print(self, '正在慢慢地走')
# 通过类调用实例方法
User.walk()

运行上面代码,程序会报出如下错误。TypeError: User.walk() missing 1 required positional argument: 'self'

请看程序中粗体字代码,调用walk()方法缺少传入的self参数,所以导致程序出错。这说明在使用类调用实例方法时,
Python 不会自动为第一个参数绑定调用者。实际上也没法自动绑定,因此实例方法的调用者是类本身,而不是对象。

如果程序依然希望使用类来调用实例方法,则必须手动为方法的第一个参数传入参数值。例如,将上面的粗体字代码改为如下形式。
u = User()
# 显式为方法的第一个参数绑定参数值
User.walk(u)

上面粗体字代码显式地为walk()方法的第一个参数绑定了参数值,这样的调用效果完全等同于执行u.walk()

实际上,当通过 User 类调用 walk() 实例方法时,Python 只要求手动为第一个参数绑定参数值,并不要求必须绑定 User 对象,
因此也可使用如下代码进行调用。

# 显式为方法的第一个参数绑定fkit字符串参数值
User.walk('fkit')
如果按上面方式进行绑定,那么 'fkit' 字符串就会被传给 walk()方法的第一个参数self。 因此,运行上面代码,将会看到如下输出结果。

fkit 正在慢慢地走

Python的类可以调用实例方法,但使用类调用实例方法时,Python 不会自动为方法的第一个参数self绑定参数值;
程序必须显式地为第一个参数 self 传入方法调用者。这种调用方式被称为"未绑定方法"。
"""


class User:
    def walk(self):
        print(self, '正在慢慢地走')


# 通过类调用实例方法
# User.walk()
u = User()
# 显式为方法的第一个参数绑定参数值
User.walk(u)

# 显式为方法的第一个参数绑定fkit字符串参数值
User.walk('fkit')
