"""
15.5.2	使用poplib模块收取邮件

使用 poplib 模块收取邮件也很简单,该模块提供了 poplib.POP3 和 poplib.POP3_SSL 两个类,
分别用于连接普通的 POP 服务器和基于 SSL 的 POP 服务器。

一旦使用 poplib.POP3 或 poplib.POP3_SSL 连接到服务器之后,接下来基本就按照 POP3 协议与服务器进行交互。
为了更好地理解 poplib 模块的运行机制,下面先简单介绍POP3 协议内容。

POP3 协议也属于请求-响应式交互协议,当客户端连接到服务器之后,客户端向 POP 服务器发送请求,
而 POP 服务器则对客户端生成响应数据,客户端可通过响应数据下载得到邮件内容。
当下载完成后,邮件客户端可以删除或修改任意邮件,而无须与电子邮件服务器进行进一步交互

POP3 的命令和响应数据都是基于 ASCII 文本的,并以CR 和 LF(/r/n) 作为行结束符,响应数据包括一个表示返回状态的符号(+/-)和描述信息。

请求和响应的标准格式如下：
请求标准格式：命令   [参数] CRLF
响应标准格式：+OK/[-ERR] description CRLF

POP3 协议客户端的命令和服务器端对应的响应数据如下。
(1)user  name: 向 POP 服务器发送登录的用户名。
(2)pass string: 向 POP 服务器发送登录的密码。
(3)quit: 退出 POP 服务器。
(4)stat: 统计邮件服务器状态,包括邮件数和总大小。
(5)list[msg_no]: 列出全部邮件或指定邮件。返回邮件编号和对应大小。
(6)retr msg_no: 获取指定邮件的内容(根据邮件编号来获取,编号从1开始)。
(7)dele  msg_no: 删除指定邮件(根据邮件编号来删除,编号从1开始)。
(8)noop: 空操作。仅用于与服务器保持连接。
(9)rset: 用于撤销 dele命令。

poplib 模块完全模拟了上面命令,poplib.POP3 或 poplib.POP3_SSL 为上面命令提供了相应的方法,
开发者只要依次使用上面命令即可从服务器端下载对应的邮件。

使用poplib收取邮件可分为两步。
①使用 poplib.POP3 或 poplib.POP3_SSL 按 POP3 协议从服务器端下载邮件。
②使用 email.parser.Parser 或 email.parser.BytesParser 解析邮件内容,得到EmailMessage 对象,
从 EmailMessage 对象中读取邮件内容。
"""
import mimetypes
import os.path
import poplib
from email.parser import BytesParser
from email.policy import default

# 输入邮件地址, 口令和POP3服务器地址:
email = 'kongyeeku@qq.com'
password = '123456'
pop3_server = 'pop.qq.com'

# 连接到POP 3服务器:
# conn = poplib.POP3(pop3_server, 110)
conn = poplib.POP3_SSL(pop3_server, 995)
# 可以打开或关闭调试信息:
conn.set_debuglevel(1)
# 可选:打印POP 3服务器的欢迎文字:
print(conn.getwelcome().decode('utf-8'))
# 输入用户名、密码信息
# 相当于发送POP 3的user命令
conn.user(email)
# 相当于发送POP 3的pass命令
conn.pass_(password)
# 获取邮件统计信息,相当于发送POP 3的stat命令
message_num, total_size = conn.stat()
print('邮件数: %s. 总大小: %s' % (message_num, total_size))
# 获取服务器上的邮件列表,相当于发送POP 3的list命令
# resp保存服务器的响应码
# mails列表保存每封邮件的编号、大小
resp, mails, octets = conn.list()
print(resp, mails)
# 获取指定邮件的内容（此处传入总长度,也就是获取最后一封邮件）
# 相当于发送POP 3的retr命令
# resp保存服务器的响应码
# data保存该邮件的内容
resp, data, octets = conn.retr(len(mails))
# 将data的所有数据（原本是一个字节列表）拼接在一起
msg_data = b'\r\n'.join(data)
# 将字符串内容解析成邮件,此处一定要指定policy=default
msg = BytesParser(policy=default).parsebytes(msg_data)  # ①
print(type(msg))
print('发件人:' + msg['from'])
print('收件人:' + msg['to'])
print('主题:' + msg['subject'])
print('第一个收件人名字:' + msg['to'].addresses[0].username)
print('第一个发件人名字:' + msg['from'].addresses[0].username)
for part in msg.walk():
    counter = 1
    # 如果maintype是multipart,说明是容器（用于包含正文、附件等）
    if part.get_content_maintype() == 'multipart':
        continue
    # 如果maintype是multipart,说明是邮件正文部分
    elif part.get_content_maintype() == 'text':
        print(part.get_content())
    # 处理附件
    else:
        # 获取附件的文件名
        filename = part.get_filename()
        # 如果没有文件名,程序要负责为附件生成文件名
        if not filename:
            # 根据附件的contnet_type来推测它的后缀名
            ext = mimetypes.guess_extension(part.get_content_type())
            # 如果推测不出后缀名
            if not ext:
                # 使用.bin作为后缀名
                ext = '.bin'
            # 程序为附件来生成文件名
            filename = 'part-%03d%s' % (counter, ext)
        counter += 1
        # 将附件写入的本地文件
        with open(os.path.join('.', filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))
