"""
13.3.2	使用 pip 工具管理模块

前面在介绍安装 MySQL 服务器时,已经选择安装 MySQL 提供的 Python 数据库模块,而且根据最后的安装提示,显示已经安装成功。

问题是：我们有没有办法来查看是否已经安装成功了呢?或者说,如果在安装 MySQL 服务器时忘记了选择Connector/Python模块,
现在是否还有补救措施?答案是肯定的。

Python 自带了一个 pip 工具用来查看、管理所安装的各种模块。

1. 查看已安装的模块
查看已安装的模块,使用如下命令。

pip  show packagename

启动命令行窗口,在窗口中输入如下命令。
pip show mysql-connector-python

在上面的命令中, mysql-connector-python 就是该模块的名字。运行该命令,可以看到如下输出结果。
Name: mysql-connector-python
Version: 8.0.33
Summary: MySQL driver written in Python
Home-page: http://dev.mysql.com/doc/connector-python/en/index.html
Author: Oracle and/or its affiliates
Author-email:
License: GNU GPLv2 (with FOSS License Exception)
Location: d:\python\lib\site-packages
Requires: protobuf
Required-by:

从上面的输出结果可以看到,已经成功安装了 mysql-connector-python 8.0.33 Python的 GUI 库,
以及该模块的官方网址和安装路径等有用的信息。

2. 卸载已安装的模块

卸载已安装的模块,使用如下命令。
pip uninstall  packagename

在命令行窗口中输入如下命令。
pip  uninstall mysql-connector-python

运行该命令,可以看到如下输出结果。

上面的提示信息询问是否要删除 mysql-connector-python 模块,如果删除该模块,将会删除3个目录。
如果希望删除,则可以在输入"y"之后按回车键。接下来将看到系统提示如下信息。
Successfully uninstalled   mysql-connector-python-8.0.11.1 Python的 GUI 库

该信息显示mysql-connector-python-8.0.11被删除成功。

执行该删除命令后,Python 将不再包含 mysql-connector-python 模块,相当于在安装 MySQL 服务器时没有选择Connector/Python模块。

如果要查看已安装的所有模块,可以使用如下命令。
pip list

3. 安装模块
安装模块,使用如下命令。
pip install packagename

在命令行窗口中输入如下命令。
pip install  mysql-connector-python

运行该命令,将看到程序下载并安装 mysql-connector-python 模块的过程,最后会生成如下提 示信息。
Successfully  installed  mysql-connector-python-8.0.11.1 Python 的 GUI 库
上面的信息提示该模块安装成功。

如果希望安装不同版本的模块,则可指定版本号。例如：
pip   install  packagename ==1.0.4           #安装指定版本
提示：除使用 MySQL 官方提供的 Python 模块来连接 MySQL 数据库之外,还有一个使用广泛的连接 MySQL 数据库的模块：
MySQL-python,其官方站点为 https://pypi.org/project/MySQL-python/。(官网看了一下14年之后就不维护了)

13.3.3	执行DDL语句

在使用 mysql-connector-python 模块操作 MySQL  数据库之前,同样先检查一下该模块的全局属性。
import mysql.connector
mysql.connector.apilevel
'2.0'
mysql.connector.paramstyle
'pyformat'

从上面的输出信息可以看到,mysql-connector-python 数据库模块同样遵守 DB API 2.0 规范,
且该模块允许在 SQL 语句中使用扩展的格式代码(pyformat)来代表参数。

使用 MySQL 模块对 MySQL 数据库执行 DDL 语句,与使用 SQLite 模块对 SQLite 数据库执行 DDL 语句并没有太大的区别,
只是 MySQL 数据库有服务器进程,默认通过 3306 端口对外提供服务。因此,Python 程序在连接 MySQL
数据库时可指定远程服务器 IP 地址和端口,如果不指定服务器 IP 地址和端口,则使用默认的服务器IP 地 址localhost和默认端口3306。

下面程序示范了如何连接 MySQL  数据库,并通过 DDL 语句来创建两个数据表。
"""
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = mysql.connector.connect(user='root', password='32147',
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
"""
与连接 SQLite 的程序相比,上面程序最大的区别就在于那行粗体字代码：
程序要连接 localhost 主机上3306端口服务的 python 数据库,必须先在本机的 MySQL 数据库服务器中创建一个 python 数据库。

上面程序中的①~⑤步与前面并无区别,程序在第③步执行了两次,每次分别执行一条 create 语句。
因此,该程序执行完成后,将会看到当前数据库中包含两个数据表：user_tb和 order_tb,
且在 order_tb表中有一个外键列引用了 user_tb 表的 user_id 主键列。

需要指出的是,此处程序使用 execute()方法执行的 create 语句与前面操作 SQLite 数据库时所使用的 create 语句略有差异,
但这个差异是由两个数据库本身所引起的,与 Python 程序并没有任何关系。

如果 Python 程序提示某条 SQL 语句有语法错误,则最好先利用此处介绍的 MySQL 的命令行客户端测试这条 SQL 语句,
以保证该语句的语法正确。

提示：同一条 SQL 语句,在有的数据库上可能是成功的,而在其他数据库上可能会失败,
这是由于不同数据库所支持的 SQL 虽然大体是相同的,但在实现细节上略有差异。
"""