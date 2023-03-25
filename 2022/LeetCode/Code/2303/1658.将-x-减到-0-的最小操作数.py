#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''让窗口的值等于n-5，求最大窗口'''
        max_length, start = -1, 0
        sum_sub_array, max_sum = 0, sum(nums)-x
        for end, tail in enumerate(nums):
            sum_sub_array += tail
            while start <= end and sum_sub_array > max_sum:
                sum_sub_array -= nums[start]
                start += 1
            if sum_sub_array == max_sum:
                max_length = max(max_length, end-start+1)
        return len(nums)-max_length if max_length != -1 else -1
# @lc code=end

