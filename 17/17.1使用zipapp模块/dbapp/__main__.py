"""
17.1.2	创建独立应用

通过上面介绍的方式打包得到的档案包中只有当前项目的 Python 文件,
如果Python应用还需要使用第三方模块和包(比如前面介绍的需要连接 MySQL 的应用),那么仅打包该应用的 Python 程序是不够的。

为了创建能独立启动的应用(自带依赖模块和包),需要执行两步操作。
① 将应用依赖的模块和包下载到应用目录中。
② 使用 zipapp 将应用和依赖模块一起打包成档案包。

下面在 codes\17\17.1 目录下再创建一个 dbapp 子目录,该子目录将会作为本应用的目录。
将 codes\13\13.2 目录下的 exec_select.py 文件拷贝到 dbapp 子目录下,然后对文件中的程序略做修改,
将程序中代码放在 query_db()函数内定义。修改后的 exec_select.py文件被保存在codes\1717.1\dbapp 子目录下。

接下来在codes\17\17.1\dbapp\目录下新建一个 __main__.py 文件作为程序入口,这样程序在打包档案包时就不需要指定程序入口了。

下面是 __main__.py 文件的代码。
"""
from exec_select import *

# 执行query_db()函数
query_db()
"""
最后按照如下步骤将 dbapp 子目录下的应用打包成独立应用。
① 通过命令行工具在codes\17\17.1 目录下执行如下命令。
python  -m  pip  install -r  requirements.txt  --target       dbapp

上面命令实际上就是使用pip模块来安装模块,其中python -m pip install表示要安装模块。
--target 选项指定将模块安装到指定目录下,此处指定将依赖模块安装到 dbapp 子目录下。
-r 选项指定要安装哪些模块,此处使用 requirements.txt 文件列出要安装的模块和包。-r选项支持两个值。
(1)直接指定要安装的模块或包。
(2)使用清单文件指定要安装的模块和包。

当应用依赖的模块较多时,建议使用清单文件来列出所依赖的模块。

如果直接运行上面命令,pip 模块会提示找不到 requirements.txt 文件,因此需要在codes117\17.1
目录下添加一个requirements.txt文件,并在该文件中增加如下一行。
mysql-connector-python

如果项目需要依赖多个模块,则可以在 requirements.xt 文件中定义多行,每行定义一个模块。

重新运行上面命令,将可以看到 pip 开始下载 mysql-connector-python 模块,
下载完成后将可以在 dbapp 子目录下看到大量有关mysql-connector-python模块的文件。
② 如果pip 在 dbapp 子目录下生成了.dist-info 目录,则建议删除该目录。
③ 使用zipapp 模块执行打包操作。由于本例的dbapp 子目录下包含了 __main__.py 文件,该
文件将会作为程序入口,因此打包时不需要指定-m 选项。使用如下命令来打包。
python  -m   zipapp     dbapp

与上一节所使用的命令相比,该命令没有使用 -m 选项来指定程序入口,该程序将会使用档案包中的 main  .py 文件作为程序入口。

运行上面命令,将会得到一个大约为18MB 的档案包。因为该档案包自包含了 mysql-connector-python模块,所以其比较大。

在创建了独立应用之后,只要目标机器上安装了合适版本的Python解释器,即可运行该独立应用。\
我们可以先使用如下命令卸载在Python 目录下安装的mysql-connector-python模块。
pip uninstall mysql-connector-python

此时在本机的 Python 目录下不再包含mysql-connector-python 模块,但dbapp.pyz程序依然可以正常运行——
因为它自包含了mysql-connector-python模块。
"""
