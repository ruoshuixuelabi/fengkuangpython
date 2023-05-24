"""
执行查询依然按照前面介绍的步骤进行,只是改为执行 select 语句。
由于 select 语句执行完成后可以得到查询结果,因此程序可通过游标的 fetchone()、fetchmany(n)、fetchall() 来获取查询结果。
正如它们的名字所暗示的,fetchone()用于获取一条记录,fetchmany(n)用于获取 n 条记录,fetchall()用于获取全部记录。

如下程序示范了如何执行查询语句,并输出查询结果。
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
"""
上面程序使用 execute()方法执行了一条 select 语句,接下来程序使用循环,通过游标的 description 属性获取查询的列信息,
也可以通过游标来获取查询结果,如上面程序中的粗体字代码所示。
查询返回的记录数: -1
_id	name	pass	gender	
--------------------------------
(3, '小白', '123456', 'female')
小白-->123456
(4, '小猪', '123456', 'male')
小猪-->123456
(5, '小牛', '123456', 'male')
小牛-->123456
(6, '小唐', '123456', 'male')
小唐-->123456
(7, '武松', '3444', 'male')
武松-->3444
(8, '林冲', '44444', 'male')
林冲-->44444
(9, '孙悟空', '123456', 'male')
孙悟空-->123456

从上面的运行结果来看,程序返回了所有 id 大于2的记录,这就是上面程序查询所返回的结果。

由于每条 select 语句都可能返回多个查询结果,因此不能使用 executemany()执行查询语句,这没什么意义。

注意：不要试图使用 executemany()方法执行 select 语句,否则程序将会报错：
ProgrammingError: executemany() can only execute DML  statements。
"""