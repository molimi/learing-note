#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] and slow <= fast:         # 保证慢指针在快指针之后
                if nums[slow]:
                    slow += 1
                else:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
                    fast += 1
            else:
                fast += 1
        return nums
# @lc code=end

