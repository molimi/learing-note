#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先把行和列记录下来，然后分别赋值为 0
        m, n = len(matrix), len(matrix[0])
        row_set = []
        col_set = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.append(i)
                    col_set.append(j)
        for row in row_set:
            matrix[row] = [0] * n
        for col in col_set:
            for i in range(m):
                matrix[i][col] = 0
        return matrix
# @lc code=end

