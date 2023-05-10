"""
15.3	基于 TCP 协议的网络编程

TCP/IP 通信协议是一种可靠的网络协议,它在通信的两端各建立一个 socket,从而形成虚拟的网络链路。
一旦建立了虚拟的网络链路,两端的程序就可以通过该链路进行通信了。Python 的 socket 模块为基于 TCP 协议的网络通信提供了良好的封装,
Python 使用 socket 对象来代表两端的通信端口,并通过 socket 进行网络通信。

15.3.1	TCP协议基础

IP 是 Internet上使用的一个关键协议,它的全称是Internet Protocol,即 Internet 协议,通常简称 IP 协议。
通过使用 IP 协议,使 Internet 成为一个允许连接不同类型的计算机和不同操作系统的网络。

要使两台计算机彼此能进行通信,必须使这两台计算机使用同一种"语言",IP 协议只保证计算机能发送和接收分组数据。
IP 协议负责将消息从一个主机传送到另一个主机,消息在传送的过程中被分割成一个个小包。

尽管通过安装 IP 软件,保证了计算机之间可以发送和接收数据,但 IP 协议还不能解决数据分组在传输过程中可能出现的问题。
因此,连接 Internet 的计算机还需要安装 TCP 协议来提供可靠且无差错的通信服务。

TCP 被称作端对端协议,这是因为它在两台计算机的连接中起了重要作用——当一台计算机需要与另一台远程计算机连接时,
TCP 协议会让它们之间建立一个虚拟链路,用于发送和接收数据。

TCP 协议负责收集这些数据包,并将其按照适当的顺序传送,接收端接收到数据包后再将其正确地还原。
TCP 协议保证数据包在传送过程中准确无误。TCP 协议采用重发机制——当一个通信实体发送一个消息给另一个通信实体后,
需要接收到另一个通信实体的确认信息,如果没有接收到该确认信息,则会重发信息。

通过重发机制,TCP 协议向应用程序提供了可靠的通信连接,使其能够自动适应网络上的各种变化。
即使在 Internet 暂时出现堵塞的情况下,TCP 协议也能够保证通信的可靠性。

图 15.4 显示了 TCP 协议控制两个通信实体互相通信的示意图。

只有把 TCP 和 IP 两个协议结合起来,才能保证 Internet 在复杂的环境下正常运行。
凡是要连接到 Internet 的计算机,都必须同时安装和使用 TCP/IP 协议。

15.3.2	使用socket创建TCP服务器端

程序在使用 socket 之前,必须先创建 socket 对象,可通过该类的如下构造器来创建 socket 实例。
socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)
上面构造器的前三个参数比较重要,其中：
(1)family 参数用于指定网络类型。该参数支持socket.AF_UNIX(UNIX 网络)、
socket.AF_INET (基于IPv4协议的网络)和socket.AF_INET6(基于IPv6协议的网络)这三个常量。
(2)type 参数用于指定网络 Sock 类型。该参数可支持 SOCK_STREAM(默认值,创建基于TCP协议的socket)、
SOCK_DGRAM(创建基于 UDP 协议的socket) 和 SOCK_RAW(创建原始socket)。一般常用的是SOCK_STREAM 和 SOCK_DGRAM。
(3)proto 参数用于指定协议号,如果没有特殊要求,该参数默认为0,并可以忽略。

在创建了 socket 之后,接下来需要将两个 socket 连接起来。
从图15.4中并没有看出 TCP 协议控制的两个通信实体之间有服务器端和客户端之分,
这是因为此图是两个通信实体之间已经建立虚拟链路之后的示意图。
在两个通信实体之间没有建立虚拟链路时,必须有一个通信实体先做出"主动姿态",主动接收来自其他通信实体的连接请求。

作为服务器端使用的 socket 必须被绑定到指定IP地址和端口,并在该IP地址和端口进行监听,接收来自客户端的连接。

socket对象提供了如下常用方法。
(1)socket.accept()：作为服务器端使用的 socket 调用该方法接收来自客户端的连接。
(2)socket.bind(address)：作为服务器端使用的 socket 调用该方法,将该 socket 绑定到指定 address,
该address可以是一个元组,包含IP地址和端口。
(3)socket.close(): 关闭连接,回收资源。
(4)socket.connect(address): 作为客户端使用的socket调用该方法连接远程服务器。
(5)socket.connect_ex(address): 该方法与上一个方法的功能大致相同,只是当程序出错时,该方法不会抛出异常,而是返回一个错误标识符。
(6)socket.listen([backlog]): 作为服务器端使用的socket调用该方法进行监听。
(7)socket.makefile(mode='r,buffering=None,*,encoding=None,errors=None, newline=None):创建一个和该socket关联的文件对象。
(8)socket.recv(bufsize[,flags]):接收socket中的数据。该方法返回bytes对象代表接收到的数据。
(9)socket.recvfrom(bufsize[,flags]): 该方法与上一个方法的功能大致相同,只是该方法的返回值是(bytes,address)元组。
(10)socket.recvmsg(bufsize[,ancbufsize[,flags]]):该方法不仅接收来自socket的数据,还接收来自 socket 的辅助数据,
因此该方法的返回值是一个长度为4的元组——(data,ancdata, msg flags,address),其中ancdata代表辅助数据。
(11)socket.recvmsg into(buffers[,ancbufsize[,flags]]):类似于socket.recvmsg()方法,但该方法将接收到的数据放入buffers中。
(12)socket.recvfrom into(buffer[,nbytes[,flags]]): 类似于socket.recvfrom()方法,但该方法将接收到的数据放入buffer中。
(13)socket.recv into(buffer[,nbytes[,flags]]):类似于recv()方法,但该方法将接收到的数据放入 buffer中。
(14)socket.send(bytes[,flags]): 向 socket发送数据,该socket必须与远程socket建立了连接。
该方法通常用于在基于TCP 协议的网络中发送数据。
(15)socket.sendto(bytes,address)。向 socket 发送数据,该 socket 应该没有与远程 socket 建立连接。
该方法通常用于在基于 UDP 协议的网络中发送数据。
(16)socket.sendfle(file,offset=0,count=None): 将整个文件内容都发送出去,直到遇到文件的 EOF。
(17)socket.shutdown(how): 关闭连接。其中 how 用于设置关闭方式。

掌握了这些常用的方法之后,可以大致归纳出 TCP 通信的服务器端编程的基本步骤。
① 服务器端先创建一个 socket 对象。
② 服务器端 socket 将自己绑定到指定 IP 地址和端口。
③ 服务器端 socket 调用 listen() 方法监听网络。
④ 程序采用循环不断调用socket 的accept() 方法接收来自客户端的连接。代码片段如下：

# 创建socket对象
s = socket.socket()
# 将socket绑定到本机IP和端口
s.bind(('192.168.1.88', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
while True:
    # 每当接收到客户端socket的请求时,该方法返回对应的socket和远程地址
    c, addr = s.accept()

上面程序先创建了一个socket对象,接下来将该socket绑定到192.168.1.88的30000端口,其中192.168.1.88是程序所在计算机的 IP 地址。

提示：上面程序使用 30000 作为该 socket 的监听端口,通常推荐使用 1024 以上的端口,主要是为了避免与其他应用程序的通用端口发生冲突。

15.3.3	使用socket通信

客户端也是先创建一个socket对象,然后调用 socket 的 connect()方法建立与服务器端的连接,这样就可以建立一个基于 TCP 协议的网络连接。
TCP 通信的客户端编程的基本步骤大致归纳如下。
① 客户端先创建一个socket 对象。
② 客户端socket 调用connect() 方法连接远程服务器。代码片段如下：

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('192.168.1.88', 30000))    # ①

当执行上面程序中的粗体字代码时,将会连接到指定服务器,让服务器端socket的 accept()方法向下执行,
于是服务器端和客户端就产生一对互相连接的 socket。

当服务器端和客户端产生了对应的 socket之后,就得到了如图15.4所示的通信示意图,
程序无须再区分服务器端和客户端,而是通过各自的socket进行通信。通过前面介绍我们知道, socket 提供了大量方法来发送和接收数据。
(1)发送数据：使用 send()方法。注意, sendto()方法用于UDP 协议的通信。
(2)接收数据：使用recv_xxx()方法。

下面的服务器端程序非常简单,它仅仅建立socket, 并监听来自客户端的连接,只要客户端连 接进来,程序就会向socket发送一条简单的信息。
"""
# 导入 socket 模块
import socket

# 创建socket对象
s = socket.socket()
# 将socket绑定到本机IP和端口
s.bind(('172.20.102.27', 30000))
# 服务端开始监听来自客户端的连接
s.listen()
while True:
    # 每当接收到客户端socket的请求时,该方法返回对应的socket和远程地址
    c, addr = s.accept()
    print(c)
    print('连接地址：', addr)
    c.send('您好,您收到了服务器的新年祝福！'.encode('utf-8'))
    # 关闭连接
    c.close()
