"""
上面这封邮件是最简单的,没有为该邮件设置主题、发件人名字和收件人名字,邮件内容也只是简单的文本。

如果要为邮件设置主题、发件人名字和收件人名字,那么只需设置 EmailMessage 对象的相应属性即可。
如果程序要将邮件内容改为 HTML 内容,那么只需将调用EmailMessage 的 set_content()方法的第二个参数设置为html 即可。
例如,如下程序只是对EmailMessage 进行了修改。
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
# conn = smtplib.SMTP(smtp_server, 25)
conn = smtplib.SMTP_SSL(smtp_server, 465)
conn.set_debuglevel(1)
conn.login(from_addr, password)  # ①
# 创建邮件对象
msg = EmailMessage()
# 设置邮件内容,指定邮件内容为HTML
msg.set_content('<h2>邮件内容</h2>' +
                '<p>您好,这是一封来自Python的邮件<p>' +
                '来自<a href="http://www.crazyit.org">疯狂联盟</a>', 'html', 'utf-8')
msg['subject'] = '一封HTML邮件'
msg['from'] = '李刚 <%s>' % from_addr
msg['to'] = '新用户 <%s>' % to_addr
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
# 退出连接
conn.quit()
"""
该程序与上一个程序基本相似,只是在调用 set_content()方法时将第二个参数改为了"html"此外,
程序增加了上面3行粗体字代码,分别用于设置邮件主题、发件人名字和收件人名字。

运行上面程序,在目标邮箱内可以看到如图15.8所示的邮件。打开该邮件,将可以看到如图15.9 所示的邮件内容。
"""