#
# @lc app=leetcode.cn id=2451 lang=python3
#
# [2451] 差值数组不同的字符串
#

# @lc code=start
from typing import List
class Solution:
    def oddString(self, words: List[str]) -> str:
        def calculate(word):
            res = []
            n = len(word)
            for i in range(1, n):
                res.append(ord(word[i])-ord(word[i-1]))
            return tuple(res)
        
        nums_dict = dict()
        for word in words:
            temp = calculate(word)
            if temp in nums_dict:
                nums_dict[temp].append(word)
            else:
                nums_dict[temp] = [word]
        for key, value in nums_dict.items():
            if len(value) == 1:
                return value[0]
            
s = Solution()
print(s.oddString(["abm","bcn","alm"]))
# @lc code=end

