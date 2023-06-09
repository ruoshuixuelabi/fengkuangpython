print("5%3的值为：", 5 % 3)  # 输出2
print("5.2%3.1的值为：", 5.2 % 3.1)  # 输出2.1
print("-5.2%-3.1的值为：", -5.2 % -3.1)  # 输出-2.1
print("5.2%-2.9的值为：", 5.2 % -2.9)  # 输出-0.6
print("5.2%-1.5的值为：", 5.2 % -1.5)  # 输出-0.8
print("-5.2%1.5的值为：", -5.2 % 1.5)  # 输出0.8
# print("5对0.0求余的结果是:", 5 % 0.0) # 导致错误
"""
前三个算式的运行结果比较简单,它们进行的都是很简单的求余计算。
但 5.2 % -2.9 的结果有点奇怪,我们预计它为-0.6,但实际输出的是 -0.5999999999999996。这里有两个问题。
(1)第一个问题：为什么预计 5.2 % -2.9的结果是-0.6呢?因为Python求余运算的逻辑是用被除数减去除数的N 倍,
此处的 N 是 -2,因此得到结果是-0.6。
(2)第二个问题：为什么实际输出的是-0.5999999999999996呢?这是由浮点数的存储机制导致的。
计算机底层的浮点数的存储机制并不是精确保存每一个浮点数的值,读者暂时不需要花太多的时间去理解浮点数的存储机制,
只要知道浮点数在 Python 中可能产生精度丢失的问题部行。
比如此处正常计算的结果应该是-0.6,但实际计算出来的结果是一个非常接近 -0.6的值。
"""
