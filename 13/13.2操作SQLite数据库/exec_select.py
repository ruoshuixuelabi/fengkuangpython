"""
执行查询依然按照前面介绍的步骤进行,只是改为执行select语句。
由于select语句执行完成后可以得到查询结果,因此程序可通过游标的fetchone()、fetchmany(n)、fetchall()来获取查询结果。
正如它们的名字所暗示的, fetchone()用于获取一条记录, fetchmany(n)用于获取 n 条记录, fetchall()用于获取全部记录。

如下程序示范了如何执行查询语句,并输出查询结果。

由于每条select语句都可能返回多个查询结果,因此不能使用executemany()执行查询语句,这 没什么意义。

注意：不要试图使用 executemany()方法执行 select 语句,否则程序将会报错：
ProgrammingError: executemany() can only execute DML  statements。
"""
# 导入访问SQLite的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用执行select语句查询数据
c.execute('select * from user_tb where _id > ?', (2,))
print('查询返回的记录数:', c.rowcount)
# 通过游标的description属性获取列信息
for col in c.description:
    print(col[0], end='\t')
print('\n--------------------------------')
while True:
    # 获取一行记录,每行数据都是一个元组
    row = c.fetchone()
    # 如果抓取的row为None,退出循环
    if not row:
        break
    print(row)
    print(row[1] + '-->' + row[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
