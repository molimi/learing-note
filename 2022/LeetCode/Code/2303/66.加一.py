#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join(list(map(str, digits)))
        return list(map(int, list(str(int(number) + 1))))


# @lc code=end
