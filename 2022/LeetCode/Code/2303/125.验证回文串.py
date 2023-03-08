#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
# 这个题目也可以使用双指针解决，遇到字母或数字就判断首尾指针是否相等

# @lc code=start
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        if not s:
            return True
        s = s.lower()
        pattern = re.compile(r'[^a-z0-9]')   # 正则表达式，把数字和字母都剔除掉
        new_str = pattern.sub('', s)
        return new_str == new_str[::-1]
        '''
        new_str = ''.join(ch.lower() for ch in s if ch.isalnum())
        return new_str == new_str[::-1]
# @lc code=end

