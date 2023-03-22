#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.strip().split()
        return len(str_list[-1])


# @lc code=end
