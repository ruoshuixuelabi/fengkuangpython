"""
在导入整个模块时可以为模块指定别名。例如如下程序。
"""
# 导入sys整个模块,并指定别名为s
import sys as s

# 使用s模块别名作为前缀来访问模块中的成员
print(s.argv[0])
"""
上面粗体字代码在导入 sys 模块时指定了别名s,因此在程序中使用 sys 模块内的成员时,必须添加模块别名 s 作为前缀。
运行该程序,可以看到如下输出结果。
"""