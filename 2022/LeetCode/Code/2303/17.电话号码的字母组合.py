#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """实现笛卡尔积"""
        if not digits:
            return []
        alpha_dict = {'2': 'abc', '3':'def', '4': 'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9': 'wxyz'}
        return [''.join(item) for item in list(product(*[alpha_dict[digit] for digit in digits]))]

# @lc code=end

