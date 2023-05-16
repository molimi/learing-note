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
        if not root:    return []   # 空树
        stack = []                  # 不能提前将root结点加入stack中'
        res = []
        cur = root
        while cur or stack:
            if cur:                 # 先迭代访问最底层左子树结点
                stack.append(cur)
                cur = cur.left
            else:                   # 到达最左节点后处理栈顶结点
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right     # 取栈顶元素右结点
        return res
        '''
        res = []
        def traverse(root):
            if not root: return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        traverse(root)
        return res
        '''
# @lc code=end

