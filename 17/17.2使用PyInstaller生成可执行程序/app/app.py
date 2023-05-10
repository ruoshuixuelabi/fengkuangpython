"""
17.2	使用PyInstaller生成可执行程序

在创建了独立应用(自包含该应用的依赖包)之后,还可以使用 PyInstaller 将 Python 程序生成可直接运行的程序,
这个程序就可以被分发到对应的 Windows 或 Mac  OS X 平台上运行。

17.2.1	安装PyInstaller

Python 默认并不包含 PyInstaller 模块,因此需要自行安装 PyInstaller 模块。

安装 PyInstaller 模块与安装其他 Python 模块一样,使用 pip 命令安装即可。在命令行输入如下 命令。
pip install pyinstaller

提示：强烈建议使用pip在线安装的方式来安装 PyInstaller 模块,不要使用离线包的方式来安装!
这是因为 PyInstaller 模块还依赖其他模块,因此 pip 在安装 PyInstaller 模块时会先安装它的依赖模块。

运行上面命令,应该看到如下输出结果。
Successfully  installed          pyinstaller-x.x.x
其中的x.x.x代表PyInstaller的版本。

在 PyInstaller 模块安装成功之后,在 Python 的安装目录下的Scripts(D:\Python\Python36\ Scripts)
目录下会增加一个pyinstaller.exe程序,接下来就可以使用该工具将Python程序生成EXE 程序了。

17.2.2	生成可执行程序

Pyinstaller 工具的命令语法如下：
pyinstaller 选 项Python 源文件

不管这个 Python 应用是单文件的应用,还是多文件的应用,只要在使用 pyinstaller 命令时编译作为程序入口的 Python 程序即可。

提示：PyInstaller 工具是跨平台的,它既可以在 Windows 平台上使用,也可以在Mac OS X平台上运行。
在不同的平台上使用 PyInstaller 工具的方法是一样的,它们支持的选项也是一样的。

下面先处理上一节的app 应用,将codes\17\17.1\目录下的app 目录复制到codes\17\17.2
目录下,对codes\17\17.2app\目录下的app.py 文件略做修改,将该文件改成可执行的 Python 程序。例 如如下代码。
"""
from say_hello import *


def main():
    print('程序开始执行')
    print(say_hello('孙悟空'))


# 增加调用main()函数
if __name__ == '__main__':
    main()
"""
接下来使用命令行工具进入codes\17\17.2\app\ 目录下,在该目录下执行如下命令。
pyinstaller  -F       app.py

执行上面命令,将看到详细的生成过程。当生成完成后,将会在codes\17\17.2\app\目录下看到多了一个dist目录,
并在该目录下看到有一个app.exe文件,这就是使用PyInstaller工具生成的 EXE 程序。

在命令行窗口中进入codes\17\17.2\app\dist\目录下,在该目录下执行app.exe,将会看到该程序生成如下输出结果。

提示：由于该程序没有图形用户界面,因此,如果读者试图通过双击来运行该程序,则只能看到程序窗口一闪就消失了,
这样将无法看到该程序的输出结果

在上面命令中使用了-F 选项,该选项指定生成单独的 EXE 文件,因此,在dist目录下生成了一个单独的大约为6MB 的 app.exe文件
(在Mac OS X平台上生成的文件就叫app,没有后缀);与-F 选项对应的是-D 选项(默认选项),该选项指定生成一个目录(包含多个文件)来作为程序。

下面先将 PyInstaller 工具在app 目录下生成的build、dist目录删除,并将app.spec文件也删除, 然后使用如下命令来生成 EXE 文件。
pyinstaller -D app.py

执行上面命令,将看到详细的生成过程。当生成完成后,将会在codes\17\17.2app\
目录下看到多了一个dist目录,并在该目录下看到有一个app 子目录,该子目录的内容如图17.1所示。

从图17.1可以看出,在该子目录下包含了大量 .dll 文件和 .pyz文件,它们都是 app.exe 程序的
支撑文件。在命令行窗口中运行该app.exe程序,同样可以看到与前一个app.exe程序相同的输出结果。

Pyinstaller 不仅支持-F、 -D 选项,而且也支持如表17.1所示的常用选项。

表17.1 Pyinstaller 支持的常用选项
选项	                                    作用
-h,-help	                            查看该模块的帮助信息
-F,-onefile	                        产生单个的可执行文件
-D,--onedir	                        产生一个目录(包含多个文件)作为可执行程序
-a,-ascii	                            不包含Unicode字符集支持
-d,-debug	                        产生debug版本的可执行文件
-w,-windowed,-noconsole	指定程序运行时不显示命令行窗口(仅对Windows有效)
-c,-nowindowed,-console	指定使用命令行窗口运行程序(仅对Windows有效)
-o DIR.-out=DIR	                指定spec文件的生成目录。如果没有指定,则默认使用当前目录来生成spec文件
-p DIR,-path=DIR	            设置Python导入模块的路径(和设置PYTHONPATH环境变量的作用相似)。
也可使用路径分隔符(Windows使用分号,Linux使用冒号)来分隔多个路径
-n NAME,-name=NAME	    指定项目(产生的spec)名字。如果省略该选项,那么第一个脚本的主文件名将作为spec 的名字

在表17.1中列出的只是PyInstaller模块所支持的常用选项,如果需要了解PyInstaller选项的详细信息,则可通过 pyinstaller -h来查看。


"""
