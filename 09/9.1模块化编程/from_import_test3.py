"""
在使用from…import导入模块成员时也可同时导入多个成员，例如如下程序。
"""
# 导入sys模块的argv,winver成员
from sys import argv, winver

# 使用导入成员的语法,直接使用成员名访问
print(argv[0])
print(winver)
