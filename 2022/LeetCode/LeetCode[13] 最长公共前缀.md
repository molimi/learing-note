## 1 最长公共前缀

### 1.1 题目描述
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

题目链接：[https://leetcode.cn/problems/longest-common-prefix/](https://leetcode.cn/problems/longest-common-prefix/)

### 1.2 思路分析
这道题目其实不难，但可以有多种求解思路，所以记录下来供自己学习

```python
from cmath import inf


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        if k == 1:  # 考虑间隔为1的情况
            max_value = max(nums)
        elif k == length:
            max_value = sum(nums)
        else:
            max_value = temp = sum(nums[:k])
            for i in range(k, len(nums)):
                temp = temp + nums[i] - nums[i-k]
                if max_value < temp:
                    max_value = temp
        return (max_value/k)
```