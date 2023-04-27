"""
虽然上面程序演示的是使用 executemany()重复执行 insert语句,但实际上程序完全可以使用 executemany()重复执行
update语句或delete语句,只要其第二个参数是一个序列,序列的每个元素都可对被执行SQL 语句的参数赋值即可。
如下程序示范了如何重复执行update语句。
"""
# 导入访问SQLite的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用executemany()方法把同一条SQL语句执行多次
c.executemany('update user_tb set name=? where _id=?',
              (('小孙', 2),
               ('小白', 3),
               ('小猪', 4),
               ('小牛', 5),
               ('小唐', 6)))
# 通过rowcount获取被修改的记录条数
print('修改的记录条数：', c.rowcount)
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
正如从上面粗体字代码所看到的,此时使用 executemany()执行的update语句中包含两个参数,
因此调用 executemany()方法的第二个参数是一个元组,该元组中的每个元素只包含两个元素,
这两个元素就用于为update语句中的两个"?"占位符赋值。

上面程序还使用游标的rowcount 属性来获取update语句所修改的记录条数。

运行上面程序,可以看到user_tb表中 id 为2~6的记录的name 都被修改了。
"""