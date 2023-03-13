#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums_dict = defaultdict(int)
        count = 0
        for num1 in nums1:
            for num2 in nums2:
                nums_dict[num1+num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                    count += nums_dict.get(-num3-num4, 0)
        return count

# @lc code=end

