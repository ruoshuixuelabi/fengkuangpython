"""
14.3.2	运行和阻塞状态

如果处于就绪状态的线程获得了 CPU,  开始执行 run()方法的线程执行体,则该线程处于运行状态。
如果计算机只有一个 CPU, 那么在任何时刻只有一个线程处于运行状态。
当然,在一个具有多处理器的机器上,将会有多个线程并行(Parallel) 执行;当线程数大于处理器数时,依然会存在多个线程在同一个CPU 上轮换的情况。

当一个线程开始运行后,它不可能一直处于运行状态(除非它的线程执行体足够短,瞬间就执行结束了),
线程在运行过程中需要被中断,目的是使其他线程获得执行的机会,线程调度的细节取决于底层平台所采用的策略。
对于采用抢占式调度策略的系统而言,系统会给每一个可执行的线程一个小时间段来处理任务;
当该时间段用完后,系统就会剥夺该线程所占用的资源,让其他线程获得执行的机会。在选择下一个线程时,系统会考虑线程的优先级。

所有现代的桌面和服务器操作系统都采用抢占式调度策略,但一些小型设备如手机等则可能采用协作式调度策略,
在这样的系统中,只有当一个线程调用了它的sleep()或 yield()方法后才会放弃 其所占用的资源——
也就是必须由该线程主动放弃其所占用的资源。

当发生如下情况时,线程将会进入阻塞状态。
(1)线程调用 sleep()方法主动放弃其所占用的处理器资源。
(2)线程调用了一个阻塞式I/O方法,在该方法返回之前,该线程被阻塞。
(3)线程试图获得一个锁对象,但该锁对象正被其他线程所持有。关于锁对象的知识,后面将有更深入的介绍。
(4)线程在等待某个通知 (Notify)。

当前正在执行的线程被阻塞之后,其他线程就可以获得执行的机会。
被阻塞的线程会在合适的时候重新进入就绪状态,注意是就绪状态,而不是运行状态。
也就是说,被阻塞线程的阻塞解除后, 必须重新等待线程调度器再次调度它。

针对上面几种情况,当发生如下特定的情况时可以解除阻塞,让该线程重新进入就绪状态。
(1)调用sleep(方法的线程经过了指定的时间。
(2)线程调用的阻塞式I/O方法已经返回。
(3)线程成功地获得了试图获取的锁对象。
(4)线程正在等待某个通知时,其他线程发出了一个通知。

图14.3显示了线程状态转换图。

从图14.3中可以看出,线程从阻塞状态只能进入就绪状态,无法直接进入运行状态。
就绪和运行状态之间的转换通常不受程序控制,而是由系统线程调度所决定的,当处于就绪状态的线程获得处理器资源时,该线程进入运行状态;
当处于运行状态的线程失去处理器资源时,该线程进入就绪状态。

14.3.3	线程死亡

线程会以如下三种方式结束,结束后就处于死亡状态。
(1)run()方法或代表线程执行体的target函数执行完成,线程正常结束。
(2)线程抛出 一个未捕获的Exception或 Error。

注意：当主线程结束时,其他线程不受任何影响,并不会随之结束。一旦子线程启动起来后,它就拥有和主线程相同的地位,它不会受主线程的影响。

为了测试某个线程是否已经死亡,可以调用线程对象的 is_alive()方法,
当线程处于就绪、运 行、阻塞三种状态时,该方法将返回True;当线程处于新建、死亡两种状态时,该方法将返回False。

注意：不要试图对一个已经死亡的线程调用start()方法使它重新启动,死亡就是死亡, 该线程将不可再次作为线程运行。

下面程序尝试对处于死亡状态的线程再次调用start()方法。
"""
import threading


# 定义action函数准备作为线程执行体使用
def action(max):
    for i in range(100):
        print(threading.current_thread().name + " " + str(i))


# 创建线程对象
sd = threading.Thread(target=action, args=(100,))
for i in range(300):
    # 调用threading.current_thread()函数获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 启动线程
        sd.start()
        # 判断启动后线程的is_alive()值,输出True
        print(sd.is_alive())
    # 当线程处于新建、死亡两种状态时,is_alive()方法返回False
    # 当i > 20时,该线程肯定已经启动过了,如果sd.is_alive()为False时
    # 那就是死亡状态了
    if i > 20 and not (sd.is_alive()):
        # 试图再次启动该线程
        sd.start()
"""
上面程序中的粗体字代码试图在线程已死亡的情况下再次调用 start()方法来启动该线程。
运行上面程序,将引发 RuntimeError 异常,这表明处于死亡状态的线程无法再次运行。

注意：不要对处于死亡状态的线程调用start()方法,程序只能对处于新建状态的线程调用 start()方法,
对处于新建状态的线程两次调用 start()方法也是错误的。它们都会引发 RuntimeError 异常。

看到这里,可能有读者感觉Python的多线程编程有些似曾相识,有点类似于《疯狂Java讲义》中关于多线程的介绍。
的确如此,不要以为我写错了。实际上,Python 的多线程模型完全是借用 Java的。
在Python参考文档(https://docs.python.org/3/library/threading.html) 页面中有如下一段说明(已翻译为中文)。

该模块的设计是基于 Java 多线程模型的。在Java 多线程模型中,Lock 和 Condition是每个对象的基本行为
(作者注：其实这只是 Java 1.5 之前的默认行为, Java 1.5引入了独立的 Lock 和  Condition)。
在 Python中 ,Lock 和 Condition是独立的对象。
Python 的线程类只支持Java线程类的方法子集,目前Python的线程不支持优先级,不支持线程组,
线程不支持destroy()、stop()、suspend()、 resume()和interrupt()方法,Java线程类的静态方法通常对应于threading模块内的模块级函数。

从上面的介绍不难看出,如果有很好的Java多线程编程基础,那么学习Python多线程编程基本上毫无压力,因为它们大致是相同的。
(1)Java创建线程对象有两种方式：①创建Thread 子类的实例;
②以Runnable 或 Callable对象为target, 创建Thread对象。
Python创建线程对象同样有两种方式：①创建Thread子类 的实例；
②以指定函数为target, 创 建Thread对象。其中Java的 Runnable或 Callable对象的核心就是作为线程执行体的函数;
而由于Python直接支持函数编程,因此可以直接用函 数作为Thread的 target来创建线程对象。
(2)Java 的 Thread对象支持的方法, Python对象基本也支持。除了destroy()、stop()、suspend()、
resume()、interrupt()方法,这些方法在Java中早已标记为过时,同样不推荐使用。
(3)Java 的 Thread类支持的类方法(静态方法),在threading模块中以模块级函数存在。

因此,如果读者学习过《疯狂 Java 讲义》的多线程编程一章,那么学习本章内容将会非常轻松。
提示：虽然 IT 行业的编程语言有很多,但真正有变化的并不多,有时候无非就是一些小小的语法糖而已。
当真正学习到编程语言的本质之后,上手任何编程语言都非常快。
"""