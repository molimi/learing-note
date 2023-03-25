#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''滑动窗口'''
        if k <= min(nums):
            return 0
        ans, start, product = 0, 0, 1
        for end, tail in enumerate(nums):
            product *= tail
            while product >= k:
                product //= nums[start]
                start += 1
            ans += end - start + 1  # 数组累加
        return ans
# @lc code=end

