



LeetCode[48] 旋转图像

LeetCode[54] 螺旋矩阵

LeetCode[59] 螺旋矩阵Ⅱ

## 1 二维数组遍历


<blockquote><ul>
<li><p><a href="https://leetcode.cn/problems/rotate-image/" target="_blank">48. 旋转图像</a> </p>
<li><p><a href="https://leetcode.cn/problems/spiral-matrix/" target="_blank">54. 螺旋矩阵</a></p>
<li><p><a href="https://leetcode.cn/problems/spiral-matrix-ii/" target="_blank">59. 螺旋矩阵Ⅱ</a></p></li>
</ul></blockquote> 

### 1.1 旋转图像
#### 1.1.1 题目描述
<img src ="https://img-blog.csdnimg.cn/527e6eab2a274c3393c50dadc9333e6f.png#pic_center" width = 80%>


题目链接：[https://leetcode.cn/problems/rotate-image/](https://leetcode.cn/problems/rotate-image/)

#### 1.1.2 辅助矩阵

如下图所示，矩阵顺时针旋转 $90^{\circ}$ 后，可找到以下规律：
- 「第 $i$ 行」元素旋转到「第 $n−1−i$ 列」元素；
- 「第 $j$ 列」元素旋转到「第 $j$ 行」元素；
因此，对于矩阵任意第 $i$ 行、第 $j$ 列元素 $matrix[i][j]$，矩阵旋转 $90^{\circ}$ 后「元素位置旋转公式」为：

$$\begin{aligned} matrix[i][j] & \rightarrow matrix[j][n - 1 - i] \\ 
原索引位置 & \rightarrow 旋转后索引位置 \end{aligned}$$

​<img src ="https://img-blog.csdnimg.cn/3e3cf587324f4c7c9464903449d64b3f.png#pic_center" width = 48%>
 
根据以上「元素旋转公式」，考虑遍历矩阵，将各元素依次写入到旋转后的索引位置。但仍存在问题：在写入一个元素 $matrix[i][j] \rightarrow matrix[j][n - 1 - i]$ 后，原矩阵元素 $matrix[j][n - 1 - i]$ 就会被覆盖（即丢失），而此丢失的元素就无法被写入到旋转后的索引位置了。

为解决此问题，考虑借助一个「辅助矩阵」暂存原矩阵，通过遍历辅助矩阵所有元素，将各元素填入「原矩阵」旋转后的新索引位置即可。

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 深拷贝 matrix -> tmp
        tmp = copy.deepcopy(matrix)
        # 根据元素旋转公式，遍历修改原矩阵 matrix 的各元素
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = tmp[i][j]
```

遍历矩阵所有元素的时间复杂度为 $O(N^2)$；由于借助了一个辅助矩阵，空间复杂度为 $O(N^2)$。

#### 1.1.3 原地修改

考虑不借助辅助矩阵，通过在原矩阵中直接「原地修改」，实现空间复杂度 O(1)O(1)O(1) 的解法。

以位于矩阵四个角点的元素为例，设矩阵左上角元素 $A$、右上角元素 $B$、右下角元素 $C$、左下角元素 $D$。矩阵旋转 $90^{\circ}$ 后，相当于依次先后执行 $D \rightarrow A$，$C \rightarrow D$，$B \rightarrow C$，$A \rightarrow B$ 修改元素，即如下「首尾相接」的元素旋转操作：
$$A \leftarrow D \leftarrow C \leftarrow B \leftarrow A$$

<img src ="https://img-blog.csdnimg.cn/b7ff4b6434574b498d34bde77020eccb.png#pic_center" width = 48%>

如上图所示，由于第 $1$ 步 $D \rightarrow A$ 已经将 $A$ 覆盖（导致 $A$ 丢失），此丢失导致最后第 $4$ 步 $A \rightarrow B$ 无法赋值。为解决此问题，考虑借助一个「辅助变量 tmp」预先存储 $A$，此时的旋转操作变为：

$$暂存 tmp = A \\
A \leftarrow D \leftarrow C \leftarrow B \leftarrow tmp$$

<img src ="https://img-blog.csdnimg.cn/664f32437e234c8cadfee8d166b4bea8.png#pic_center" width = 48%>

如上图所示，一轮可以完成矩阵 4 个元素的旋转。因而，只要分别以矩阵左上角 $\frac{1}{4}$ 的各元素为起始点执行以上旋转操作，即可完整实现矩阵旋转。

具体来看，当矩阵大小 $n$ 为偶数时，取前 $\frac{n}{2}$ 行、前 $\frac{n}{2}$ 列的元素为起始点；当矩阵大小 $n$ 为奇数时，取前 $\frac{n}{2}$ 行、前 $\frac{n + 1}{2}$ 列的元素为起始点。

令 $matrix[i][j]=A$，根据文章开头的元素旋转公式，可推导得适用于任意起始点的元素旋转操作：

$$
暂存 tmp = matrix[i][j] \\
matrix[i][j] \leftarrow matrix[n - 1 - j][i] \leftarrow matrix[n - 1 - i][n - 1 - j] \leftarrow matrix[j][n - 1 - i] \leftarrow tmp $$

如下图所示，为示例矩阵的算法执行流程。

<img src ="https://img-blog.csdnimg.cn/b1faf898fef444e3bbbc9b82eaa3c7d8.gif#pic_center" width = 48%>

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 设矩阵行列数为 n
        n = len(matrix)
        # 起始点范围为 0 <= i < n // 2 , 0 <= j < (n + 1) // 2
        # 其中 '//' 为整数除法
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 暂存 A 至 tmp
                tmp = matrix[i][j]
                # 元素旋转操作 A <- D <- C <- B <- tmp
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
```

**复杂度分析**

时间复杂度 $O(N^2)$： 其中 $N$ 为输入矩阵的行（列）数。需要将矩阵中每个元素旋转到新的位置，即对矩阵所有元素操作一次，使用 $O(N^2)$ 时间。
空间复杂度 $O(1)$： 临时变量 $tmp$ 使用常数大小的额外空间。值得注意，当循环中进入下轮迭代，上轮迭代初始化的 $tmp$ 占用的内存就会被自动释放，因此无累计使用空间。

#### 1.1.4 对角线反转，左右翻转

<center class = "half"><img src ="https://img-blog.csdnimg.cn/637cd943a28e4e0daecd5f3f22183a20.png#pic_left" width = "30%"><img src = "https://img-blog.csdnimg.cn/a9352cbe7d3c4c00846e7d7231242b95.png#pic_left"  width = "36%"></center></p>

<center class = "half"><img src ="https://img-blog.csdnimg.cn/491d82fa5e2e44d4b0713af46b490eb6.png#pic_left" width = "30%"><img src = "https://img-blog.csdnimg.cn/2fbb1a6b7cc6476dad1952ac70124bd4.png#pic_left"  width = "30%"></center></p>

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            # 注意这里j的范围 如果j的范围也是0到n-1那么会出现交换后又交换回来 等于没有交换
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for line in matrix:
            line.reverse()      # 左右翻转
```
#### 1.1.5 上下反转，对角线反转

<img src ="https://img-blog.csdnimg.cn/f416b80bd9b645fbb1092edf25f8b9fa.png#pic_center" width = 48%>

```python
class Solution:
    def rotate(self, matrix):
        matrix[:] = matrix[::-1]        # 上下反转
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```


### 1.2 螺旋矩阵
#### 1.2.1 题目描述
<img src ="https://img-blog.csdnimg.cn/6d55d8fc218f4a21a4bcaf7306d6931d.png#pic_center" width = 80%>

题目链接：[https://leetcode.cn/problems/spiral-matrix/](https://leetcode.cn/problems/spiral-matrix/)


#### 1.2.2 思路分析

**1. 按照「形状」进行模拟**
解题的核心思路是按照右、下、左、上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界：

<img src ="https://img-blog.csdnimg.cn/0ec43be24ea44f77a266d4faaa015e72.png#pic_center" width = 48%>

随着螺旋遍历，相应的边界会收缩，直到螺旋遍历完整个数组：

<img src ="https://img-blog.csdnimg.cn/d334b5ff1aea41b7a115a5ec96daf5f4.png#pic_center" width = 48%>

```python
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    upper_bound = 0
    lower_bound = len(matrix) - 1
    left_bound = 0
    right_bound = len(matrix[0]) - 1
    res = []
    # res.length == m * n 则遍历完整个数组
    while len(res) < m * n:
        if upper_bound <= lower_bound:
            # 在顶部从左向右遍历
            for j in range(left_bound, right_bound + 1):
                res.append(matrix[upper_bound][j])
            # 上边界下移
            upper_bound += 1
        
        if left_bound <= right_bound:
            # 在右侧从上向下遍历
            for i in range(upper_bound, lower_bound + 1):
                res.append(matrix[i][right_bound])
            # 右边界左移
            right_bound -= 1
        
        if upper_bound <= lower_bound:
            # 在底部从右向左遍历
            for j in range(right_bound, left_bound - 1, -1):
                res.append(matrix[lower_bound][j])
            # 下边界上移
            lower_bound -= 1
        
        if left_bound <= right_bound:
            # 在左侧从下向上遍历
            for i in range(lower_bound, upper_bound - 1, -1):
                res.append(matrix[i][left_bound])
            # 左边界右移
            left_bound += 1
    
    return res
```

**2. 按照「方向」进行模拟**

(1) 起始位置

螺旋矩阵的遍历起点是矩阵的左上角，也就是 `(0, 0)` 位置。

(2) 移动方向

起始位置的下一个移动方向是向右。在遍历的过程中，移动方向是固定的：
$$右→，下↓，左←，上↑$$

移动方向是按照上面的顺序循环进行的。每次当移动到了边界，才会更改方向。但边界并不是固定的，请看下面分析。

(3) 边界 

本题的边界是最大的难点，因为是随着遍历的过程而变化的。螺旋遍历的时候，已经遍历的数字不能再次遍历，所以边界会越来越小。

规则是：<font color=#9900CC><strong>如果当前行（列）遍历结束之后，就需要把这一行（列）的边界向内移动一格。</strong></font>

以下面的图为例，up, down, left, right 分别表示四个方向的边界，初始时分别指向矩阵的四个边界。如果我们把第一行遍历结束（遍历到了右边界），此时需要修改新的移动方向为向下、并且把上边界 up 下移一格，即从 旧 up 位置移动到 新 up 位置。

<img src ="https://img-blog.csdnimg.cn/48a5978f540e42ffaf12e90f76e0e8d2.jpeg#pic_center" width = 48%>

当绕了一圈后，从下向上走到 新 up 边界的时候，此时需要修改新的移动方向为向右、并且把左边界 left 下移一格，即从 旧 left 位置移动到 新 left 位置。

<img src ="https://img-blog.csdnimg.cn/ebec8294298d4d7f83df2e1ab3c8c3a6.jpeg#pic_center" width = 48%>

由此可见，根据维护的四个方向的边界，就知道什么时候更改移动方向了。

(4) 结束条件

螺旋遍历的结束条件是所有的位置都被遍历到。


**代码实现：**
- up, down, left, right 分别表示四个方向的边界。
- x, y 表示当前位置。
- dirs 分别表示移动方向是 右、下、左、上 。
- cur_d 表示当前的移动方向的下标，dirs[cur_d] 就是下一个方向需要怎么修改 x, y。
- `cur_d == 0 and y == right` 表示当前的移动方向是向右，并且到达了右边界，此时将移动方向更改为向下，并且上边界 up 向下移动一格。
- 结束条件是结果数组 res 的元素个数能与 matrix 中的元素个数。


```python
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])
        left, right, up, down = 0, N - 1, 0, M - 1
        res = []
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        while len(res) != M * N:
            res.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res
