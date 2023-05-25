#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
        # BFS
        res = []
        que = deque([root])
        while que:
            size = len(que)
            total = 0
            for _ in range(size):
                node = que.popleft()
                total += node.val
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(total/size)
        return res
        '''
        # DFS
        def dfs(root: Optional[TreeNode], level: int) -> List[float]:
            if not root: return
            if len(total) < level:          
                total.append(root.val)
                count.append(1)
            else:
                total[level-1] += root.val
                count[level-1] += 1
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        count, total = [], []
        dfs(root, 1)
        return [t/c for t, c in zip(total, count)]
# @lc code=end

