#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
<<<<<<< HEAD
#

=======
# 思路：双指针，快速查找
>>>>>>> 667449772d496b68931119ce29307e1155363522

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
<<<<<<< HEAD
        for i in range(len(nums)):
            for j in range(i, len(nums) - 1):
                if nums[j] == nums[i]:
                    nums[j] = nums[j + 1]


# @lc code=end
=======
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1
# @lc code=end

>>>>>>> 667449772d496b68931119ce29307e1155363522
