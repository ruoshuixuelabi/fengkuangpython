"""
1.  如果需要使用 arithmetic_chart、billing和 print_shape这三个模块,则可以在程序中执行如下导入代码
2.  上面程序中第一行粗体字代码是"import fk package",由于导入包的本质只是加载并执行包里的 __init__.py 文件,
因此执行这条导入语句之后,程序只能使用 fk_package 目录下的 __init__.py 文件中定义的程序单元。
对于本例而言,由于fk_package\__init__.py文件内容为空,因此这条导入语 句没有任何作用。
3.  第二行粗体字代码是"import fk_package.print_shape",这条导入语句的本质就是加载并执行 fk_package 包下的 print_shape.py文件,
并将其赋值给 fk_package.print_shape 变量。因此执行这条 导入语句之后,程序可访问
fk_package\print_shape.py 文件所定义的程序单元,但需要添加 fk_package.print_shape 前缀。
4.  第三行粗体字代码是"from fk_package import billing",
这条导入语句的本质是导入 fk_package 包(也是模块)下的billing成员(其实是模块)。
因此执行这条导入语句之后,程序可使用 fk_package\billing.py文件定义的程序单元,而且只需要添加billing前缀。
5.  第四行粗体字代码与第二行粗体字代码的导入效果相同。
6.  该程序后面分别测试了 fk_package 包下的 print_shape、billing、arithmetic_chart这三个模块的功能。
运行上面程序,可以看到三个模块的功能完全可以正常显示。
7.  上面程序虽然可以正常运行,但此时存在两个问题。
(1)为了调用包内模块中的程序单元,需要使用很长的前缀,这实在是太麻烦了。
(2)包内 __init__.py 文件的功能完全被忽略了。
8.  想一想就知道：包内的 __init__.py 文件并不是用来定义程序单元的,而是用于导入该包内模块的成员,
这样即可把模块中的成员导入变成包内成员,以后使用起来会更加方便。
"""
# 导入fk_package包,实际上就是导入包下 __init__.py文件
import fk_package
# 导入fk_package包下的 print_shape 模块,
# 实际上就是导入fk_package目录下的print_shape.py
import fk_package.print_shape
# 实际上就是导入fk_package包（模块）导入print_shape模块
from fk_package import billing
# 导入fk_package包下的arithmetic_chart模块,
# 实际上就是导入fk_package目录下的 arithmetic_chart.py
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)
