#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 一行递归完成
        '''
        if not root: return 0
        return 1+self.countNodes(root.left) + self.countNodes(root.right)
        '''
        return self.get_num_nodes(root)

    def get_num_nodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left_num = self.get_num_nodes(root.left)
        right_num = self.get_num_nodes(root.right)
        return left_num + right_num + 1

    
# @lc code=end

