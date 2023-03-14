#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
# 两个两个合并

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
import heapq 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = lists[0]
        for item in lists[1:]:
            head = self.mergeTwoLists(head, item)
        return head
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

        priority_queue = []
        for llist in lists: 
            while llist:
                heapq.heappush(priority_queue, llist.val)       # 把llist中的数据逐个加到堆中
                llist = llist.next
        dummy = ListNode(0)                                     # 构造虚节点
        p = dummy
        while priority_queue:
            p.next = ListNode(heapq.heappop(priority_queue))    # 依次弹出最小堆的数据
            p = p.next
        return dummy.next 
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        n = len(lists)                          # 记录子链表数量
        return self.mergeSort(lists, 0, n - 1)  # 调用归并排序函数
    
    def mergeSort(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l == r:
            return lists[l]
        m = (l + r) // 2
        L = self.mergeSort(lists, l, m)         # 循环的递归部分
        R = self.mergeSort(lists, m + 1, r)
        return self.mergeTwoLists(L, R)         # 调用两链表合并函数
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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


# @lc code=end