# 退出服务器,相当于发送POP 3的quit命令
conn.quit()
"""
上面程序中第一段粗体字代码就是通过 poplib 模块使用 POP 3 命令从服务器端下载邮件的步骤,
其实就是依次发送user、pass、stat、list、retr命令的过程。当retr命令执行完成后,将得到最后一封邮件的数据：data,
该 data 是一个 list 列表,因此程序需要先将这些数据拼接成一个整体,然后使用①号代码将邮件数据恢复成 EmailMessage 对象。

这里有一点需要指出,程序在创建 BytesParser(解析字节串格式的邮件数据)或Parser(解析字符串格式的邮件数据)时,
必须指定policy=default;否则,BytesParse 或 Parser 解析邮件数据得到的就是过时的 Message 对象,处理起来非常不方便。

注意：在创建BytesParse或 Parser解析器时,一定要指定 policy=default;否则,解析出来的对象就是 Message,而不是新的 EmailMessage。

程序在①号代码之后特意输出了解析得到的msg 类型,此时应该看到的是 EmailMessage,而不是过时的Message 对象。

在①号代码之前,就是完成 poplib 模块收取邮件的第一步：从服务器端下载邮件;
在①号代码之后,就是完成poplib模块收取邮件的第二步：解析邮件内容。

如果程序要获取邮件的发件人、收件人和主题,直接通过 EmailMessage 的相应属性来获取即可,
与前面为EmailMessage 设置发件人、收件人和主题的方式是对应的。

如果程序要读取 EmailMessage 的各部分,则需要调用该对象的walk()方法,该方法返回一个可迭代对象,
程序使用for循环遍历walk()方法的返回值,对邮件内容进行逐项处理。
(1)如果邮件某项的 maintype 是'multipart',则说明这一项是容器,用于包含邮件内容、附件等其他项。
(2)如果邮件某项的 maintype 是'text',则说明这一项的内容是文本,通常就是邮件正文或文本附件。
对于这种文本内容,程序直接将其输出到控制台中。
(3)如果邮件某项的 maintype 是其他,则说明这一项的内容是附件,程序将附件内容保存在本地文件中。

运行上面程序,可以看到程序收取了指定邮件的最后一封邮件,并将邮件内容输出到控制台中,将邮件附件保存在本地文件中。

15.6	本章小结

本章重点介绍了 Python 网络编程的相关知识。本章先简要介绍了计算机网络的相关知识,
并介绍了IP 地址和端口的概念,这是进行网络编程的基础。
本章详细介绍了urllib 模块及其子模块的功能和用法,这是Python 网络编程中使用最广泛的工具。

本章详细介绍了基于 TCP 协议和 UDP 协议的 socket 通信,这是基于传输层协议的编程,属于比较底层的、真正的网络编程。
本章并没有介绍一个简单的通信示例,而是真正以逐步迭代的方式开发一个C/S 结构的多人网络聊天工具,
通过这个示例可以让读者真正掌握基于 TCP 协议和 UDP  协议的网络编程。
读者要注意 TCP 协议和UDP 协议的区别：基于TCP 协议的两个通信实体之间 存在虚拟链路连接,
因此在使用基于TCP 协议的socket通信时,首先要建立两个socket之间的连 接,然后通过send()、recv()方法来发送和接收数据;
而基于UDP 协议的两个通信实体之间并无连接,因此程序必须使用sendto()方法来发送数据,并且在发送时要指定数据的目标地址。
此外,本章还介绍了通过selectors模块实现非阻塞通信的方式。

本章最后介绍了两个应用层协议的网络编程---使用 smtplib 和 poplib 模块。
Python 使用 smtplib来发送邮件,使用poplib来收取邮件,而收发邮件是实际编程中应用非常广泛的功能。
读者通过学习 smtplib 和 poplib这两个应用层协议的支持模块,也可以大致了解到 Python 的其他应用层协议支持模块的用法。

本章练习
1. 编写一个程序,使用urlib.request读 取http://www.crazyit.org首页的内容。
2. 编写一个程序,结合使用urllib.request和 re模块,下载并识别http://www.crazyit.org首 页 的全部链接地址。
3. 开发并完善本章介绍的聊天室程序,并为该程序提供界面。
4. 开发并完善本章介绍的多点广播程序,并为该程序提供界面,使之成为一个局域网内的聊 天程序。
5. 结合使用 smtplib 和 poplib模块,开发一个简单的邮件客户端程序,该客户端程序既可以 发送邮件,也可以收取邮件。
"""