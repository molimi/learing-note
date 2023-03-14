#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''建立 key-value 然后 print'''
        return Counter(nums).most_common(1)[0][0]
# @lc code=end

