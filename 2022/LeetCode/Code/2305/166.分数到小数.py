#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0: return str(numerator//denominator)
        res = []
        if numerator * denominator < 0:
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator//denominator))
        res.append('.')
        remainder = numerator % denominator
        index_map = dict()
        while remainder and remainder not in index_map:
            index_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder//denominator))
            remainder %= denominator
        if remainder:
            ind = index_map[remainder]
            res.insert(ind, '(')
            res.append(')')
        return ''.join(res)
