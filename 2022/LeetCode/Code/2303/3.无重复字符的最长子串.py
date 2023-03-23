#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, hash_map = 0, set()
        start = 0
        for end, ch in enumerate(s):
            hash_map.add(ch)
            if end - start + 1 == len(hash_map):
                max_len = max(max_len, end - start + 1)
            while end - start + 1 > len(hash_map):
                if s[start] in hash_map:
                    hash_map.remove(s[start])
                if s[start] == ch:
                    hash_map.add(ch)
                start += 1
        return max_len
# @lc code=end

