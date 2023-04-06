#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result = []
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if i == size - 1:           # 判断一下是否到达最右边
                    result.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
        return result
# @lc code=end

