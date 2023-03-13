#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                p1 = slow.next          # 为什么指向下一个节点呢？否则陷入死循环
                p2 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p2
            else:
                fast = fast.next.next
                slow = slow.next
        return None

# @lc code=end

