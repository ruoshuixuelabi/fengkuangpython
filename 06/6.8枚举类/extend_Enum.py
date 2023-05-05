"""
如果要定义更复杂的枚举,则可通过继承 Enum 来派生枚举类,在这种方式下程序就可以为枚举额外定义方法了。例如如下程序。
"""
import enum


class Orientation(enum.Enum):
    # 为序列值指定value值
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print('这是一个代表方向【%s】的枚举' % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation['WEST'])
# 通过枚举值来访问枚举
print(Orientation('南'))
# 调用枚举的info()方法
Orientation.EAST.info()
# 遍历Orientation枚举的所有成员
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)
"""
上面程序通过继承 Enum 派生了 Orientation 枚举类,通过这种方式派生的枚举类既可额外定义方法,
如上面的info()方法所示,也可为枚举指定value(value的值默认是1、2、3、 …)。

虽然此时 Orientation 枚举的 value 是 str 类型,但该枚举同样可通过value来访问特定枚举,
如上面程序中的Orientation('南'),这是完全允许的。运行上面代码,可以看到如下输出结果。
"""