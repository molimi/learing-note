#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        results = []
        que = deque([root])
        while que:
            result = []
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            results.append(result)
        return results[::-1]
# @lc code=end

