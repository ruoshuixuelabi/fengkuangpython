"""
2.2.2   使用 print 函数输出变量

前面使用 print() 函数时都只输出了一个变量,但实际上 print() 函数完全可以同时输出多个变量,而且它具有更多丰富的功能。
print() 函数的详细语法格式如下：
print(value,...,sep=' ',end='\n',file=sys.stdout,flush=False)

从上面的语法格式可以看出,value 参数可以接受任意多个变量或值,因此 print() 函数完全可以输出多个值。例如如下代码。
"""
user_name = 'Charlie'
user_age = 8
# 同时输出多个变量和字符串
print("读者名:", user_name, "年龄:", user_age)
# 从输出结果来看,使用 print() 函数输出多个变量时,print() 函数默认以空格隔开多个变量,
# 如果读者希望改变默认的分隔符,可通过sep 参数进行设置。例如输出语句：
# 同时输出多个变量和字符串,指定分隔符
print("读者名:", user_name, "年龄:", user_age, sep='|')
# 在默认情况下,print()函数输出之后总会换行,这是因为print()函数的end 参数的默认值是"\n", 这个"\n"就代表了换行。
# 如果希望print()函数输出之后不会换行,则重设end 参数即可,例如如下代码。
# 指定end参数,指定输出之后不再换行
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
# file参数指定 print() 函数的输出目标, file 参数的默认值为 sys.stdout,该默认值代表了系统标准输出,也就是屏幕,
# 因此print()函数默认输出到屏幕。实际上,完全可以通过改变该参数让print()函数输出到特定文件中,例如如下代码。
f = open("poem.txt", "w", encoding="utf-8")  # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()
"""
运行上面代码,可以看到如下输出结果。
读者名: Charlie 年龄: 8

从输出结果来看,使用print()函数输出多个变量时,print()函数默认以空格隔开多个变量,
如果读者希望改变默认的分隔符,可通过 sep 参数进行设置。例如输出语句：
print("读者名:", user_name, "年龄:", user_age, sep='|')
运行上面代码,可以看到如下输出结果。
读者名:|Charlie|年龄:|8

在默认情况下,print()函数输出之后总会换行,这是因为print()函数的end 参数的默认值是"\n",这个"\n"就代表了换行。
如果希望print()函数输出之后不会换行,则重设end 参数即可,例如如下代码。
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")

上面三条print()语句会执行三次输出,但由于它们都指定了end="",因此每条print()语句的输出都不会换行,依然位于同一行。
运行上面代码,可以看到如下输出结果。
40 	50 	60 	

file参数指定print()函数的输出目标,file 参数的默认值为sys.stdout,该默认值代表了系统标准输出,
也就是屏幕,因此print()函数默认输出到屏幕。实际上,完全可以通过改变该参数让 print() 函数输出到特定文件中,例如如下代码。
f = open("poem.txt", "w", encoding="utf-8")  # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()

提示：上面程序中的 open()函数用于打开一个文件,本书第12章还会详细介绍关于文件操作的内容。
 
print() 函数的 fush 参数用于控制输出缓存,该参数一般保持为False即可,这样可以获得较好的性能。
"""
