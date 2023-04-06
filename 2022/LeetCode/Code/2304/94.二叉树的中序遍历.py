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
        if not root: return []
        stack = []                      # 不能提前将root结点加入stack中
        result = []
        cur = root
        while cur or stack:         
            if cur:                     # 先迭代访问最底层的左子树结点
                stack.append(cur)
                cur = cur.left
            else:                       # 到达最左节点后处理栈顶结点
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right         # 取栈顶元素右节点
        return result

        '''
        self.result = []
        self.traversal(root)
        return self.result
    
    def traversal(self, root: Optional[TreeNode]):
        if not root: return 
        self.traversal(root.left)               # 前
        self.result.append(root.val)            # 中
        self.traversal(root.right)              # 后
        '''
# @lc code=end

