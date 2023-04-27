from functools import update_wrapper


def fk_decorator(f):
    def wrapper(*args, **kwds):
        print('调用被装饰函数')
        return f(*args, **kwds)

    update_wrapper(wrapper, f)
    return wrapper


@fk_decorator
def test():
    """test函数的说明信息"""
    print('执行test函数')


test()
print(test.__name__)
print(test.__doc__)
