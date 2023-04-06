## Python标准库模块之heapq与bisect

## 1 heapq
### 1.1 介绍

堆是非线性的树形的数据结构，有2种堆，最大堆与最小堆。Python 的`heapq` 模块默认的是最小堆。堆数据结构最重要的特征是 `heap[0]` 永远是最小的元素。
- 最大堆：树中父节点的值总是大于等于任意子节点的值
- 最小堆：树中父节点的值总是小于等于任意子节点的值

我们一般使用二叉堆来实现优先级队列，它的内部调整算法复杂度为 $log_N$

常用方法如下：

<table><thead><tr><th style="text-align:left"><div><div class="table-header"><p>heappush(heap,item)</p></div></div></th><th style="text-align:left"><div><div class="table-header"><p>往堆中插入一条新的值</p></div></div></th></tr></thead><tbody><tr><td style="text-align:left"><div><div class="table-cell"><p>heappop(heap)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>从堆中弹出最小值</p></div></div></td></tr><tr><td style="text-align:left"><div><div class="table-cell"><p>heapreplace(heap,item)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>从堆中弹出最小值，并往堆中插入item</p></div></div></td></tr><tr><td style="text-align:left"><div><div class="table-cell"><p>heappushpop(heap,item)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>Python3中的heappushpop更高级</p></div></div></td></tr><tr><td style="text-align:left"><div><div class="table-cell"><p>heapify(x)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>以线性时间将一个列表转化为堆</p></div></div></td></tr><tr><td style="text-align:left"><div><div class="table-cell"><p>merge(*iterables,key=None,reverse=False)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>合并对个堆，然后输出</p></div></div></td></tr><tr><td style="text-align:left"><div><div class="table-cell"><p>nlargest(n,iterable,key=None)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>返回可枚举对象中的n个最大值并返回一个结果集list</p></div></div></td></tr><tr><td style="text-align:left"><div><div class="table-cell"><p>nsmallest(n,iterable,key=None)</p></div></div></td><td style="text-align:left"><div><div class="table-cell"><p>返回可枚举对象中的n个最小值并返回一个结果集list</p></div></div></td></tr></tbody></table>


### 1.2 创建堆

heapq有两种方式创建堆， 一种是使用一个空列表，然后使用 `heapq.heappush()` 函数把值加入堆中，另外一种就是使用 `heap.heapify(list)` 转换列表成为堆结构

```python
import heapq

# 第一种
"""
函数定义：
heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆

print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]


# 第二种
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]
```

heapq 模块还有一个 `heapq.merge(*iterables)` 方法，用于合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器。类似于 `sorted(itertools.chain(*iterables))`，但返回的是可迭代的。输入的 list 无序，merge 后无序，若输入的 list有序，merge 后也有序


```python
"""
函数定义：
heapq.merge(*iterables)
    - Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
    - Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).
"""
nums1 = [32, 3, 5, 34, 54, 23, 132]
nums2 = [23, 2, 12, 656, 324, 23, 54]

ans = heapq.merge(nums1, nums2)
print(list(ans))        # [23, 2, 12, 32, 3, 5, 34, 54, 23, 132, 656, 324, 23, 54]
nums1 = sorted(nums1)
nums2 = sorted(nums2)

res = heapq.merge(nums1, nums2)
print(list(res))        # [2, 3, 5, 12, 23, 23, 23, 32, 34, 54, 54, 132, 324, 656]
```

heapq 里面没有直接提供建立大根堆的方法，可以采取如下方法：每次 push 时给元素加一个负号（即取相反数），此时最小值变最大值，反之亦然，那么实际上的最大值就可以处于堆顶了，返回时再取负即可。

```python
nums = []
for num in [1, 5, 20, 18, 10, 200]:
    heapq.heappush(nums, -num)
print(list(map(lambda x:-x, nums)))
```

### 1.3 访问堆内容

堆创建好后，可以通过 `heapq.heappop()` 函数弹出堆中最小值。

```python
import heapq
nums = [2, 43, 45, 23, 12]
heapq.heapify(nums)

print(heapq.heappop(nums))
# out: 2

# 如果需要所有堆排序后的元素
result = [heapq.heappop(nums) for _ in range(len(nums))]
print(result)
# out: [12, 23, 43, 45]
```

如果需要删除堆中最小元素并加入一个元素，可以使用 `heapq.heaprepalce()` 函数。



