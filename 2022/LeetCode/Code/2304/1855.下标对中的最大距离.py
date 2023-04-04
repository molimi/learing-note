#
# @lc app=leetcode.cn id=1855 lang=python3
#
# [1855] 下标对中的最大距离
#

# @lc code=start
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(nums, target, left, right):
            while left < right:
                mid = (left + right)//2
                if nums[mid] < target:
                    right = mid
                else:
                    left = mid + 1
            return left-1

        length = len(nums2)
        ans = 0
        for i, num in enumerate(nums1):
            ind = binary_search(nums2, num, i, length)
            ans = max(ans, ind-i)
        return ans
# @lc code=end

