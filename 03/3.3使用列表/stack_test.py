"""
1.  pop()方法用于实现元素出栈功能。栈是一种特殊的数据结构，它可实现先入后出(FILO)功能，即先加入栈的元素，反而后出栈。
2.  在其他编程语言所实现的"栈"中，往往会提供一个push()方法，用于实现入栈操作，
但Python 的列表并没有提供push()方法，我们可以使用append()方法来代替push()方法实现入栈操作。
3.  与所有编程语言类似的是，出栈操作既会移出列表的最后一个元素，也会返回被移出的元素。
"""
stack = []
# 向栈中“入栈”3个元素
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")
print(stack)  # ['fkit', 'crazyit', 'Charlie']
# 第一次出栈：最后入栈的元素被移出栈
print(stack.pop())
print(stack)  # ['fkit', 'crazyit']
# 再次出栈
print(stack.pop())
print(stack)  # ['fkit']
