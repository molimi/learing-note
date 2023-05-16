数学(三) -- LC[]

## 1 二叉树层序遍历
### 1.1 题目描述

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

<img src ="https://img-blog.csdnimg.cn/d4b246a57e414055ae47f2b6964eb65e.jpeg#pic_center" width = 48%>

> 输入：root = [3,9,20,null,null,15,7]
> 输出：[[3],[9,20],[15,7]]

> 输入：root = [1]
> 输出：[[1]]

> 输入：root = []
> 输出：[]


题目链接：[https://leetcode.cn/problems/binary-tree-level-order-traversal/description/](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)


### 1.2 思路分析

本文将会讲解为什么这道题适合用广度优先搜索(BFS)，以及 BFS 适用于什么样的场景。

DFS（深度优先搜索）和 BFS（广度优先搜索）就像孪生兄弟，提到一个总是想起另一个。然而在实际使用中，我们用 DFS 的时候远远多于 BFS。那么，是不是 BFS 就没有什么用呢？

如果我们使用 DFS/BFS 只是为了遍历一棵树、一张图上的所有结点的话，那么 DFS 和 BFS 的能力没什么差别，我们当然更倾向于更方便写、空间复杂度更低的 DFS 遍历。不过，某些使用场景是 DFS 做不到的，只能使用 BFS 遍历。这就是本文要介绍的两个场景：「层序遍历」、「最短路径」。


#### 1.2.1 DFS 与 BFS






#### 1.2.2 BFS 的应用一：层序遍历









## 2 最短路径

<img src ="https://img-blog.csdnimg.cn/a011509955b14db8882b748e071dae49.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/as-far-from-land-as-possible/description/](https://leetcode.cn/problems/as-far-from-land-as-possible/description/)






#### 1.2.3 BFS 的应用二：最短路径









_______

## 参考
- BFS 的使用场景总结：层序遍历、最短路径问题：[https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/244853/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/](https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/244853/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/)

