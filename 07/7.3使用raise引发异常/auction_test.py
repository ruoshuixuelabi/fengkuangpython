"""
7.3.3	except和 raise同时使用
在实际应用中对异常可能需要更复杂的处理方式—— 当一个异常出现时,单靠某个方法无法完 全处理该异常,必须由几个方法协作才可完全处理该异常。也就是说,在异常出现的当前方法中, 程序只对异常进行部分处理,还有些处理需要在该方法的调用者中才能完成,所以应该再次引发异 常,让该方法的调用者也能捕获到异常。
为了实现这种通过多个方法协作处理同一个异常的情形,可以在except块中结合raise语句来 完成。如下程序示范了except和 raise同时使用的方法。
"""


class AuctionException(Exception): pass


class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            # 此处只是简单地打印异常信息
            print("转换出异常：", e)
            # 再次引发自定义异常
            #            raise AuctionException("竞拍价必须是数值,不能包含其他字符！")  # ①
            raise AuctionException(e)
        if self.init_price > d:
            raise AuctionException("竞拍价比起拍价低,不允许竞拍！")
        initPrice = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid("df")
    except AuctionException as ae:
        # 再次捕获到bid()方法中的异常,并对该异常进行处理
        print('main函数捕捉的异常：', ae)


main()
"""
1.  上面程序中粗体字代码对应的 except 块捕获到异常后,系统打印了该异常的字符串信息,接着引发一个AuctionException异常,
通知该方法的调用者再次处理该AuctionException异常。所以程序中的main()函数,也就是bid()方法的调用者还可以再次捕获
AuctionException异常,并将该异 常的详细描述信息打印出来。
2.  这种except和 raise结合使用的情况在实际应用中非常常用。实际应用对异常的处理通常分成两个部分：
①应用后台需要通过日志来记录异常发生的详细情况；②应用还需要根据异常向应用使用者传达某种提示。
在这种情形下,所有异常都需要两个方法共同完成,也就必须将 except 和 raise 结合使用。
3.  如果程序需要将原始异常的详细信息直接传播出去,Python 也允许用自定义异常对原始异常进行包装,
只要将上面①号粗体字代码改为如下形式即可。
raise  AuctionException(e)
4.  上面就是把原始异常e包装成了AuctionException异常,这种方式也被称为异常包装或异常转译。
"""