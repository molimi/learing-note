## 1 最大子数组之和
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/83fb20322365469ca197c67983291575.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/maximum-subarray/](https://leetcode.cn/problems/maximum-subarray/)

### 1.2 求解思路

**1. 暴力法**
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        max_sum = float('-inf')
        for i in range(length):
            sum_sub_array = 0
            for j in range(i, length):
                sum_sub_array += nums[j]
                max_sum = max(max_sum, sum_sub_array)
        return max_sum
```

<img src ="https://img-blog.csdnimg.cn/4a5c31becb264e0e9c3c3e3786ea309a.gif#pic_center" width = 64%>


**2. 动态规划**

**关键 1：理解题意**

题目要我们找出和最大的连续子数组的值是多少，「连续」是关键字，连续很重要，不是子序列。

题目只要求返回结果，不要求得到最大的连续子数组是哪一个。这样的问题通常可以使用「动态规划」解决。

**关键 2：如何定义子问题（如何定义状态）**

设计状态思路：把不确定的因素确定下来，进而把子问题定义清楚，把子问题定义得简单。动态规划的思想通过解决了一个一个简单的问题，进而把简单的问题的解组成了复杂的问题的解。

我们 不知道和最大的连续子数组一定会选哪一个数，那么我们可以求出 所有 经过输入数组的某一个数的连续子数组的最大和。


例如，示例 1 输入数组是 [-2,1,-3,4,-1,2,1,-5,4] ，我们可以求出以下子问题：

- 子问题 1：经过 −2 的连续子数组的最大和是多少；
- 子问题 2：经过 1 的连续子数组的最大和是多少；
- 子问题 3：经过 −3 的连续子数组的最大和是多少；
- 子问题 4：经过 4 的连续子数组的最大和是多少；
- 子问题 5：经过 −1 的连续子数组的最大和是多少；
- 子问题 6：经过 2 的连续子数组的最大和是多少；
- 子问题 7：经过 1 的连续子数组的最大和是多少；
- 子问题 8：经过 −5 的连续子数组的最大和是多少；
- 子问题 9：经过 4 的连续子数组的最大和是多少。

一共 9 个子问题，这些子问题之间的联系并没有那么好看出来，这是因为 子问题的描述还有不确定的地方（这件事情叫做「有后效性」，我们在本文的最后会讲解什么是「无后效性」）。

例如「子问题 3」：经过 −3 的连续子数组的最大和是多少。

「经过 −3 的连续子数组」我们任意举出几个：

- [-2,1,-3,4] ，−3 是这个连续子数组的第 3 个元素；
- [1,-3,4,-1] ，−3 是这个连续子数组的第 2 个元素；
- ……

我们不确定的是：−3 是连续子数组的第几个元素。那么我们就把 -3 定义成连续子数组的最后一个元素。在新的定义下，我们列出子问题如下：
- 子问题 1：以 −2 结尾的连续子数组的最大和是多少；
- 子问题 2：以 1 结尾的连续子数组的最大和是多少；
- 子问题 3：以 −3 结尾的连续子数组的最大和是多少；
- 子问题 4：以 4 结尾的连续子数组的最大和是多少；
- 子问题 5：以 −1 结尾的连续子数组的最大和是多少；
- 子问题 6：以 2 结尾的连续子数组的最大和是多少；
- 子问题 7：以 1 结尾的连续子数组的最大和是多少；
- 子问题 8：以 −5 结尾的连续子数组的最大和是多少；
- 子问题 9：以 4 结尾的连续子数组的最大和是多少。

我们加上了「结尾的」，这些子问题之间就有了联系。我们单独看子问题 1 和子问题 2：

- 子问题 1：以 −2 结尾的连续子数组的最大和是多少；
以 −2 结尾的连续子数组是 [-2]，因此最大和就是 −2。

- 子问题 2：以 1 结尾的连续子数组的最大和是多少；
以 1 结尾的连续子数组有 [-2,1] 和 [1] ，其中 [-2,1] 就是在「子问题 1」的后面加上 1 得到。$-2 + 1 = -1 < 1$，因此「子问题 2」 的答案是 1。

大家发现了吗，如果编号为 $i$ 的子问题的结果是负数或者 0 ，那么编号为 $i + 1$ 的子问题就可以把编号为 $i$ 的子问题的结果舍弃掉（这里 $i$ 为整数，最小值为 1 ，最大值为 8），这是因为：
- 一个数 a 加上负数的结果比 a 更小；
- 一个数 a 加上 0 的结果不会比 a 更大；
- 而子问题的定义必须以一个数结尾，因此如果子问题 i 的结果是负数或者 0，那么子问题 $i + 1$ 的答案就是以 nums[i] 结尾的那个数。

因为我们把子问题定义的更清楚，子问题之间的联系就容易观察到。这是我们定义子问题、定义状态的经验。

接下来我们按照编写动态规划题解的步骤，把「状态定义」「状态转移方程」「初始化」「输出」「是否可以空间优化」全都写出来。

定义状态（定义子问题）
dp[i]：表示以 nums[i] 结尾 的 连续 子数组的最大和。

说明：「结尾」和「连续」是关键字。

状态转移方程（描述子问题之间的联系）
根据状态的定义，由于 nums[i] 一定会被选取，并且以 nums[i] 结尾的连续子数组与以 $nums[i-1]$ 结尾的连续子数组只相差一个元素 nums[i] 。

假设数组 nums 的值全都严格大于 0，那么一定有 $dp[i] = dp[i - 1] + nums[i]$。

可是 $dp[i-1]$ 有可能是负数，于是分类讨论：
- 如果 $dp[i - 1] > 0$，那么可以把 nums[i] 直接接在 $dp[i - 1]$ 表示的那个数组的后面，得到和更大的连续子数组；
- 如果 $dp[i - 1] <= 0$，那么 nums[i] 加上前面的数 $dp[i - 1]$ 以后值不会变大。于是 dp[i] 「另起炉灶」，此时单独的一个 nums[i] 的值，就是 dp[i]。

以上两种情况的最大值就是 dp[i] 的值，写出如下状态转移方程：

$$
dp[i] =
\begin{cases}
dp[i - 1] + nums[i], & if \quad dp[i - 1] > 0 \\
nums[i], & if \quad dp[i - 1] \le 0
\end{cases}$$
​
记为「状态转移方程 1」。

状态转移方程还可以这样写，反正求的是最大值，也不用分类讨论了，就这两种情况，取最大即可，因此还可以写出状态转移方程如下：

$$dp[i] = \max \{nums[i],\; dp[i - 1] + nums[i]\}$$

记为「状态转移方程 2」。

友情提示：求解动态规划的问题经常要分类讨论，这是因为动态规划的问题本来就有「最优子结构」的特点，即大问题的最优解通常由小问题的最优解得到。因此我们在设计子问题的时候，就需要把求解出所有子问题的结果，进而选出原问题的最优解。



思考初始值
dp[0] 根据定义，只有 1 个数，一定以 nums[0] 结尾，因此 $dp[0] = nums[0]$。

思考输出
注意：

这里状态的定义不是题目中的问题的定义，不能直接将最后一个状态返回回去；

这个问题的输出是把所有的 `dp[0]、dp[1]、……、dp[n - 1]` 都看一遍，取最大值。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
```

进一步优化空间：

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        pre = 0
        res = nums[0]
        for i in range(size):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res
```

<img src ="https://img-blog.csdnimg.cn/d785fe3ad0ae4faca4492bfee165ee34.gif#pic_center" width = 64%>



**3. 贪心算法**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 时间复杂度：O(n), 遍历了一遍
        # 空间复杂度:O(1), 用了2个变量
        cur_sum=nums[0]
        max_sum=nums[0]
        # range范围是[1，len(nums)) 左开右闭，切记切记
        for i in range(1,len(nums)):
            # 若当前指针指向元素之前的和小于0，则丢弃此元素之前的数列(拖后腿的丢弃！！！)
            # 当前和=当前值 与 当前值+之前最大和 的比较中较大的那个、
            # 通俗易懂的理解：看当前这个值和之前数列的和，是否会拖当前这个值的后腿，如果扯后腿了说明没必要把之前的数列放到当前和，如果没有扯后腿则把最新的较大数放在当前和里面
            cur_sum=max(nums[i],cur_sum+nums[i])
            # 最大和=当前和 与 最大和 的比较中较大的那个
            # 通俗易懂的理解：当前和就相当于当前潜在的最大和，把原来的最大和 与当前的潜在最大和进行比较，如果当前和比较大，则更换最大和，否则不更换
            max_sum=max(cur_sum,max_sum)
        return max_sum
```

<img src ="https://img-blog.csdnimg.cn/7bdd6072212644bb911156d09f5ecb6a.gif#pic_center" width = 64%>


**4. 分治法**
连续子序列的最大和主要由这三部分子区间里元素的最大和得到：
- 第 1 部分：子区间 $[left, mid]$；
- 第 2 部分：子区间 $[mid + 1, right]$；
- 第 3 部分：包含子区间 $[mid , mid + 1]$ 的子区间，即 nums[mid] 与 nums[mid + 1] 一定会被选取。
对这三个部分求最大值即可

```python
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                   self.__max_sub_array(nums, mid + 1, right),
                   self.__max_cross_array(nums, left, mid, right))

    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max
```

<img src ="https://img-blog.csdnimg.cn/2e9190592d95469d82b2104d35502c66.gif#pic_center" width = 64%>

## 2 乘积最大子数组
### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/74be9ea8449a42e1bc17a487680e7134.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/maximum-product-subarray/description/](https://leetcode.cn/problems/maximum-product-subarray/description/)

### 2.2 求解思路

如果我们用 $f_{\max}(i)$ 来表示以第 $i$ 个元素结尾的乘积最大子数组的乘积，$a$ 表示输入参数 nums，那么根据前面「53. 最大子序和」的经验，我们很容易推导出这样的状态转移方程：

$$f_{\max}(i) = \max_{i = 1}^{n} \{ f(i - 1) \times a_i, a_i \}$$

它表示以第 $i$ 个元素结尾的乘积最大子数组的乘积可以考虑 $a_i$ 加入前面的 $f_{\max}(i - 1)$ 对应的一段，或者单独成为一段，这里两种情况下取最大值。求出所有的 $f_{\max}(i)$ 之后选取最大的一个作为答案。

**可是在这里，这样做是错误的。为什么呢？**

因为这里的定义并不满足「最优子结构」。具体地讲，如果 $a = \{ 5, 6, -3, 4, -3 \}$，那么此时 $⁡f_{\max}$ 对应的序列是 $\{ 5, 30, -3, 4, -3 \}$，按照前面的算法我们可以得到答案为 30，即前两个数的乘积，而实际上答案应该是全体数字的乘积。我们来想一想问题出在哪里呢？问题出在最后一个 −3 所对应的 $⁡f_{\max}$ 的值既不是 −3，也不是 $4 \times (-3)$，而是 $5 \times 6 \times (-3) \times 4 \times (-3)$。所以我们得到了一个结论：当前位置的最优解未必是由前一个位置的最优解转移得到的。

我们可以根据正负性进行分类讨论。

考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大。于是这里我们可以再维护一个 $f_{\min}(i)$，它表示以第 $i$ 个元素结尾的乘积最小子数组的乘积，那么我们可以得到这样的动态规划转移方程：

$$
    \begin{aligned}
        f_{\max}(i) &= \max_{i = 1}^{n} \{ f_{\max}(i - 1) \times a_i, f_{\min}(i - 1) \times a_i, a_i \} \\
        f_{\min}(i) &= \min_{i = 1}^{n} \{ f_{\max}(i - 1) \times a_i, f_{\min}(i - 1) \times a_i, a_i \}
    \end{aligned} 
$$

它代表第 $i$ 个元素结尾的乘积最大子数组的乘积 $f_{\max}(i)$，可以考虑把 $a_i$ 加入第 $i - 1$ 个元素结尾的乘积最大或最小的子数组的乘积中，二者加上 $a_i$，$i$ 个元素结尾的乘积最大子数组的乘积。第 $i$ 个元素结尾的乘积最小子数组的乘积 $f_{\min}(i)$ 同理。


```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp, min_dp = [nums[0]], [nums[0]]
        for i in range(1, len(nums)):
            max_dp.append(max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i]))
            min_dp.append(min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i]))

        return max(max_dp)
```

进一步优化：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''动态规划'''
        max_product, min_product, ans = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            max_nums, min_nums = max_product, min_product
            max_product = max(max_nums*num, min_nums*num, num)
            min_product = min(max_nums*num, min_nums*num, num)
            ans = max(ans, max_product)
        return ans
```
____

## 参考
- 经典动态规划问题（理解「无后效性」）：[https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/?orderBy=most_votes](https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/?orderBy=most_votes)