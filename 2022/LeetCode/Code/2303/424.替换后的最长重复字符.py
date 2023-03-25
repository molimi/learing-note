#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_n, max_len, start = 0, 0, 0
        hash_map = [0] * 26                         # 把字母映射到列表中
        for end, tail in enumerate(s):
            ind = ord(tail) - ord('A')      
            hash_map[ind] += 1
            max_n = max(max_n, hash_map[ind])       # 统计其那面出现的最多的字母
            if sum(hash_map) == max_n+k:            # 满足要求
                max_len = max(max_len, end-start+1)
            while sum(hash_map) > max_n+k:
                hash_map[ord(s[start])-ord('A')] -= 1
                start += 1
        return max_len if max_len else len(s)       #  这里有个问题就是，如果不需要更换，输出就会报错
    
# @lc code=end

