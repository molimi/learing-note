#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        successor = None                # 后继节点
        def reverse_n(head, n):         # 反转以 head 为起点的 n 个节点，返回新的头节点
            global successor
            if n == 1:
                successor = head.next   # 记录第 n + 1 个节点
                return head
            last = reverse_n(head.next, n-1)    # 以 head.next 为起点，需要反转前 n-1 个节点
            head.next.next = head
            head.next = successor       # 让反转之后的 head 节点和后面的节点连起来
            return last
        
        if left == 1:       # 相当于反转前 n 个元素
            return reverse_n(head, right)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
# @lc code=end