```



### 1.3 螺旋矩阵Ⅱ
#### 1.3.1 题目描述
<img src ="https://img-blog.csdnimg.cn/7fe64c24624b491ebdac3573b9ff41e3.png#pic_center" width = 48%>

题目链接：[https://leetcode.cn/problems/spiral-matrix-ii/](https://leetcode.cn/problems/spiral-matrix-ii/)


#### 1.3.2 思路分析

**1. 按照「形状」进行填充**

<img src ="https://img-blog.csdnimg.cn/10d868bcb53940a7a246b8cbf8cff260.png#pic_center" width = 48%>

```python
def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    upper_bound, lower_bound = 0, n - 1
    left_bound, right_bound = 0, n - 1
    # 需要填入矩阵的数字
    num = 1
    
    while num <= n * n:
        if upper_bound <= lower_bound:
            # 在顶部从左向右遍历
            for j in range(left_bound, right_bound+1):
                matrix[upper_bound][j] = num
                num += 1
            # 上边界下移
            upper_bound += 1
        
        if left_bound <= right_bound:
            # 在右侧从上向下遍历
            for i in range(upper_bound, lower_bound+1):
                matrix[i][right_bound] = num
                num += 1
            # 右边界左移
            right_bound -= 1
        
        if upper_bound <= lower_bound:
            # 在底部从右向左遍历
            for j in range(right_bound, left_bound-1, -1):
                matrix[lower_bound][j] = num
                num += 1
            # 下边界上移
            lower_bound -= 1
        
        if left_bound <= right_bound:
            # 在左侧从下向上遍历
            for i in range(lower_bound, upper_bound-1, -1):
                matrix[i][left_bound] = num
                num += 1
            # 左边界右移
            left_bound += 1
    
    return matrix
