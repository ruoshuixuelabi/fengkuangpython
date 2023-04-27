"""
需要说明的是, MySQL 数据库模块的连接对象有一个 autocommit 属性,如果将该属性设为 True,
则意味着关闭该连接的事务支持,程序每次执行 DML 语句之后都会自动提交,这样程序就无须调用连接对象的commit()方法来提交事务了。
例如如下程序。
"""
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = conn = mysql.connector.connect(user='root', password='32147',
                                      host='localhost', port='3306',
                                      database='python', use_unicode=True)
# 将autocommit设置True,关闭事务
conn.autocommit = True
# ②、获取游标
c = conn.cursor()
# ③、调用执行insert语句插入数据
c.execute('insert into user_tb values(null, %s, %s, %s)', ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values(null, %s, %s, %s, %s)', ('鼠标', '34.2', '3', 1))
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
"""
在上面程序中,将连接对象的 autocommit 设为True, 这意味着该连接将会自动提交每条 DML 语句,
相当于关闭了事务,所以程序也不需要调用连接对象的 commit()方法来提交事务。
"""