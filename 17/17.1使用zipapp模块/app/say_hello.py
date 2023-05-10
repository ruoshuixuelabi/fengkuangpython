"""
经过复杂的开发、调试之后,终于得到一个 Python 程序,这个程序或许精巧,或许有些古拙,
但它是我们心血的结晶,我们当然希望将这个程序发布出来。本章将会介绍两个常用的发布工具：zipapp 和 PyInstaller

zipapp模块可用于生成可执行的 Python 档案包,这个档案包会包含目录下所有的Python程序。
如果使用 pip 工具先将 Python 程序所依赖的模块下载到目标目录下,那么就可以生成可独立运行的 Python程序——
只要目标机器上安装有Python解释器环境即可。

PyInstaller 工具则更强大,它可以直接将 Python 程序编译成 Windows、Mac OS X 平台上的可执行程序,
这种可执行程序可直接被分发到其他Windows、Mac OS X 计算机上,而无须在这些机器上安装 Python 环境。

17.1  使用 zipapp 模块

Python 提供了一个 zipapp 模块,通过该模块可以将一个Python模块(可能包含很多个源程序)打包成一个Python应用,
甚至发布成一个Windows 的可执行程序。

17.1.1	生成可执行的Python档案包

zipapp 是一个可以直接运行的模块,该模块用于将单个 Python 文件或整个目录下的所有文件打包成可执行的档案包。该模块的命令行语法如下：
python -m    zipapp source  [options]

在上面命令中,source 参数代表要打包的 Python 源程序或目录,该参数既可以是单个的 Python 文件,也可以是文件夹。
如果 source 参数是文件夹,那么 zipapp 模块会打包该文件夹中的所有 Python 文件。

该命令的options支持如下选项。
-o <output>,--output=<output>：该选项指定输出档案包的文件名。如果不指定该选项,
所生成的档案包的文件名默认为 source 参数值,并加上 .pyz 后缀。
-p <interpreter>,--python=<interpreter>：该选项用于指定Python解释器。
-m<mainfn>,--main=<mainfn>：该选项用于指定 Python 程序的入口函数。该选项应该为pkg.mod:fn形式,
其中pkg.mod是一个档案包中的包或模块,fn 是指定模块中的函数。如果不指定该选项,则默认从模块中的 __main__.py 文件开始执行。
-c,-compress：从 Python 3.7 开始支持该选项。该选项用于指定是否对档案包进行压缩来减小文件的大小,默认是不压缩。
--info：该选项用于在诊断时显示档案包中的解释器。
-h,--help：该选项用于显示 zipapp 模块的帮助信息。

下面在codes\17\17.1 目录下建立一个 app 子目录,该子目录用于包含多个Python程序。首先在该目录下开发一个 say_hello.py 程序。
"""


def say_hello(name):
    return name + ",您好！"
