"""
同时,在导入多个模块时也可以为模块指定别名,例如如下程序。
"""
# 导入sys、os两个模块,并为sys指定别名s,为os指定别名o
import sys as s, os as o

# 使用模块别名作为前缀来访问模块中的成员
print(s.argv[0])
print(o.sep)
"""
上面粗体字代码一次导入了 sys 和 os 两个模块,并分别为它们指定别名为s、o,
因此程序可以通过s、o 两个前缀来使用sys、os 两个模块内的成员。在 Windows 平台上运行该程序,可以看到如下输出结果。
"""