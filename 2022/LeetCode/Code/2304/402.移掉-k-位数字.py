#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k           # 最后数组的元素可能多于输出的
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'

# @lc code=end

