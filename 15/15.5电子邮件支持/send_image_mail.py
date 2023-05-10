"""
如果希望实现图文并茂的邮件,也就是在邮件中插入图片,则首先要给邮件添加附件------不要直接在邮件中嵌入外链的图片,
很多邮箱出于安全考虑,都会禁用邮件中外链的资源。因此,如果直接在 HTML 右键中外链其他图片,那么该图片很有可能显示不出来。

为了给邮件添加附件,只需调用 EmailMessage 的 add_attachment()方法即可。该方法支持很多参数,最常见的参数如下。
(1)maintype：指定附件的主类型。比如指定 image 代表附件是图片。
(2)subtype：指定附件的子类型。比如指定为png,代表附件是PNG 图片。一般来说,子类型受主类型的限制。
(3)filename：指定附件的文件名。
(4)cid=img：指定附件的资源 ID,邮件正文可通过资源 ID 来引用该资源。 例如,如下程序为邮件添加了3个附件。
"""
import smtplib, email.utils
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
# 随机生成两个图片id
first_id, second_id = email.utils.make_msgid(), email.utils.make_msgid()
# 设置邮件内容,指定邮件内容为HTML
msg.set_content('<h2>邮件内容</h2>' +
                '<p>您好,这是一封来自Python的邮件' +
                '<img src="cid:' + second_id[1:-1] + '"><p>' +
                '来自<a href="http://www.crazyit.org">疯狂联盟</a>' +
                '<img src="cid:' + first_id[1:-1] + '">', 'html', 'utf-8')
msg['subject'] = '一封HTML邮件'
msg['from'] = '李刚 <%s>' % from_addr
msg['to'] = '新用户 <%s>' % to_addr
with open('E:/logo.jpg', 'rb') as f:
    # 添加第一个附件
    msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename='test.png', cid=first_id)
with open('E:/fklogo.gif', 'rb') as f:
    # 添加第二个附件
    msg.add_attachment(f.read(), maintype='image', subtype='gif', filename='test.gif', cid=second_id)
with open('E:/fkit.pdf', 'rb') as f:
    # 添加第三个附件,邮件正文不需引用该附件,因此不指定cid
    msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='test.pdf', )
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
# 退出连接
conn.quit()
"""
该程序与上一个程序的最大区别在于增加了第三段粗体字代码,它们为邮件添加了三个附件。
由于邮件正文不需要引用第三个附件,因此程序添加第三个附件时没有指定cid属性。

在添加附件时指定cid属性之后,程序就可以在邮件正文中通过该cid来引用附件,如上面程序中邮件正文的前两行粗体字代码所示。

运行上面程序,可以在目标邮箱内看到一封新邮件。打开该邮件,将看到如图15.10所示的邮件内容。

通过上面三个示例,可以发现使用 smtplib 模块发送邮件很简单,基本只需要连接服务器、创建邮件和发送邮件三个步骤。
如果要构建复杂的邮件内容,则主要通过 EmailMessage 对象来进行设置。
EmailMessage 也是 Python 3.x对邮件处理的巨大简化,它把对邮件内容的各种处理都封装在 EmailMessage类中,因此使得编程变得轻松、简单。
"""