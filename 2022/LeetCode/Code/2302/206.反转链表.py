#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        # reverse_head 表示 head.next 后面一整段反转之后的头结点，所以最后return reverse_head
        reverse_head = self.reverseList(head.next)
        # 此时 head.next 指向的已经是反转部分的尾巴
        head.next.next = head
        # head 指向 None，表示此时 head 已经是尾巴了
        head.next = None
        return reverse_head
# @lc code=end

