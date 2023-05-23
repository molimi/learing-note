#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        # # deque相比list的好处是，list的pop(0)是O(n)复杂度，deque的popleft()是O(1)复杂度
        que = deque([root])
        while que:
            res.append(que[-1].val)         # 每次都取最后一个node就可以
            size = len(que)
            for _ in range(size):           # 执行这个遍历的目的是获取下一层所有的node
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        return res
# @lc code=end

