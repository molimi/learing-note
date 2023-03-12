#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [i for i in range(1, n**2+1)]
        ans = [[0]*n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        k = 0
        while left <= right and top <= bottom:
            for i in range(left, right):
                ans[top][i] = nums[k]
                k += 1
            for j in range(top, bottom+1):
                ans[j][right] = nums[k]
                k += 1
            for p in range(right-1, left, -1):
                ans[bottom][p] = nums[k]
                k += 1
            for q in range(bottom, top, -1):
                ans[q][left] = nums[k]
                k += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans
# @lc code=end

