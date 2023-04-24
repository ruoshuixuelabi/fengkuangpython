"""
1.	在某些情况下,程序需要在定义函数时为一个或多个形参指定默认值——
这样在调用函数时就可以省略为该形参传入参数值,而是直接使用该形参的默认值。
2.	为形参指定默认值的语法格式如下：
			形参名=默认值
3.	从上面的语法格式可以看出,形参的默认值紧跟在形参之后,中间以英文"="隔开。例如,如下程序为name、message 形参指定了默认值。
4.  下面程序中在定义 say_hi() 函数时为name、message 形参指定了默认值,
因此程序中第二行粗体字代码调用say hi()函数时没有为name、message 参数指定参数值,此时name、message 参数将会使用其默认值；
程序第二次调用say hi()函数时为name 参数(使用位置参数)指定了参数值,
5.  此时message参数将会使用默认值；
程序第三次调用 say hi() 函数时为name、message 参数(使用 位置参数)都指定了参数值,因此这两个参数都使用开发者传入的参数值；
程序第四次调用 say hi() 函数时只为message参数(使用关键字参数)传入了参数值,此时name 参数将使用默认值。
6.  因为Python规定：关键字参数必须位于位置参数的后面。因此提示错误： positional argument follows keyword argument。
"""


# 为两个参数指定默认值
def say_hi(name="孙悟空", message="欢迎来到疯狂软件"):
    print(name, ", 您好")
    print("消息是：", message)


# 全部使用默认参数
say_hi()
# 只有message参数使用默认值
say_hi("白骨精")
# 两个参数都不使用默认值
say_hi("白骨精", "欢迎学习Python")
# 只有name参数使用默认值
say_hi(message="欢迎学习Python")

say_hi("欢迎学习Python")

# say_hi(name="白骨精", "欢迎学习Python")

# say_hi("欢迎学习Python" , name="白骨精")

say_hi("白骨精", message="欢迎学习Python")
say_hi(name="白骨精", message="欢迎学习Python")
