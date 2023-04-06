#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat
        reshape_mat = [[0]*c for _ in range(r)]
        p, q = 0, 0
        for i in range(m):
            for j in range(n):
                if p < r:
                    if q < c:
                        reshape_mat[p][q] = mat[i][j]
                        q += 1
                    else:
                        p += 1
                        q = 0
                        reshape_mat[p][q] = mat[i][j]
                        q += 1
        return reshape_mat

s = Solution()
print(s.matrixReshape([[1, 2], [3, 4], [5, 6]], 2, 3))
# @lc code=end

