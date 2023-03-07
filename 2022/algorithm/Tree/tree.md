非线性结构————树
## 1 树的概念
### 1.1 定义
树（英语：tree）是一种抽象数据类型（ADT）或是实作这种抽象数据类型的数据结构，用来模拟具有树状结构性质的数据集合。它是由 $n$（$n\geq 1$）个有限节点组成一个具有层次关系的集合。把它叫做“树”是因为它看起来像一棵倒挂的树，也就是说它是根朝上，而叶朝下的。它具有以下的特点：
- 每个节点有零个或多个子节点；
- 没有父节点的节点称为根节点；
- 每一个非根节点有且只有一个父节点；
- 除了根节点外，每个子节点可以分为多个不相交的子树；

<img src ="https://img-blog.csdnimg.cn/d20a43960d7d422190f27012c9bf4536.png#pic_center" width = 48%>

### 1.2 树的术语
- 节点的度：一个节点含有的子树的个数称为该节点的度；
- 树的度：一棵树中，最大的节点的度称为树的度；
- 叶节点或终端节点：度为零的节点；
- 父亲节点或父节点：若一个节点含有子节点，则这个节点称为其子节点的父节点；
- 孩子节点或子节点：一个节点含有的子树的根节点称为该节点的子节点；
- 兄弟节点：具有相同父节点的节点互称为兄弟节点；

如下图，A 节点就是 B 节点的父节点，B 节点是 A 节点的子节点。B、C、D 这三个节点的父节点是同一个节点，所以它们之间互称为兄弟节点。我们把没有父节点的节点叫做根节点，也就是图中的节点 E。我们把没有子节点的节点叫做叶子节点或者叶节点，比如图中的 G、H、I、J、K、L 都是叶子节点。

<img src ="https://img-blog.csdnimg.cn/431333176934482dbf81cb1efead8663.png#pic_center" width = 48%>

- 节点的层次：从根开始定义起，根为第1层，根的子节点为第2层，以此类推；
- 树的高度或深度：树中节点的最大层次；
- 堂兄弟节点：父节点在同一层的节点互为堂兄弟；
- 节点的祖先：从根到该节点所经分支上的所有节点；
- 子孙：以某节点为根的子树中任一节点都称为该节点的子孙；
- 森林：由 $m$（$m\geq 0$）棵互不相交的树的集合称为森林。

<img src ="https://img-blog.csdnimg.cn/4a0c2172395b4a1a883cd70f3a5d48ee.png#pic_center" width = 48%>

### 1.3 树的种类
- 无序树：树中任意节点的子节点之间没有顺序关系，这种树称为无序树，也称为自由树；
- 有序树：树中任意节点的子节点之间有顺序关系，这种树称为有序树；
  - 二叉树：每个节点最多含有两个子树的树称为二叉树；
      - 完全二叉树：对于一颗二叉树，假设其深度为d(d>1)。除了第d层外，其它各层的节点数目均已达最大值，且第d层所有节点从左向右连续地紧密排列，这样的二叉树被称为完全二叉树，其中满二叉树的定义是所有叶节点都在最底层的完全二叉树;
      - 平衡二叉树（AVL树）：当且仅当任何节点的两棵子树的高度差不大于1的二叉树；
      - 排序二叉树（二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树）；
  - 霍夫曼树（用于信息编码）：带权路径最短的二叉树称为哈夫曼树或最优二叉树；
  - B树：一种对读写操作进行优化的自平衡的二叉查找树，能够保持数据有序，拥有多余两个子树。

#### 1.4 树的存储和表示

**1. 链式存储法**

一种基于指针或者引用的二叉链式存储法，每个节点有三个字段，其中一个存储数据，另外两个是指向左右子节点的指针。我们只要拎住根节点，就可以通过左右子节点的指针，把整棵树都串起来。这种存储方式我们比较常用。大部分二叉树代码都是通过这种结构来实现的。结构如下图：

<img src ="https://img-blog.csdnimg.cn/435ac08c2f6940a28e8fee81e660e959.png#pic_center" width = 48%>


**2. 顺序存储法**

