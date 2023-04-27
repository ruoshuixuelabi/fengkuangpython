"""
13.3.5	执行查询语句

使用 MySQL  数据库模块执行查询语句,与使用SQLite 数据库模块执行查询语句基本相似,只需注意SQL 语句中的占位符的差别即可。
例如,如下程序示范了查询MySQL  数据库中的数据。
"""
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = conn = mysql.connector.connect(user='root', password='32147',
                                      host='localhost', port='3306',
                                      database='python', use_unicode=True)
# ②、获取游标
c = conn.cursor()
# ③、调用执行select语句查询数据
c.execute('select * from user_tb where user_id > %s', (2,))
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
# 直接使用for循环来遍历游标中的结果集
for row in c:
    print(row)
    print(row[1] + '-->' + row[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
上面程序中的粗体字代码调用execute()方法执行select语句查询数据,在该 SQL 语句中同样使用了%s作为占位符,
这就是与SQLite 数据库模块的差别。

该程序直接使用for循环来遍历游标所包含的查询数据,这完全是可以的——因为游标本身就是可遍历对象。
运行上面的程序,可以看到如下查询结果。

MySQL  数据库模块的游标对象同样支持fetchone()、fetchmany()、fetchall(方法,
在本书配套代码的codes13-13.3 目录下可以看到一个exec_select2.py程序,该程序使用fetchmany(3))方法每次获取3条记录。
"""