#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        p, p1, p2 = head, dummy1, dummy2
        count = 0
        while p:
            if count % 2 == 0:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            count += 1
            temp = p.next
            p.next = None
            p = temp
        p1.next = dummy2.next
        return dummy1.next

# @lc code=end

