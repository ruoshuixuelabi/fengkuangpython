"""
为了解决第二个问题,可以考虑使用一个 dict (字典)来保存聊天室所有用户和对应 socket 之间的映射关系——
这样服务器端就可以根据用户名来找到对应的socket。

服务器端提供了一个dict的子类,并提供了根据value获取key、 根据 value删除key等方法。
"""


class CrazyitDict(dict):
    # 根据value查找key
    def key_from_value(self, val):
        # 遍历所有key组成的集合
        for key in self.keys():
            # 如果指定key对应的value与被搜索的value相同,则返回对应的key
            if self[key] == val:
                return key
        return None

    # 根据value删除key
    def remove_by_value(self, val):
        # 遍历所有key组成的集合
        for key in self.keys():
            # 如果指定key对应的value与被搜索的value相同,则返回对应的key
            if self[key] == val:
                self.pop(key)
                return


"""
严格来讲,CrazyitDict已经不是一个标准的dict结构了,但程序需要这样一个数据结构来保存用户名和对应 socket 之间的映射关系,
这样既可以通过用户名找到对应的socket,也可以根据 socket 找到对应的用户名。
"""
