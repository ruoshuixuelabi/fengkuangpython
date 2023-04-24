"""
1.  全局变量默认可以在所有函数内被访问,但如果在函数中定义了与全局变量同名的变量,此时就会发生局部变量遮蔽(hide)全局变量的情形。
例如如下程序。
"""
name = 'Charlie'
def test ():
    # 直接访问name全局变量
    print(name) # Charlie
    name = '孙悟空'
test()
print(name)
    