"""
15.3.7	selectors模块

前面介绍的 socket 都是采用阻塞方式进行通信的,当程序调用 recv() 方法从 socket 中读取数据时,
如果没有读取到有效的数据,当前线程就会被阻塞。为了解决这个问题,上面程序采用了多线程并发编程：
服务器端为每个客户端连接都启动一个单独的线程,不同的线程负责对应的 socket 的通信工作。

通过 selectors 模块允许 socket 以非阻塞方式进行通信：selectors 相当于一个事件注册中心,
程序只要将 socket 的所有事件注册给 selectors 管理,当 selectors 检测到 socket 中的特定事件之后,程序就调用相应的监听方法进行处理。

selectors主要支持两种事件。
(1)selectors.EVENT_READ：当 socket 有数据可读时触发该事件。当有客户端连接进来时也会触发该事件。
(2)selectors.EVENT_WRITE：当 socket 将要写数据时触发该事件。

使用selectors实现非阻塞式编程的步骤大致如下。
①创建 selectors 对象。
②通过 selectors 对象为 socket 的 selectors.EVENT_READ 或 selectors.EVENT_WRITE 事件注册监听器函数。
每当socket有数据需要读写时,系统负责触发所注册的监听器函数。
③在监听器函数中处理 socket 通信。

下面程序使用 selectors 模块实现非阻塞式通信的服务器端。
"""
import selectors
import socket

# 创建默认的selectors对象
sel = selectors.DefaultSelector()


# 负责监听"有数据可读"事件的函数
def read(skt, mask):
    try:
        # 读取数据
        data = skt.recv(1024)
        if data:
            # 将读取的数据采用循环向每个socket发送一次
            for s in socket_list:
                s.send(data)  # Hope it won't block
        else:
            # 如果该socket已被对方关闭,关闭该socket,
            # 并从socket_list列表中删除
            print('关闭', skt)
            sel.unregister(skt)
            skt.close()
            socket_list.remove(skt)
    # 如果捕捉到异常, 将该socket关闭,并从socket_list列表中删除
    except:
        print('关闭', skt)
        sel.unregister(skt)
        skt.close()
        socket_list.remove(skt)


socket_list = []


# 负责监听"客户端连接进来"事件的函数
def accept(sock, mask):
    conn, addr = sock.accept()
    # 使用socket_list保存代表客户端的socket
    socket_list.append(conn)
    conn.setblocking(False)
    # 使用sel为conn的EVENT_READ事件注册read监听函数
    sel.register(conn, selectors.EVENT_READ, read)  # ②


sock = socket.socket()
sock.bind(('192.168.1.88', 30000))
sock.listen()
# 设置该socket是非阻塞的
sock.setblocking(False)
# 使用sel为sock的EVENT_READ事件注册accept监听函数
sel.register(sock, selectors.EVENT_READ, accept)  # ①
# 采用死循环不断提取sel的事件
while True:
    events = sel.select()
    for key, mask in events:
        # key的data属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监听函数, key的 fileobj 属性获取被监听的socket对象
        callback(key.fileobj, mask)
"""
上面程序中定义了两个监听器函数：accept()和read(),其中 accept() 函数作为"有客户端连接进来"事件的监听函数,
主程序中的①号粗体字代码负责为socket的 selectors.EVENT_READ事件注册该函数;
read()函数则作为"有数据可读"事件的监听函数,如accept()函数中的②号粗体字代码所示。

通过上面这种方式,程序避免了采用死循环不断地调用socket的accept()方法来接受客户端连接,
也避免了采用死循环不断地调用socket的 recv()方法来接收数据。socket的accept()、recv()方法调用都是写在事件监听函数中的,
只有当事件(如"有客户端连接进来"事件、"有数据可读"事件)发生时, accept()和recv()方法才会被调用,这样就避免了阻塞式编程。

为了不断地提取selectors中的事件,程序最后使用一个死循环不断地调用 selectors 的 select() 方法"监测"事件,
每当监测到相应的事件之后,程序就会调用对应的事件监听函数。
"""
