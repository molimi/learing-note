#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 层序遍历实现反转
        if not root: return None
        q = deque([root])
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root
        '''
        # 前序遍历，交换左右子树
        if not root: return None
        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return root

        # 递归遍历
        if not root: return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        '''
# @lc code=end

