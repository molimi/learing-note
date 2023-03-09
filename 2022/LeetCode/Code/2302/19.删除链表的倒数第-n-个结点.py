#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head.next
        dummy = ListNode(-1, head)
        fast = dummy.next
        # 快指针先走n步
        for _ in range(n):
            fast = fast.next
        slow = dummy
        # 快慢指针同时走，直到 fast 指针到达尾部节点，此时 slow 到达倒数第 N 个节点的前一个节点
        while fast:
            fast, slow = fast.next, slow.next
        # 删除节点，并重新连接
        slow.next = slow.next.next
        return dummy.next
# @lc code=end

