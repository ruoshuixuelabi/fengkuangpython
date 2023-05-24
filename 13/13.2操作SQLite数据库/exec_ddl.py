"""
13.2 操作SQLite数据库

Python 默认自带了 SQLite 数据库和 SQLite 数据库的 API 模块------在 Python 安装目录下的 DLLs 子目录中可以看到 sqlite3.dlI 文件,
该文件就是 SQLite 数据库的核心文件;也可以在 Python 安装目录下的 Lib 目录中看到 sqlite3 子目录,它就是 SQLite 数据库的API 模块。

SQLite 与 Oracle、MySQL 等服务器级的数据库不同,SQLite 只是一个嵌入式的数据库引擎,
专门适用于在资源有限的设备上(如手机、 PDA 等)进行适量数据的存取。

虽然 SQLite 支持绝大部分SQL 92语法,也允许开发者使用 SQL 语句操作数据库中的数据,但 SQLite 并不像Oracle、MySQL
等数据库那样需要安装、启动服务器进程, SQLite 数据库只是一 个文件,它不需要服务器进程。

提示：从本质上看, SQLite 的操作方式只是一种更便捷的文件操作。后面会看到,当应用程序创建或打开一个SQLite 数据库时,
其实只是打开一个文件准备读写。因此,有人说 SQLite 有点像 Microsoft 的 Access, 其实 SQLite 的实际功能要强大得多

下面详细介绍操作 SQLite 数据库的情形。在使用 SQLite 数据库模块之前,先检查该模块的全局属性。

import sqlite3
print(sqlite3.apilevel)
2.0
print(sqlite3.paramstyle)
qmark

从上面的输出可以看到,Python 自带的SQLite 数据库模块遵守 DB API 2.0  规范,且该模块要求在 SQL 语句中使用问号作为参数。

13.2.1 创建数据表

程序只要通过数据库连接对象打开游标,接下来就可以用游标来执行DDL 语句 ,DDL 语句负责创建表、修改表或删除表。

使用connect()方法打开或创建一个数据库,例如如下代码。
conn = sqlite3.connect('first.db')

上面代码就用于打开或创建一个 SQLite 数据库。如果first.db文件(该文件就是一个数据库)存在,那么程序就是打开该数据库;
如果该文件不存在,则会在当前目录下创建相应的文件(即对应于数据库)。

上面代码将会在当前目录下创建一个 first.db 文件,如果程序希望创建内存中的数据库,则只需将 first.db 改为特殊名称: memory:即可。

如下程序示范了如何创建数据表。
"""
# 导入访问SQLite的模块
import sqlite3

print(sqlite3.apilevel)
print(sqlite3.paramstyle)
# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、执行DDL语句创建数据表
c.execute('''create table user_tb(
	_id integer primary key autoincrement,
	name text,
	pass text, 
	gender text)''')
# 执行DDL语句创建数据表
c.execute('''create table order_tb(
	_id integer primary key autoincrement,
	item_name text,
	item_price real,
    item_number real,
	user_id inteter,
    foreign key(user_id) references user_tb(_id) )''')
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
上面程序使用①~⑤清晰地标出了使用 Python DB API 2.0执行数据库访问的步骤。

上面程序中第③步执行了两次,每次分别执行一条 create 语句,因此该程序执行完成后,将会看到在当前数据库中包含两个数据表：
user_tb 和 order_tb,且在 order_tb 表中有一个外键列引用 user_tb 表的 id主键列。

程序中第③步使用 execute()方法执行的就是标准的 DDL 语句,因此,只要读者拥有 SQL 语法知识,
就可以使用 Python DB API 模块来执行这些 SQL 语句,非常简单。

SQLite 数据库所支持的 SQL 语句与 MySQL 大致相同,开发者完全可以把已有的 MySQL 经验"移植"到 SQLite 数据库上。
当然,当Python程序提示某条 SQL 语句有语法错误时,最好先利用SQLite数据库管理工具(下一节介绍)来测试这条语句,
以保证这条 SQL 语句的语法正确。

需要指出的是,SQLite 内部只支持 NULL、INTEGER、REAL(浮点数)、TEXT(文本)和BLOB(大二进制对象)这5种数据类型,
但实际上 SQLite 完全可以接受varchar(n)、char(n)、 decimal(p,s)等数据类型,
只不过 SQLite 会在运算或保存时将它们转换为上面5种数据类型中相应的类型。

除此之外,SQLite 还有一个特点,就是它允许把各种类型的数据保存到任何类型的字段中,开发者可以不用关心声明该字段所使用的数据类型。
例如,可以把字符串类型的值存入 INTEGER 类型的字段中,也可以把数值类型的值存入布尔类型的字段中……
但有一种情况例外——被定义为"INTEGER PRIMARY KEY"的字段只能存储64位整数,
当使用这种字段保存除整数以外的其他类型的数据时,SQLite 会产生错误。

由于 SQLite 允许在存入数据时忽略底层数据列实际的数据类型,因此在编写建表语句时可以省略数据列后面的类型声明。
例如,对于 SQLite 数据库如下 SQL 语句也是正确的。
create table my_test
(
id  integer primary key autoincrement,
name,
pass,
gender
);
"""
