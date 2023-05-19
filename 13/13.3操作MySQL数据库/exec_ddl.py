"""
13.3.2	使用pip 工具管理模块

前面在介绍安装 MySQL 服务器时,已经选择安装 MySQL 提供的 Python 数据库模块,而且根据最后的安装提示,显示已经安装成功。

问题是：我们有没有办法来查看是否已经安装成功了呢?或者说,如果在安装 MySQL 服务器时忘记了选择Connector/Python模块,
现在是否还有补救措施?答案是肯定的。

Python自带了 一 个pip 工具用来查看、管理所安装的各种模块。

1. 查看已安装的模块
查看已安装的模块,使用如下命令。

pip    show   packagename

启动命令行窗口,在窗口中输入如下命令。
pip      show      mysql-connector-python

在上面的命令中, mysql-connector-python 就是该模块的名字。运行该命令,可以看到如下输出结果。

从上面的输出结果可以看到,已经成功安装了mysql-connector-python 8.0.11.1 Python的 GUI 库, 以及该模块的官方网址和安装路径等有用的信息。

2. 卸载已安装的模块

卸载已安装的模块,使用如下命令。
pip      uninstall  packagename

在命令行窗口中输入如下命令。
pip  uninstall mysql-connector-python

运行该命令,可以看到如下输出结果。

上面的提示信息询问是否要删除 mysql-connector-python模块,如果删除该模块,将会删除3个目录。
如果希望删除,则可以在输入"y"之后按回车键。接下来将看到系统提示如下信息。
Successfully     uninstalled   mysql-connector-python-8.0.11.1 Python的 GUI 库

该信息显示mysql-connector-python-8.0.11被删除成功。

执行该删除命令后, Python 将不再包含 mysql-connector-python 模块,相当于在安装 MySQL 服务器时没有选择Connector/Python模块。

如果要查看已安装的所有模块,可以使用如下命令。
pip    list

3. 安装模块
安装模块,使用如下命令。
pip      install      packagename
在命令行窗口中输入如下命令。
pip     install    mysql-connector-python

运行该命令,将看到程序下载并安装 mysql-connector-python 模块的过程,最后会生成如下提 示信息。

Successfully             installed             mysql-connector-python-8.0.11.1 Python的 GUI 库

上面的信息提示该模块安装成功。

如果希望安装不同版本的模块,则可指定版本号。例如：
pip            install           packagename            ==1.0.4           #安装指定版本
提示：除使用MySQL官方提供的Python模块来连接MySQL数据库之外,还有一个使用广泛的连接MySQL 数据库的模块：
MySQL-python, 其官方站点为https://pypi.org/project/MySQL-python/。

13.3.3	执行DDL语句

在使用mysql-connector-python模块操作 MySQL  数据库之前,同样先检查一下该模块的全局属性。

从上面的输出信息可以看到, mysql-connector-python数据库模块同样遵守DB API 2.0规范, 且该模块允许在SQL 语句中使用扩展的格式代码 (pyformat) 来代表参数。
使用MySQL  模块对MySQL  数据库执行 DDL 语句,与使用SQLite 模块对SQLite 数据库执行 DDL 语句并没有太大的区别,
只是MySQL  数据库有服务器进程,默认通过3306端口对外提供服务。
因此, Python 程序在连接 MySQL  数据库时可指定远程服务器IP 地址和端口,如果不指定服务器 IP 地址和端口,
则使用默认的服务器IP 地 址localhost和默认端口3306。

下面程序示范了如何连接MySQL  数据库,并通过DDL 语句来创建两个数据表。
"""
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = conn = mysql.connector.connect(user='root', password='32147',
                                      host='localhost', port='3306',
                                      database='python', use_unicode=True)
# ②、获取游标
c = conn.cursor()
# ③、执行DDL语句创建数据表
c.execute('''create table user_tb(
	user_id int primary key auto_increment,
	name varchar(255),
	pass varchar(255), 
	gender varchar(255))''')
# 执行DDL语句创建数据表
c.execute('''create table order_tb(
	order_id integer primary key auto_increment,
	item_name varchar(255),
	item_price double,
    item_number double,
	user_id int,
    foreign key(user_id) references user_tb(user_id) )''')
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
