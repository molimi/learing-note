#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        hash_dict = dict()
        for i, num in enumerate(nums):
            if target - num in hash_dict:
                return [hash_dict[target - num], i]
            else:
                hash_dict[num] = i
        '''
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums and nums.index(temp) != i:
                return [i, nums.index(temp)]
# @lc code=end

