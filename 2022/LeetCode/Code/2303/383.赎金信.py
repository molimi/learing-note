#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1, dict2 = Counter(magazine), Counter(ransomNote)
        for k, v in dict2.items():
            if k in dict1:
               if  dict1[k] < v:
                   return False
            else:
                return False
        return True

# @lc code=end

