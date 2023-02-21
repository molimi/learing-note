在整个基本数据结构的讨论中，我们使用了Python列表来实现抽象数据类型。列表是一个功能强大而简单的收集容器，并为程序员提供了各种各样的操作。然而，并非所有的编程语言都有内置的list列表类型。在这些情况下，程序员必须自己来实现列表。

无序表List的操作如下：
```python
List()：创建一个空列表
add(item)：添加一个数据项到列表中，假设item原先不存在于列表中
remove(item)：从列表中移除item，列表被修改，item原先应存在于表中
search(item)：在列表中查找item，返回布尔类型值
isEmpty()：返回列表是否为空
size()：返回列表包含了多少数据项
append(item)：添加一个数据项到表末尾，假设item原先不存在于列表中
index(item)：返回数据项在表中的位置
insert(pos, item)：将数据项插入到位置pos，假设item原先不存在与列表中，同时原列表具
有足够多个数据项，能让item占据位置pos
pop()：从列表末尾移除数据项，假设原列表至少有1个数据项
pop(pos)：移除位置为pos的数据项，假设原列表存在位置pos
```

为了实现无序表数据结构，可以采用链接表的方案。

数据项存放位置并没有规则，但如果在数据项之间建立链接指向，就可以保持其前后相对位置


## 1 无序链表 UNORDEREDLIST
### 1.1 节点 NODE
链表实现的最基本元素是节点Node，每个节点至少要包含2个信息：数据项本身，以及指向下一个节点的引用信息
注意next为None的意义是没有下一个节点了，这个很重要


```python
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next
```
可以采用链接节点的方式构建数据集来实现无序表
链表的第一个和最后一个节点最重要
如果想访问到链表中的所有节点，就必须从第一个节点开始沿着链接遍历下去


### 1.2 无序链表 



## 2 有序链表 ORDEREDLIST