#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(nums):
            result = []
            for num in nums:
                if num.isdigit():
                    result.append(num)
            return len(result) == len(set(result))
        for row in board:
            if not isValid(row):
                return False
        length = len(board)
        row_board = [[0]*9 for _ in range(length)]
        col_board = [[0]*9 for _ in range(length)]
        mini_board = [[[0]*9 for _ in range(3)] for _ in range(3)]      # 三维数组就很巧妙
        for i in range(length):
            for j in range(length):
                if board[i][j].isdigit():
                    temp = int(board[i][j])-1
                    row_board[i][temp] += 1
                    col_board[j][temp] += 1
                    mini_board[i//3][j//3][temp] += 1
                    if row_board[i][temp] > 1 or col_board[j][temp] > 1 or mini_board[i//3][j//3][temp] > 1:
                        return False
        return True
        
# @lc code=end

