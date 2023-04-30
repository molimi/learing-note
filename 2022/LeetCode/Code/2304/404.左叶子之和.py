#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
from typing import *
# 列表转二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(nums: List) -> TreeNode:
    """ 由输入列表生成树，返回根节点 """
    q = []
    if not nums:
        return
    root = TreeNode(val=nums.pop(0))
    q.append(root)
    while q:
        curr = q.pop(0)
        if nums:
            if nums[0] != None:
                curr.left = TreeNode(val=nums.pop(0))
                q.append(curr.left)
            else:
                nums.pop(0)
        if nums:
            if nums[0] != None:
                curr.right = TreeNode(val=nums.pop(0))
                q.append(curr.right)
            else:
                nums.pop(0)
    return root


from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 深度优先搜索
        self.res = 0
        def traversal(root):
            if not root: return
            if root.left:
                if not root.left.left and not root.left.right:
                    self.res += root.left.val
                else:
                    traversal(root.left)
            if root.right:
                traversal(root.right)
        traversal(root)
        return self.res
        '''
        # 广度优先搜索
        if not root: return 0
        que = deque([root])
        res = 0
        while que:
            length = len(que)
            for _ in range(length):
                curr = que.popleft()
                if curr.left: 
                    if not curr.left.left and not curr.left.right:
                        res += curr.left.val
                    else:
                        que.append(curr.left)
                if curr.right: que.append(curr.right)
        return res

s = Solution()

print(s.sumOfLeftLeaves(list_to_tree([3, 9, 20, None, None, 15, 7])))
'''


# @lc code=end

