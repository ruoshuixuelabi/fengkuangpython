"""
2.3.2 浮点型
1. 浮点型数值用于保存带小数点的数值，Python的浮点数有两种表示形式。
(1)十进制形式：这种形式就是平常简单的浮点数，例如5.12、512.0、0.512。浮点数必须包含一个小数点，否则会被当成整数类型处理。
(2)科学计数形式：例如5.12e2 (即5.12×10²)、5.12E2 (也是5.12×10²)。
2. 必须指出的是，只有浮点型数值才可以使用科学计数形式表示。例如51200是一个整型值，但512E2则是浮点型值。
3. Python不允许除以0。不管是整型值还是浮点型值，Python都不允许除以0
"""
af1 = 5.2345556
# 输出af1的值
print("af1的值为:", af1)
af2 = 25.2345
print("af2的类型为:", type(af2))
f1 = 5.12e2
print("f1的值为:", f1)
# 虽然5e3的值是5000,但它依然是浮点型值,而不是整型值,因为 Python 会自动将该数值变为5000.0
f2 = 5e3
print("f2的值为:", f2)
print("f2的类型为:", type(f2))  # 看到类型为float
