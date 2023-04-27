"""
partialmethod()与 partial()函数的作用基本相似,区别只是 partial()函数用于为函数的部分参数绑定值：
而 partialmethod()函数则用于为类中方法的部分参数绑定值。如下程序示范了 partialmethod()函数的用法。
"""
from functools import *


class Cell:
    def __init__(self):
        self._alive = False

    # @property装饰器指定该方法可使用属性语法访问
    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    # 指定set_alive()方法就是将set_state()方法的state参数指定为True
    set_alive = partialmethod(set_state, True)
    # 指定set_dead()方法就是将set_state()方法的state参数指定为False
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)
# 相当于调用c.set_state(True)
c.set_alive()
print(c.alive)
# 相当于调用c.set_state(False)
c.set_dead()
print(c.alive)
"""
上面程序定义了一个Cell(细胞)类,在该类中定义了一个 set_state()方法,该方法用于设置该细胞的状态。
接下来程序中两行粗体字代码使用 partialmethod()函数为 set_state()方法绑定了参数值;
将 set_state()方法的参数值绑定为True 之后赋值给了 set_alive()方法；将 set_state()方法的参数值绑定为False之后赋值给了 set_dead() 方法。
因此,程序调用c.set_alive()就相当于调用c.set_state(True); 程序调用c.set_dead()就相当于调用 c.set_state(False)。
"""
