# 02-python列表类型不同操作的时间效率
# 程序 = 数据结构+算法
# 总结：算法是为了解决实际问题而设计的，数据结构是算法需要处理的问题载体
from timeit import Timer

def t1():
    li = []
    for i in range(1000):
        li.append(i)
timer1 = Timer('t1()','from __main__ import t1')
print("1-:",timer1.timeit(10)) # 执行10次的平均时间

def t2():
    li = []
    for i in range(1000):
        li += [i]
timer2 = Timer('t2()','from __main__ import t2')
print("2-:",timer2.timeit(1000))

def t3():
    li = [i for i in range(1000)]
timer3 = Timer('t3()','from __main__ import t3')
print("1-:",timer3.timeit(1000))

def t4():
    li = list(range(1000))
timer4 = Timer('t4()','from __main__ import t4')
print("4-:",timer4.timeit(1000))

def t5():
    li = []
    for i in range(1000):
        li.append(i)
timer5 = Timer('t5()','from __main__ import t5')
print("5-:",timer5.timeit(1000))

def t6():
    li = []
    for i in range(1000):
        li.extend([i]) # 从列表末尾加
timer6 = Timer('t6()','from __main__ import t6')
print("6-:",timer6.timeit(1000))

def t7():
    li = []
    for i in range(1000):
        li.insert(0,i) # 从列表头部加
timer7 = Timer('t7()','from __main__ import t7')
print("7-:",timer7.timeit(1000))
