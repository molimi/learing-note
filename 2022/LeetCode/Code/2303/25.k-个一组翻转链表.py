#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k== 1 or not head or not head.next:
            return head
        dummy = ListNode(-1, head)
        prev1, prev2, curr = dummy, dummy, dummy.next
        count = -1
        while prev1:        # 查找节点个数
            count += 1
            prev1 = prev1.next
        tail = curr
        for i in range(count//k):
            if i != 0:
                prev2 = tail
                tail = curr
            for _ in range(k):
                temp = curr.next
                curr.next = prev2.next
                prev2.next = curr
                tail.next = temp
                curr = temp
        return dummy.next
