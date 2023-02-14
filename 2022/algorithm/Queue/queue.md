## 1 队列
### 1.1 简单队列
队列是一种有次序的数据集合，其特征是新数据项的添加总发生在一端（通常称为“尾rear”端）；而现存数据项的移除总发生在另一端（通常称为“首front”端）。当一个元素被加入到队列之后，它就从队尾开始向队首前进，直到它成为下一个即将被移出队列的元素。


最新被加入的元素必须处于队尾，在队列停留最长时间的元素处于队首。这种原则有时候叫做“先进先出”（FIFO, first-in first-out），有时候也叫做“先到先服务”。

### 1.2 双端队列
双端队列（deque 或 double-ended queue）与队列类似，也是一系列元素的有序组合。其两端称为队首（front）和队尾（rear），元素在到达两端之前始终位于双端队列中。与队列不同的是，双端队列对元素添加和删除的限制不那么严格，元素可以从两端插入，也可以从两端删除。可以说，双端队列这种混合的线性数据结构拥有栈和队列各自拥有的所有功能。图3是一个由Python数据对象构成的双端队列。 应当指出，双端队列虽然具备栈和队列的许多特征，但其中的数据项不满足严格的“后进先出”或“先进先出”顺序，这使得插入和删除操作的规律性需要由用户自己维持。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/187f20e80da9444096e045a8ce3ad770.png#pic_center" width=48%><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图3 一个由 Python 数据对象构成的双端队列</div> </center>

## 2 队列的抽象数据类型
### 2.1 简单队列
抽象数据类型队列通过以下的一些结构和操作来定义。如前文所述，一个队列由一系列有序的元素构成，它们从叫做“队尾”的一端进入队列，再从叫做“队首”的另一端被移出队列。队列保持“先进先出”的特性。下面是队列的一些操作：
```python
Queue()：创建一个空队列对象，返回值为Queue对象；
enqueue(item)：将数据项item添加到队尾，无返回值；
dequeue()：从队首移除数据项，返回值为队首数据项，队列被修改；
isEmpty()：测试是否空队列，返回值为布尔值
size()：返回队列中数据项的个数。
```
我们需要决定列表的哪一端做队尾，哪一端用来做队首。下面的一段代码设定队列的队尾在列表的0位置。这使得我们能够利用列表的insert 功能来向队列的队尾添加新的元素。而pop操作则可以用来移除队首的元素（也就是列表的最后一个元素）。这也意味着enqueue的复杂度是O(n)，而dequeue的复杂度是O(1)。
```python
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):        # 复杂度O(n)
        self.items.insert(0, item)
    
    def dequeue(self):      # 复杂度O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)
```
## 2.2 双端队列
双端队列的定义的操作如下：
```python
Deque()：创建一个空双端队列
addFront(item)：将item加入队首
addRear(item)：将item加入队尾
removeFront()：从队首移除数据项，返回值为移除的数据项
removeRear()：从队尾移除数据项，返回值为移除的数据项
isEmpty()：返回deque是否为空
size()：返回deque中包含数据项的个数
```

```python
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
```

## 3 队列的应用
### 3.1 热土豆问题
首先，让我们来考虑一个叫做热土豆的儿童游戏。在这个游戏中（见图1）小孩子们围成一个圆圈并以最快的速度接连传递物品，并在游戏的一个特定时刻停止传递，这时手中拿着物品的小孩就离开圆圈，游戏进行至只剩下一个小孩。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/7fa47a861f554a68b2697d0bc9e3e208.png#pic_center" width=48%><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1 六人传土豆游戏</div> </center>

现在，我们也将热土豆问题称作Josephus问题。这个故事是关于公元1世纪著名历史学家Flavius Josephus 的，传说在犹太民族反抗罗马统治的战争中，Josephus 和他的39个同胞在一个洞穴中与罗马人相对抗。当注定的失败即将来临之时，他们决定宁可死也不投降罗马。于是他们围成一个圆圈，其中一个人被指定为第一位然后他们按照顺时针进行计数，每数到第七个人就把他杀死。传说中Josephus 除了熟知历史之外还是一个精通于数学的人。他迅速找出了那个能留到最后的位置。最后一刻，他没有选择自杀而是加入了罗马的阵营。这个故事还有许多不同的版本。有些是以三为单位进行计数，有些则是让最后一个留下的骑马逃走。但不管是哪个版本，其核心原理都是一致的。

求解思路：1）模拟程序采用队列来存放所有参加游戏的人名，按照传递土豆方向从队首排到队尾；游戏时，队首始终是持有土豆的人。2）模拟游戏开始，只需要将队首的人出队，随即再到队尾入队，算是土豆的一次传递；传递了num次后，将队首的人移除，不再入队如此反复，直到队列中剩余1人。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/aec224781b454d46bfaabd3231fefaa6.png#pic_center" width=48%><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图2 用队列模拟热土豆问题</div> </center>

**参考代码：**

```python
import Queue

def hot_potato(namelist, nums):
    sim_queue = queue.Queue()
    for name in namelist:
        sim_queue.enqueue(name)
    
    while sim_queue.size() > 1:
        for _ in range(nums):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
```
### 3.2 回文词判定

一个能用双端队列数据结构轻松解决的问题是经典的“回文词”问题。回文词指的是正读和反读都一样的词，如：radar、toot 和madam。我们想要编写一个算法来检查放入的字符串是否为回文词。

这个问题的解决方案是用一个双端队列来存储这个字符串。我们遍历这个字符串并把它的每个字母添加到双端队列的尾端。现在这个双端队列看起来非常像一个普通队列，但我们可以利用双端队列两端的对称性。双端队列的首端用来存储第一个字符，尾端用来存储最后一个字符。(如下图所示)
<img src ="https://img-blog.csdnimg.cn/87ae6f710dc4431389791760fc9d4a73.png#pic_center" width = 36%>


```python
import Deque

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
``