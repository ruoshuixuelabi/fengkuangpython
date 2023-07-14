"""
在一个函数体内调用它自身,被称为函数递归。函数递归包含了一种隐式的循环,它会重复执行某段代码,但这种重复执行无须循环控制。

例如有如下数学题。已知有一个数列：f(0)=1,f(1)=4,f(n+2)=2*(n+1)+f(n),其中n是大于0的整数,求(10)的值。
这道题可以使用递归来求得。下面程序将定义一个fn()函数,用于计算(10)的值。
"""


def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        # 函数中调用它自身,就是函数递归
        return 2 * fn(n - 1) + fn(n - 2)


# 输出fn(10)的结果
print("fn(10)的结果是:", fn(10))
"""
在上面的 fn() 函数体中再次调用了 fn() 函数,这就是函数递归。注意在 fn() 函数体中调用 fn 的形式：
 return 2 * fn(n - 1) + fn(n - 2)
 
对于fn(10), 即等于 2 * fn(9)+fn(8),其中fn(9)又等于2*fn(8)+fn(7)……依此类推,最终会计算到 fn(2)等于 2 *fn(1)+fn(0),
即fn(2)是可计算的,这样递归带来的隐式循环就有结束的时候,然后一路反算回去,最后就可以得到fn(10)的值。

仔细看上面递归的过程,当一个函数不断地调用它自身时,必须在某个时刻函数的返回值是确定的,即不再调用它自身;
否则,这种递归就变成了无穷递归,类似于死循环。因此,在定义递归函数时有一条最重要的规定：递归一定要向已知方向进行。

例如,如果把上面数学题改为如此。已知有一个数列：{(20)=1,(21)=4,{(n+2)=2*f(n+1) +f(n),
其中n 是大于0的整数,求(10)的值。那么fn()的函数体就应该改为如下形式：
def  fn(n):
    if  n == 20:
        return 1
    elif  n == 21:
        return  4
    else  :
        #在函数体中调用它自身,就是函数递归
        return    fn(n + 2)- 2 * fn(n + 1)

从上面的 fn() 函数来看,当程序要计算 fn(10) 的值时,fn(10) 等于 fn(12)-2 * fn(11)而 fn(11) 等 于fn(13)-2* fn(12)……依此类推,
直到fn(19)等于fn(21)-2*fn(20),此时就可以得到fn(19)的值,然后依次反算到fn(10)的值。
这就是递归的重要规则：对于求fn(10)而言,如果fn(0)和 fn(1) 是已知的,
则应该采用fn(n)=2*fn(n-1)+fn(n-2) 的形式递归,因为小的一端已知;
如果fn(20) 和fn(21)是已知的,则应该采用fn(n)=fn(n+2)-2*fn(n+1) 的形式递归,因为大的一端已知。

递归是非常有用的,例如程序希望遍历某个路径下的所有文件,但这个路径下的文件夹的深度是未知的,
那么就可以使用递归来实现这个需求。系统可定义一个函数,该函数接收一个文件路径作为参数,
该函数可遍历出当前路径下的所有文件和文件路径——在该函数的函数体中再次调用函数自身来处理该路径下的所有文件路径。
总之,只要在一个函数的函数体中调用了函数自身,就是函数递归。递归一定要向已知方向进行。
"""