#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)                  # 会移动头结点，这里虚拟头结点
        last_sorted, curr = head, head.next         # last_sorted 维护已排序部分的最后一个位置；curr 为遍历的待插入元素
        while curr:           # 外层循环遍历完链表所有数；内层循环遍历[head, lastSort]这段位置找插入
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next      # 大，直接后移，或者直接 last_sorted = cur
            else:
                prev = dummy                        # 用来遍历已经排序的部分
                while prev.next.val <= curr.val:    # 从前往后比较，找插入的位置
                    prev = prev.next
                last_sorted.next = curr.next        # 找到位置进行插入操作
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next                 # 指针后移
        return dummy.next

# @lc code=end

