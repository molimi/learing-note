#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        return temp == temp[::-1]


# @lc code=end
