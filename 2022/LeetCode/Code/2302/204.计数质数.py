#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
# 思路：直接遍历会超时，采用官方提供的厄拉多塞筛法

# @lc code=start
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        flag_list = [1 for _ in range(n)]
        flag_list[:2] = [0, 0]
        for i in range(2, int(n**0.5)+1):
            if flag_list[i]:
                '''
                for j in range(i*i, n, i):
                    flag_list[j] = 0
                '''
                flag_list[i*i:n:i] = [0] * ((n - i * i - 1) // i + 1)
        return sum(flag_list)
        

# @lc code=end

