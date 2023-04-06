#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        que = deque([root])
        while que:
            size = len(que)
            temp = 0
            for _ in range(size):
                cur = que.popleft()
                temp += cur.val
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            result.append(temp/size)
        return result

# @lc code=end

