"""
1. 通过sys 模块的argv 属性可获取运行Python 程序的命令行参数。 argv 属性值是一个列表,其列表元素和运行参数的关系如图10.1所示。
2. 因此,如果需要获取运行Python 程序时传入的参数,可以通过argv[1]、argv[2]……来获取。 例如下面程序。
3. 上面程序是最简单的"HelloWorld"级的程序,只是这个程序增加了输出 argv 列表的长度、遍历 argv 列表元素的代码。
4. 使用"python argv_test.py"命令运行上面程序,可以看到如下输出结果。
5. 此时看到 argv 列表的长度为1,argv的第一个元素就是被运行的Python 程序。
6.  如果某个参数本身包含了空格,则应该将该参数用双引号("")括起来;否则, Python 会把这个空格当成参数分隔符,而不是参数本身。
例如,采用如下命令来运行上面程序。 python   argv_test.py   "Python  Swift"
可以看到argv 列表的长度是2,第一个列表元素是被运行的Python 程序,第二个列表元素的 值是"Python Swift"。
"""
from sys import argv

# 输出argv列表的长度
print(len(argv))
# 遍历argv列表的每个元素
for arg in argv:
    print(arg)
