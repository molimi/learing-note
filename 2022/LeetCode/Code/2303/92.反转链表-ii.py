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
        if  head.next == None:
            return head
        dummy = ListNode(-1, head)
        prev = dummy
        for _ in range(left-1):     # 迭代法，先找到起点
            prev= prev.next         # 来到 left 节点的前一个节点
        curr = prev.next            # cur 是真正反转的指针
        tail = curr
        for _ in range(right-left+1):
            node = curr.next        # node 保存 curr.next 的临时指针，保存后面的顺序
            curr.next = prev.next   # 将要反转的节点，接入到 left 节点
            prev.next = curr        
            tail.next = node
            curr = node
        return dummy.next

# @lc code=end

