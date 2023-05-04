"""
4.4.8  for 表达式

for表达式用于利用其他区间、元组、列表等可迭代对象创建新的列表。for表达式的语法格式如下：
[表达式 for 循环计数器 in 可迭代对象]

从上面的语法格式可以看出,for表达式与普通for循环的区别有两点。
(1)在for关键字之前定义一个表达式,该表达式通常会包含循环计数器。
(2)for表达式没有循环体,因此不需要冒号。

for表达式当然也是有循环的,它同样会对可迭代对象进行循环------可迭代对象包含几个对象,
该循环就对for之前的"表达式"执行几次(相当于for之前的表达式就是循环体),并将每次执行的值收集起来作为新的列表元素。

for表达式最终返回的是列表,因此for表达式也被称为列表推导式。

如果将 for 表达式的方括号改为圆括号,for表达式将不再生成列表,而是生成一个生成器(generator), 该生成器同样可使用for循环迭代。

对于使用圆括号的for表达式,它最终返回的是生成器,因此这种for表达式也被称为生成器推导式。
"""
a_range = range(10)
# 对a_range执行for表达式
a_list = [x * x for x in a_range]
# a_list集合包含10个元素
print(a_list)
# 还可以在for表达式后面添加if条件,这样for表达式将只迭代那些符合条件的元素。例如如下代码
b_list = [x * x for x in a_range if x % 2 == 0]
# a_list集合包含5个元素
print(b_list)
# 如果将 for 表达式的方括号改为圆括号,for 表达式将不再生成列表,而是生成一个生成器(generator),该生成器同样可使用 for 循环迭代。
# 对于使用圆括号的for表达式,它最终返回的是生成器,因此这种for表达式也被称为生成器推导式。例如如下代码。
# 使用for表达式创建生成器
c_generator = (x * x for x in a_range if x % 2 == 0)
# 使用for循环迭代生成器
for i in c_generator:
    print(i, end='\t')
print()
# 在前面看到的 for 表达式都只有一个循环,实际上 for 表达式可使用多个循环,就像嵌套循环一样。例如如下代码。
d_list = [(x, y) for x in range(5) for y in range(4)]
# d_list列表包含20个元素
print(d_list)
dd_list = []
for x in range(5):
    for y in range(4):
        dd_list.append((x, y))
print(dd_list)

e_list = [[x, y, z] for x in range(5) for y in range(4) for z in range(6)]
# 3_list列表包含120个元素
print(e_list)

src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
# 只要y能整除x,就将它们配对在一起
result = [(x, y) for x in src_b for y in src_a if y % x == 0]
print(result)