顺序存储：将数据结构存储在固定的数组中，然在遍历速度上有一定的优势，但因所占空间比较大，是非主流二叉树。我们把根节点存储在下标 i = 1 的位置，那左子节点存储在下标 2 * i = 2 的位置，右子节点存储在 2 * i + 1 = 3 的位置。以此类推，B 节点的左子节点存储在 2 * i = 2 * 2 = 4 的位置，右子节点存储在 2 * i + 1 = 2 * 2 + 1 = 5 的位置。即如果节点 X 存储在数组中下标为 i 的位置，下标为 2 * i 的位置存储的就是左子节点，下标为 2 * i + 1 的位置存储的就是右子节点。

<img src ="https://img-blog.csdnimg.cn/c66bf7536a684e90b3a94513067a9ccc.png#pic_center" width = 48%>

不过上图是一颗完全二叉树，所以数组仅仅浪费了下标为0的存储位置，如果是非完全二叉树，则可能会浪费比较多的数组内存空间。所以当要存储的树是一颗完全二叉树时，数组才是最合适的选择。所以，二叉树通常以链式存储。

## 2 二叉树

二叉树是每个节点最多有两个子树的树结构。通常子树被称作“左子树”(left subtree)和“右子树”(right subtree)。

### 2.1 二叉树的性质
**1.层结点**
在二叉树的第 $i$ 层上最多有 $2^{i-1}$ 个结点(i>=1)

**2.总结点**
深度为 $k$ 的二叉树最多有 $2^{k+1}-1$ 个结点(k>=1)

3.深度
具有 $n$ 个结点的完全二叉树的深度为 $\lfloor \log_{2}n \rfloor$

**4. 结点数**

对于任意一棵二叉树，度为 0 的结点数等于度为 2 的结点数 +1。

**5. 孩子结点**

对完全二叉树，若从上至下、从左至右编号，则编号为 $i$ 的结点，其左孩子编号必为 $2i$，其右孩子编号必为 $2i＋1$ ；其双亲的编号必为i/2（i＝1 时为根，除外）

> 完全二叉树————若设二叉树的高度为$h$，除第 $h$ 层外，其它各层 $(1~h-1)$ 的结点数都达到最大个数，第 $h$ 层有叶子结点，并且叶子结点都是从左到右依次排布，这就是完全二叉树。

<img src ="https://img-blog.csdnimg.cn/d3b40212d019401896367fcef3432c4f.jpeg#pic_center" width = 48%>

> 满二叉树——除了叶结点外每一个结点都有左右子叶且叶子结点都处在最底层的二叉树。

<img src ="https://img-blog.csdnimg.cn/980756af95ce485e91522f45d0622afa.jpeg#pic_center" width = 48%>

### 2.2 二叉树的实现

**1. 列表实现**

```python
#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/27
@version: 0.1
@description: 树的列表实现
"""

def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)     # 取出左子树
    if len(t) > 1:      # 左子树已存在
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)     # 取出右子树
    if len(t) > 1:      # 右子树已存在
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root
    
def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
print(r)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(get_right_child(r)))
```

**2. 链表实现**

```python

```



### 2.3 二叉树的遍历
#### 2.3.1 前序遍历

<img src ="https://img-blog.csdnimg.cn/ac5af9257cd54b67ad5fb11de2a599a1.webp#pic_center" width = 48%>



#### 2.3.2 中序遍历


<img src ="https://img-blog.csdnimg.cn/1dc89d79090447f38a7cde9087ea81f0.webp#pic_center" width = 48%>


#### 2.3.3 后序遍历

<img src ="https://img-blog.csdnimg.cn/2582aba782e549bea397d06e094f2171.webp#pic_center" width = 48%>

#### 2.3.4 遍历算法的简单应用





### 2.4 线索二叉树


### 2.5 树和二叉树转换




______

## 参考
- 树结构详解：[http://c.biancheng.net/data_structure/tree/](http://c.biancheng.net/data_structure/tree/)
- 树和二叉树全面总结：[https://juejin.cn/post/7065513748789723150](https://juejin.cn/post/7065513748789723150)
- 数据结构与算法————二叉树：[https://www.cnblogs.com/jasonbourne3/p/17143620.html](https://www.cnblogs.com/jasonbourne3/p/17143620.html)
- 二叉树入门和刷题：[https://zhuanlan.zhihu.com/p/136758152](https://zhuanlan.zhihu.com/p/136758152)