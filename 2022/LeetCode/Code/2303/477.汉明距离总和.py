#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        '''两层遍历，分别统计总会超时'''
        ans = 0
        for i in range(32):
            temp = sum((num >> i) & 1 for num in nums)
            ans += temp * (len(nums) - temp)
        return ans
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i]^nums[j]
                while temp:
                    temp &= (temp-1)
                    ans += 1
        return ans
        '''
# @lc code=end

