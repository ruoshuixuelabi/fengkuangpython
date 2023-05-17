"""
假如程序要把 deque 当成队列使用,则意味着一端只用来添加元素,另一端只用来删除元素,因此调用append、popleft方法即可。
例如如下程序。
"""
from collections import deque

q = deque(('Kotlin', 'Python'))
# 元素加入队列
q.append('Erlang')
q.append('Swift')
print('q中的元素：', q)
# 元素出队列,先添加的元素先出队列
print(q.popleft())
print(q.popleft())
print(q)
"""
从上面的运行结果可以看出,程序先添加的元素"Kotlin"最先出队列,这体现了队列的FIFO的特征。
"""
