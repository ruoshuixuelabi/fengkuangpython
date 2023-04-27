"""
1.  random 模块主要包含生成伪随机数的各种功能变量和函数。
2.  在 Python 的交互式解释器中先导入 random 模块,然后输入random.__all__ 命令( __all__ 变量代表了该模块开放的公开接口),
即可看到该模块所包含的全部属性和函数。
3.  开发者同样不需要完全记住这些属性和函数的含义,在使用时可参考 https://docs.python.org/3/library/random.html。
4.  在random 模块下提供了如下常用函数。
(1)random.seed(a=None,version=2)：指定种子来初始化伪随机数生成器。
(2)random.randrange(start,stop[,step])：返回从start开始到stop结束、步长为step的随机数。
其实就相当于choice(range(start,stop,step)的效果,只不过实际底层并不生成区间对象。
(3)random.randint(a,b)：生成一个范围为a≤N≤b 的随机数。其等同于randrange(a,b+1)的效果。
(4)random.choice(seq)：从 seq 中随机抽取一个元素,如果 seq 为空,则引发IndexError异常。
(5)random.choices(seq,weights=None,*,cum_weights=None,k=1)：从 seq 序列中抽取k 个元素,
还可通过weights指定各元素被抽取的权重(代表被抽取的可能性高低)。
(6)random.shuffle(x[,random])：对x序列执行洗牌"随机排列"操作。
(7)random.sample(population,k)：从 population序列中随机抽取 k 个独立的元素。
(8)random.random()：生成一个从0.0(包含)到1.0(不包含)之间的伪随机浮点数。
(9)random.uniform(a,b)：生成一个范围为a≤N≤b 的随机数。
(10)random.expovariate(lambd)：生成呈指数分布的随机数。其中lambd参数(其实应该是lambda,
只是lambda 是 Python 关键字,所以简写成lambd) 为1除以期望平均值。
如果 lambd 是正值,则返回的随机数是从0到正无穷大;如果lambd 为负值,则返回的随机数是从负无穷大到0。

5.  提示：关于生成伪随机浮点数的函数,Python 还提供了random.triangular(low,high, mode)、random.gauss(mu,sigma)等,
它们用于生成呈对称分布、高斯分布的随机数。由于这种随机数需要一些数学知识来理解它们,而且平时开发并不常用,
因此这里就不深入展开介绍了。
6.  下面程序示范了random 模块中常见函数的功能和用法。
"""
import random

# 生成范围为0.0≤x<1.0的伪随机浮点数
print(random.random())
# 生成范围为2.5≤x<10.0的伪随机浮点数
print(random.uniform(2.5, 10.0))
# 生成呈指数分布的伪随机浮点数
print(random.expovariate(1 / 5))
# 生成从0到9的伪随机整数
print(random.randrange(10))
# 生成从0到100的随机偶数
print(random.randrange(0, 101, 2))
# 随机抽取一个元素
print(random.choice(['Python', 'swift', 'Kotlin']))
book_list = ['Python', 'swift', 'Kotlin']
# 对列表元素进行随机排列
random.shuffle(book_list)
print(book_list)
# 随机抽取4个独立的元素
print(random.sample([10, 20, 30, 40, 50], k=4))
