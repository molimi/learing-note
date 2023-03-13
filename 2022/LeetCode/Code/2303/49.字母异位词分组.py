#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()
        for item in strs:
            temp = ''.join(sorted(item))
            if temp in str_dict:
                str_dict[temp].append(item)
            else:
                str_dict[temp] = [item]
        return list(str_dict.values())

# @lc code=end

