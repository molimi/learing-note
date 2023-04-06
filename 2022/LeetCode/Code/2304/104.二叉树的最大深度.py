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
              
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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
        
# @lc code=end

