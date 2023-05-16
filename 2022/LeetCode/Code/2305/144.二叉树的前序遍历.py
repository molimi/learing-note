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
        # 递归写法
        '''
        if not root: return []
        res = []
        def traversal(root):
            if not root: return 
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res
        '''
        # 迭代写法
        if not root: return []
        st = [root]         # 使用栈
        res = []
        while st:
            node = st.pop()
            res.append(node.val)
            if node.right: st.append(node.right)        # 先右后左，后序遍历直接倒序就可以
            if node.left: st.append(node.left)
        return res
# @lc code=end

