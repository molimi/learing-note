这个是`Numpy`的学习笔记(二)，记录在实际应用中经常碰到的函数。

1. np.where()
`np.where(condition, x, y)`有两种用法：
- 满足条件(condition)，输出x，不满足输出y。
- 只有条件 (condition)，没有x和y，则输出满足条件元素的坐标 (等价于`np.argwhere`)。这里的坐标以tuple的形式给出，通常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标。

示例：
```python
In [1]: import numpy as np
In [2]: array1 = np.random.randint(1, 10, 6)
In [3]: print(array1)
Out[3]: 
[3 3 2 6 7 2]
In [4]: np.where(array1 > 5, 1, -1)
Out[4]: 
[-1 -1 -1  1  1 -1]
In [5]: np.where(array1 > 5)
Out[5]: 
(array([3, 4], dtype=int64),)
In [6]: array1[np.where(array1 > 5)]
Out[6]: 
array([6, 7])
```
1. np.argwhere

查找按元素分组的非零数组元素的索引。
```python
np.argwhere(arr)
```
示例：
```python
In [7]: array2 = np.arange(6).reshape(2, 3)
In [8]: print(array2)
Out[8]: 
[[0 1 2]
 [3 4 5]]
In [9]: print(np.argwhere(array2 % 2 == 0))
Out[9]: 
[[0 0]
 [0 2]
 [1 1]]
In [10]: print(np.where(array2 % 2 == 0))
Out[10]: (array([0, 0, 1], dtype=int64), array([0, 2, 1], dtype=int64))
In [11]: array3 = np.array([0,1,1,0,0,1,1,0,0])
In [12]: np.argwhere(array3)
Out[12]:
array([[1],
       [2],
       [5],
       [6]], dtype=int64)

In [13]: np.argwhere(array3)[:, 0]
Out[13]: array([1, 2, 5, 6], dtype=int64)
```
说明：`np.argwhere`输出是一列元素，使用`[:,0]`变成一行元素。