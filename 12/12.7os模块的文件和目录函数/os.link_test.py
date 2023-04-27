"""
os.fdopen(fd[,mode[,bufsize]]): 通过文件描述符fd打开文件,并返回对应的文件对象。
os.closerange(fd_low,fd_high): 关闭从fd_low(包含)到fd_high (不包含)范围的所有文件描述符。
os.dup(fd):  复制文件描述符。
os.dup2(fd,fd2):  将一个文件描述符fd 复制到另一个文件描述符 fd2 中 。
os.ftruncate(fd,length): 将 fd 对应的文件截断到length长度,因此此处传入的length参数不应该超过文件大小。
os.remove(path):删除path对应的文件。如果path 是一个文件夹,则抛出 OSError 错误。 如果要删除目录,则使用os.rmdir()。
os.link(src,dst): 创建从src到 dst的硬链接。硬链接是UNIX 系统的概念,如果在Windows 系统中就是复制目标文件。
os.symlink(src,dst): 创建从src到 dst的符号链接,对应于Windows 的快捷方式。

提示：由于Windows 权限的缘故,因此必须以管理员身份执行os.symlink()函数来创建快捷方式。

下面程序示范了在Windows 系统中使用os.symlink(src,dst)函数来创建快捷方式。
"""
import os

# 为os.link_test.py文件创建快捷方式
os.symlink('os.link_test.py', 'tt')
# 为os.link_test.py文件创建硬连接（Windows上就是复制文件）
os.link('os.link_test.py', 'dst')