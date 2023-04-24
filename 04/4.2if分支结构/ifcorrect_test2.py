"""
1.  对于任何的ifelse语句,从表面上看,else后没有任何条件,或者elif后只有一个条件——但这不是真相,
因为else的含义是"否则"——else本身就是一个条件!这也是把if、else后的代码 块统称为条件执行体的原因, 
else的隐含条件是对前面条件取反。因此,上面代码实际上可改写为如下形式。
2.  此时就比较容易看出为什么会发生上面的错误。对于age>40  and  not(age>20)这个条件，又
可改写成age>40  and  age<=20,这样永远都不可能出现满足该条件的age。
对于age>60    &&!(age> 20)&&!(age>40&&!(age>20)) 这个条件，则更不可能出现满足该条件的age。
因此，程序永远都不会判断中年人和老年人的情形。
"""
age = 45
if age > 60 :
    print("老年人")
# 在原本的if条件中增加了else的隐含条件
if age > 40 and not(age >60) :
    print("中年人")
# 在原本的if条件中增加了else的隐含条件
if age > 20 and not(age > 60) and not(age > 40 and not(age >60)) :
    print("青年人")
