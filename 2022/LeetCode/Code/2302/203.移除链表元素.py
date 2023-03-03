#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

<<<<<<< HEAD

=======
>>>>>>> 6d61b721a789b2d9c152161f4439f936a1080775
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
<<<<<<< HEAD
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
=======
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
# @lc code=end

>>>>>>> 6d61b721a789b2d9c152161f4439f936a1080775
