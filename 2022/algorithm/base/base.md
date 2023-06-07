---
title: Python数据结构与算法篇（一）-- 算法分析基础
author: Carpe Diem
top: false
abbrlink: db7d7796
date: 2023-06-06 15:31:11
tags:
categories:
- Python
- 算法与数据结构
description:
img:
cover:
coverImg:
---

近期在学习《数据结构与算法分析Python》，本篇主要介绍算法分析的基础，介绍Python中List和Dic常用操作的时间复杂度，最后用一个变位词的例子比较不同算法的复杂度。

<!--more-->

## 1 前言

算法分析主要就是从计算资源消耗的角度来评判和比较算法，更高效利用计算资源，或者更少占用计算资源的算法，就是好算法。计算资源主要分为两种，一种是算法解决问题过程中需要的存储空间或内存，另一种是算法的执行时间。


**温馨提示：** 存储空间受到问题自身数据规模的变化影响要区分哪些存储空间是问题本身描述所需，哪些是算法占用，这个不容易


算法复杂度表示法：
- 大O(n)表示法：表示了所有上限中最小的那个上限
- 大Ω表示法：表示了所有下限中最大的那个下限
- 大θ表示法：如果上下限相同，那么就可以用大θ表示

算法：解决问题的方法和步骤
- 评价算法的好坏：渐近时间复杂度和渐近空间复杂度。
- 渐近时间复杂度的大O标记：
  - $O(c)$- 常量时间复杂度 - 布隆过滤器 / 哈希存储
  - $O(log_2n)$ - 对数时间复杂度 - 折半查找（二分查找）
  - $O(n)$ - 线性时间复杂度 - 顺序查找 / 计数排序
  - $O(n*log_2n)$ - 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
  - $O(n^2)$ - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
  - $O(n^3)$ - 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
  - $O(2^n)$ - 几何级数时间复杂度 - 汉诺塔
  - $O(n!)$ - 阶乘时间复杂度 - 旅行经销商问题 - NPC

<p><center class = "half"><img src ="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/005.522kgotj5gs0.webp#pic_left" width = "48%"><img src = "https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/006.wrpp4q8w3s0.webp#pic_left"  width = "48%"></center></p>


## 2 Python数据类型的性能
list类型各种操作（interface）的实现方法有很多，如何选择具体哪种实现方法？
总的方案就是，让最常用的操作性能最好，牺牲不太常用的操作
80/20。准则：80%的功能其使用率只有20%
List基本操作的大O数量级
|Operation | Big-O Efficiency |
|--|--|
| index[] | O(1) |
| index assignment | O(1) |
| append | O(1) |
| pop() |O(1)  |
| pop(i) | O(n) |
| insert(i, item) | O(n)  |
| del operator | O(n)  |
| iteration | O(n)  |
| contains(in) | O(n)  |
| get slice[x:y] |  O(k) |
| del slice  |  O(n) |
| set slice | O(n+k)  |
| reverse |  O(n) |
| concatenate |  O(k) |
| sort | O(nlogn)  |
| multiply |  O(nk)  |

字典与列表不同，根据关键码（key）找到数据项，而列表是根据位置（index）。最常用的取值get和赋值set，其性能为O(1)；另一个重要操作`contains(in)`是判断字典中是否存在某个关键码（key），这个性能也是O(1)
Dict基本操作的大O数量级
|Operation | Big-O Efficiency |
|--|--|
| copy | O(n) |
| get item | O(1) |
| set item | O(1) |
| delete item |O(1)  |
| contains (in) | O(1) |
| iteration | O(n)  |

