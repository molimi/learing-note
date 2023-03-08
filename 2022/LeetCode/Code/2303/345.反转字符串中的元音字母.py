#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        str_set = set("aeiouAEIOU")
        head, tail = 0, len(s) - 1
        str_list = list(s)
        while head < tail:
            if str_list[head] in str_set and str_list[tail] in str_set:
                str_list[head], str_list[tail] = str_list[tail], str_list[head]
                head += 1
                tail -= 1
            elif str_list[head] in str_set and str_list[tail] not in str_set:
                tail -= 1
            elif str_list[head] not in str_set and str_list[tail] in str_set:
                head += 1
            else:
                head += 1
                tail -= 1
        
        return ''.join(str_list)
# @lc code=end