```
**2. 按照「方向」进行填充**


**(1) 四个变量标记边界**
```python
class Solution(object):
    def generateMatrix(self, n):
        if n == 0: return []
        res = [[0] * n for i in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        count = 0
        while count != n * n:
            res[x][y] = count + 1
            count += 1
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res
```

**(2) 使用非 0 数字标记边界**

我们在遍历的过程中，需要依次放入 $1-N^2$ 数字，如果我们把结果数组的所有位置初始化为 0，那么非 0 的位置就代表我们已经遍历过了，相当于边界。

当遍历到数组的原始边界或者撞到了非 0 的数字，表示当前方向已经遍历到了边界，需要更改移动方向。这个做法的优点是省去了维护 4 个变量表示的边界。

<img src ="https://img-blog.csdnimg.cn/1034bcd0845e452badf50151e7361ae0.jpeg#pic_center" width = 48%>

初始移动方向是向右，如果遇到了数组边界或者遇到了非 0 的数字，那么就要转动方向。转向的方法是 `cur_d = (cur_d + 1) % 4`，cur_d 表示了当前的方向是 directions 中的哪个，顺序依次是 右、下、左、上。

```python
class Solution(object):
    def generateMatrix(self, n):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0] * n for i in range(n)]
        x, y = 0, 0
        count = 0
        cur_d = 0
        while count != n * n:
            res[x][y] = count + 1
            count += 1
            dx, dy = directions[cur_d][0], directions[cur_d][1]
            newx, newy = x + dx, y + dy
            if newx < 0 or newx >= n or newy < 0 or newy >= n or res[newx][newy] != 0:
                cur_d = (cur_d + 1) % 4
                dx, dy = directions[cur_d][0], directions[cur_d][1]
            x, y = x + dx, y + dy
        return res
```




## 参考
- 旋转图像（辅助矩阵 / 原地修改，清晰图解）：[https://leetcode.cn/problems/rotate-image/solutions/1228078/48-xuan-zhuan-tu-xiang-fu-zhu-ju-zhen-yu-jobi/](https://leetcode.cn/problems/rotate-image/solutions/1228078/48-xuan-zhuan-tu-xiang-fu-zhu-ju-zhen-yu-jobi/)
- 矩阵遍历问题的四部曲：[https://leetcode.cn/problems/spiral-matrix-ii/solutions/659234/ju-zhen-bian-li-wen-ti-de-si-bu-qu-by-fu-sr5c/](https://leetcode.cn/problems/spiral-matrix-ii/solutions/659234/ju-zhen-bian-li-wen-ti-de-si-bu-qu-by-fu-sr5c/)