更多，请参考Python官方的算法复杂度网站：[https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

**例子**
timeit模块对函数计时：创建一个Timer对象，指定需要反复运行的语句和只需要运行一次的“安装语句”；然后调用这个对象的timeit方法，其中可以指定反复运行多少次，如下：
```python
from timeit import Timer
t = Timer("函数名()","from __main__ import 函数名")
print(“%f seconds\n” % t.timeit(number = 1000))
```

```python
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
```
结论：由于不同计算机，运算时间有差异，但可以发现：列表连接（concat）最慢，List range最快，速度相差近100倍，append也要比concat快得多


## 3 线性结构
线性结构是一种有序数据项的集合，其中每个数据项都有唯一的前驱和后继，除了第一个没有前驱，最后一个没有后继，新的数据项加入到数据集中时，只会加入到原有某个数据项之前或之后，具有这种性质的数据集，就称为线性结构。

不同线性结构的关键区别在于数据项增减的方式，有的结构只允许数据项从一端添加，而有的结构则允许数据项从两端移除。

接下来学习的主要是栈Stack，队列Queue，双端队列Deque和列表List


## 4 案例分析

案例一：“变位词”判断问题
问题描述：所谓“变位词”是指两个词之间存在组成字母的重新排列关系，如heart和earth，python和typhon，这里为了降低难度：假设参与判断的两个词仅由小写字母构成，而且长度相等。

解题目标：写一个bool函数，以两个词作为参数，返回这两个词是否变位词

**1. 检查标记**
（1）每个位置进行比对，用字符串1的字符遍历字符串2，检查标记一个字符要用特定值None 来代替，作为标记。然而，由于字符串不可变，首先要把第二个字符串转化成一个列表。第一个字符串中的每一个字符都可以在列表的字符中去检查，如果找到，就用None 代替以示标记。算法复杂度：$O(n^2)$

参考代码：
```python
def anagram_solution(s1, s2):
    a_list = list(s2)
    still_ok = True
    pos1 = 0
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == a_list[pos2]:
                a_list[pos2] = None
                found = True
            else:
                pos2 += 1

        if found:
            pos1 += 1
        else:
            still_ok = False
    return still_ok

def main():
    print(anagram_solution('abcd', 'cadb'))           # True
    print(anagram_solution('abababa', 'abab'))        # False    
    print(anagram_solution('abgsgg', 'ababjjsj'))     # False    

main()
```

**2. 排序比较法**

尽管s1和s2并不相同，但若为变位词它们一定包含完全一样的字符，利用这一特点，我们可以采用另一种方法。我们首先从a到z给每一个字符串按字母顺序进行排序，如果它们是变位词，那么我们将得到两个完全一样的字符串。此外，我们可以先将字符串转化为列表，再利用Python 中内建的`sort`方法对列表进行排序。下面代码展示了这种方法。由于用到排序算法，所以算法复杂度为$O(nlogn)$。
参考代码：
```python
def anagram_solution(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)
    a_list1.sort()
    a_list2.sort()
    return (a_list1 == a_list2)   # 排序后比较

def main():
    print(anagram_solution('abcde', 'edcba'))       # True
    print(anagram_solution('abcd', 'edcba'))        # False
    print(anagram_solution('abababab', 'abab'))     # False

main()
```

**3. 暴力匹配法**
解决这个问题的典型暴力方法是尝试所有的可能。为了解决变位词检测问题，我们可以简单地构造一个由s1中所有字符组成的所有可能的字符串的列表，并检查s2是否在列表中。然而这个方法有一个困难之处。当我们构造由s1中字符组成的所有可能字符串时，第一个字符有n个可能，第二个字符有n-1种可能，第三个则是n-2种，以此类推。所有可能字符串的总数是$n*(n-1)*(n-2)*...*3*2*1$。也就是n!。尽管这些字符串中的一些可能是重复的，但程序不能提前预见到，所以还是会产生$n!$个字符串。看前言里的算法复杂度，就知道$O(n!)$增长比$O(2^n)$还要快。


4. 计数比较法

解决变位词问题的最后一个方法利用了任何变位词都有相同数量的a，相同数量的b，相同数量的c等等。为判断两个字符串是否为变位词，我们首先计算每一个字符在字符串中出现的次数。由于共有26个可能的字符，我们可以利用有26 个计数器的列表，每个计数器对应一个字符。每当我们看到一个字符，就在相对应的计数器上加一。最终，如果这两个计数器列表相同，则这两个字符串是变位词。下面展示了这种方法：

```python
def count(s):
    count_list = [0] * 26
    for i in range(len(s)):
        pos = ord(s[i]) - ord('a')
        count_list[pos] += 1
    return count_list

def anagram_solution(s1, s2):
    return count(s1) == count(s2)

def main():
    print(anagram_solution('apple', 'pleap'))                   # True
    print(anagram_solution('abd', 'ggsabad'))                   # False
    print(anagram_solution('abab', 'bbaa'))                     # True
    print(anagram_solution('gsgddjkdsdgds', 'dsdgdsgsgddjk'))   # True

main()
```

这个方法有一些循环操作。然而不同于第一个方法，所有循环都不是嵌套的。前两个计数字符数的循环都是n重。而因为字符串中总共有26种可能的字符，第三个比较两个计数列表的循环总是执行26步。把它们全部加起来就得到$T(n)=2n+26$，也就是$O(n)$。这样，我们就找到了一个解决这个问题的线性复杂度的算法。

**小结**
关于空间需求，尽管最后一个方法可以以线性的时间复杂度来运行，但是这是以使用了额外的空间来存储两个计数器列表为代价的。换句话说，这个算法牺牲了空间来换取时间。这是一个常见的现象。很多情况下你需要在时间和空间的权衡中做出选择。在这个例子中，额外的空间消耗并不足道。但是如果可能的字母多达几百万种，这将是一个问题。作为一个计算机科学家，当要做出算法选择时，需要你根据具体问题来决定利用计算资源的最好方式。



线性结构：线性结构是-种有序数据项的集合，其中每个数据项都有唯一的前驱和后继（数据集）

## 2 栈
1、栈Stack ：栈顶和栈底，栈的特性：反转次序，后进先出（主要应用：网页、word编辑）
抽象数据类型“栈”定义为如下的操作：（默认左端为栈底，右端为栈顶）

```python
Stack( )：创建一个空栈，不包含任何数据项
push(item)：将item加入栈顶，无返回值，append()
pop( )：将栈顶数据项移除，并返回，栈被修改pop()
peek( ):“窥视” 栈顶数据项，返回栈顶的数据项但不移除，栈不被修改。
isEmpty( )：返回栈是否为空栈
size( )：返回栈中有多少个数据项
```

栈的应用：简单括号匹配（最后打开的右括号必须与第一个左括号匹配），十进制转换为二进制。

中缀表达式（优先级），前后缀表达式转换，所以在很多情况下，表达式的计算机表示都避免用复杂的中缀形式；在前缀和后缀表达式中，操作符的次序完全决定了运算的次序，不再有混淆
所以说，无论表达式多复杂，需要转换成前缀或者后缀，只需要两个步骤：将中缀表达式转换为全括号形式；将所有的操作符移动到子表达式所在的左括号(前缀)或者右括号(后缀)处，替代之，再删除所有的括号

## 3 队列
2、队列Queue ，队列是一种有次序的数据集合，其特征是新数据项的添加总发生在一端(通常为“尾rear”端)，而现存数据项的移除总发生在另一端(通常称为首front”端)，原则：先进先出，队列仅有一个入口和一个出口。（主要应用：打印队列，进程调度，键盘缓冲，）主要适用于实际模拟仿真
抽象数据类型Queue由如下操作定义：（默认左端为队尾，右端为队首）

```python
Queue( )：创建一个空队列对象，返回值为Queue对象
enqueue(item)：将数据项item添加到队尾，无返回值insert(0,item)  复杂度O(n)
dequeue( )：从队首移除数据项，返回值为队首数据项，队列被修改复杂度O(1)
isEmpty( )：测试是否空队列，返回布尔值
size( )：返回队列中数据项的个数
```

3、双端队列Deque：一种有次序的数据集，跟队列相似，其两端可以称作“首“”“尾”端，但deque中数据项既可以从队首加入，也可以从队尾加入；数据项也可以从两端移除。某种意义上说，双端队列集成了栈和队列的能力。（应用：回文词判定）
deque定义的操作如下：
```python
Deque()：创建一个空双端队列
addFront(item)：将item加入队首
addRear(item)：将item加入队尾
removeFront( )：从队首移除数据项，返回值为移除的数据项
removeRear( )：从队首移除数据项，返回值为移除的数据项
isEmpty( )：返回deque是否为空
size( )：返回deque中包含数据项的个数
```


4、无序表List：一种数据项按照相对位置存放的数据集。操作如下：
```python
List( )：创建一个空列表
add(item)：添加一个数据项到列表中，假设item原先不存于列表中
remove(item)：从列表中移除item，列表被修改，item原先应存在于列表中
search(item)：在列表中查找item，返回布尔类型值
isEmpty( )：返回列表是否为空
size( )：返回列表包含了多少数据项
append(item)：添加一个数据项到列表末尾，假设item原先不存在于列表中
index(item)：返回数据项在表中的位置
insert(pos,item)：将数据项插入到位置pos，假设item原先不存在列表中，同时原列表具有足够多个数据项，能让item占据位置pos
pop( )：从列表末尾移除数据项，假设原列表至少有一个数据项
pop(pos)：移除位置为pos的数据项，假设原列表存在位置pos
```

列表List（数据项的增减方式不同）
采用链表实现无序表，数据项存放位置并没有规则，但如果在数据项之间建立链接指向，就可以保持其前后相对位置。链表实现的最基本元素是节点Node（包含数据项本身，以及指向下一个节点的引用信息）。
有序表OrderedList：有序表是一种数据项依照其某可比性质(如整数大小、字母表先后)来决定在列表
中的位置。操作如下：


```python
OrderedList( )：创建一个空列表
add(item)：添加一个数据项到列表中，假设item原先不存于列表中
remove(item)：从列表中移除item，列表被修改，item原先应存在于列表中
search(item)：在列表中查找item，返回布尔类型值
isEmpty( )：返回列表是否为空
size( )：返回列表包含了多少数据项
index(item)：返回数据项在表中的位置
pop( )：从列表末尾移除数据项，假设原列表至少有一个数据项
pop(pos)：移除位置为pos的数据项，假设原列表存在位置pos
```