"""
下面程序使用from…import导入模块成员的最简单语法来导入指定成员。
"""
# 导入sys模块的argv成员
from sys import argv

# 使用导入成员的语法,直接使用成员名访问
print(argv[0])
"""
上面粗体字代码导入了sys 模块中的argv 成员,这样即可在程序中直接使用argv成员,无须使用任何前缀。运行该程序,可以看到如下输出结果。
"""