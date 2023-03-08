#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
# 思路一：统计0和1出现的次数，直接把数组重新赋值
# 思路二：单指针，依次交换位置

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, p0, p1 = 0, 0 , len(nums)-1
        while i <= p1:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 -= 1
            else:
                i += 1

# @lc code=end

