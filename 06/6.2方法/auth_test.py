"""
下面例子示范了如何通过函数装饰器为函数添加权限检查的功能。程序代码如下。
"""


def auth(fn):
    def auth_fn(*args):
        # 用一条语句模拟执行权限检查
        print("----模拟执行权限检查----")
        # 回调要装饰的目标函数
        fn(*args)

    return auth_fn


@auth
def test(a, b):
    print("执行test函数,参数a: %s, 参数b: %s" % (a, b))


# 调用test()函数,其实是调用装饰后返回的auth_fn函数
test(20, 15)
"""
上面程序使用 @auth 修饰了 test() 函数,这会使得 test() 函数被替换成 auth(函数所返回的 auth_fn 函数,
而 auth_fn 函数的执行流程是：①先执行权限检查;②回调被修饰的目标函数——
简单来说,auth_fn  函数就为被修饰函数添加了一个权限检查的功能。运行该程序,可以看到如下输出结果。
----模拟执行权限检查----
执行test函数,参数a: 20, 参数b: 15
"""
