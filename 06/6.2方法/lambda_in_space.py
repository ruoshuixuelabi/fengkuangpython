"""
但下面代码就有区别。下面代码示范了在全局空间和类命名空间内分别定义 lambda 表达式。
"""
global_fn = lambda p: print('执行lambda表达式,p参数: ', p)


class Category:
    cate_fn = lambda p: print('执行lambda表达式,p参数: ', p)


# 调用全局范围内的global_fn,为参数p传入参数值
global_fn('fkit')  # ①
c = Category()
# 调用类命名空间内的cate_fn,Python自动绑定第一个参数
c.cate_fn()  # ②
"""
上面程序中的两行粗体字代码分别在全局空间、类命名空间内定义了两个 lambda 表达式,
在全局空间内定义的 lambda 表达式就相当于一个普通函数,因此程序使用调用函数的方式来调用该 lambda 表达式,
并显式地为第一个参数绑定参数值,如上面程序中①号代码所示。

对于在类命名空间内定义的 lambda 表达式,则相当于在该类命名空间中定义了一个函数,这个函数就变成了实例方法,
因此程序必须使用调用方法的方式来调用该 lambda 表达式,Python 同样会为该方法的第一个参数(相当于 self 参数)绑定参数值,
如上面程序中②号代码所示。
"""