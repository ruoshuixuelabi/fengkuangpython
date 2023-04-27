"""
2. 使用 Pipe 实现进程通信

使用 Pipe 实现进程通信,程序会调用 multiprocessing.Pipe() 函数来创建一个管道,该函数会返回两个 PipeConnection 对象,
代表管道的两个连接端(一个管道有两个连接端,分别用于连接通信的两个进程)。

PipeConnection对象包含如下常用方法。
(1)send(obj):发送一个obj给管道的另一端,另一端使用recv()方法接收。
需要说明的是,该 obj 必须是可 picklable 的(Python的序列化机制),如果该对象序列化之后超过32MB,则很可能会引发ValueError异常。
(2)recv():  接收另一端通过 send()方法发送过来的数据。
(3)fileno():  关于连接所使用的文件描述器。
(4)close():  关闭连接。
(5)poll([timeout]): 返回连接中是否还有数据可以读取。
(6)send_bytes(buffer[,offset[,size]]): 发送字节数据。如果没有指定offset、size参数,则默认发送buffer字节串的全部数据;
如果指定了offset和 size参数,则只发送 buffer 字节串中从 offset 开始、长度为size的字节数据。
通过该方法发送的数据,应该使用 recv_bytes()或 recv_bytes_into 方法接收。
(7)recv_bytes([maxlength]): 接收通过 send_bytes() 方法发送的数据, maxlength 指定最多接收的字节数。该方法返回接收到的字节数据。
(8)recv_bytes_into(buffer[,offset]): 功能与 recv_bytes() 方法类似,只是该方法将接收到的数据放在 buffer 中。
下面程序将会示范如何使用Pipe来实现两个进程之间的通信。
"""
import multiprocessing


def f(conn):
    print('(%s) 进程开始发送数据...' % multiprocessing.current_process().pid)
    # 使用conn发送数据
    conn.send('Python')


if __name__ == '__main__':
    # 创建Pipe,该函数返回两个PipeConnection对象
    parent_conn, child_conn = multiprocessing.Pipe()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(child_conn,))
    # 启动子进程
    p.start()
    print('(%s) 进程开始接收数据...' % multiprocessing.current_process().pid)
    # 通过conn读取数据
    print(parent_conn.recv())  # Python
    p.join()
"""
上面程序中第一行粗体字代码(子进程)通过PipeConnection向管道发送数据,数据将会被发送给管道另一端的父进程。
第二行粗体字代码(父进程)通过PipeConnection从管道读取数据,程序就可以读取到另一端子进程写入的数据,
这样就实现了父、子两个进程之间的通信。

运行上面程序,可以看到如下输出结果。

14.10 本章小结

本章主要介绍了Python 并发编程的相关知识。本章重点介绍了Python 的多线程编程支持,并简要介绍了Python 的多进程编程。
本章首先简单介绍了线程的基本概念,并讲解了线程和进程之 间的区别与联系。
本章详细讲解了如何创建和启动多个线程,也详细介绍了线程的生命周期。
本章通过示例程序示范了控制线程的几个方法,还详细讲解了线程同步的意义和必要性,并介绍了使用 Lock 实现线程同步的方法。
本章介绍了三种实现线程通信的方式：使用Condition对象、阻塞队列和 Event 实现线程通信。
此外,本章也介绍了使用线程池来管理线程。由于线程属于创建成本较大 的对象,因此在程序中应该考虑复用线程,
在实际开发中使用线程池是一个不错的选择。

本章还介绍了与线程相关的工具类,比如线程局部变量、定时器和任务调度等。
本章最后介绍了 Python 的多进程编程支持,包括使用 os.fork() 方法和 Process 类创建新进程两种方式,
也介绍了使用进程池管理进程的方式和实现进程通信的两种方法。
需要指出的是,使用多进程实现并发的开销比使用多线程的开销大,因此推荐程序尽量使用多线程来实现并发
"""
