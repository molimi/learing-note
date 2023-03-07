#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
# 暴力匹配算法

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1, length2 = len(haystack), len(needle)
        for i in range(length1 - length2 + 1):
            if haystack[i:i + length2] == needle:
                return i
        return -1
# @lc code=end

