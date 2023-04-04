#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp, min_dp = [nums[0]], [nums[0]]
        for i, num in enumerate(nums[1:], start=1):
            max_dp.append(max(max_dp[i-1]*num, min_dp[i-1]*num, num))
            min_dp.append(min(max_dp[i-1]*num, min_dp[i-1]*num, num))

        return max(max_dp)

# @lc code=end

