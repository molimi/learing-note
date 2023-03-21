#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''return (sum(set(nums))*3-sum(nums)) // 2'''
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num >> i) & 1
            if sum % 3 == 1:
                ans |= 1 << i
        return ~(ans^0xffffffff) if sum % 3 == 1 else ans   //  # 看最后sum位接是否为1
# @lc code=end

