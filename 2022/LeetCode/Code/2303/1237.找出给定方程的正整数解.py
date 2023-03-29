#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x, y = 1, 1000
        result = []
        while x <= 1000 and y >= 1:
            res = customfunction.f(x, y)
            if res > z:
                y -= 1
            elif res < z:
                x += 1
            else:
                result.append([x,y])
                x += 1
                y -= 1
        return result
        
# @lc code=end