```python
import heapq

nums = [1, 2, 4, 5, 3]
heapq.heapify(nums)

heapq.heapreplace(nums, 23)

print([heapq.heappop(nums) for _ in range(len(nums))])
# out: [2, 3, 4, 5, 23]
```

`heappushpop(heap, item)`： heappush 方法和 heappop 方法的合体，先 `heappush(heap, item)`，再 `heappop(heap)`。

```python
nums = [20, 5, 1, 18, 200, 10]
heapq.heapify(nums)
heapq.heappushpop(nums, 100)
print([heapq.heappop(nums) for _ in range(len(nums))])      # [5, 10, 18, 20, 100, 200]
```

`heapq.heapreplace()` 与 `heapq.heappushpop()` 相反，先进行 `heappop()`，再进行`heappush()`。堆的大小不变。 如果堆为空则引发 IndexError。这个单步骤操作比依次执行`heappop() + heappush()` 更高效，并且在使用固定大小的堆时更为适宜。 `pop/push` 组合总是会从堆中返回一个元素并将其替换为 item。返回的值可能会比添加的 item 更大。 如果不希望如此，可考虑改用 `heappushpop()`。 它的 push/pop 组合会返回两个值中较小的一个，将较大的值留在堆中。




### 1.4 获取堆最大或最小值

如果需要获取堆中最大或最小的范围值，则可以使用 `heapq.nlargest()` 或 `heapq.nsmallest()` 函数

```python
"""
函数定义：
heapq.nlargest(n, iterable[, key])¶
    - Return a list with the n largest elements from the dataset defined by iterable. 
    - key if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower
    - Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
"""
import heapq

nums = [1, 3, 4, 5, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

"""
输出：
[5, 4, 3]
[1, 2, 3]
"""
```

这两个函数还接受一个key参数，用于dict或其他数据结构类型使用：

```python
import heapq
from pprint import pprint
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
pprint(cheap)
pprint(expensive)

"""
输出：
[{'name': 'YHOO', 'price': 16.35, 'shares': 45},
 {'name': 'FB', 'price': 21.09, 'shares': 200},
 {'name': 'HPQ', 'price': 31.75, 'shares': 35}]
[{'name': 'AAPL', 'price': 543.22, 'shares': 50},
 {'name': 'ACME', 'price': 115.65, 'shares': 75},
 {'name': 'IBM', 'price': 91.1, 'shares': 100}]
"""
```

### 1.5 堆排序

**方法一 (压入堆并出堆)**

```python
import heapq

def heap_sort(sequences):
    heap = []
    for seq in sequences:
        heapq.heappush(heap, seq)

    return [heapq.heappop(heap) for _ in range(len(heap))]
        
if __name__ == "__main__":
    li = [30,40,60,10,20,50]
    print(heap_sort(li))            # [10, 20, 30, 40, 50, 60]
```

**方法二 (使用nlargest或nsmallest)**


```python
li = [30,40,60,10,20,50]
# nlargest
n = len(li)
print ("nlargest:",heapq.nlargest(n, li))       #  nlargest: [60, 50, 40, 30, 20, 10]
# nsmallest
print ("nsmallest:", heapq.nsmallest(n, li))    # nsmallest: [10, 20, 30, 40, 50, 60]
```

**方法三 (使用heapify)**

```python
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]
```

若是从大到小排列，有两种方法：
- 先建立小根堆，然后每次`heappop()`，此时得到从小大的排列，再reverse
- 利用相反数建立大根堆，然后 `heappop(-元素)`。即 `push(-元素)`，`pop(-元素)`


### 1.6 优先队列

优先队列 是堆的常用场合，并且它的实现包含了多个挑战：
- 排序稳定性：你该如何令相同优先级的两个任务按它们最初被加入时的顺序返回？
- 如果优先级相同且任务没有默认比较顺序，则 (priority, task) 对的元组比较将会中断。
- 如果任务优先级发生改变，你该如何将其移至堆中的新位置？
- 或者如果一个挂起的任务需要被删除，你该如何找到它并将其移出队列？

针对前两项挑战的一种解决方案是将条目保存为包含优先级、条目计数和任务对象 3 个元素的列表。 条目计数可用来打破平局，这样具有相同优先级的任务将按它们的添加顺序返回。 并且由于没有哪两个条目计数是相同的，元组比较将永远不会直接比较两个任务。

