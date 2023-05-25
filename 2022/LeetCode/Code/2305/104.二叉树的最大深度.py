#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

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
        '''
        # BFS
        if not root: return 0
        que = deque([root])
        depth = 0
        while que:
            size = len(que)
            depth += 1
            for _ in range(size):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

        return depth
        
        # DFS 自底向上
        if not root: return 0
        # 感受一下这里是将最底层的结果往上抛
        # 因为这里的递归边界条件是叶子节点
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
        '''
        res = 0
        def dfs(root, depth):
            nonlocal res
            if not root: return
            if not root.left and not root.right:
                res = max(res, depth)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 1)
        return res

            
  

# @lc code=end

