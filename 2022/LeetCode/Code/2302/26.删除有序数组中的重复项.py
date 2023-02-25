#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i, len(nums) - 1):
                if nums[j] == nums[i]:
                    nums[j] = nums[j + 1]


# @lc code=end
