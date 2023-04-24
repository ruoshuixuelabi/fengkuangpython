"""
1.  实际上,Python 完全允许使用对象来访问该对象所属类的类变量(当然还是推荐使用类访问类变量)。例如如下程序。
2.  上面程序的Record 中定义了两个类变量,接下来程序完全可以使用Record 对象来访问这两个类变量。
3.  在上面程序的Record 类的info()方法中,程序使用self访 问Record 类的类变量,此时self代 表 info()方法的调用者,
也就是Record 对象,因此这是合法的。
4.  在主程序代码区,程序创建了Record 对象,并通过对象调用Record 对象的item、date类变量,这也是合法的。
5.  实际上,程序通过对象访问类变量,其本质还是通过类名在访问类变量。运行上面程序,将看到如下输出结果。
6.  由于通过对象访问类变量的本质还是通过类名在访问,因此如果类变量发生了改变,当程序访问这些类变量时也会读到修改之后的值。
"""


class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2016-06-16'

    def info(self):
        print('info方法中: ', self.item)
        print('info方法中: ', self.date)


rc = Record()
print(rc.item)  # '鼠标'
print(rc.date)  # '2016-06-16'
rc.info()

# 修改Record类的两个类变量
Record.item = '键盘'
Record.date = '2016-08-18'
# 调用info()方法
rc.info()
