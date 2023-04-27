"""
同时,在导入多个模块时也可以为模块指定别名,例如如下程序。
"""
# 导入sys、os两个模块,并为sys指定别名s,为os指定别名o
import sys as s, os as o

# 使用模块别名作为前缀来访问模块中的成员
print(s.argv[0])
print(o.sep)
