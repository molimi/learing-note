#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
# 滑动窗口

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if min(nums) > target or sum(nums) < target:
            return 0
        min_len = inf
        head, tail = 0, 0
        total = 0
        while tail < len(nums):
            total += nums[tail]
            while total >= target:
                min_len = min(min_len, tail - head + 1)
                total -= nums[head]
                head += 1
            tail += 1

        return min_len
# @lc code=end

