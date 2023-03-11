#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """这道题目考察排序知识，这里直接用sorted"""
        result_list = [num ** 2 for num in nums]
        return sorted(result_list)
# @lc code=end

