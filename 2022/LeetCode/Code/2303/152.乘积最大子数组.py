#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''动态规划，既存在正数又存在负数'''
        max_product, min_product, ans = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            max_nums, min_nums = max_product, min_product
            max_product = max(max_nums*num, min_nums*num, num)
            min_product = min(max_nums*num, min_nums*num, num)
            ans = max(ans, max_product)
        return ans

# @lc code=end

