#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
# 思路一：构造一维前缀和数组

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])          # 矩阵的行和列
        self.pre_sum = [[0]*(n+1) for _ in range(m+1)]      # 构造一维前缀和矩阵
        for i in range(m):
            for j in range(n):
                self.pre_sum[i+1][j+1] = self.pre_sum[i+1][j] + self.pre_sum[i][j+1] - self.pre_sum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.pre_sum[row2+1][col2+1] - self.pre_sum[row1][col2+1] - self.pre_sum[row2+1][col1] + self.pre_sum[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

