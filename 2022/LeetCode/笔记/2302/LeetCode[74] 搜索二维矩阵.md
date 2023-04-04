## 1 搜索二维矩阵
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/673e79014bee442e8a98410bfe982ff4.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/search-a-2d-matrix/](https://leetcode.cn/problems/search-a-2d-matrix/)

### 1.2 求解思路

**方法一：遍历**
该方法就是遍历查找每个位置，看 target 是否出现。这个方法也能通过本题。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        # return any(target in row for row in matrix)
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == target:
                    return True
        return False
```

- 时间复杂度： $O(M * N)$
- 间复杂度：$O(1)$

**方法二：从左下角或者右上角开始查找**

这个方法是利用了矩阵的性质，如果我们从右上角开始遍历：
- 如果要搜索的 target 比当前元素大，那么让行增加；
- 如果要搜索的 target 比当前元素小，那么让列减小；

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False
```
 
- 时间复杂度：$O(M + N)$
- 空间复杂度：$O(1)$

**方法三：先寻找到所在行**

该方法利用了题目给出的矩阵的性质：每行元素都是单调递增的，并且下一行的元素会比本行更大。所以：

如果 target 大于这一行的末尾元素，那么 target 一定不在这一行中，只能出现在矩阵的下面的行中。

那么，假如 $target < matrix[i][N - 1]$ 时，说明 target 可能在本行中出现，而且由于下面各行的元素都大于 $matrix[i][N - 1]$，所以，不可能在下面的行中出现。此时，可以在本行中使用顺序查找，或者二分查找。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            if target > matrix[i][N - 1]:
                continue
            if target in matrix[i]:
                return True
        return False
```

- 时间复杂度： 在行中遍历查找的时间复杂度是：$O(M+N)$；在行中进行二分查找的时间复杂度是 $O(M+log(N))$
- 空间复杂度：$O(1)$


**方法四：两次二分查找**
这个方法可以说是方法三的改进。在方法三种，我们是先遍历找到 target 在哪一行，然后在该行遍历或者二分查找的 target 。其实也可以先用二分找到 target 所在的行，然后在该行二分找到 target。

具体做法是，先找到 $matrix[i][0]$ 小于 target 并且 $matrix[i + 1][0] > target$ 的第 $i$ 行，然后在该行内进行二分找到 target。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        target_row = bisect.bisect_right(col0, target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col >= N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False
```

- 时间复杂度： $O(log(M) + log(N))$
- 空间复杂度：$O(1)$

**方法五：全局二分**

这个方法，是我们在二维矩阵上进行二分查找，这其实相当于把二维矩阵当做一维来做，要求每一行的最后一个元素小于下一行的第一个元素。

根据 mid 求出在二维矩阵中的具体位置，然后判断 left 和 right 的移动方式。整体做法和一维数组的二分没有区别。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        left, right = 0, M * N - 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[mid // N][mid % N]
            if cur == target:
                return True
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```
- 时间复杂度： $O(log(M∗N))$
- 空间复杂度：$O(1)$

**方法六：reshape成一维数组**

如果用python刷题，在leetcode中是支持使用 numpy 的，可以把 matrix 成一维有序的数组，然后按照一维数组去操作查找。

```python
import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        matrix = np.reshape(matrix, [1, -1])
        return target in matrix
```



_____



## 2 搜索二维矩阵Ⅱ
### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/3143f9fdd4384dfd94ae9db6916959f2.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/search-a-2d-matrix-ii/](https://leetcode.cn/problems/search-a-2d-matrix-ii/)



### 2.2 求解思路

**方法一：直接查找**

直接遍历整个矩阵 $\textit{matrix}$，判断 $\textit{target}$ 是否出现即可。
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False
```
- 时间复杂度：$O(mn)$。
- 空间复杂度：$O(1)$。


**方法二：减而治之**

(1) 选择左下角为起点，以下展示了「减治」的过程

<img src ="https://img-blog.csdnimg.cn/8cd650c2c81c47cb86d49efa865e4af1.gif#pic_center" width = 64%>

总结出搜索的规律是：
- 如果当前数比目标元素小，当前列就不可能存在目标值，「指针」就向右移一格（纵坐标加 1）；
- 如果当前数比目标元素大，当前行就不可能存在目标值，「指针」就向上移一格（横坐标减 1）。

```python
class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        # 起点：左下角
        x, y = rows-1, 0

        # 不越界的条件是：行大于等于 0，列小于 cols
        while x >= 0 and y < cols:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
        return False
```

复杂度分析：
- 时间复杂度：$O(M + N)$，$M$是这个矩阵的行数，$N$是这个矩阵的列数，我们看到，这种算法是不回头的，至多走 $M + N$ 步就能搜索到目标数值，或者判定目标数值在矩阵中不存在；
- 空间复杂度：$O(1)$，算法使用了常数个变量。


(2) 如果选择右上角为起点，以下展示了「减治」的过程

<img src ="https://img-blog.csdnimg.cn/b6925b52500a4aadb2d21563542273a7.gif#pic_center" width = 64%>

总结出「搜索」的规律是：
- 如果当前数比目标元素大，当前列就不可能存在目标值，「指针』就向左移一格（纵坐标减 1）；
- 如果当前数比目标元素小，当前行就不可能存在目标值，「指针」就向下移一格（横坐标加 1）。

```python
class Solution:
    def searchMatrix(self, matrix, target):
        # 特判
        rows, cols = len(matrix), len(matrix[0])

        # 起点：右上
        x, y = 0, cols-1
        
        # 不越界的条件是：行小于 rows，列大于等于 0
        while x < rows and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False
```

**方法三：二分查找**

由于矩阵 $\textit{matrix}$ 中每一行的元素都是升序排列的，因此我们可以对每一行都使用一次二分查找，判断 $\textit{target}$ 是否在该行中，从而判断 $\textit{target}$ 是否出现。

**(1) 详细版**
```python
class Solution:
    def searchMatrix(self, matrix, target):
        def binay_search(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    l = mid + 1
                if nums[mid] > target:
                    r = mid - 1
            return False
        cols = len(matrix[0])
        for line in matrix:
            if line[0] <= target and line[cols - 1] >= target:
                if binay_search(line, target):
                    return True
        return False
```

**(2) 简化版**

```python
class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            ind = bisect.bisect_left(row, target)
            if ind < len(matrix[0]) and row[ind] == target:
                return True
        return False
```

- 时间复杂度：$O(m \log n)$。对一行使用二分查找的时间复杂度为 $O(\log n)$，最多需要进行 $m$ 次二分查找。
- 空间复杂度：$O(1)$。

### 参考
- 减而治之、二分查找：[https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/14389/er-fen-fa-pai-chu-fa-python-dai-ma-java-dai-ma-by-/?orderBy=most_votes](https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/14389/er-fen-fa-pai-chu-fa-python-dai-ma-java-dai-ma-by-/?orderBy=most_votes)
