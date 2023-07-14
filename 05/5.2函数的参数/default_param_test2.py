"""
由于 Python 要求在调用函数时关键字参数必须位于位置参数的后面,
因此在定义函数时指定了默认值的参数(关键字参数)必须在没有默认值的参数之后。例如如下代码。
"""


# 定义一个打印三角形的函数,有默认值的参数必须放在后面
def printTriangle(char, height=5):
    for i in range(1, height + 1):
        # 先打印一排空格
        for j in range(height - i):
            print(' ', end='')
        # 再打印一排特殊字符
        for j in range(2 * i - 1):
            print(char, end='')
        print()


printTriangle('@', 6)
printTriangle('#', height=7)
printTriangle(char='*')
"""
上面程序定义了一个 printTriangle()函数,该函数的第一个 char 参数没有默认值,第二个 height 参数有默认值。

上面程序中第一次调用 printTriangle()时,程序使用两个位置参数分别为 char、height 传入参数值,这当然是允许的;
第二次调用 printTriangle()时,第一个参数使用位置参数,那么该参数值将传给 char 参数,
第二个参数使用关键字参数为height参数传入参数值,这也是允许的;
第三次调用 printTriangle()时,只使用关键字参数为char参数传入参数值,此时height参数将使用默认值,这是符合语法的。

Python 要求将带默认值的参数定义在形参列表的最后。
"""
