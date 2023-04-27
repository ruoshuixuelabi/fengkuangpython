"""
1.  此外,在 os 模块下还包含大量操作文件和目录的功能函数,本书将会在第12章专门介绍这些功能函数。
2.  在 os 模块下还包含各种进程管理函数,它们可用于启动新进程、中止已有进程等。在 os 模块下与进程管理相关的函数如下。
(1)os.abort()：生成一个 SIGABRT 信号给当前进程。在 UNIX 系统上,默认行为是生成内核转储;在Windows 系统上,进程立即返回退出代码3。
(2)os.execl(path,arg0,arg1,…)：该函数还有一系列功能类似的函数,比如os.execle()、os.execlp()等,这些函数都是使用参数列表
arg0,arg1,… 来执行path所代表的执行文件的。
(3)os.forkpty()：fork 一个子进程。
(4)os.kill(pid,sig)：将 sig 信号发送到pid对应的过程,用于结束该进程。
(5)os.killpg(pgid,sig)：将 sig 信号发送到pgid对应的进程组。
(6)os.popen(cmd,mode='r,buffering=-1)：用于向 cmd 命令打开读写管道(当mode 为 r 时为只读管道,当mode 为 rw 时为读写管道),
buffering缓冲参数与内置的open()函数有相同的含义。该函数返回的文件对象用于读写字符串,而不是字节。
(7)os.spawnl(mode,path,…)：该函数还有一系列功能类似的函数,比如os.spawnle()、os.spawnlp()等,这些函数都用于在新进程中执行新程序。
(8)os.startfile(path[,operation])：对指定文件使用该文件关联的工具执行operation对应的操作。
如果不指定operation操作,则默认执行打开(open)操作。 operation参数必须是有效的命令行操作项目,
比如open(打开)、edit(编辑)、print(打印)等。
(9)os.system(command)：运行操作系统上的指定命令。

3.  注意：由于os.exec*()函数都是 POSIX  系统的直接映射,因此如果使用该命令来执行 Python程序,传入的arg0参数没有什么作用。
os._exit(n)用于强制退出Python解释器。 将其放在try块中可以阻止 finally 块的执行。
4.  下面程序示范了在os 模块中与进程管理相关的函数的功能。
5.  在使用 os.execl() 函数运行新进程之后,也会取代原有的进程,因此上面程序将这行代码放在了最后。
"""
import os

# 运行平台上的cmd命令
os.system('cmd')
# 使用Excel打开g：\abc.xls文件
os.startfile('g：\\abc.xls')
os.spawnl(os.P_NOWAIT, 'E：\\Tools\\编辑工具\\Notepad++.7.5.6.bin.x64\\notepad++.exe', ' ')
# 使用python命令执行os_test.py程序
os.execl("D：\\Python\\Python36\\python.exe", " ", 'os_test.py', 'i')
