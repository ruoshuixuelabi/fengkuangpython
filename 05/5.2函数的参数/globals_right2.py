"""
在函数中声明全局变量

为了避免在函数中对全局变量赋值(不是重新定义局部变量),可使用global语句来声明全局变量。因此,可将程序改为如下形式。
"""
name = 'Charlie'


def test():
    # 声明name是全局变量,后面的赋值语句不会重新定义局部变量
    global name
    # 直接访问name全局变量
    print(name)  # Charlie
    name = '孙悟空'


test()
print(name)  # 孙悟空
