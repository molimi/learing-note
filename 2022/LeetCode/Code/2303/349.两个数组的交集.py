#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
        '''
        result = []
        if len(nums1_set) < len(nums2_set):
            for item in nums1_set:
                if item in nums2_set:
                    result.append(item)
        else:
            for item in nums2_set:
                if item in nums1_set:
                    result.append(item)
        return result
        '''
# @lc code=end


