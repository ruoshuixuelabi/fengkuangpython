"""
1.  此外,deque 还有一个rotate()方法,该方法的作用是将队列的队尾元素移动到队头,使之首尾相连。例如如下程序。
2.  从上面的输出结果来看,每次执行rotate()方法,deque 的队尾元素都会被移到队头,这样就形成了首尾相连的效果。
"""
from collections import deque

q = deque(range(5))
print('q中的元素：', q)
# 执行旋转,使之首尾相连
q.rotate()
print('q中的元素：', q)
# 再次执行旋转,使之首尾相连
q.rotate()
print('q中的元素：', q)
