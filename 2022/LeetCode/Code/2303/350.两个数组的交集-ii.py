#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set = set(nums1).intersection(set(nums2))
        result = []
        for num in num_set:
            temp = min(nums1.count(num), nums2.count(num))
            result += temp * [num]
        return result
# @lc code=end

