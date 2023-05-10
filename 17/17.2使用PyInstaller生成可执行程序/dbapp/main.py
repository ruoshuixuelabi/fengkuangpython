"""
下面再创建一个带图形用户界面,可以访问 MySQL 数据库的应用程序。

在 codes\17\17.2\目录下创建一个 dbapp 目录,并在该目录下创建 Python 程序,其中 exec_select.py 程序负责查询数据,
main.py 程序负责创建图形用户界面来显示查询结果。
这两个程序在前面章节中已有详细介绍,此处不再给出,读者可通过本书配套代码中的codes\17\17.2\dbapp目录来查看这两个程序。

通过命令行工具进入codes\17\17.2\dbapp\目录下,在该目录下执行如下命令。
PyInstaller -F     -w  main.py

上面命令中的-F 选项指定生成单个的可执行程序,-w 选项指定生成图形用户界面程序(不需要命令行界面)。
运行上面命令,该工具同样在codes\17\17.2\dbapp\目录下生成了一个dist子目录,并在该子目录下生成了一个main.exe文件。

直接双击运行main.exe程序(该程序有图形用户界面,因此可以双击运行),将可以看到如图 17.2所示的运行结果。

提示：上面程序的运行结果需要查询 MySQL 的 python 数据库中的user_tb数据表。简单来说,该程序的运行结果依赖本书13.3节插入的数据。

17.3 本章小结

本章主要介绍了两种打包Python 程序的工具：zipapp和 PyInstaller。
zipapp 主要用于将Python 应用打包成一个.pyz 文件。
不管开发 Python 应用时有多少个源文件或多少个依赖包,使用 zipapp 都可以将它们打包成一个.pyz 文件,该文件依然需要Python 环境来执行。PyInstaller则直接将Python 程序打包成可执行程序,而且该工具还是跨平台的,因此使用非常方便。使用PyInstaller打包出来 的程序,完全可以被分发到对应平台的目标机器上直接运行,无须在目标机器上安装 Python 解 释 器环境。
本章练习
1. 将第11章介绍的桌面弹球游戏打包成可执行的Python 档案包。
2. 使 用PyInstaller将第11章介绍的五子棋游戏生成可执行程序。
"""
from exec_select import *
from tkinter import *


def main():
    description, rows = query_db()
    # 创建窗口
    win = Tk()
    win.title('数据库查询')
    # 通过description获取列信息
    for i, col in enumerate(description):
        lb = Button(win, text=col[0], padx=50, pady=6)
        lb.grid(row=0, column=i)
    # 直接使用for循环查询得到的结果集
    for i, row in enumerate(rows):
        for j in range(len(row)):
            en = Label(win, text=row[j])
            en.grid(row=i + 1, column=j)
    win.mainloop()


if __name__ == '__main__':
    main()
