#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
# 使用全局变量总是会有问题

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque          
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 按层次遍历，深度
        if not root: return 0
        q = deque([root])
        depth = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            depth += 1
        return depth
        '''
        # 按中左右遍历
        self.res = 0                # 记录最大深度
        self.depth= 0               # 记录遍历到的节点的深度
        self.traverse(root)
        return self.res 
    
    # 二叉树遍历框架
    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root: return 
        # 前序位置
        self.depth += 1
        if not root.left and not root.right:        # 左右子树都为空，才是最大的深度
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置
        self.depth -= 1
        '''
        
# @lc code=end

