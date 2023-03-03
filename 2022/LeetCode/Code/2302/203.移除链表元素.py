#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        if head == None:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head

# @lc code=end
