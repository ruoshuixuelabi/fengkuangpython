"""
4.2.1 不要忘记缩进

代码块一定要缩进,否则就不是代码块。例如如下程序。
"""
s_age = input("请输入您的年龄:")
age = int(s_age)
if age > 20 :
print("年龄已经大于20岁了")
"""
上面程序的 if 条件与下面的 print 语句位于同一条竖线上,这样在 if 条件下就没有受控制的代码块了。因此,上面程序执行时会报出如下错误。

 File "no_indent.py", line 9
    print("年龄已经大于20岁了")
    ^
IndentationError: expected an indented block after 'if' statement on line 8

进程已结束,退出代码1


注意：if条件后的条件执行体一定要缩进。只有缩进后的代码才能算条件执行体。

接下来读者会产生一个疑问：代码块(条件执行体)到底要缩进多少呢?这个随意。
你可以缩进1个空格、2个空格、3个空格 … … 或1个 Tab 位,这都是符合语法要求的。但从编程习惯来看,Python 通常建议缩进4个空格。
"""