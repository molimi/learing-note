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
        # 迭代法
        if not root: return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)         # 中结点先处理
            if node.right:
                stack.append(node.right)    # 右子树先入栈
            if node.left:
                stack.append(node.left)     # 左子树先入栈
        return result

        '''
        # 递归实现
        self.result = []                # 使用布局变量存储结果
        self.traverse(root)
        return self.result
    
    def traversal(self, root):
        if not root: return
        self.result.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        '''
# @lc code=end

