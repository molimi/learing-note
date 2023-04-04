#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 双指针还可以解决
        m, n = len(matrix),  len(matrix[0])
        row, col = 0, n-1
        while row < m and col >= 0:
            temp = matrix[row][col]
            if temp == target:
                return True
            elif temp < target:
                row += 1
            else:
                col -= 1
        return False
# @lc code=end

