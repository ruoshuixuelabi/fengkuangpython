"""
2.4.4 使用input 和 该raw_input 获取用户输入
1. input()函数用于向用户生成一条提示，然后获取用户输入的内容。
由于input()函数总会将用户输入的内容放入字符串中，因此用户可以输入任何内容，input()函数总是返回一个字符串。
2. 从下面的运行过程可以看出，无论输入哪种内容，始终可以看到input()函数返回字符串，程序总会将用户输入的内容转换成字符串。
3. 需要指出的是，Python 2.x提供了一个 raw_input()函数，该raw_input()函数就相当于Python 3.x中的input()函数。
4. 而 Python 2.x也提供了一个input()函数，该input()函数则比较怪异：要求用户输入的必须是符合Python 语法的表达式。
通常来说，用户只能输入整数、浮点数、复数、字符串等。重点是格式必须正确，比如输入字符串时必须使用双引号，否则 Python 就会报错。
5. 在Python 2.x中应该尽量使用 raw_input()函数来获取用户输入;Python 2.x中 的 raw_input()等同于Python 3.x中 的input()。
"""
msg = input("请输入你的值：")
print(type(msg))
print(msg)
