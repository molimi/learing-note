#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        # BFS
        if not root: return []
        que = deque([root])
        res = []
        while que:
             size = len(que)
             max_value = float('-inf')
             for _ in range(size):
                 node = que.popleft()
                 max_value = max(max_value, node.val)
                 if node.left: que.append(node.left)
                 if node.right: que.append(node.right)
             res.append(max_value)
        return res
        '''
        # DFS
        def dfs(root, level):
            if not root: return 
            if len(res) < level:
                res.append(root.val)
            else:
                res[level-1] = (max(root.val, res[level-1]))
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        res = []
        dfs(root, 1)
        return res

# @lc code=end

