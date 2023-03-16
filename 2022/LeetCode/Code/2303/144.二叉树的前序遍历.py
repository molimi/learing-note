#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.pre_order(root, result)
        return result

    def pre_order(self, root: TreeNode, result: list):
        if not root:
            return
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)
        
        
# @lc code=end

