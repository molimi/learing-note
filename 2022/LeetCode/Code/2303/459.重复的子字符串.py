#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
# 题目标的简单，但不一定容易通过

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """好像这个思路不行啊，先找到不重复的子串，KMP算法后面再学"""
        length = len(s)
        for i in range(1, length//2+1):                             # 把一个字符的排除在外，比如a\aaa
            if length % i == 0:                                     # 必须是子串长度的整数倍
                if all(s[j] == s[j-i] for j in range(i, len(s))):   # 满足s[j] == s[j-i]
                    return True
        return False

# @lc code=end

