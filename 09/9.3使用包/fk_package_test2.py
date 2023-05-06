# 导入fk_package包,实际上就是导入包下__init__.py文件
import fk_package

# 直接使用fk_package前缀即可调用它所包含的模块内的程序单元。
fk_package.print_blank_triangle(5)
im = fk_package.Item(4.5)
print(im)
fk_package.print_multiple_chart(5)
"""
上面粗体字代码是导入 fk_package 包,导入该包的本质就是导入该包下的 __init__.py文件。
而 __init__.py文件又执行了导入,它们会把三个模块内的程序单元导入 fk_package 包中,
因此程序的下面代码可使用 fk_package. 前缀来访问三个模块内的程序单元。
运行上面程序,同样可以看到正常的运行结果。
"""