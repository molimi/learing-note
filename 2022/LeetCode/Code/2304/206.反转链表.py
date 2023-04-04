#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # 方法一：迭代法
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
        # 方法二：从前向后的递归法
        def reverse(prev, curr):
            if not curr: return prev
            temp = curr.next
            curr.next = prev
            # 可以和双指针法的代码进行对比，如下递归的写法，其实就是做了这两步
            # pre = cur
            # cur = temp
            return reverse(curr, temp)
        # 和双指针法初始化是一样的逻辑
        # cur = head
        # pre = NULL
        return reverse(None, head)
        
        # 方法三：从后往前翻转指针指向，从第二个开始的递归算法
        if not head or not head.next:       # 边缘条件判断    
            return head
        last = self.reverseList(head.next)  # 递归调用，翻转第二个节点开始往后的链表
        head.next.next = head               # 翻转头节点与第二个节点的指向
        head.next = None                    # 此时的 head 节点为尾节点，next 需要指向 None
        return last
        
        # 使用虚拟头结点反转链表
        dummy = ListNode(-1)
        dummy.next = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next
        '''
        
        # 栈的使用
        stack = []              # 创建栈 每一个结点都入栈
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        dummy = ListNode(-1)    #  创建一个虚拟头结点
        curr = dummy
        while stack:
            node = stack.pop()
            curr.next = node
            curr = curr.next
        curr.next = None        # 最后一个元素的next要赋值为空
        return dummy.next
# @lc code=end

