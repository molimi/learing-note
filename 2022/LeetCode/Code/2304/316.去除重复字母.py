#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        hash_map = Counter(s)
        for ch in s:
            if ch not in stack:
                while stack and ch < stack[-1] and hash_map[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            hash_map[ch] -= 1
        return ''.join(stack)
# @lc code=end