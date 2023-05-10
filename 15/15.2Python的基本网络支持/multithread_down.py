"""
有了上面的 DownUtil 工具类之后,接下来就可以在主程序中调用该工具类的 download()方法执行下载,如下面的程序所示。
"""
from DownUtil import *

du = DownUtil("http://www.crazyit.org/data/attachment/" \
              + "forum/201801/19/121212ituj1s9gj8g880jr.png", 'a.png', 3)
du.download()


def show_process():
    print("已完成：%.2f" % du.get_complete_rate())
    global t
    if du.get_complete_rate() < 1:
        # 通过定时器启动0.1之后执行show_process函数
        t = threading.Timer(0.1, show_process)
        t.start()


# 通过定时器启动0.1之后执行show_process函数
t = threading.Timer(0.1, show_process)
t.start()
"""
运行上面程序,即可看到程序从www.crazyit.org下载得到一个名为a.png的图片文件。
"""