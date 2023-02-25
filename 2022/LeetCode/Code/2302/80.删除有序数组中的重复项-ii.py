#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 1, 2
        while fast < len(nums):
            if nums[fast] != nums[slow-1]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return  slow + 1

# @lc code=end

