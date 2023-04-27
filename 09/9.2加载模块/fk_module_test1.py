"""
接下来,在相同的路径下定义如下程序来使用该模块。
由于前面在PYTHONPATH环境变量中已经添加了点(.),因此 Python 程序总可以加载相同
路径下的模块。所以,上面程序可以导入相同路径下的fk module模块。运行上面程序,可以看到 如下输出结果。
"""
import fk_module

print("================")
# 打印fk_module的类型
print(type(fk_module))
print(fk_module)
print(fk_module.name)
print(fk_module.hello)
