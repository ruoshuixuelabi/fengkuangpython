"""
然后在该目录下开发一个app-py程序来使用say hello模块。
"""
from say_hello import *


def main():
    print('程序开始执行')
    print(say_hello('孙悟空'))


"""
在命令行工具中进入 codes\17\17.1 目录下,然后执行如下命令。

python -m   zipapp   app -o   first.pyz   -m  "app:main"

上面命令指定将当前目录下的 app 子目录下的所有 Python 源文件打包成一个档案包,
并通过 -o 选项指定所生成的档案包的文件名为first.pyz;-m选项指定使用app.py模块中的 main 函数作为程序入口。

运行上面命令,将会生成一个first.pyz文件。接下来可以使用python命令来运行first.pyz文件。
python first.pyz
程序开始执行
孙悟空,您好！

通过命令行工具在codes\17\17.1 目录下执行如下命令。
python   -m     zipapp     app     -m     "app:main"
上面命令没有指定-o 选项,这意味着该命令将会使用默认的输出文件名： source参数值加.pyz 后缀。运行上面命令,将会在当前目录下生成一个app.pyz文件。
"""
