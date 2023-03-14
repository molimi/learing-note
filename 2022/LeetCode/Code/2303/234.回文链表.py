#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        prev, val_list = head, []
        while prev:
            val_list.append(prev.val)
            prev = prev.next
        return val_list == val_list[::-1]
        '''
        p, slow, fast = head, head, head
        while fast and fast.next:   # 快慢指针找到中间节点
            p = slow
            slow = slow.next
            fast = fast.next.next
        left, right = head, self.reverse_list(slow)     # 额外维持的半条链表 遍历半个链表
        q = right
        while right:                                        # 两个半长链表的比较 遍历两个 半长链表
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        p.next = self.reverse_list(q)
        return True
    
    def reverse_list(self, head: Optional[ListNode]):
        prev, curr = None, head
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node
        return prev
# @lc code=end

