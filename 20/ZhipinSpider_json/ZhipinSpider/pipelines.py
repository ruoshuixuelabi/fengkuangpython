"""
20.2.4	使用JSON导出信息

仅在控制台打印所爬取到的信息是不够的,程序既可以将这些信息保存到文件中,也可以将这些信息写入数据库中。
下面程序将示范将信息以 JSON 格式保存到文件中。

Scrapy项目使用 Pipeline 处理被爬取信息的持久化操作,因此程序只要修改 pipelines.py 文件即可。
程序原来只是打印 item 对象所包含的信息,现在应该把item 对象中的信息存入文件中。该文件修改后的代码如下。
"""
import json


class ZhipinspiderPipeline(object):
    # 定义构造器,初始化要写入的文件
    def __init__(self):
        self.json_file = open("job_positions.json", "wb+")
        self.json_file.write('[\n'.encode("utf-8"))

    # 重写close_spider回调方法,用于关闭文件
    def close_spider(self, spider):
        print('----------关闭文件-----------')
        # 后退2个字符,也就是去掉最后一条记录之后的换行符和逗号
        self.json_file.seek(-2, 1)
        self.json_file.write('\n]'.encode("utf-8"))
        self.json_file.close()

    def process_item(self, item, spider):
        # 将item转换成JSON字符串
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # 写入JSON字符串
        self.json_file.write(text.encode("utf-8"))


"""
上面程序中第一行粗体字代码将 item 对象转换为 JSON 字符串,第二行粗体字代码将该JSON 字符串写入文件中。
从上面代码来看,该Pipeline类依然非常简单——只是简单的文件I/O。

程序为该 Pipeline 类定义了构造器,该构造器可用于初始化资源;程序还为该Pipeline类重写了close spider()方法,
该方法负责关闭构造器初始化的资源。

使用scrapy crawl job_position命令启动爬虫,此时将不会看到程序在控制台打印该爬虫所爬取到的10页职位信息。
当程序运行结束之后,可以在项目目录下找到 job_positions.json 文件,该文件包含了300条热门职位信息。
"""
