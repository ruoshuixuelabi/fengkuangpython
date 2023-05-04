# 下面定义了3个test()函数,但函数的形参列表不同
# 系统可以区分它们,这被称为函数重载
def test():
    print("无参数的test()函数")


# 该函数类型为(String): Unit
def test(msg):
    print("重载的test()函数", msg)


# 该函数类型为(Int): String
def test(msg):
    print("重载的test()函数%s,带返回值" % msg)
    return "test"


## 调用test()时没有传入参数,因此系统调用上面没有参数的test()函数
# test()
# 调用带String参数的test()函数
test("fkjava")
# 调用带Int参数的test()函数,该函数返回字符串
rt = test(30)
print(rt)
