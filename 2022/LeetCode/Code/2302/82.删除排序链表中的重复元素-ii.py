#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                if prev:
                    prev.next = cur
                else:
                    head = cur
            else:
                prev = cur
                cur = cur.next
        return head

        flag = False
        while cur and cur.next:
            if cur.val == cur.next.val:
                if prev:
                    prev.next = cur.next.next
                else:
                    head = cur.next.next
                cur = cur.next.next
                flag = True
            elif flag:
                prev.next = cur.next
                cur = cur = cur.next.next
            else:
                prev = cur
                cur = cur.next
                flag = False

        return head



# @lc code=end

