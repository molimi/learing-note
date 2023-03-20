#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        set1 = set(list(range(len(nums)+1)))
        set2 = set(sorted(nums))
        ans = list(set1.difference(set2))
        return ans[0]
        '''
        ans = 0
        for i, num in enumerate(nums):  # 此处 num 代表nums， i 代表原数组
            ans ^= i ^ num
        return ans ^ len(nums)          # 因为原数组比nums长度多1, 所有这里多异或了一次
# @lc code=end

