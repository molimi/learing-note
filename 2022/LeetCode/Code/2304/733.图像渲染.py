#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from collections import deque
from typing import List
import copy
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image         # 这里要注意，否则下面可能陷入死循环
        m, n = len(image), len(image[0])
        hash_deque = deque([(sr, sc)])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]         # 上下左右，避免写多个if语句
        origin_color = image[sr][sc]
        while hash_deque:
            size = len(hash_deque)
            for _ in range(size):
                (x, y) = hash_deque.popleft()                   # 每次队列移除队首元素
                image[x][y] = color
                for direction in directions:
                    new_x, new_y = x+direction[0], y+direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and image[new_x][new_y] == origin_color:      
                        hash_deque.append((new_x, new_y))
        return image

# @lc code=end

