"""
2.4.4 使用input 和 raw_input 获取用户输入

input() 函数用于向用户生成一条提示,然后获取用户输入的内容。由于input()函数总会将用户输入的内容放入字符串中,
因此用户可以输入任何内容,input() 函数总是返回一个字符串。

例如如下程序
"""
msg = input("请输入你的值：")
print(type(msg))
print(msg)
"""
第一次运行该程序,我们输入一个整数,运行过程如下：
请输入你的值：2
<class 'str'>

第二次运行该程序,我们输入一个浮点数,运行过程如下：
请输入你的值：1.2
<class 'str'>

第三次运行该程序,我们输入一个字符串,运行过程如下：
请输入你的值：ghello
<class 'str'>
ghello

从上面的运行过程可以看出,无论输入哪种内容,始终可以看到input()函数返回字符串,程序总会将用户输入的内容转换成字符串。

需要指出的是, Python 2.x 提供了一个 raw_input() 函数,该 raw_input()函数就相当于Python 3.x 中的 input()函数。

而 Python 2.x也提供了一个 input() 函数,该 input()函数则比较怪异：要求用户输入的必须是符合 Python 语法的表达式。
通常来说,用户只能输入整数、浮点数、复数、字符串等。重点是格式必须正确,比如输入字符串时必须使用双引号,否则 Python 就会报错。

使用Python 2.x来运行上面程序,假如输入一个整数,运行过程如下：
请输入你的值：2
<class 'int'>
2

使用Python2.x 来运行上面程序,假如输入一个复数,运行过程如下：
请输入你的值：2+3j
<type 'complex'>
(2+3j)

NameError:       name       'Hello'       is       not       defined
上面程序报错的原因是： Python 2.x 的 input()函数要求用户输入字符串时必须用引号把字符串 括起来。

注意：在 Python 2.x中应该尽量使用 raw_input()函数来获取用户输入;Python 2.x 中的 raw_input()等同于 Python 3.x中的 input()。
"""
