"""
还可使用 @property 装饰器来修饰方法,使之成为属性。例如如下程序。
"""


class Cell:
    # 使用@property修饰方法,相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state

    # 为state属性设置setter方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    # 为is_dead属性设置getter方法,只有getter方法属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()
# 修改state属性
c.state = 'Alive'
# 访问state属性
print(c.state)
# 访问is_dead属性
print(c.is_dead)
"""
上面程序中第一行粗体字代码使用 @property 修饰了 state() 方法,这样就使得该方法变成了 state 属性的 getter 方法。
如果只有该方法,那么 state 属性只是一个只读属性。

当程序使用@property修饰了 state 属性之后,又多出一个 @state.setter 装饰器,该装饰器用于修饰 state 属性的 setter方法,
如上面程序中第二行粗体字代码所示。这样 state 属性就有了 getter 和 setter方法,state 属性就变成了读写属性。

程序中第三行粗体字代码使用 @property 修饰了 is_dead 方法,该方法就会变成 is_dead 属性的 getter方法。
此处同样会多出一个 @is_dead.setter 装饰器,但程序并未使用该装饰器修饰setter方法,因此 is_dead 属性只是一个只读属性。
"""
