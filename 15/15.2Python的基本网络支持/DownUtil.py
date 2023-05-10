"""
通过 urlopen() 函数打开远程资源之后,也可以非常方便地读取远程资源——甚至实现多线程下载。
如下程序实现了一个多线程下载的工具类。
"""
from urllib.request import *
import threading


class DownUtil:
    def __init__(self, path, target_file, thread_num):
        # 定义下载资源的路径
        self.path = path
        # 定义需要使用多少个线程下载资源
        self.thread_num = thread_num
        # 指定所下载的文件的保存位置
        self.target_file = target_file
        # 初始化threads数组
        self.threads = []

    def download(self):
        # 创建Request对象
        req = Request(url=self.path, method='GET')
        # 添加请求头
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        # 打开要下载的资源
        f = urlopen(req)
        # 获取要下载的文件大小
        self.file_size = int(dict(f.headers).get('Content-Length', 0))
        f.close()
        # 计算每个线程要下载的资源大小
        current_part_size = self.file_size // self.thread_num + 1
        for i in range(self.thread_num):
            # 计算每个线程下载的开始位置
            start_pos = i * current_part_size
            # 每个线程使用一个wb模式打开的文件进行下载
            t = open(self.target_file, 'wb')
            # 定位该线程的下载位置
            t.seek(start_pos, 0);
            # 创建下载线程
            td = DownThread(self.path, start_pos, current_part_size, t)
            self.threads.append(td)
            # 启动下载线程
            td.start()

    # 获取下载的完成百分比
    def get_complete_rate(self):
        # 统计多个线程已经下载的总大小
        sum_size = 0
        for i in range(self.thread_num):
            sum_size += self.threads[i].length
        # 返回已经完成的百分比
        return sum_size / self.file_size


class DownThread(threading.Thread):
    def __init__(self, path, start_pos, current_part_size, current_part):
        super().__init__()
        self.path = path
        # 当前线程的下载位置
        self.start_pos = start_pos
        # 定义当前线程负责下载的文件大小
        self.current_part_size = current_part_size
        # 当前线程需要下载的文件块
        self.current_part = current_part
        # 定义该线程已下载的字节数
        self.length = 0

    def run(self):
        # 创建Request对象
        req = Request(url=self.path, method='GET')
        # 添加请求头
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        # 打开要下载的资源
        f = urlopen(req)
        # 跳过self.start_pos个字节,表明该线程只下载自己负责的那部分内容
        for i in range(self.start_pos):
            f.read(1)
        # 读取网络数据,并写入本地文件
        while self.length < self.current_part_size:
            data = f.read(1024)
            if data is None or len(data) <= 0:
                break
            self.current_part.write(data)
            # 累计该线程下载的总大小
            self.length += len(data)
        self.current_part.close()
        f.close()


"""
上面程序中定义了 DownThread  线程类,该线程类负责读取从 start_pos 开始、
长度为 current_part_size的所有字节数据,并写入本地文件对象中。 DownThread 线程类的run()方法就是一个简单的输入/输出实现。

程序中 DownUtils 类的 download()方法负责按如下步骤来实现多线程下载。
① 使用urlopen() 方法打开远程资源。
② 获取指定的URL 对象所指向资源的大小(通过Content-Length响应头获取)。
③ 计算每个线程应该下载网络资源的哪个部分(从哪个字节开始,到哪个字节结束)。
④ 依次创建并启动多个线程来下载网络资源的指定部分。
提示：上面程序已经实现了多线程下载的核心代码,如果要实现断点下载,
则需要额外增加一个配置文件(读者可以发现,所有的断点下载工具都会在下载开始时生成两个文件：
一个是与网络资源具有相同大小的空文件;一个是配置文件),该配置文件分别记录每个线程已经下载到哪个字节,
当网络断开后再次开始下载时,每个线程根据配置文件中记录的位置向后下载即可。
"""
