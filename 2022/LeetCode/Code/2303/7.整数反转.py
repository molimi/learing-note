#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        flag = True
        if x_str[0].isdigit():
            flag = True
        else:
            flag = False
            x_str = x_str[1:]
        new_x = int(x_str[::-1]) if flag else - int(x_str[::-1])
        return 0 if new_x < -(2**31) or new_x > (2**31-1) else new_x
# @lc code=end