不可比较任务问题的另一种解决方案是创建一个忽略任务条目并且只比较优先级字段的包装器类:

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
```

其余的挑战主要包括找到挂起的任务并修改其优先级或将其完全移除。 找到一个任务可使用一个指向队列中条目的字典来实现。

移除条目或改变其优先级的操作实现起来更为困难，因为它会破坏堆结构不变量。 因此，一种可能的解决方案是将条目标记为已移除，再添加一个改变了优先级的新条目：

```python
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
```

### 1.7 复杂度分析

**1. 各方法复杂度**
- `heapq.heapify(x)`: $O(n)$
- `heapq.heappush(heap, item)`: $O(log(n))$
- `heapq.heappop(heap)`: $O(log(n))$
即插入或删除元素时，所有节点自动调整，保证堆的结构的复杂度为 $O(log(n))$
- `heapq.nlargest(k, iterable)` 和 `nsmallest(k, iterable)`：$O(n*log(t))$

**2. 关于排序和取TopN时各方法的快慢比较**

在关于排序和取Top N值时，到底使用什么方法最快，python3 cookbook给出了非常好的建议：
- 当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest()。
- 仅仅想查找唯一的最小或最大(N=1)的元素的话，那么使用 min() 和 max() 函数。
- 如果 N 的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 (sorted(items)[:N] 或者是 sorted(items)[-N:])。


```python
# priority 优先级
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heappush 在队列 _queue 上插入第一个元素
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop 在队列 _queue 上删除第一个元素
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
```

调用 `push()` 方法，实现将列表转化为堆数据

插入的是元组，元组大小比较是从第一个元素开始，第一个相同，再对比第二个元素，我们这里采用的方案是如果优先级相同，那么就根据第二个元素，谁先插入堆中，谁的 index 就小，那么它的值就小

测试：

```python
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
```

输出：

```python
Item('bar')
Item('spam')
Item('foo')
```


## 2 bisect

`bisect` 库是 Python 标准库中的一部分，它提供了二分查找的功能。二分查找是一种在有序列表中查找某一特定元素的搜索算法。它的时间复杂度为 $O(\log n)$，比顺序查找的时间复杂度 $O(n)$ 要有效率。


在算法面试题中，二分法是个常考的题型。如果题目旨在让你实现二分法，还是需要自己手写。但是遇到一些并非是二分法为主体的题目，但是会用到二分法时，为了方便起见可以直接调用`bisect`方法，而无需手写二分法。而且`bisect`底层是用C实现的，会比直接用python手写二分法快。


bisect 库提供了 `bisect_left`、`bisect_right`、`insort_left`、`insort_right` 四个函数，用于在有序列表中查找或插入元素。

<table border="1" cellpadding="1" cellspacing="1" style="width:449px;"><tbody><tr><td style="width:135px;">名称</td><td style="width:311px;">功能</td></tr><tr><td style="width:135px;"><strong>bisect_left()</strong></td><td style="width:311px;"><strong>查找&nbsp;</strong>目标元素左侧插入点</td></tr><tr><td style="width:135px;"><strong>bisect_right()</strong></td><td style="width:311px;"><strong>查找&nbsp;</strong>目标元素右侧插入点</td></tr><tr><td style="width:135px;"><strong>bisect()</strong></td><td style="width:311px;">同&nbsp;bisect_right()</td></tr><tr><td style="width:135px;"><strong>insort_left()</strong></td><td style="width:311px;">查找目标元素左侧插入点，并保序地&nbsp;<strong>插入&nbsp;</strong>元素</td></tr><tr><td style="width:135px;"><strong>insort_right()</strong></td><td style="width:311px;">查找目标元素右侧插入点，并保序地&nbsp;<strong>插入&nbsp;</strong>元素</td></tr><tr><td style="width:135px;"><strong>insort()</strong></td><td style="width:311px;">同&nbsp;insort_right()</td></tr></tbody></table>

使用 bisect 模块的方法之前，须确保待操作对象是 有序序列，即元素已按 从大到小 / 从小到大 的顺序排列。

### 2.1 bisect_left

bisect_left 函数用于在有序列表中二分查找某一位置，使得在该位置插入指定元素后仍保持有序，返回该位置，如果元素已经存在，则返回它的左边位置。

函数原型如下：

```python
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
```
其中，a 是一个有序列表，x 是要查找的元素，lo 和 hi 是查找范围的左右边界，key 是一个函数，用于从列表中提取比较的键值。

```python
import bisect                           # 导入 bisect 库
a = [1, 2, 3, 3, 5, 6, 6, 6, 8, 10]     # 有序列表
print(bisect.bisect_left(a, 4))         # 查找元素 4 的位置 4
print(bisect.bisect_left(a, 6))         # 查找元素 6 的位置 5
```


### 2.2 bisect_right

bisect_right 函数用于在有序列表中二分查找某一位置，使得在该位置插入指定元素后仍保持有序，返回该位置，如果元素已经存在，则返回它的右边位置。

函数原型如下：

```python
bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
```

其中，a 是一个有序列表，x 是要查找的元素，lo 和 hi 是查找范围的左右边界，key 是一个函数，用于从列表中提取比较的键值。

示例：
```python
import bisect                           # 导入 bisect 库
a = [1, 2, 3, 3, 5, 6, 6, 6, 8, 10]     # 有序列表
print(bisect.bisect_right(a, 4))        # 查找元素 4 的位置 4
print(bisect.bisect_right(a, 6))        # 查找元素 6 的位置 8
```


除此之外，bisect_right 还可以简写为 bisect:

```python
import bisect                           # 导入 bisect 库
a = [1, 2, 3, 3, 5, 6, 6, 6, 8, 10]     # 有序列表
print(bisect.bisect(a, 4))              # 查找元素 4 的位置 4
print(bisect.bisect(a, 6))              # 查找元素 6 的位置 8
```


### 2.3 insort_left

insort_left 函数用于在有序列表中二分查找某一位置，使得在该位置插入指定元素后仍保持有序，然后将元素插入该位置，如果元素已经存在，则插入到它的左边位置。

函数原型如下：
```python
bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)
```

其中，a 是一个有序列表，x 是要插入的元素，lo 和 hi 是查找范围的左右边界，key 是一个函数，用于从列表中提取比较的键值。

示例：
```python
import bisect                                       # 导入 bisect 库
a = [1, 2, 3, 3, 5, 6, 6, 6, 8, 10]                 # 有序列表
bisect.insort_left(a, 4)                            # 插入元素 4
print(a)  # [1, 2, 3, 3, 4, 5, 6, 6, 6, 8, 10]
bisect.insort_left(a, 6)                            # 插入元素 6
print(a)  # [1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 8, 10]
```

### 2.4 insort_right

insort_right 函数用于在有序列表中二分查找某一位置，使得在该位置插入指定元素后仍保持有序，然后将元素插入该位置，如果元素已经存在，则插入到它的右边位置。

函数原型如下：

```python
bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)
```

其中，a 是一个有序列表，x 是要插入的元素，lo 和 hi 是查找范围的左右边界，key 是一个函数，用于从列表中提取比较的键值。

示例：
```python
import bisect                                   # 导入 bisect 库
a = [1, 2, 3, 3, 5, 6, 6, 6, 8, 10]             # 有序列表
bisect.insort_right(a, 4)                       # 插入元素 4
print(a)  # [1, 2, 3, 3, 4, 5, 6, 6, 6, 8, 10]
bisect.insort_right(a, 6)                       # 插入元素 6
print(a)  # [1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 8, 10]
```

除此之外，insort_right 还可以简写为 insort ：

```python
import bisect                               # 导入 bisect 库
a = [1, 2, 3, 3, 5, 6, 6, 6, 8, 10]         # 有序列表
bisect.insort(a, 4)                         # 插入元素 4
print(a)  # [1, 2, 3, 3, 4, 5, 6, 6, 6, 8, 10]
bisect.insort(a, 6)                         # 插入元素 6
print(a)  # [1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 8, 10]
```

`insort` 函数的实质是调用 `bisect` 函数获取插入位置，然后调用 `list.insert` 函数将元素插入到该位置。

_____

## 参考

- Python标准库模块之heapq：[https://www.jianshu.com/p/801318c77ab5](https://www.jianshu.com/p/801318c77ab5)
- heapq --- 堆队列算法：[https://docs.python.org/zh-cn/3/library/heapq.html](https://docs.python.org/zh-cn/3/library/heapq.html)
- bisect --- 数组二分查找算法：[https://docs.python.org/zh-cn/3/library/bisect.html](https://docs.python.org/zh-cn/3/library/bisect.html)
- Python 二分查找之bisect库的使用详解：[https://www.likecs.com/show-308653910.html](https://www.likecs.com/show-308653910.html)