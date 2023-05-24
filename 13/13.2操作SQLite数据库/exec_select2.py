"""
上面程序使用 fetchone()方法每次获取一条记录,这是比较常见的做法。

实际上,程序也可以使用 fetchmany(n)或 fetchall()方法一次获取多条记录。例如,可将上面程序中的粗体字代码改为如下形式。
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
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
while True:
    # 每次抓取3条记录,该方法返回一个由3条记录组成的列表
    rows = c.fetchmany(3)
    # 如果抓取的rows为None,退出循环
    if not rows:
        break
    # 再次使用循环遍历获取的列表
    for r in rows:
        print(r)
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
上面程序使用 fetchmany(3)每次获取3条记录,该方法返回由3条记录组成的列表,因此程序还需要遍历该列表才能取出每条记录。

一般来说,在程序中应该尽量避免使用 fetchall()来获取查询返回的全部记录。这是因为程序可能并不清楚实际查询会返回多少条记录,
如果查询返回的记录数量太多,那么调用 fetchall()一次获取全部记录可能会导致内存开销过大,情况严重时可能导致系统崩溃。
"""
