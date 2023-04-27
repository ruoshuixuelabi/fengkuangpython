"""
os.chroot(path): 改变当前进程的根目录。
os.listdir(path): 返回path对应目录下的所有文件和子目录。
os.mkdir(path[,mode]): 创建path对应的目录,其中 mode 用于指定该目录的权限。
该mode 参数代表一个 UNIX  风格的权限,比如 0o777 代表所有者可读/可写/可执行、组用户可读/ 可写/可执行、其他用户可读/可写/可执行。
os.makedirs(path[,mode]): 其作用类似于mkdir(),但该函数的功能更加强大,它可以递归创建目录。
比如要创建 abc/xyz/wawa 目录,如果在当前目录下没有 abc 目录,那么使用 mkdir()函数就会报错,
而使用makedirs()函数则会先创建abc,然后在其中创建 xyz 子目录,最后在xyz 子目录下创建wawa 子目录。

如下程序示范了如何创建目录。
"""
import os

path = 'my_dir'
# 直接在当前目录下创建目录
os.mkdir(path, 0o755)
path = "abc/xyz/wawa"
# 递归创建目录
os.makedirs(path, 0o755)
"""
正如从上面两行粗体字代码所看到的,第一行粗体字代码直接在当前目录下创建 my_dir 子目
录,因此可以使用 mkdir() 函数创建;第二行粗体字代码需要程序递归创建 abc/xyz/wawa 目录,因此使用 makedirs() 函数。

上面程序中第一行粗体字代码直接重命名当前目录下的 my_dir 子目录,程序会将该子目录重命名为your dir;
第二行粗体字代码则执行递归重命名,程序会将 wawa 重命名为 haha, 将 xyz 重命名为bar, 将 abc 重命名为 foo。
"""
