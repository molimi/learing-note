#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums:
                index = nums.index(temp)
                if index != i:
                    break
        return [i, index]


# @lc code=end
