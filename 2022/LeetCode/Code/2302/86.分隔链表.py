#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy1 存放小于x链表的虚拟头结点， 度没有 存放不小于x的虚拟头结点
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        # p1, p2 指针负责生成结果链表
        p1, p2 = dummy1, dummy2
        # p 负责遍历链表，类似合并两个有序链表的逻辑
        # 这里是将两个链表分解成两个链表
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p 
                p2 = p2.next
            # 断开原链表中的每个结点的 next 指针
            temp = p.next
            p.next = None
            p = temp
        # 合并两个链表
        p1.next = dummy2.next
        return dummy1.next

# @lc code=end

