#
# @lc app=leetcode.cn id=1330 lang=python3
#
# [1330] 翻转子数组得到最大的数组值
#

# @lc code=
from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        '''暴力法，超时'''
        base, d = 0, 0
        length = len(nums)
        for i in range(length-1):
            base += abs(nums[i]-nums[i+1])
        for i in range(length):
            for j in range(i+1, length):
                if i == 0 and j == length-1:
                    temp = 0
                elif i ==  0:
                    temp = abs(nums[i] - nums[j+1]) - abs(nums[j] - nums[j+1])
                elif j == length-1:
                    temp = abs(nums[i-1] - nums[j]) - abs(nums[i-1] - nums[i])
                else:
                    temp = abs(nums[i-1] - nums[j]) + abs(nums[i] - nums[j+1]) - abs(nums[j] - nums[j+1]) - abs(nums[i-1] - nums[i])
                d = max(d, temp)
        return base + d if d > 0 else base


s = Solution()
s.maxValueAfterReverse([2, 3, 1, 5, 4])
# @lc code=end

