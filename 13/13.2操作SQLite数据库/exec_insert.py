"""
13.2.3	使用序列重复执行DML语句

使用游标的execute()方法也可以执行 DML 的 insert、update、delete语句,这样即可对数据库执行插入、修改和删除数据操作。

例如,如下程序示范了向数据库的两个数据表中分别插入一条数据。
"""
# 导入访问SQLite的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用执行insert语句插入数据
c.execute('insert into user_tb values(null, ?, ?, ?)', ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values(null, ?, ?, ?, ?)', ('鼠标', '34.2', '3', 1))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
上面程序与exec_ddl.py程序基本相同,只是程序调用execute()方法执行的不是 DDL 语句,而是 insert语句,这样程序即可向数据表中插入数据。

由于Python 的 SQLite 数据库 API 默认是开启了事务的,因此必须调用上面程序中的粗体字代码来提交事务;
否则,程序对数据库所做的修改(包括插入数据、修改数据、删除数据)不会生效。

运行上面程序,将会向first.db数据库的两个数据表中各插入一条数据。打开SQLite Expert, 可以看到如图13.6所示的数据。
"""