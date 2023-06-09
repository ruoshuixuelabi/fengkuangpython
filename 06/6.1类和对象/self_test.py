"""
需要说明的是,自动绑定的 self 参数并不依赖具体的调用方式,不管是以方法调用还是以函数调用的方式执行它,self 参数一样可以自动绑定。
例如如下程序。

下面程序中第一行粗体字代码以方法形式调用User对象的 test() 方法,此时方法调用者当然会自动绑定到方法的第一个参数(self参数);
程序中第二行粗体字代码以函数形式调用 User 对象的 test() 方法,看上去此时没有调用者了,
但程序依然会把实际调用者绑定到方法的第一个参数,因此上面程序中两行粗体字代码的输出结果完全相同。
"""


class User:
    def test(self):
        print('self参数: ', self)


u = User()
# 以方法形式调用test()方法
u.test()  # <__main__.User object at 0x00000000021F8240>
# 将User对象的test方法赋值给foo变量
foo = u.test
# 通过foo变量(函数形式)调用test()方法。
foo()  # <__main__.User object at 0x00000000021F8240>
