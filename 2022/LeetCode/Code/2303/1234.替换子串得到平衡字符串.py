#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        '''滑动窗口'''
        min_length, start = float('inf'), 0
        hash_map, length = Counter(s), len(s)//4
        if all(hash_map[ch] == length for ch in "QWER"):
            return 0
        for end, tail in enumerate(s):
            hash_map[tail] -= 1
            while all(hash_map[ch] <= length for ch in "QWER"):     # 此时子串满足条件，可以缩小窗口
                min_length = min(min_length, end-start+1)
                hash_map[s[start]] += 1
                start += 1
        return min_length

# @lc code=end

