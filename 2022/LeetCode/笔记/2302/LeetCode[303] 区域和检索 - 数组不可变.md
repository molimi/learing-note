
## 1 区域和检索 - 数组不可变
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/6c311e9172d64af0ada626010b52f52f.png#pic_center" width = 80%>

题目链接：[https://leetcode.cn/problems/range-sum-query-immutable/](https://leetcode.cn/problems/range-sum-query-immutable/)

### 1.2 思路分析

最朴素的想法是存储数组 nums 的值，每次调用 sumRange 时，通过循环的方法计算数组 nums 从下标 $i$ 到下标 $j$ 范围内的元素和，需要计算 $j−i+1$ 个元素的和。由于每次检索的时间和检索的下标范围有关，因此检索的时间复杂度较高，如果检索次数较多，则会超出时间限制。

由于会进行多次检索，即多次调用 sumRange，因此为了降低检索的总时间，应该降低 sumRange 的时间复杂度，最理想的情况是时间复杂度 $O(1)$。为了将检索的时间复杂度降到 $O(1)$，需要在初始化的时候进行预处理。


注意到当 $i≤j$ 时，sumRange(i,j) 可以写成如下形式：

$$\begin{aligned} & \operatorname{sum} \operatorname{Range}(i, j) \\ = & \sum_{k=i}^j n u m s[k] \\ = & \sum_{k=0}^j n u m s[k]-\sum_{k=0}^{i-1} n u m s[k]\end{aligned}$$

由此可知，要计算 sumRange(i,j)，则需要计算数组 nums 在下标 $j$ 和下标 $i−1$ 的前缀和，然后计算两个前缀和的差。

如果可以在初始化的时候计算出数组 nums 在每个下标处的前缀和 nums_array，即可满足每次调用 sumRange 的时间复杂度都是 $O(1)$。

**示例代码：**

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = [0]            # 便于计算累加和
        for i in range(len(nums)):
            self.nums_array.append(self.nums_array[i] + nums[i])  # 计算nums累加和

    def sumRange(self, left: int, right: int) -> int:
        return self.nums_array[right+1] - self.nums_array[left]
````
下面以数组 [1, 12, -5, -6, 50, 3] 为例，展示了求 nums_array 的过程。

<img src ="https://img-blog.csdnimg.cn/4b31ae76da124c33816a1437e36a8b0c.gif#pic_center" width = 64%>



**复杂度分析**

时间复杂度：初始化 $O(n)$，每次检索 $O(1)$，其中 $n$ 是数组 nums 的长度。
初始化需要遍历数组 nums 计算前缀和，时间复杂度是 $O(n)$。

每次检索只需要得到两个下标处的前缀和，然后计算差值，时间复杂度是 $O(1)$。

空间复杂度：$O(n)$，其中 $n$ 是数组 nums 的长度。需要创建一个长度为 $n+1$ 的前缀和数组。


## 2 二维区域和检索 - 矩阵不可变
### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/b1d84fe0f1fb40a1bc34c6d625033739.png#pic_center" width = 80%>

题目链接：[https://leetcode.cn/problems/range-sum-query-2d-immutable/](https://leetcode.cn/problems/range-sum-query-2d-immutable/)


### 2.2 思路分析

这部分借鉴自：[笨猪爆破组的题解————从暴力法开始优化 「二维前缀和」做了什么事 | leetcode.304](https://leetcode.cn/problems/range-sum-query-2d-immutable/solution/er-wei-qian-zhui-he-jian-dan-tui-dao-tu-sqekv/)

