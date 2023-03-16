#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.in_order(root, result)
        return result
    
    def in_order(self, root, result):
        if not root: return
        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)
# @lc code=end

