import sys

# 定义一个字符串列表
my_list = ["Hello", "Python", "Spring"]
# 使用异常处理来遍历arr数组的每个元素
try:
    i = 0
    while True:
        print(my_list[i])
        i += 1
except:
    pass

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
