Python Typing模块-类型注解




## 1 itertools模块
在Python中，迭代器（Iterator）是常用来做惰性序列的对象，只有当迭代到某个值的时候，才会进行计算得出这个值。因此，迭代器可以用来存储无限大的序列，这样我们就不用把他一次性放在内存中，而只在需要的时候进行计算。所以，对于读取大文件或者无线集合，最好是使用迭代器。实际上，Python2的大多数函数都是返回列表等序列，而Python3都已经改进为返回迭代器。

Python的内置模块itertools就是用来操作迭代器的一个模块，包含的函数都是能够创建迭代器来用于for循环或者next()。其中函数主要可以分为三类，分别是无限迭代器，有限迭代器，组合迭代器。

### 1.1 无限迭代器（Infinite Iterators）
有时间来补
[https://zhuanlan.zhihu.com/p/51003123](https://zhuanlan.zhihu.com/p/51003123)



### 1.2 组合迭代器（Combinatoric Iterators）



### 1.3 有限迭代器（Iterators Terminating on the Shortest Input Sequence）



### 1.4 itertools.islice

`itertools.islice`的基本用法为：
```python
itertools.islice(iterable, start, stop[, step])
```
可以返回从迭代器中的start位置到stop位置的元素。如果stop为None，则一直迭代到最后位置。
例子；
```python
from itertools import islice
islice('ABCDEFG', 2)        # 返回一个迭代器：<itertools.islice at 0x108c29b88>，遍历返回：A B
islice('ABCDEFG', 2， 4)    # 遍历返回：C D
islice('ABCDEFG', 2, None)  # 遍历返回: C D E F G
```

