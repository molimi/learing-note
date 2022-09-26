# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/16
@version: 0.1
@description: 对比列表不同操作的时间效率
"""
from timeit import Timer

def test1():
    """循环连接列表"""
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    """append方式"""
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    """列表推导式"""
    l = [i for i in range(1000)]

def test4():
    """range函数调用转成列表"""
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat %f seconds\n" % t1.timeit(number=1000))           # concat 1.077540 seconds

t2 = Timer("test2()", "from __main__ import test2")
print("append %f seconds\n" % t2.timeit(number=1000))           # append 0.049203 seconds

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension %f seconds\n" % t3.timeit(number=1000))    # comprehension 0.039851 seconds

t4 = Timer("test4()", "from __main__ import test4")
print("list range %f seconds\n" % t4.timeit(number=1000))       # list range 0.016467 seconds