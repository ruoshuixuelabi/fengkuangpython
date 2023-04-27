"""
第12章介绍了使用文件来保存程序状态,这种方式虽然简单、易用,但只适用于保存一些格式简单、数据量不太大的数据。
对于数据量巨大且具有复杂关系的数据,当然还是推荐使用数据库进行保存。

Python 为操作不同的数据库提供了不同的模块。别忘了,Python 的魅力之一就是它的模块,无论你想做什么,总能找到对应的模块。
可能有人会想,世界上那么多数据库,难道使用 Python 操作每个数据库都要学习对应的模块?理论上确实如此,但各位读者不用担心：
这些模块内 API 的设计大同小异,因此掌握 Python 的一个数据库模块之后,再看其他数据库模块时就会有似曾相识的感觉。

为了让读者体会使用Python操作不同数据库的相似性,本章会分别介绍如何使用Python操作 SQLite 内置数据库和开源的 MySQL 数据库。

Python 3.6默认内置了操作SQLite数据库的模块,但如果Python程序需要操作 MySQL 数据库,
则需要自行下载操作 MySQL 数据库的Python模块。

提示 ：世界上的数据库非常多,流行的商业级数据库有Oracle、DB2、SQL Server等,
通常这些数据库厂商都会提供对应的 Python 模块来操作相应的数据库;开源的数据库有 MySQL、PostgreSQL 和 Firebird等,
它们同样会提供对应的 Python模块来操作相应的数据库。
前面提到这些数据库都是关系型数据库,而关系型数据库也不是唯一类型的数据库,目前一些 NoSQL 数据库也比较流行,如MangoDB、Redis 等。

本章主要介绍基于 SQL 的数据库操作方式,但本书并不打算介绍 SQL 的 DDL、DML、查询语句的详细语法,
如果读者需要了解这方面的知识,可参考《疯狂Java讲义》的第13章。

13.1  Python数据库API简介

虽然 Python 需要为操作不同的数据库使用不同的模块,但不同的数据库模块并非没有规律可循——
因为它们基本都遵守Python制订的 DB API 协议,目前该协议的最新版本是2.0,因此这些数据库模块有很多操作其实都是相同的。
下面先介绍不同数据库模块之间的通用内容。

13.1.1	全局变量

Python推荐支持DB API 2.0 的数据库模块都应该提供如下3个全局变量。
(1)apilevel: 该全局变量显示数据库模块的API 版本号。对于支持DB API 2.0版本的数据库模块来说,该变量值通常就是2.0。
如果这个变量不存在,则可能该数据库模块暂时还不支持 DB API 2.0。读者应该考虑选择使用支持该数据库的其他数据库模块。
(2)threadsafety: 该全局变量指定数据库模块的线程安全等级,该等级值为0~3,其中3代表该模块完全是线程安全的;
1表示该模块具有部分线程安全性,线程可以共享该模块,但不能共享连接;0则表示线程完全不能共享该模块。
(3)paramstyle: 该全局变量指定当 SQL 语句需要参数时,可以使用哪种风格的参数。该变量可能返回如下变量值。
①format: 表示在 SQL 语句中使用Python标准的格式化字符串代表参数。
例如,在程序中需要参数的地方使用%s, 接下来程序即可为这些参数指定参数值。
②pyformat: 表示在 SQL 语句中使用扩展的格式代码代表参数。比如使用%(name),
这样即可使用包含key 为 name 的字典为该参数指定参数值。
③qmark: 表示在 SQL 语句中使用问号(?)代表参数。在SQL 语句中有几个参数,全部用问号代替。
④numeric:表示在 SQL 语句中使用数字占位符(:N) 代表参数。
例如：1代表一个参数,:2 也表示一个参数,这些数字相当于参数名,因此它们不一定需要连续。
⑤named: 表示在 SQL 语句中使用命名占位符(:name)代表参数。例如：name 代表一个参数, :age也表示一个参数。

通过查阅这些全局变量,即可大致了解该数据库 API 模块的对外的编程风格,至于该模块内部的实现细节,
完全由该模块实现者负责提供,通常不需要开发者关心。

13.1.2     数据库API 的核心类

遵守DB API 2.0协议的数据库模块通常会提供一个connect()函数,该函数用于连接数据库, 并返回数据库连接对象。

数据库连接对象通常会具有如下方法和属性。
(1)cursor(factory=Cursor): 打开游标。
(2)commit():  提交事务。
(3)rollback(): 回滚事务。
(4)close(): 关闭数据库连接。
(5)isolation_level: 返回或设置数据库连接中事务的隔离级别。
(6)in_transaction: 判断当前是否处于事务中。

上面第一个方法可以返回一个游标对象,游标对象是Python DB API的核心对象,该对象主要用于执行各种 SQL 语句,
包括DDL、DML、select 查询语句等。使用游标执行不同的SQL 语句返回不同的数据。

游标对象通常会具有如下方法和属性。
(1)execute(sql[,parameters]):执行SQL 语句。parameters参数用于为SQL 语句中的参数指定值。
(2)executemany(sql,seq_of_parameters):重复执行 SQL 语句。可以通过 seq_of_parameters 序列为 SQL 语句中的参数指定值,
该序列有多少个元素, SQL 语句被执行多少次。
(3)executescript(sql script):这不是DB API 2.0的标准方法。该方法可以直接执行包含多条SQL 语句的SQL 脚本。
(4)fetchone(): 获取查询结果集的下一行。如果没有下一行,则返回None。
(5)fetchmany(size=cursor.arraysize): 返回查询结果集的下 N 行组成的列表。如果没有更多的数据行,则返回空列表。
(6)fetchall(): 返回查询结果集的全部行组成的列表。
(7)close(): 关闭游标。
(8)rowcount:  该只读属性返回受SQL 语句影响的行数。对于executemany()方法,该方法所修改的记录条数也可通过该属性获取。
(9)lastrowid: 该只读属性可获取最后修改行的rowid。
(10)arraysize:用于设置或获取fetchmany()默认获取的记录条数,该属性默认为1。有些数据库模块没有该属性。
(11)description: 该只读属性可获取最后一次查询返回的所有列的信息。
(12)connection: 该只读属性返回创建游标的数据库连接对象。有些数据库模块没有该属性。

总结来看, Python的 DB API 2.0由一个connect()开始, 一共涉及数据库连接和游标两个核心 API。 它们的分工如下。
(1)数据库连接：用于获取游标、控制事务。
(2)游标：执行各种 SQL 语句。

掌握了上面这些API 之后,接下来可以大致归纳出Python  DB API 2.0 的编程步骤。

13.1.3 操作数据库的基本流程

使用Python DB API 2.0操作数据库的基本流程如下。
①调用 connect()方法打开数据库连接,该方法返回数据库连接对象。
②通过数据库连接对象打开游标。
③使用游标执行 SQL 语句(包括DDL、DML、select查询语句等)。如果执行的是查询语句,则处理查询数据。
④关闭游标。
⑤关闭数据库连接。

13.2 操作SQLite数据库

Python 默认自带了 SQLite 数据库和 SQLite 数据库的API 模块------在Python 安装目录下的 DLLs 子目录中可以看到sqlite3.dlI文件,
该文件就是 SQLite 数据库的核心文件;也可以在 Python 安装目录下的 Lib 目录中看到sqlite3子目录,它就是SQLite 数据库的API 模块。

SQLite 与 Oracle、MySQL 等服务器级的数据库不同, SQLite 只是一个嵌入式的数据库引擎,
专门适用于在资源有限的设备上(如手机、 PDA 等)进行适量数据的存取。

虽然SQLite 支持绝大部分SQL 92语法,也允许开发者使用 SQL 语句操作数据库中的数据,但 SQLite 并不像Oracle、MySQL
等数据库那样需要安装、启动服务器进程, SQLite 数据库只是一 个文件,它不需要服务器进程。

提示：从本质上看, SQLite 的操作方式只是一种更便捷的文件操作。后面会看到,当应用程序创建或打开一个SQLite 数据库时,
其实只是打开一个文件准备读写。因此,有人说 SQLite 有点像Microsoft的 Access, 其实 SQLite 的实际功能要强大得多

下面详细介绍操作SQLite 数据库的情形。在使用SQLite 数据库模块之前,先检查该模块的全局属性。

import sqlite3
print(sqlite3.apilevel)
print(sqlite3.paramstyle)

从上面的输出可以看到,Python 自带的SQLite 数据库模块遵守 DB API 2.0  规范,且该模块要求在 SQL 语句中使用问号作为参数。

13.2.1 创建数据表

程序只要通过数据库连接对象打开游标,接下来就可以用游标来执行DDL 语句 ,DDL 语句负责创建表、修改表或删除表。

使用connect()方法打开或创建一个数据库,例如如下代码。
conn = sqlite3.connect('first.db')

上面代码就用于打开或创建一个 SQLite 数据库。如果first.db文件(该文件就是一个数据库)存在,那么程序就是打开该数据库;
如果该文件不存在,则会在当前目录下创建相应的文件(即对应于数据库)。

上面代码将会在当前目录下创建一个first.db 文件,如果程序希望创建内存中的数据库,则只需将 first.db 改为特殊名称: memory: 即可。

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
上面程序使用①~⑤清晰地标出了使用Python DB API2.0执行数据库访问的步骤。

上面程序中第③步执行了两次,每次分别执行一条create语句,因此该程序执行完成后,将会看到在当前数据库中包含两个数据表：
user_tb 和 order_tb, 且在 order_tb 表中有一个外键列引用 user_tb 表的 id主键列。

程序中第③步使用 execute() 方法执行的就是标准的 DDL 语句,因此,只要读者拥有SQL 语法知识,
就可以使用Python DB API模块来执行这些SQL 语句,非常简单。

SQLite数据库所支持的 SQL 语句与 MySQL 大致相同,开发者完全可以把已有的MySQL 经验"移植"到 SQLite 数据库上。
当然,当Python程序提示某条 SQL 语句有语法错误时,最好先利用SQLite数据库管理工具(下一节介绍)来测试这条语句,
以保证这条 SQL 语句的语法正确。

需要指出的是, SQLite 内部只支持 NULL、INTEGER、REAL(浮点数)、TEXT(文本)和BLOB(大二进制对象)这5种数据类型,
但实际上 SQLite 完全可以接受varchar(n)、char(n)、 decimal(p,s)等数据类型,
只不过SQLite会在运算或保存时将它们转换为上面5种数据类型中相应的类型。

除此之外, SQLite 还有一个特点,就是它允许把各种类型的数据保存到任何类型的字段中,开发者可以不用关心声明该字段所使用的数据类型。
例如,可以把字符串类型的值存入INTEGER类型的字段中,也可以把数值类型的值存入布尔类型的字段中……
但有一种情况例外——被定义为"INTEGER   PRIMARY   KEY"的字段只能存储64位整数,
当使用这种字段保存除整数以外的其他类型的数据时, SQLite 会产生错误。
由于 SQLite 允许在存入数据时忽略底层数据列实际的数据类型,因此在编写建表语句时可以省略数据列后面的类型声明。
例如,对于SQLite数据库如下 SQL 语句也是正确的。
"""