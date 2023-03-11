#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.back_strip(s) == self.back_strip(t)

    def back_strip(self, s):
        s_list = []
        for item in s:
            if item == '#':     
                if s_list:          # 判断一下前面没有字母，不做处理
                    s_list.pop()
            else:
                s_list.append(item)
        return ''.join(s_list)
# @lc code=end

