#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1 , head)
        prev, curr = dummy, dummy.next
        k = 1
        tail = curr
        while curr:
            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            tail.next = temp
            curr = temp
            k += 1
            if k % 2:
                prev = tail
                tail = curr
        return dummy.next
# @lc code=end