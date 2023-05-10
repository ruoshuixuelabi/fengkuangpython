"""
15.2.3	使用urllib.request读取资源

在 urllib.request 子模块下包含了一个非常实用的 urllib.request.urlopen(url,data=None)方法,该方法用于打开 url指定的资源,
并从中读取数据。根据请求 url 的不同,该方法的返回值会发生动态改变。
如果url是一个HTTP 地址,那么该方法返回一个http.client.HTTPResponse对象。 例如如下程序。
"""
from urllib.request import *

# 打开URL对应的资源
result = urlopen('http://www.crazyit.org/index.php')
# 按字节读取数据
data = result.read(326)
# 将字节数据恢复成字符串
print(data.decode('utf-8'))

# 用context manager来管理打开的URL资源
with urlopen('http://www.crazyit.org/index.php') as f:
    # 按字节读取数据
    data = f.read(326)
    # 将字节数据恢复成字符串
    print(data.decode('utf-8'))
"""
上面程序都是向http://www.crazyit.org/index.php发送请求,并请求下载该页面的内容。
只不过第一个示例程序是直接获取 http://www.crazyit.org/index.php 资源的数据;
第二个示例程序则使用 context manager来管理通过urlopen打开的资源。

运行上面程序,可以看到程序分两次获取并输出了http://www.crazyit.org/index.php页面内容。
"""
