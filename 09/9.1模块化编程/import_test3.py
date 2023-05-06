"""
使用导入整个模块的语法也可一次导入多个模块,多个模块之间用逗号隔开。例如如下程序。
"""
# 导入sys、os两个模块
import sys, os

# 使用模块名作为前缀来访问模块中的成员
print(sys.argv[0])
# os模块的sep变量代表平台上的路径分隔符
print(os.sep)
"""
上面粗体字代码一次导入了 sys 和 os 两个模块,因此程序要使用sys、os 两个模块内的成员,
只要分别使用sys、os模块名作为前缀即可。
在Windows 平台上运行该程序,可以看到如下输出结果 (os 模块的sep 变量代表平台上的路径分隔符)。
import_test3.py
\
"""