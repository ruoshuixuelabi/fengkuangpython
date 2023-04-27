"""
1.  将 fk_package 包下的 __init__.py 文件编辑成如下形式。
2.  上面第一行 from.…import 用于导入当前包(模块)中的 print_shape(模块),这样即可在 fk_package 中使用 print_shape 模块。
但这种导入方式是将 print_shape 模块导入了 fk_package 包中, 因此当其他程序使用 print_shape 内的成员时,
依然需要通过 fk_package.print_shape 前缀进行调用。第二行导入语句用于将 .print_shape 模块内的所有程序单元导入
fk_package 模块中,这样以后只要使用 fk_package.前缀就可以使用三个模块内的程序单元。例如如下程序。
"""
# 从当前包导入print_shape模块
from . import print_shape
# 从.print_shape导入所有程序单元到fk_package中
from .print_shape import *
# 从当前包导入billing模块
from . import billing
# 从.billing导入所有程序单元到fk_package中
from .billing import *
# 从当前包导入arithmetic_chart模块
from . import arithmetic_chart
# 从.arithmetic_chart导入所有程序单元到fk_package中
from .arithmetic_chart import *
