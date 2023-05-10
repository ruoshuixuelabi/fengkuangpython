"""
下面是该示例的客户端程序。该客户端程序更加简单——客户端程序只需要读取 socket 中的数据,
因此只要使用selectors为 socket注册"有数据可读"事件的监听函数即可。
"""
import selectors, socket, threading

# 创建默认的selectors对象
sel = selectors.DefaultSelector()


# 负责监听“有数据可读”事件的函数
def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print(data.decode('utf-8'))
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('192.168.1.88', 30000))
# 设置该socket是非阻塞的
s.setblocking(False)
# 使用sel为s的EVENT_READ事件注册read监听函数
sel.register(s, selectors.EVENT_READ, read)  # ①


# 定义不断读取用户键盘输入的函数
def keyboard_input(s):
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        # 将用户的键盘输入内容写入socket
        s.send(line.encode('utf-8'))


"""
上面程序中的①号粗体字代码为socket的 EVENT_READ 事件注册了read()监听函数,这样每当socket中有数据可读时,
程序就会触发read()函数来读取socket中的数据。

程序最后也采用死循环不断地调用 selectors的 select()方法"监测"事件,每当监测到相应的事件之后,程序就会调用对应的事件监听函数。

先运行上面的服务器端程序,该程序运行后只是作为服务器,看不到任何输出信息。
再运行多个客户端程序——相当于启动多个聊天室客户端登录该服务器。
接下来可以在任何一个客户端通过键盘输入一些内容,然后按回车键,即可在所有客户端(包括自己)的控制台上接收到刚刚输入的内容。
这也是一个粗略的C/S 结构的聊天室应用。
"""
# 采用线程不断读取用户的键盘输入
threading.Thread(target=keyboard_input, args=(s,)).start()
while True:
    # 获取事件
    events = sel.select()
    for key, mask in events:
        # key的data属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监听函数, key的fileobj属性获取被监听的socket对象
        callback(key.fileobj, mask)
