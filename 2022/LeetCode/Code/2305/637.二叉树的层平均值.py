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
# @lc code=end

