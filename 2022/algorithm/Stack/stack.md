## 1 栈
堆栈是一种特殊的抽象数据结构或者组合，其主要的操作为将元素从头部加入栈中，称为进栈和将头部元素移除，称为出栈。

一个栈（有时称“叠加栈”）是一个项的有序集合。添加项和移除项都发生在同一“端”。这一端通常被称为“顶”。另一端的顶部被称为“底”。

栈的“底”是有标志性的，因为存储在栈中更靠近“底”的项就是栈中储存时间最长的项。最新添加的项在移除项时也会第一个被移除。这种排序原则有时也称为LIFO(LIFO-Last-In-First-Out)法，也就是“后进先出”。项的排序基于它在集合中存在的时间长度。越新的项越靠近“顶”，越老的项越靠近“底”。如下图所示，堆栈是一种LIFO的数据结构。

<img src="https://img-blog.csdnimg.cn/4142210b7ba04944b607c2352962df26.png#pic_center" width=50%>


**小结：** 栈Stack ：栈顶和栈底，栈的特性：反转次序，后进先出（主要应用：网页、word编辑）

## 2 栈的抽象数据类型

栈的抽象数据类型是由以下结构和操作定义的。抽象数据类型“栈”定义为如下的操作：（默认左端为栈底，右端为栈顶）

```python
Stack( )：创建一个空栈，不包含任何数据项
push(item)：将item加入栈顶，无返回值，append()
pop( )：将栈顶数据项移除，并返回，栈被修改pop()
peek( )：“窥视” 栈顶数据项，返回栈顶的数据项但不移除，栈不被修改。
isEmpty( )：返回栈是否为空栈
size( )：返回栈中有多少个数据项。不需要参数，返回一个整数。
```


```python
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
    my_stack.push('i')
    print(my_stack.size())
    print(my_stack.pop())
    print(my_stack.peek())
```

## 3 栈的应用

### 3.1 简单括号匹配
问题描述：括号的使用必须遵循“平衡”规则，即每个开括号要恰好对应一个闭括号，其次每对开闭括号要正确的嵌套。如下：
- 正确的括号：(()()()())，(((())))，(()((())()))
- 错误的括号：((((((())，()))，(()()(()
思考：从左到右扫描括号串，最新打开的左括号，应该匹配最先遇到的右括号，这样，第一个左括号（最早打开），就应该匹配最后一个右括号（最后遇到），体现了次序反转的识别，正好符合栈的特性。
实现流程如下：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/8619e7874bf447e7b025bb9e5a9263d1.png#pic_center" width=50%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">算法流程图</div> </center>

**参考代码：**
```python
import stack

def par_checker(symbol_string):
    new_stack = stack.Stack()
    for item in symbol_string:
        if item == "(":
            new_stack.push(item)
        elif item == ")":
            if new_stack.is_empty():
                return False
            new_stack.pop()
    return new_stack.is_empty()

def main():
    print(par_checker('((()))'))
    print(par_checker('((())'))
    print(par_checker('(()))'))
    print(par_checker('())'))


if __name__ == "__main__":
    main()
```

在实际的应用里，我们会碰到更多种括号，如python中列表所用的方括号“[]”，字典所用的花括号“{}”，元组和表达式所用的圆括号“()”。这些不同的括号有可能混合在一起使用，要注意各自的开闭匹配问题。

**参考代码：**
```python
import stack

def par_checker(symbol_string):
    par_stack = stack.Stack()
    for item in symbol_string:
        if item in '([{':
            par_stack.push(item)
        elif item in ')]}':
            if par_stack.is_empty():
                return False
            else:
                close = par_stack.pop()
                if not matches(close, item):
                    return False
    return par_stack.is_empty()

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

def main():
    print(par_checker('{{([][])}()}'))          # True
    print(par_checker('[{()]'))                 # False

main()
```
### 3.2 十进制转换为二进制
十进制转换为二进制，采用的是“除以2求余数”的算法，将整数不断除以
2，每次得到的余数就是由低到高的二进制位，“除以2”的过程，得到的余数是从低到高的次序，而输出则是从高到低，所以需要一个栈来反转次序。
<img src="https://img-blog.csdnimg.cn/e620ee3af63f40aca41e74490de1b4d3.png#pic_center" width=50%>

**参考代码：**
```python
import stack

def divide_by_2(dec_number):
    number_stack = stack.Stack()
    while dec_number:
        number_stack.push(dec_number % 2)
        dec_number = dec_number // 2
    
    output_string = ''
    while not number_stack.is_empty():
        output_string += str(number_stack.pop())
    
    return output_string

def main():
    print(divide_by_2(42))          # 101010
    print(divide_by_2(156))         # 10011100
    print(divide_by_2(463))         # 111001111

main()
```

十进制转换为二进制的算法，很容易可以扩展为转换到任意N进制，只需要将“除以2求余数”算法改为“除以N求余数”算法就可以。

参考代码：
```python
import stack

def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    number_stack = stack.Stack()
    while dec_number:
        number_stack.push(dec_number % base)
        dec_number = dec_number // base

    output_string = ''
    while not number_stack.is_empty():
        output_string += digits[number_stack.pop()]

    return output_string

def main():
    print(base_converter(152, 2))       # 10011000
    print(base_converter(152, 8))       # 230
    print(base_converter(152, 16))      # 98

main()
```

### 3.3 表达式转换
中缀表达式（优先级），前后缀表达式转换，所以在很多情况下，表达式的计算机表示都避免用复杂的中缀形式；在前缀和后缀表达式中，操作符的次序完全决定了运算的次序，不再有混淆




### 3.4 后缀表达式求值
所以说，无论表达式多复杂，需要转换成前缀或者后缀，只需要两个步骤：将中缀表达式转换为全括号形式；将所有的操作符移动到子表达式所在的左括号(前缀)或者右括号(后缀)处，替代之，再删除所有的括号

