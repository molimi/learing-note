#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        length = len(nums2)
        for num in nums1:
            try:
                for i in range(nums2.index(num)+1, length):
                    if nums2[i] > num:
                        result.append(nums2[i])
                        break
                if i == length-1 or nums2.index(num)== length-1:
                    result.append(-1)
            except:
                result.append(-1)
        return result
# @lc code=end

