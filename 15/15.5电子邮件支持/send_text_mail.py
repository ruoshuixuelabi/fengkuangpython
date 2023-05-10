"""
15.5	电子邮件支持

Python 为邮件支持提供了smtplib、smtpd、poplib等模块,使用这些模块既可发送邮件,也可收取邮件。

15.5.1	使用smtplib模块发送邮件

使用 Python 的 smtplib 模块来发送邮件非常简单,大部分底层的处理都由smtplib进行了封装,

开发者只需要按照如下3步来发送邮件即可。
①连接 SMTP 服务器,并使用用户名、密码登录服务器。
②创建 EmailMessage 对象,该对象代表邮件本身。
③调用代表与 SMTP 服务器连接的对象的 sendmail()方法发送邮件。下面程序按照上面步骤示范了如何发送邮件
"""
import smtplib
from email.message import EmailMessage

# 定义SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 定义发件人地址
from_addr = 'kongyeeku@qq.com'
# 定义登录邮箱的密码
password = '123456'
# 定义收件人地址:
to_addr = 'kongyeeku@163.com'

# 创建SMTP连接
#conn = smtplib.SMTP(smtp_server, 25)
conn = smtplib.SMTP_SSL(smtp_server,465)
conn.set_debuglevel(1)
conn.login(from_addr, password)            #①
# 创建邮件对象
msg = EmailMessage()
# 设置邮件内容
msg.set_content('您好,这是一封来自Python的邮件', 'plain', 'utf-8')
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
# 退出连接
conn.quit()
"""
上面程序中的3行粗体字代码基本代表了使用 Python 的 smtp 模块发送邮件的3大核心步骤,
其中①号代码使用了发件人的地址和密码来登录邮箱。关于该程序有以下几点需要说明。
(1)程序中提供的邮箱密码是错误的,不用尝试。读者必须改为使用自己的邮箱地址和密码。
(2)早期 SMTP 服务器都采用普通的网络连接,因此默认端口是25。但现在绝大部分 SMTP都是基于SSL(Secure Socket Layer)的,
这样保证网络上传输的信息都是加密过的,从而使得信息更加安全。这种基于SSL 的 SMTP 服务器的默认端口是465。
上面程序中第一行粗体字代码连接的是 QQ 邮箱的基于 SSL 的 SMTP 服务器,QQ 邮箱服务器不支持普通的SMTP。
(3)国内有些公司的免费邮箱(比如 QQ 邮箱)默认是关闭了 SMTP 的,因此需要读者登录邮箱进行设置。
(4)由于该程序发送的邮件太简单,邮件没有主题,而且程序在测试过程中可能会发送很多邮件,
因此有些邮箱服务商会将该程序发送的邮件当成垃圾邮件。

注意：早期 Python 2.x 提供了email.mime、email.header、email.charset、email.encoders.  email.iterators等库来处理邮件,
这些库设计得过于烦琐,用起来极为不便,因此读者应该尽快改为使用最新的 Python 库。
本书不会介绍这些过时的库。具体可参考 https://docs.python.org/3/ibrary/email.html页面的说明。

由于程序打开了smtplib调试模式(将debuglevel设置为1),因此在运行该程序时,可以看到SMTP 发送邮件的详细过程。
当程序运行结束后,将可以在收件人邮箱中看到一封新邮件(可能在垃圾邮件内),如图15.7 所示。
"""