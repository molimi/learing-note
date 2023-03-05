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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        dumpy = ListNode(-1)
        dumpy.next = head
        prev = dumpy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dumpy.next
# @lc code=end

>>>>>>> 6d61b721a789b2d9c152161f4439f936a1080775
