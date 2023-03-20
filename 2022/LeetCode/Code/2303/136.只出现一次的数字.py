#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''异或运算'''
        re = 0
        for num in nums:
            re ^= num
        return re
# @lc code=end

