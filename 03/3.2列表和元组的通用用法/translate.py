"""
当然,也可以对列表、元组同时进行加法、乘法运算。例如,把用户输入的日期翻译成英文表示形式——
就是添加英文的"第"后缀。对于1、2、3来说,英文的"第"后缀分别用st、nd、rd 代表,其他则使用th代表。

为此,可使用如下代码来完成该转换。
"""
# 同时对元组使用加法、乘法
order_endings = ('st', 'nd', 'rd') \
                + ('th',) * 17 + ('st', 'nd', 'rd') \
                + ('th',) * 7 + ('st',)
# 将会看到st、nd、rd、17个th、st、nd、rd、7个th、st
print(order_endings)
day = input("输入日期(1-31)：")
# 将字符串转成整数
day_int = int(day)
print(day + order_endings[day_int - 1])
"""
上面粗体字代码同时对('th',)元组使用了乘法,再将乘法得到的结果使用加法连接起来,最终得到一个元组,该元组共有31个元素。

可能有读者对(th',)这种写法感到好奇,此处明明只有一个元素,为何不省略逗号?这是因为 ('th')只是字符串加上圆括号,
并不是元组,也就是说, ('th')和'th'是相同的。为了表示只有一个元素的元组,必须在唯一的元组元素之后添加英文逗号。
"""
