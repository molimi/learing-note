## 1 区间加法
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/c48d4af553ac4de6ab9518b7ca4750e6.jpeg#pic_center" width = 64%>

### 1.2 求解思路

常规的思路很容易，给区间 nums[i: j] 加上 val，那就⼀个 for 循环给它们都加上呗，但这种思路的时间复杂度是 $O(N)$，由于这个场景下对 nums 的修改⾮常频繁，所以效率会很低下。

这⾥就需要差分数组的技巧，差分数组是与前缀和数组所对应的一种逆操作，类似于求导和积分，也就是说，对差分数组求前缀和，可以得到原数组，同样的，对前缀和数组求差分，也可以得到原数组。

差分数组的性质是：当我们希望对原数组的某一个区间[i, j]施加一个增量 inc 时，差分数组d对应的变化是：d[i]增加inc，d[j+1]减少inc，并且这种操作是可以叠加的。

下面举个例子：

<img src ="https://img-blog.csdnimg.cn/83077c9e4b54423397418b869910227b.png#pic_center" width = 64%>

差分数组是一个辅助数组，从侧面来表示给定某一数组的变化，一般用来对数组进行区间修改的操作。

还是上面那个表里的例子，我们需要进行以下操作：
1. 将区间[1，4]的数值全部加上3
2. 将区间[3，5]的数值全部减去5

很简单对吧，你可以进行枚举。但是如果给你的数据量是1e5，操作量1e5，限时1000ms你暴力枚举能莽的过去吗？慢到你怀疑人生直接。这时我们就需要使用到差分数组了。

其实当你将原始数组中元素同时加上或者减掉某个数，那么他们的差分数组其实是不会变化的。

利用这个思想，咱们将区间缩小，缩小的例子中的区间 [1,4] 吧这是你会发现只有 d[1] 和 d[5] 发生了变化，而 d[2], d[3], d[4]却保持着原样，

<img src ="https://img-blog.csdnimg.cn/9ecb494bbaf24dec92c88f3de9d2ab9e.png#pic_center" width = 64%>

进行下一个操作，

<img src ="https://img-blog.csdnimg.cn/1b8075b18478477bbb20549f422a0d6c.png#pic_center" width = 64%>

这时我们就会发现这样一个规律，当对一个区间进行增减某个值的时候，他的差分数组对应的区间左端点的值会同步变化，而他的右端点的后一个值则会相反地变化，其实这个很好理解。

本部分参考自：[差分详解+例题](https://blog.csdn.net/qq_44786250/article/details/100056975)


也就是说，当我们需要对原数组的不同区间施加不同的增量，我们只要按规则修改差分数组即可。所以，差分数组的主要适⽤场景是频繁对原始数组的某个区间的元素进⾏增减，但只能是区间元素同时增加或减少相同的数的情况才能用。

代码实现：
```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length+1)  # 末尾多个0，防止越界
        
        for update in updates:
            start, end, inc = update[0], update[1], update[2]
            diff[start] += inc
            diff[end + 1] -= inc
        
        for i in range(1, length):
            diff[i] += diff[i - 1]            # 对差分数组求前缀和便可得到原数组
            
        return diff[:-1]
```


## 2 航班预订统计
### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/a54af4c6c89f4c158159dd387ef5683e.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/corporate-flight-bookings/](https://leetcode.cn/problems/corporate-flight-bookings/)


### 2.2 代码实现
题⽬说的 n 是从 1 开始计数的，⽽数组索引从 0 开始，在构造差分数组时，需要相应的调整数组下标对应关系，这里在前面添加0，和三元组 (i, j, k)依次对应。

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for booking in bookings:
            start, end, inc = booking[0], booking[1], booking[2]
            diff[start] += inc
            if end < n:             # 没在末尾添加0，要判断一下边界
                diff[end+1] -= inc
        for i in range(1, n+1):
            diff[i] += diff[i-1]
        return diff[1:]
```

复杂度分析
- 时间复杂度：$O(n+m)$，其中 $n$ 为要求的数组长度，$m$ 为预定记录的数量。我们需要对于每一条预定记录处理一次差分数组，并最后对差分数组求前缀和。
- 空间复杂度：$O(1)$。




## 3 拼车
### 3.1 题目描述

<img src ="https://img-blog.csdnimg.cn/d57ec96324f5472db1e0f367d2b8707c.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/car-pooling/](https://leetcode.cn/problems/car-pooling/)


### 3.2 思路分析

1. 首先大致可以看出这也是数组子区间增减问题，使用数组画出来看一下，是否能用差分数组

2. 定义数组保存每一站车上人数，接客是对子区间全部元素加 n 运算，多次上下车后，看最终数组每一站人数是否超过capacity，超过则说明有乘客上不来

3. 注意：
- 接人影响的子区间为[start, end-1]，因为这批乘客在下车站已经下车了
- 0 <= trips[i][1] < trips[i][2] <= 1000，可以看出trips中start/end就是数组下标，这里可以直接定义差分数组大小，也可以使用循环找到最多有几站

以trips = [[2,1,5],[3,3,7]], capacity = 4为例，数组变化：

<img src ="https://img-blog.csdnimg.cn/e7e89be191ca4846b43c3b1b1ca9e797.png#pic_center" width = 64%>

4. 说明：

- 数组长度为8，表示全程 0~7 共8个站点，元素值表示在第i站车上人数
- 没有接人时为原数组，接人是对数组的修改
- 最后看每站人数是否超过capacity
- 因为3/4站人数超过capacity，说明到第3站有乘客上不来

5. 观察上面数组变化，可以看出是子区间内元素全部加 n，多次修改后求修改后数组的问题——典型的差分数组求解，对应差分数组变化：

<img src ="https://img-blog.csdnimg.cn/ef6da4a7baa445498d76c08c05bb0f72.png#pic_center" width = 64%>


```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * (1001)      # 题目中最多有1001个车站
        max_station = 0          # 找到车站数
        for trip in trips:
            inc, start, end = trip[0], trip[1], trip[2]
            diff[start] += inc
            diff[end] -= inc      # 第end站乘客已经下车，这里就不用end+1
            max_station = max(max_station, end)
        for i in range(1, max_station+1): # 进行区间求和
            diff[i] += diff[i-1]
        if max(diff[:max_station]) > capacity:
            return False
        return True
```