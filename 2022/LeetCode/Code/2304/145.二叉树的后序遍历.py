#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代遍历
        if not root: return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)                     # 中结点先处理
            if node.left: stack.append(node.left)       # 左子树先入栈
            if node.right: stack.append(node.right)     # 右子树后入栈
        return result[::-1]                             # 将最终数组反转

        '''
        # 递归遍历
        self.result = []
        self.traversal(root)
        return self.result

    def traversal(self, root: Optional[TreeNode])-> List[int]:
        if not root: return
        self.traversal(root.left)               # 左
        self.traversal(root.right)              # 右
        self.result.append(root.val)            # 中
        '''
# @lc code=end

