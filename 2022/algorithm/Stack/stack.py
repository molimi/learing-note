"""
@author: CarpeDiem
@date: 22/9/15
@version: 0.1
@description: 栈要考虑大小
"""
'''
class Stack(object):
    def __init__(self, limit):
        self.stack = []         # 初始化栈
        self.limit = limit      # 栈容量极限

    def push(self, data):
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError("超出栈的容量")
        else:
            # 空栈不能弹出元素
            self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        # 查看栈顶元素，如果使用pop就必须保证有元素，但使用最后一项可以返回None
        if self.stack:
            return self.stack[-1]
        

    def is_empty(self):
        # 判断栈是否为空
        return not bool(self.stack)

    def size(self):
        # 返回栈的大小
        return len(self.stack)
'''

class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.stack = []
    
    # 进栈
    def push(self, item):
        self.stack.append(item)

    # 出栈
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")
    
    # 是否为空栈，返回布尔值
    def is_empty(self):
        return self.stack == []
    
    # 返回栈顶元素
    def peek(self):
        return self.stack[-1]
    
    # 返回元素数目
    def size(self):
        return len(self.stack)



if __name__ == "__main__":
    # 初始化一个栈对象
    my_stack = Stack()
    my_stack.push('h')
    my_stack.push('a')
    print(my_stack.size())
    print(my_stack.pop())
    print(my_stack.peek())