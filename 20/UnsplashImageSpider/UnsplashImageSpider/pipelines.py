"""
③ 开发 Pipeline。Pipeline 负责保存 Spider 返回的Item 对象(封装了爬取到的数据)。
本项目爬取的目标是图片,因此程序得到图片的 URL 之后,既可将这些 URL 地址导入专门的下载工具中批量下载,
也可在Python程序中直接下载。本项目的 Pipeline 将使用 urllib.request 包直接下载。下面是该项目的Pipeline程序。
"""
from urllib.request import *


class UnsplashimagespiderPipeline(object):
    def process_item(self, item, spider):
        # 每个item代表一个要下载的图片
        print('----------' + item['image_id'])
        real_url = item['download'] + "?force=true"
        try:
            pass
            # 打开URL对应的资源
            with urlopen(real_url) as result:
                # 读取图片数据
                data = result.read()
                # 打开图片文件
                with open("images/" + item['image_id'] + '.jpg', 'wb+') as f:
                    # 写入读取的数据
                    f.write(data)
        except:
            print('下载图片出现错误' % item['image_id'])


"""
上面程序中第一行粗体字代码用于拼接下载图片的完整地址。可能有读者会问：为何要在图片下载地址的后面追加"?force=true"?
这并不是本项目所能决定的,读者可以把鼠标指针移动到 https://unsplash.com 
网站中各图片右下角的下载按钮上,即可看到各图片的下载地址都会在 download 后追加"?force=true", 此处只是模拟这种行为而已。

程序中第二行粗体字代码使用 urlopen()函数获取目标 URL 的数据,接下来即可读取图片数据, 并将图片数据写入下载的目标文件中。
"""
