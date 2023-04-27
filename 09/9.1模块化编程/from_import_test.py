"""
下面程序使用from…import导入模块成员的最简单语法来导入指定成员。
"""
# 导入sys模块的argv成员
from sys import argv
# 使用导入成员的语法,直接使用成员名访问
print(argv[0])
