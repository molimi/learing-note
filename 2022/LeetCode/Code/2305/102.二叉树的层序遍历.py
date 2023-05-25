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
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS
        def dfs(root, level):
            if not root: return
            # 假设 res 是 [[1], [2,3]]， level 是 3，就再插入一个 [root.val] 放到 res 中
            if len(res) < level:
                res.append([root.val])
            else:
                # 将当前节点的值加入到res中，level 代表当前层，假设 level 是 3，节点值是 99
			    # res 是 [[1], [2,3], [4]]，加入后 res 就变为 [[1], [2,3], [4,99]]
                res[level-1].append(root.val)
            # 递归的处理左子树，右子树，同时将层数 level+1
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        res = []
        dfs(root, 1)
        return res
# @lc code=end

