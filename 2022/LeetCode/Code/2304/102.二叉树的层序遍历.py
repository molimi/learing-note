#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.helper(root, 0)
        return self.res

    def helper(self, root: Optional[TreeNode], depth) -> Optional:
        if not root: return []
        if len(self.res) == depth: self.res.append([])
        self.res[depth].append(root.val)
        if root.left: self.helper(root.left, depth+1)
        if root.right: self.helper(root.right, depth+1)


        '''
        # 二叉树层序遍历迭代解法
        if not root: return []
        results = []
        que = deque([root])
        while que:
            size = len(que)
            result = []
            for _ in range(size):       # 这里一定要使用固定大小size，不要使用len(que)，因为len(que)是不断变化的
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)
        return results
        '''
# @lc code=end

