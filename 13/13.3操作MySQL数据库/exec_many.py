"""
与 SQLite 数据库模块类似的是,
MySQL 数据库模块同样支持使用 executemany() 方法重复执行一条 SQL 语句。例如如下程序。
"""
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = conn = mysql.connector.connect(user='root', password='32147',
                                      host='localhost', port='3306',
                                      database='python', use_unicode=True)
# ②、获取游标
c = conn.cursor()
# ③、调用executemany()方法把同一条SQL语句执行多次
c.executemany('insert into user_tb values(null, %s, %s, %s)',
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
该程序与前面使用 SQLite 数据库模块重复执行SQL 语句的程序基本相同,只是该程序在 SQL 语句中使用了%s 作为占位符。

使用MySQL 数据库模块中游标的executemany(方法同样可重复执行update、delete语句,
在本书配套代码的 codesl13-13.3 目录下可找到一个 executemany_update.py 程序,
该程序使用 executemany()方法重复执行update语句,这完全是允许的。
"""
