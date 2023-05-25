#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        # BFS
        if not root: return []
        results = []
        que = deque([root])
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                node = que.popleft()
                result.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            results.append(result)
        results.reverse()
        return results
        '''
        # DFS
        def dfs(root, level):
            if not root: return
            if len(res) < level:
                res.append([root.val])
            else:
                res[level-1].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1) 
        
        res = []
        dfs(root, 1)
        return res[::-1]
# @lc code=end

