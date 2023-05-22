import os

path = 'my_dir'
# 直接重命名当前目录下的子目录
os.rename(path, 'your_dir')
path = "abc/xyz/wawa"
# 递归重命名子目录
os.renames(path, 'foo/bar/haha')
"""
上面程序中第一行粗体字代码直接重命名当前目录下的 my_dir 子目录,程序会将该子目录重命名为 your_dir;
第二行粗体字代码则执行递归重命名,程序会将 wawa 重命名为haha,将 xyz 重命名为 bar,将 abc 重命名为 foo。
"""
