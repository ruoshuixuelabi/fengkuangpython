"""
在使用 from…import 同时导入多个模块成员时也可指定别名,同样使用as 关键字为成员指定 别名,例如如下程序。
"""
# 导入sys模块的argv,winver成员,并为其指定别名v、wv
from sys import argv as v, winver as wv

# 使用导入成员(并指定别名)的语法,直接使用成员的别名访问
print(v[0])
print(wv)
"""
上面粗体字代码导入了 sys 模块中的argv、winver 成员,并分别为它们指定了别名v、wv,
这样即可在程序中通过 v 和 wv 两个别名使用argv、winver 成员,无须使用任何前缀。运行该程序,可以看到如下输出结果。
"""