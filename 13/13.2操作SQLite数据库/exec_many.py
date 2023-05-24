"""
如果程序使用 executemany() 方法,则可以多次执行同一条 SQL 语句。例如如下程序
"""
# 导入访问SQLite的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用executemany()方法把同一条SQL语句执行多次
c.executemany('insert into user_tb values(null, ?, ?, ?)',
              (('sun', '123456', 'male'),
               ('bai', '123456', 'female'),
               ('zhu', '123456', 'male'),
               ('niu', '123456', 'male'),
               ('tang', '123456', 'male')))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
上面粗体字代码调用 executemany() 方法执行一条 insert 语句,但调用该方法的第二个参数是一个元组,
该元组的每个元素都代表执行该 insert 语句一次,在执行 insert 语句时这些元素负责为该语句中的"?"占位符赋值。

运行上面程序,将向 user_tb 数据表中插入5条数据。打开 SQLite Expert, 可以看到如图13.7 所示的数据。
"""