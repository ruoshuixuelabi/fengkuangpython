"""

4.6.1   数字转人民币读法

下面会实现在实际开发中常用的一个工具函数：将一个浮点数转换成人民币读法的字符串,这个程序需要使用数组。
实现这个函数的思路是,首先把这个浮点数分成整数部分和小数部分。提取整数部分很容易,
直接将这个浮点数强制类型转换成一个整数即可,这个整数就是浮点数的整数部分；再使用浮点数减去整数就可以得到这个浮点数的小数部分。
然后分开处理整数部分和小数部分。小数部分的处理比较简单,直接截断保留2位数字,转换 成几角几分的字符串。
整数部分的处理则稍微复杂一点,但只要认真分析不难发现,中国的数字习 惯是4位一节的,
一个4位的数字可被转成几千几百几十几,至于后面添加什么单位则不确定,如果这节4位数字出现在1~4位,
则后面添加单位"元";如果这节4位数字出现在5~8位,则后面 添加单位"万";如果这节4位数字出现在9~12位,
则后面添加单位"亿";多于12位就暂不考 虑了。
因此,实现这个程序的关键就是把一个4位的数字字符串转换成中文读法。下面程序把这个需 求实现了一部分。

从上面程序的运行结果来看,初步实现了所需功能,但这个程序并不是这么简单的,对零的处理比较复杂。
例如,有两个零连在一起时该如何处理呢?还有小数部分如何翻译?因此,这个程序 还需要继续完善,希望读者能把这个程序写完。
"""
'''
  把一个浮点数分解成整数部分和小数部分字符串
  num 需要被分解的浮点数
  返回分解出来的整数部分和小数部分。
  第一个数组元素是整数部分,第二个数组元素是小数部分
'''


def divide(num):
    # 将一个浮点数强制类型转换为int型,即得到它的整数部分
    integer = int(num)
    # 浮点数减去整数部分,得到小数部分,小数部分乘以100后再取整得到2位小数
    fraction = round((num - integer) * 100)
    # 下面把整数转换为字符串
    return (str(integer), str(fraction))


han_list = ["零", "壹", "贰", "叁", "肆", \
            "伍", "陆", "柒", "捌", "玖"]
unit_list = ["十", "百", "千"]
'''
  把一个四位的数字字符串变成汉字字符串
  num_str 需要被转换的四位的数字字符串
  返回四位的数字字符串被转换成汉字字符串
'''


def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        # 把字符串转成数值
        num = int(num_str[i])
        # 如果不是最后一位数字,而且数字不是零,则需要添加单位（千、百、十）
        if i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不要添加单位
        else:
            result += han_list[num]
    return result


'''
  把数字字符串变成汉字字符串
  num_str 需要被转换的数字字符串
  返回数字字符串被转换成汉字字符串
'''


def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大,翻译不了')
        return
    # 如果大于8位,包含单位亿
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + "亿" + \
            four_to_hanstr(num_str[-8: -4]) + "万" + \
            four_to_hanstr(num_str[-4:])
    # 如果大于4位,包含单位万
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4]) + "万" + \
            four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)


num = float(input("请输入一个浮点数: "))
# 测试把一个浮点数分解成整数部分和小数部分
integer, fraction = divide(num)
# 测试把一个四位的数字字符串变成汉字字符串
print(integer_to_str(integer))
print(fraction)
