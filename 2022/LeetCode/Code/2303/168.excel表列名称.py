#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return ''.join([chr(ord('A')+item-1) for item in self.split_number(columnNumber)[::-1]])

    def split_number(self, num):
        if num < 27:
            return [num]
        if num % 26 == 0:       # 就是这里有个问题，可以整除 26 的要单独考虑，和26进制还是有区别的
            return [26] + self.split_number(num//26-1)
        else:
            return [num%26] + self.split_number(num // 26)
# @lc code=end

