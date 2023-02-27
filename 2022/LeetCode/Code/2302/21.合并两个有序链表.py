#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
<<<<<<< HEAD
#
=======
# 思路一：用递归实现
# 思路二： 迭代
>>>>>>> 667449772d496b68931119ce29307e1155363522

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
<<<<<<< HEAD
=======
        '''
        if not list1: return list2
        if not list2: return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)  # list1的val小，则把后面的合并
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        '''
        prehead = ListNode(-1)  # 哨兵节点
        prev = prehead          # 指针节点
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next
        
        prev.next = list1 if list1 else list2

        return prehead.next


>>>>>>> 667449772d496b68931119ce29307e1155363522
# @lc code=end

