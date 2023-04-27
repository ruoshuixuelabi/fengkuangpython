"""
os.chmod(path,mode):更改权限。其中 mode 参数代表要改变的权限,该参数支持的值可以是以下一个或多个值的组合。
·  stat.S_IXOTH: 其他用户有执行权限。
·  stat.S_IWOTH: 其他用户有写权限。
·  stat.S_IROTH: 其他用户有读权限。
·  stat.S_IRWXO: 其他用户有全部权限。
·  stat.S_IXGRP: 组用户有执行权限。
·  stat.S_IWGRP: 组用户有写权限。
·  stat.S_IRGRP: 组用户有读权限。
·  stat.S_IRWXG:  组用户有全部权限。
·  stat.S_IXUSR: 所有者有执行权限。
·  stat.S_IWUSR: 所有者有写权限。
·  stat.S_IRUSR: 所有者有读权限。
·  stat.S_IRWXU: 所有者有全部权限。
·  stat.S_IREAD:Windows  将该文件设为只读的。
·  stat.S_IWRITE:Windows  将该文件设为可写的。
提示：前面的那些权限都是UNIX 文件系统下有效的概念, UNIX 文件系统下的文件有一个所有者,
跟所有者处于同一组的其他用户被称为组用户。因此在 UNIX 文件系统下允许为不同用户分配不同的权限。

"""
import os, stat

# 将os.chmod_test.py文件改为只读
os.chmod('os.chmod_test.py', stat.S_IREAD)
# 判断是否可写
ret = os.access('os.chmod_test.py', os.W_OK)
print("os.W_OK - 返回值:", ret)
