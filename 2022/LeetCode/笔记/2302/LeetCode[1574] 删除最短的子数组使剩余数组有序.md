## 1 最长回文子串
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/c640eb9e930f45b3bdfcbf958f4a392d.png#pic_center" width = 64%>


题目链接：[https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/)


### 1.2 滑动窗口

**1. 枚举左端点，移动右端点**

核心思路：枚举 $\textit{left}$，增大 $\textit{right}$ 直到 $\textit{arr}[\textit{left}]\le\textit{arr}[\textit{right}]$，此时更新子数组长度的最小值。

<img src ="https://img-blog.csdnimg.cn/aeb66bf7b5bd4fd48e672df61c70320c.gif#pic_center" width = 48%>

**解疑答惑：**

问：为什么枚举一个新的 $\textit{left}$ 时，$\textit{right}$ 不会往左移？或者说，是否需要再次枚举之前枚举过的 $\textit{arr}[\textit{right}]$？

答：在向右移动时，由于 $\textit{arr}[\textit{left}]$ 和 $\textit{arr}[\textit{right}]$ 都是非递减的，所以 $\textit{right}$ 左侧之前枚举过的元素必然小于 $\textit{arr}[\textit{left}]$，无需再次枚举。这也是本题可以使用同向双指针（不定长滑动窗口）的前提。

问：在计算子数组长度时，我经常分不清下标是否要 +1 或 −1，请问如何解决？

答：第一，时刻把握住 $\textit{left}$ 和 $\textit{right}$ 的含义，对于本题来说是开区间 $(\textit{left},\textit{right})$，这两个指针指向的元素不能删除。第二，可以代入一些数据来验证，比如代入 $\textit{left}=1, \textit{right}=3$，此时只需要删除一个 $\textit{arr}[2]$，所以公式 $\textit{right}-\textit{left}-1$ 才是符合要求的。

问：为什么不用判断$\textit{left}<\textit{right}$，难道不会出现 $\textit{left}\ge\textit{right}$ 的情况吗？

答：由于提前判断了 $\textit{arr}$ 是非递减数组的情况，后面的循环 $\textit{left}$ 必定小于 $\textit{right}$。反证：如果某个时刻 $\textit{left}$ 达到了 $\textit{right}$，就说明整个数组是有序的，但这种情况已经提前判断了。

问：能不能先把 $\textit{left}$ 的最大值算出来，然后再去枚举 $\textit{left}$ 或 $\textit{right}$？

答：可以。根据对称性，这种做法和先算 $\textit{right}$ 的最小值的做法是一样的，只不过枚举的顺序相反而已。

```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:  # arr 已经是非递减数组
            return 0
        # 此时 arr[right-1] > arr[right]
        ans = right  # 删除 arr[:right]
        left = 0  # 枚举 left
        while left == 0 or arr[left - 1] <= arr[left]:
            while right < n and arr[right] < arr[left]:
                right += 1
            # 此时 arr[left] <= arr[right]，删除 arr[left+1:right]
            ans = min(ans, right - left - 1)
            left += 1
        return ans
```

**复杂度分析**
- 时间复杂度：$O(n)$，其中 $n$ 为 $\textit{nums}$ 的长度。虽然写了个二重循环，但是内层循环中对 $\textit{right}$ 加一的总执行次数不会超过 $n$ 次，所以总的时间复杂度为 $O(n)$。
- 空间复杂度：$O(1)$，仅用到若干额外变量。


**2. 枚举右端点，移动左端点**

核心思路：枚举 $\textit{right}$，增大 $\textit{left}$ 直到 $\textit{arr}[\textit{left}]>\textit{arr}[\textit{right}]$。在增大过程中去更新子数组长度的最小值。

<img src ="https://img-blog.csdnimg.cn/64f7cf1fc8254068949d3f722295ad76.gif#pic_center" width = 48%>

问：为什么枚举一个新的 $\textit{right}$ 时，$\textit{left}$ 不会往左移？或者说，是否需要再次枚举之前枚举过的 $\textit{arr}[\textit{left}]$？

答：在向右移动时，由于 $\textit{arr}[\textit{left}]$ 和 $\textit{arr}[\textit{right}]$ 都是非递减的，所以 $\textit{left}$ 左侧之前枚举过的元素必然小于等于 $\textit{arr}[\textit{right}]$，由于这样的子数组长度更长，无需再次枚举。这也是本题可以使用同向双指针（不定长滑动窗口）的前提。

问：为什么循环一定会结束？

答：代码中提前判断了 $\textit{arr}$ 已经是非递减数组的情况，所以后面的循环一定存在 $\textit{left}$，使得 $\textit{arr}[\textit{left}]>\textit{arr}[\textit{left}+1]$ 成立。

注：最坏情况下，当 $\textit{right}=n$ 时才会去移动 $\textit{left}$。
```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:  # arr 已经是非递减数组
            return 0
        # 此时 arr[right-1] > arr[right]
        ans = right  # 删除 arr[:right]
        left = 0
        while True:  # 枚举 right
            while right == n or arr[left] <= arr[right]:
                ans = min(ans, right - left - 1)  # 删除 arr[left+1:right]
                if arr[left] > arr[left + 1]:
                    return ans
                left += 1
            right += 1
```

**复杂度分析**
- 时间复杂度：$O(n)$，其中 $n$ 为 $\textit{nums}$ 的长度。虽然写了个二重循环，但是内层循环中对 $\textit{left}$ 加一的总执行次数不会超过 $n$ 次，所以总的时间复杂度为 $O(n)$。
- 空间复杂度：$O(1)$，仅用到若干额外变量。









## 参考
- 删除最短的子数组使剩余数组有序：[https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/2189149/dong-hua-yi-xie-jiu-cuo-liang-chong-xie-iijwz/](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/2189149/dong-hua-yi-xie-jiu-cuo-liang-chong-xie-iijwz/)