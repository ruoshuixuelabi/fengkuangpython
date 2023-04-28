"""
index() 方法则用于定位某个元素在列表中出现的位置,如果该元素没有出现,则会引发 ValueError 错误。
在使用 index() 方法时还可传入 start、end 参数,用于在列表的指定范围内搜索元素。如下代码示范了index()方法的用法。
"""
a_list = [2, 30, 'a', 'b', 'crazyit', 30]
# 定位元素30的出现位置
print(a_list.index(30))  # 1
# 从索引2处开始、定位元素30的出现位置
print(a_list.index(30, 2))  # 5
# 从索引2处到索引4处之间定位元素30的出现位置,找不到该元素
print(a_list.index(30, 2, 4))  # ValueError
