"""
@wraps(wrapped_func)函数装饰器与update_wrapper(wrapper, wrapped_func)函数的作用是一样的,
都用于让包装函数看上去就像被包装函数(主要就是让包装函数的 __name__、__doc__ 属性与被包装函数保持一致)。
区别是：@wraps(wrapped_func)函数装饰器直接修饰包装函数,因此不需要传入包装函数作为参数;
而update_wrapper(wrapper, wrapped_func)则需要同时传入包装函数、被包装函数作为参数。
如下程序示范了@wraps(wrapped_func)函数装饰器的用法。
"""
from functools import wraps


def fk_decorator(f):
    # 让wrapper函数看上去就像f函数
    @wraps(f)
    def wrapper(*args, **kwds):
        print('调用被装饰函数')
        return f(*args, **kwds)

    return wrapper


@fk_decorator
def test():
    """test函数的说明信息"""
    print('执行test函数')


test()
print(test.__name__)
print(test.__doc__)
"""
1.  上面程序中粗体字代码的作用是：让被包装函数(wrapper)就像 f 函数。
2.  上面程序使用 @fk_decorator 修饰 test() 函数,因此在调用 test()函数时,实际上是调用 fk_decorator 的返回值：
wrapper 函数—— 这是前面的函数装饰器的功能。
3.  也就是说,上面程序中最后三行代码看上去是访问test函数,实际上是访问 wrapper 函数。
由于程序使用@wraps(f)修饰了 wrapper 函数,因此该函数看上去就像 test 函数。
所以,程序在输出 test.__name__ 和 test.__doc__ 时(注意此处的test其实是 wrapper 函数),输出的依然是 test 函数的函数名、描述文档。

调用被装饰函数
执行test函数
test
test函数的说明信息

4.  如果注释掉程序中的粗体字代码@wraps(f),此时将不能让wrapper 函数看上去像test函数。如果再次运行该程序,将看到如下输出结果。

调用被装饰函数
执行test函数
wrapper
None
"""