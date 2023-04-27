"""
os.rmdir(path): 删除 path 对应的空目录。如果目录非空,则抛出一个OSError 异常。程序可以先用os.remove()函数删除文件。
os.removedirs(path): 递归删除目录。其功能类似于 rmdir(), 但该函数可以递归删除 abc/xyz/wawa 目录,
它会从wawa 子目录开始删除,然后删除xyz 子目录,最后删除abc 目录。

如下程序示范了如何删除目录。
"""
import os

path = 'my_dir'
# 直接删除当前目录下的子目录
os.rmdir(path)
path = "abc/xyz/wawa"
# 递归删除子目录
os.removedirs(path)
"""
上面程序中第一行粗体字代码使用 rmdir() 函数删除当前目录下的 my_dir 子目录,该函数不会执行递归删除;
第二行粗体字代码使用 removedirs()函数删除 abc/xyz/wawa 目录,该函数会执行递归删除,
它会先删除 wawa 子目录,然后删除 xyz 子目录,最后才删除 abc 目录。
"""