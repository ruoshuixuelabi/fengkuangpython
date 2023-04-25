"""
7.2.5	else块
1.  在 Python 的异常处理流程中还可添加一个else块,当try块没有出现异常时,程序会执行else 块。例如如下程序。
2.  上面程序为异常处理流程添加了else块,当程序中的try块没有出现异常时,程序就会执行else 块。
运行上面程序,如果用户输入导致程序中的try块出现了异常,则运行结果如下。
3.  看到这里,可能有读者觉得奇怪：既然只有当try块没有异常时才会执行else块,那么直接把else块的代码放在try块的代码的后面不就行了?
4.  实际上大部分语言的异常处理都没有else块,它们确实是将else块的代码直接放在try块的代码的后面的,
因为对于大部分场景而言,直接将else块的代码放在try块的代码的后面即可。
"""
s = input('请输入除数:')
try:
    result = 20 / int(s)
    print('20除以%s的结果是: %g' % (s , result))
except ValueError:
    print('值错误,您必须输入数值')
except ArithmeticError:
    print('算术错误,您不能输入0')
else:
    print('没有出现异常')
