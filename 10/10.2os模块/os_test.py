"""
10.2	os模块

os 模块代表了程序所在的操作系统,主要用于获取程序运行所在操作系统的相关信息。

在 Python 的交互式解释器中先导入 os 模块,然后输入os.__all__ 命令(__all__ 变量代表了该模块开放的公开接口),
即可看到该模块所包含的全部属性和函数。开发者同样不需要完全记住这些属性和函数的含义,
在需要用时可参考 https://docs.python.org/3/library/os.html。
os.__all__
['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', 'defpath', 'name', 'path', 'devnull', 'SEEK_SET', 'SEEK_CUR', 'SEEK_END',
 'fsencode', 'fsdecode', 'get_exec_path', 'fdopen', 'extsep', '_exit', 'DirEntry', 'F_OK', 'O_APPEND', 'O_BINARY', 'O_CREAT',
 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY',
 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'R_OK', 'TMP_MAX',
 'W_OK', 'X_OK', 'abort', 'access', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'device_encoding', 'dup', 'dup2', 'environ',
 'error', 'execv', 'execve', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size',
 'getcwd', 'getcwdb', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'link', 'listdir', 'lseek', 'lstat', 'mkdir', 'open', 'pipe', 'putenv',
 'read', 'readlink', 'remove', 'rename', 'replace', 'rmdir', 'scandir', 'set_handle_inheritable', 'set_inheritable', 'spawnv',
 'spawnve', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'symlink', 'system', 'terminal_size', 'times', 'times_result',
 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'write',
 'makedirs', 'removedirs', 'renames', 'walk', 'execl', 'execle', 'execlp', 'execlpe', 'execvp', 'execvpe', 'getenv',
 'supports_bytes_environ', 'spawnl', 'spawnle', 'popen']

此处仅介绍 os 模块中常用的属性和函数。
(1)os.name：返回导入依赖模块的操作系统名称,通常可返回'posix'、'nt'、java'等值其中之一。
(2)os.environ：返回在当前系统上所有环境变量组成的字典。
(3)os.fsencode(filename)：该函数对类路径(path-like)的文件名进行编码。
(4)os.fsdecode(filename)：该函数对类路径(path-like)的文件名进行解码。
(5)os.PathLike：这是一个类,代表一个类路径(path-like)对象。
(6)os.getenv(key,default=None)：获取指定环境变量的值。
(7)os.getlogin()：返回当前系统的登录用户名。与该函数对应的还有os.getuid()、os.getgroups()、os.getgid()等函数,
用于获取用户ID、 用户组、组ID 等,这些函数通常只在 UNIX 系统上有效。
(8)os.getpid()： 获取当前进程ID。
(9)os.getppid()： 获取当前进程的父进程ID。
(10)os.putenv(key,value)：该函数用于设置环境变量。
(11)os.cpu_count()：返回当前系统的 CPU 数量。
(12)os.sep：返回路径分隔符。
(13)os.pathsep：返回当前系统上多条路径之间的分隔符。一般在 Windows 系统上多条路径之间的分隔符是英文分号(;);
在UNIX及类UNIX系统(如Linux、Mac  OS X)上多条路径之间的分隔符是英文冒号(:)。
(14)os.linesep：返回当前系统的换行符。 一般在 Windows 系统上换行符是"\r\n";在 UNIX 系统上换行符是"\n";
在 Mac  OSMac  OS X系统上换行符是"\r"。
(15)os.urandom(size)：返回适合作为加密使用的、最多由 N 个字节组成的bytes对象。
该函数通过操作系统特定的随机性来源返回随机字节,该随机字节通常是不可预测的,因此适用于绝大部分加密场景。

下面程序示范了os 模块的大部分函数的用法。
"""
import os
# 显示导入依赖模块的操作系统的名称
print(os.name)
# 获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))
# 返回当前系统的登录用户名
print(os.getlogin())
# 获取当前进程ID
print(os.getpid())
# 获取当前进程的父进程ID
print(os.getppid())
# 返回当前系统的CPU数量
print(os.cpu_count())
# 返回路径分隔符
print(os.sep)
# 返回当前系统的路径分隔符
print(os.pathsep)
# 返回当前系统的换行符
print(os.linesep)
# 返回适合作为加密使用的、最多3个字节组成的bytes
print(os.urandom(3))
"""
从上面的输出结果可以看出,在 Windows 系统上 Python 导入依赖模块的操作系统名称为"nt";
当前系统的登录用户名是"yeeku";当前进程ID 为"3788";当前进程的父进程ID 为"9908";当前系统上有4个CPU;
当前系统(Windows)的路径分隔符是"\";当前系统(Windows)上多条路径之间的分隔符是分号(;);
但在当前系统(Windows)上换行符不能明显看到,这是因为当在 控制台输出"\r\n"时会产生两个空行。
"""