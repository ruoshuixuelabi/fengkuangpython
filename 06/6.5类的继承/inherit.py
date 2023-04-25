"""
6.5 类的继承

1.  继承是面向对象的三大特征之一,也是实现软件复用的重要手段。 Python 的继承是多继承机制,即一个子类可以同时有多个直接父类。

6.5.1   继承的语法

2.  Python 子类继承父类的语法是在定义子类时,将多个父类放在子类之后的圆括号里。语法格式如下：
class   SubClass(SuperClass1,SuperClass2,..):
    #类定义部分

3.  从上面的语法格式来看,定义子类的语法非常简单,只需在原来的类定义后增加圆括号,
并在圆括号中添加多个父类,即可表明该子类继承了这些父类。
4.  如果在定义一个 Python 类时并未显式指定这个类的直接父类,则这个类默认继承 object类。
因此,object类是所有类的父类,要么是其直接父类,要么是其间接父类。
5.  实现继承的类被称为子类,被继承的类被称为父类,也被称为基类、超类。父类和子类的关系, 是一般和特殊的关系。
例如水果和苹果的关系,苹果继承了水果,苹果是水果的子类,则苹果是一 种特殊的水果。
6.  由于子类是一种特殊的父类,因此父类包含的范围总比子类包含的范围要大,所以可以认为父类是大类,而子类是小类。
7.  从实际意义上看,子类是对父类的扩展,子类是一种特殊的父类。
从这个意义上看,使用继承来描述子类和父类的关系是错误的,用扩展更恰当。因此,这样的说法更加准确：Apple 类扩展了 Fruit类 。
8.  从子类的角度来看,子类扩展 (extend) 了父类；但从父类的角度来看,父类派生(derive)出子类。
也就是说,扩展和派生所描述的是同一个动作,只是观察角度不同而已。
9.  下面程序示范了子类继承父类的特点。下面是Fruit类的代码。
10. 上面程序开始定义了两个父类：Fruit 类和 Food 类,接下来程序定义了一个Apple 类,该Apple 类基本上是一个空类。
11. 在主程序部分,主程序创建了 Apple 对象之后,可以访问该Apple 对象的info()和 taste()方法, 这表明Apple 对象也具有了
info() 和 taste() 方法,这就是继承的作用——子类扩展(继承)了父类, 将可以继承得到父类定义的方法,这样子类就可复用父类的方法了。
"""


class Fruit:
    def info(self):
        print("我是一个水果！重%g克" % self.weight)


class Food:
    def taste(self):
        print("不同食物的口感不同")


# 定义Apple类,继承了Fruit和Food类
class Apple(Fruit, Food):
    pass


# 创建Apple对象
a = Apple()
a.weight = 5.6
# 调用Apple对象的info()方法
a.info()
# 调用Apple对象的taste()方法
a.taste()
