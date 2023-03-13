#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = len(s) % (2*k)
        s_list = list(s)
        for i in range(0, len(s)-res+1, 2*k):
            s_list[i:i+k] = s[i:i+k][::-1]
        if res < k:
            s_list[-1:-res-1] = s_list[-1:-res-1][::-1]
        else:
            s_list[-res:-res-k-1] = s_list[-res:-res-k-1][::-1]
        return ''.join(s_list)

# @lc code=end

