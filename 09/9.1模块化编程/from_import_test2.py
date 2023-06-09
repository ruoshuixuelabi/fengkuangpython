"""
使用from…import导入模块成员时也可为成员指定别名,例如如下程序。
"""
# 导入sys模块的argv成员,并为其指定别名v
from sys import argv as v

# 使用导入成员(并指定别名)的语法,直接使用成员的别名访问
print(v[0])
"""
上面粗体字代码导入了sys 模块中的 argv 成员,并为该成员指定别名v,
这样即可在程序中通过别名v 使用 argv 成员,无须使用任何前缀。运行该程序,可以看到如下输出结果。
"""