#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head     # 指针节点
        while curr and curr.next:
            if curr.val == curr.next.val:       # 不删除头结点，就没啥考虑的
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
            


# @lc code=end

