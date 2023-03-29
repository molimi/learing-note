## 1 两数之和
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/115c834af9a145adbf57f9f339ffcc3c.png#pic_center" width = 48%>

题目链接：[https://leetcode.cn/problems/two-sum/description/](https://leetcode.cn/problems/two-sum/description/)

### 1.2 求解思路

**1. 暴力枚举**
最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x

```python
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return [i, j]
```

**2. 哈希表**

创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = dict()
        for i, num in enumerate(nums):
            if target - num in hash_dict:
                return [hash_dict[target - num], i]
            else:
                hash_dict[num] = i
```


## 2 两数之和-输入有序数组
### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/e90b16c456204a99a476695f0cd0c172.png#pic_center" width = 48%>

题目链接：[https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)


### 2.2 思路分析

**1. 二分查找**

在数组中找到两个数，使得它们的和等于目标值，可以首先固定第一个数，然后寻找第二个数，第二个数等于目标值减去第一个数的差。利用数组的有序性质，可以通过二分查找的方法寻找第二个数。为了避免重复寻找，在寻找第二个数时，只在第一个数的右侧寻找。

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return [-1, -1]
```

**复杂度分析**
- 时间复杂度：$O(nlog⁡n)$，其中 $n$ 是数组的长度。需要遍历数组一次确定第一个数，时间复杂度是 $O(n)$，寻找第二个数使用二分查找，时间复杂度是 $O(logn)$，因此总时间复杂度是 $O(nlogn)$。
- 空间复杂度：$O(1)$。




**2. 双指针**

思路参考自————[一张图告诉你 O(n) 的双指针解法的本质原理](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/solutions/87919/yi-zhang-tu-gao-su-ni-on-de-shuang-zhi-zhen-jie-fa/?orderBy=most_votes)
为什么双指针往中间移动时，不会漏掉某些情况呢？

在这道题中，我们要寻找的是符合条件的一对下标 (i,j)(i, j)(i,j)，它们需要满足的约束条件是：
- i、j 都是合法的下标，即 $0 \leq i < n, 0 \leq j < n$
- i < j（题目要求）


而我们希望从中找到满足 $A[i] + A[j] == target$ 的下标 (i,j)。以 n=8 为例，这时候全部的搜索空间是：

<img src ="https://img-blog.csdnimg.cn/ccd6f26d1ceb41ccb9f510b6fd0e227d.jpeg#pic_center" width = 48%>

由于 $i、j$ 的约束条件的限制，搜索空间是白色的倒三角部分。可以看到，搜索空间的大小是 $O(n^2)$ 数量级的。如果用暴力解法求解，一次只检查一个单元格，那么时间复杂度一定是 $O(n^2)$。要想得到 $O(n)$ 的解法，我们就需要能够一次排除多个单元格。那么我们来看看，本题的双指针解法是如何削减搜索空间的：


一开始，我们检查右上方单元格 (0,7)，即计算 $A[0] + A[7]$，与 target 进行比较。如果不相等的话，则要么大于 target，要么小于 target。

<img src ="https://img-blog.csdnimg.cn/335b5249a1cd47409e99ad59dd70d3c3.jpeg#pic_center" width = 48%>

假设此时 $A[0] + A[7]$ 小于 target。这时候，我们应该去找和更大的两个数。由于 A[7] 已经是最大的数了，其他的数跟 A[0] 相加，和只会更小。也就是说 $A[0] + A[6] 、A[0] + A[5]、\cdots、A[0] + A[1]$ 也都小于 target，这些都是不合要求的解，可以一次排除。这相当于 $i=0$ 的情况全部被排除。对应用双指针解法的代码，就是 $i++$，对应于搜索空间，就是削减了一行的搜索空间，如下图所示。

<img src ="https://img-blog.csdnimg.cn/e5b35b130b324b4eb7fe9a9cba82cffa.jpeg#pic_center" width = 48%>

排除掉了搜索空间中的一行之后，我们再看剩余的搜索空间，仍然是倒三角形状。我们检查右上方的单元格 $(1,7)$，计算 $A[1] + A[7]$ 与 target 进行比较。

<img src ="https://img-blog.csdnimg.cn/192085754cf945e39bf2738466c28851.jpeg#pic_center" width = 48%>

假设此时 $A[0] + A[7]$ 大于 target。这时候，我们应该去找 和更小的两个数。由于 A[1] 已经是当前搜索空间最小的数了，其他的数跟 A[7] 相加的话，和只会更大。也就是说 $A[1] + A[7] 、A[2] + A[7]、\cdots、A[6] + A[7]$ 也都大于 target，这些都是不合要求的解，可以一次排除。这相当于 $j=0$ 的情况全部被排除。对应用双指针解法的代码，就是 $j++$，对应于搜索空间，就是削减了一列的搜索空间，如下图所示。

<img src ="https://img-blog.csdnimg.cn/b46f7ef8ae284f83abb89e97c87c0758.jpeg#pic_center" width = 48%>


可以看到，无论 $A[i] + A[j]$ 的结果是大了还是小了，我们都可以排除掉一行或者一列的搜索空间。经过 $n$ 步以后，就能排除所有的搜索空间，检查完所有的可能性。搜索空间的减小过程如下面动图所示：

<img src ="https://img-blog.csdnimg.cn/7475366987554fc5b03f81c7c4c09b4e.gif#pic_center" width = 48%>


```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail = 0, len(numbers)-1
        while head < tail:
            two_sum = numbers[head] + numbers[tail]
            if two_sum == target:
                return [head+1, tail+1]
            elif two_sum > target:
                tail -= 1
            else:
                head += 1
```

**复杂度分析**

- 时间复杂度：$O(n)$，其中 $n$ 是数组的长度。两个指针移动的总次数最多为 $n$ 次。
- 空间复杂度：$O(1)$。


## 3 三数之和
### 3.1 题目描述

<img src ="https://img-blog.csdnimg.cn/fddb00219fde407689a52836eac6282a.png#pic_center" width = 48%>

题目链接：[https://leetcode.cn/problems/3sum/](https://leetcode.cn/problems/3sum/)


### 3.2 思路分析

**1. 排序+双指针**
算法流程：
1. 特判，对于数组长度 $n$，如果数组为 `None` 或者数组长度小于 $3$，返回 []。
2. 对数组进行排序。
3. 遍历排序后数组：
    - 若 $nums[i]>0$：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
    - 对于重复元素：跳过，避免出现重复解令左指针 $L=i+1$，右指针 $R=n−1$，当 $L<R$ 时，执行循环：
        - 当 $nums[i]+nums[L]+nums[R]==0$，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 $L,R$ 移到下一位置，寻找新的解
        - 若和大于 0，说明 $nums[R]$ 太大，R 左移
        - 若和小于 0，说明 nums[L] 太小，L 右移

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []
        for i in range(len(nums_sorted)):
            if nums_sorted[i] > 0:                              # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
                return result
            '''
            # 错误去重a方法，将会漏掉-1,-1,2 这种情况
            if (nums[i] == nums[i + 1]) {
                continue;
            }
            '''
            if i>0 and nums_sorted[i] == nums_sorted[i-1]:      # 第一个数大于 0，后面的数都比它大，肯定不成立了
                continue
            left = i+1
            right = len(nums_sorted)-1
            while left < right:
                '''
                # 去重复逻辑如果放在这里，0，0，0 的情况，可能直接导致 right<=left 了，从而漏掉了 0,0,0 这种三元组
                while (right > left && nums[right] == nums[right - 1]) right--;
                while (right > left && nums[left] == nums[left + 1]) left++;
                '''
                if nums_sorted[i]+nums_sorted[left]+nums_sorted[right] == 0:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    # 在要增加 left，减小 right，但是不能重复，比如: [-2, -1, -1, -1, 3, 3, 3], 
                    # i = 0, left = 1, right = 6, [-2, -1, 3] 的答案加入后，需要排除重复的 -1 和 3
                    while left < right and nums_sorted[left] == nums_sorted[left+1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right-1]:
                        right -= 1
                    # 找到答案时双指针同时收缩
                    left += 1
                    right -= 1
                elif nums_sorted[i]+nums_sorted[left]+nums_sorted[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result
```


<img src ="https://img-blog.csdnimg.cn/e9c94225aa1a408b94283a30d59f118c.gif#pic_center" width = 48%>

**复杂度分析**
- 时间复杂度：$O(n^2)$，数组排序 $O(NlogN)$，遍历数组 $O(n)$，双指针遍历 $O(n)$，总体 $O(NlogN)+O(n)∗O(n)$，$O(n^2)$
- 空间复杂度：$O(1)$



## 4 四数之和
### 4.1 题目描述

<img src ="https://img-blog.csdnimg.cn/859ee016692d43629e0a6e59f6469c4f.png#pic_center" width = 48%>

题目链接：[https://leetcode.cn/problems/4sum/](https://leetcode.cn/problems/4sum/)


### 4.2 思路分析
**1. 排序 + 双指针**

最朴素的方法是使用四重循环枚举所有的四元组，然后使用哈希表进行去重操作，得到不包含重复四元组的最终答案。假设数组的长度是 $n$，则该方法中，枚举的时间复杂度为 $O(n^4)$，去重操作的时间复杂度和空间复杂度也很高，因此需要换一种思路。

为了避免枚举到重复四元组，则需要保证每一重循环枚举到的元素不小于其上一重循环枚举到的元素，且在同一重循环中不能多次枚举到相同的元素。

为了实现上述要求，可以对数组进行排序，并且在循环过程中遵循以下两点：
- 每一种循环枚举到的下标必须大于上一重循环枚举到的下标；
- 同一重循环中，如果当前元素与上一个元素相同，则跳过当前元素。

使用上述方法，可以避免枚举到重复四元组，但是由于仍使用四重循环，时间复杂度仍是 $O(n^4
)$。注意到数组已经被排序，因此可以使用双指针的方法去掉一重循环。

使用两重循环分别枚举前两个数，然后在两重循环枚举到的数之后使用双指针枚举剩下的两个数。假设两重循环枚举到的前两个数分别位于下标 $i$ 和 $j$，其中 $i<j$。初始时，左右指针分别指向下标 $j+1$ 和下标 $n−1$。每次计算四个数的和，并进行如下操作：
- 如果和等于 target，则将枚举到的四个数加到答案中，然后将左指针右移直到遇到不同的数，将右指针左移直到遇到不同的数；
- 如果和小于 target，则将左指针右移一位；
- 如果和大于 target，则将右指针左移一位。

使用双指针枚举剩下的两个数的时间复杂度是 $O(n)$, 因此总时间复杂度是 $O(n^3)$，低于 $O(n^4)$。

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []
        length = len(nums)
        for i in range(length): 
            # 剪枝处理
            if nums_sorted[i] > target and nums_sorted[i] >= 0:     # 只有满足target>=0或者nums_sorted>=[0]，必然不用遍历
                break
            # 对 nums_sorted[i] 去重
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            for j in range(i+1, length):        # 比原来多一层循环
                # 二级剪枝处理
                if nums_sorted[i] + nums_sorted[j] > target and nums_sorted[i] + nums_sorted[j] >= 0:
                    break   # 这里直接 return 会出错
                # 对 nums_sorted[j] 去重
                if j > i+1 and nums_sorted[j] == nums_sorted[j-1]:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    if nums_sorted[i] + nums_sorted[j] + nums_sorted[left] + nums_sorted[right] == target:
                        result.append([nums_sorted[i], nums_sorted[j], nums_sorted[left], nums_sorted[right]])
                        while left < right and nums_sorted[left] == nums_sorted[left+1]:
                            left += 1
                        while left < right and nums_sorted[right] == nums_sorted[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums_sorted[i] + nums_sorted[j] + nums_sorted[left] + nums_sorted[right] > target:
                        right -= 1
                    else:
                        left += 1
        return result
```

## 5 最接近的三数之和
### 5.1 题目描述

<img src ="https://img-blog.csdnimg.cn/b659a65060434092baf958d566165a36.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/3sum-closest/description/](https://leetcode.cn/problems/3sum-closest/description/)


### 5.2 思路分析

**1. 排序+双指针**

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sorted = sorted(nums)
        diff = float('inf')         # 初始化，因为找最小值，因此把初始值设置成实数的最大值
        length = len(nums)          # 排序是前提
        for i in range(length):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:    # 常见的剪枝操作
                continue
            left = i+1                                          # 双指针：指针对撞
            right = length-1 
            while left < right:
                temp = nums_sorted[left] + nums_sorted[right] + nums_sorted[i]
                if abs(temp-target) < diff:     
                    diff = abs(temp-target)
                    ans = temp
                # 不管是变小还是变大，尝试的作用是让 temp 与 target 更接近，即 temp 与 target 的绝对值之差越来越小
                if temp > target:        # 如果大了，尝试右边界收缩一格，让 temp 变小
                    right -= 1
                elif temp < target:     # 如果小了，尝试左边界收缩一格，让 target 变大
                    left += 1
                else:                   # 如果已经等于 target 的话, 肯定是最接近的，根据题目要求，返回这三个数的和
                    return target
        return ans
```
<img src ="https://img-blog.csdnimg.cn/4c1e5f8bccd24b64b5aa661e33078775.gif#pic_center" width = 64%>