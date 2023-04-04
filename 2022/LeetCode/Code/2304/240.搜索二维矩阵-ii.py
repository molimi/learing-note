#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 双指针
        m, n = len(matrix), len(matrix[0])
        low, high = 0, n-1
        while low < m and high > -1:    
            temp = matrix[low][high]
            if temp == target:
                return True
            elif temp > target:
                high -= 1
            else:
                low += 1
        return False
# @lc code=end

