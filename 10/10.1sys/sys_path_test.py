"""
10.1.2	动态修改模块加载路径
1.  前面介绍了使用 PYTHONPATH 环境变量来添加Python模块的加载路径,但这种方式必须预先设置好。
如果需要在程序运行时动态改变 Python 模块的加载路径,则可通过sys.path 属性来实现。
2.  sys.path也是很有用的一个属性,它可用于在程序运行时为Python动态修改模块加载路径。
例如,如下程序在运行时动态指定加载g:\fk_ext目录下的模块。
"""
import sys
# 动态添加g:\fk_ext路径作为模块加载路径
sys.path.append('g:\\fk_ext')
# 加载g:\fk_ext路径下的hello模块
import hello
