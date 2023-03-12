#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        result = []
        while left <= right and top <= bottom:
            for x in range(left, right):                # 上边
                result.append(matrix[top][x])
            for y in range(top, bottom+1):              # 右边
                result.append(matrix[y][right])
            # 考虑排到最后或者为 m*1 的数组，下边和左边就不需要排列
            if left < right and top < bottom:
                for r in range(right-1, left, -1):      # 下边
                    result.append(matrix[bottom][r])
                for s in range(bottom, top, -1):        #  左边
                    result.append(matrix[s][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result
# @lc code=end

