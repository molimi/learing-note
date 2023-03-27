#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        # 写法一
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
        left, right = 0, len(nums)          # [left, right)
        while left < right:                 
            mid = left + ((right - left)>>1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        '''
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right -= 1
        return left if left < len(nums) and nums[left] == target else -1    # 最后要判断一下是否符合条件
# @lc code=end

