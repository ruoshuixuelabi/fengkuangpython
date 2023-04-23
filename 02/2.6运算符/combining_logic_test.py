"""
1. 有些时候，程序需要使用多个逻辑运算符来组合复杂的逻辑。
例如，假设想表达如下逻辑：需 要购买一本书名必须以 "Python"结尾的图书，且图书价格小于50元或该图书是基于正式版的。
2. 编译、运行下面程序，可以看到程序输出"打算购买这本Python图书"。那么下面程序是否有问题呢?
其实问题是存在的，这是因为程序会先计算bookName.endswith('Python') and price<50,  
即使该逻辑表达式中的两个条件都是 False, 但只要后面的version =="正式版"返回True, 
整个表达式就会返回True, 从而导致程序依然会输出"打算购买这本Python 图书"
因此，即使把下面程序中的bookName改为不以"Python"结尾，程序也依然会输出"打算购买这本Python图书"。
3. 运算结果显然与逻辑需求并不一致，逻辑需求是：需要购买一本书名以"Python"结尾的图书。
 此时应该使用圆括号来保证程序先对 price<50 ll version ="正式版"求值，然后再与 ookName.endswith('Python')的结果求与。
因此，应该把程序改为如下形式(程序清单同上)。
"""
# bookName = "疯狂Python"
# price = 79
# version = "正式版"
# if bookName.endswith('Python') and price < 50 or version == "正式版" ：
#    print("打算购买这本Python图书")
# else：
#	print("不购买！")

bookName = "疯狂Python"
price = 79
version = "正式版"
if bookName.endswith('Python') and (price < 50 or version == "正式版"):
    print("打算购买这本Python图书")
else:
    print("不购买！")
