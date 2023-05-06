"""
在使用from…import导入模块成员时也可同时导入多个成员,例如如下程序。
"""
# 导入sys模块的argv,winver成员
from sys import argv, winver

# 使用导入成员的语法,直接使用成员名访问
print(argv[0])
print(winver)
"""
上面粗体字代码导入了sys 模块中的argv、winver 成员,这样即可在程序中直接使用argv、winver 两个成员,无须使用任何前缀。
运行该程序,可以看到如下输出结果(sys 的 winver 成员记录了该 Python 的版本号)。
"""