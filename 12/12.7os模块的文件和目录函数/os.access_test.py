"""
12.7.2 与权限相关的函数

与权限相关的函数如下。
os.access(path,mode)：检查 path 对应的文件或目录是否具有指定权限。该函数的第二个参数可能是以下四个状态值的一个或多个值。
(1)os.F_OK：判断是否存在。
(2)os.R_OK：判断是否可读。
(3)os.W_OK：判断是否可写。
(4)os.X_OK：判断是否可执行。

例如如下程序。
"""
import os

# 判断当前目录的权限
ret = os.access('.', os.F_OK | os.R_OK | os.W_OK | os.X_OK)
print("os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值:", ret)
# 判断os.access_test.py文件的权限
ret = os.access('os.access_test.py', os.F_OK | os.R_OK | os.W_OK)
print("os.F_OK|os.R_OK|os.W_OK - 返回值:", ret)
"""
上面程序判断当前目录的权限和 os.access_test.py文件的权限,这里特意将 os.access_test.py文件设为只读的。
运行该程序,可以看到如下输出结果。
"""
