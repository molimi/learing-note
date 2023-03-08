#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
# 暴力算法复杂度 n^2，那就双指针

# @lc code=start
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

# @lc code=end

