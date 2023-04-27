"""
1.  下面程序示范了优先使用运行程序的指定参数,然后是系统环境变量,最后才使用系统默认值的实现,程序同样将这三个搜索范围链成ChainMap。
"""
from collections import ChainMap
import os, argparse

# 定义默认参数
defaults = {'color': '蓝色', 'user': 'yeeku'}
# 创建程序参数解析器
parser = argparse.ArgumentParser()
# 为参数解析器添加-u（--user）和-c（--color）参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
# 解析运行程序的参数
namespace = parser.parse_args()
# 将程序参数转换成dict
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# 将command_line_args(解析程序参数而来)、os.environ(环境变量)、defaults链成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
# 获取color对应的value
print(combined['color'])
# 获取user对应的value
print(combined['user'])
# 获取PYTHONPATH对应的value
print(combined['PYTHONPATH'])
"""
1.  上面程序将 command_line_args、os.environ、defaults 链成ChainMap,其中 command_line_args 由程序参数解析而来,它的优先级最高。
2.  假如使用如下命令来运行该程序
python  ChainMap_test3.py  -c 红色 -u  Charlie
3.  由于上面命令指定了-c(对应于color) 和-u(对应于user) 参数,在命令行指定的参数的优先级是最高的,因此可以看到如下输出结果。
红色
Charlie
.;d:\python_module

上面输出的最后一行是PYTHONPATH 环境变量的值。

如果使用如下命令来运行该程序。

python  ChainMap_test3.py
由于上面命令没有指定任何命令行参数,因此程序访问user、color时将会使用defaults字典中 key 对应的值,所以可以看到如下输出结果。
蓝色
yeeku
D:/pycharm_display

"""
