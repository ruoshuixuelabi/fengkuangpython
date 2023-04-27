"""
与使用 SQLite 数据库模块类似, MySQL 数据库模块同样可以使用游标的execute()方法执行 DML 的 insert、update、
delete语句,对数据库进行插入、修改和删除数据操作。

例如,如下程序示范了向数据库的两个数据表中分别插入一条数据。
"""
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = conn = mysql.connector.connect(user='root', password='32147',
                                      host='localhost', port='3306',
                                      database='python', use_unicode=True)
# ②、获取游标
c = conn.cursor()
# ③、调用执行insert语句插入数据
c.execute('insert into user_tb values(null, %s, %s, %s)',
          ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values(null, %s, %s, %s, %s)',
          ('鼠标', '34.2', '3', 1))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
上面程序中两行粗体字代码分别用于向 user_tb 和 order_tb 表中插入数据。
注意该程序的 SQL 语句中的占位符：%s, 这正如 mysql.connector.paramstyle 属性所标识的 pyformat,它指定在 SQL
语句中使用扩展的格式代码来作为占位符。
"""