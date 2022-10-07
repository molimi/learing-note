## 1 题目描述
 **1. 定义**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于计算机而言，颜色不过是像素点对应的一个 24 位的数值。现给定一幅分辨率为 M×N 的画，要求你找出万绿丛中的一点红，即有独一无二颜色的那个像素点，并且该点的颜色与其周围 8 个相邻像素的颜色差充分大。


 **2. 输入格式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输入第一行给出三个正整数，分别是 M 和 N（≤ 1000），即图像的分辨率；以及 TOL，是所求像素点与相邻点的颜色差阈值，色差超过 TOL 的点才被考虑。随后 N 行，每行给出 M 个像素的颜色值，范围在 [0,2^24) 内。所有同行数字间用空格或 TAB 分开。


 **3. 输出格式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在一行中按照 (x, y): color 的格式输出所求像素点的位置以及颜色值，其中位置 x 和 y 分别是该像素在图像矩阵中的列、行编号（从 1 开始编号）。如果这样的点不唯一，则输出 Not Unique；如果这样的点不存在，则输出 Not Exist。


 ## 2 思路分析

**1. 问题分析**
- 独一无二的颜色，这个含义是指，可能存在某个点，它的所有邻居点的像素都满足这个“色差”要求，但是这个点的像素（颜色）在整个矩阵中出现不止一次，那么它就不是独一无二的，因此这样的点不是目标点；
- 该点的颜色与其周围 8 个相邻像素的颜色差充分大（注意，如果是边上的点只需要比较 5 个点，角上的点只需要比较 3 个点）。

**2. 求解思路**

- 如何判断是否独一无二：创建字典，在输入数据的同时对每个颜色值统计次数，字典的键：值关系是，颜色值：出现的次数，这样检索较快，也不占用太大空间。
- 充分理解“色差”：在中间的点我们依次判断周围 8 个点即可，但是如何解决边角上的点？有两种简单的解决办法：（1）为四条边和四个角专门写特判；（2）在遍历 8 个点的同时判断坐标是否越界，如果超出数组范围则不判断，默认符合要求。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**小技巧：**这里使用的方法是为矩阵加四条边，即原本$N\times M$的矩阵扩充到$(N+2)\times (M+2)$。且周围多出来的四条边以及四个角上的颜色都是0，这样在遍历八个点的时候就不用特别判断了，对所有的点一视同仁即可。同时，差值要加上绝对值再和`TOL`作比较。加边的同时带来了另一个微小的好处，就是数组的行和列都从 1 开始计数了，符合题目的输出要求，


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上，整个流程就是，先用字典记录每个颜色值出现的次数，然后对次数为1的像素点，遍历周围所有像素点并进行比较，而想要计算与周围的差值，就涉及该像素点是否在边界上，若是，则要小心数组越界导致段错误，为了避免这种麻烦，我们可以直接将数组四周扩大一圈，边界的值默认就是0，对符合条件的像素点记录，并进行结果的打印。下面的代码一使用嵌套列表实现，代码二使用数组实现，切片，元素查找都比较方便。
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;温馨提示：如果将输入的颜色平铺成一位数组（N×M个数据），使用`count`方法会超时！原因是，对于每个点的遍历是$O(N×M)$，然而在这个$N×M$个数据的一位数组上利用`count`方法计数，则内层相当于又嵌套了$O(N×M)$，所以时间性能十分低下。
如果采用“以空间换时间”的策略，开$2^24$的列表存储颜色值的出现次数，虽然时间复杂度降低了，但是这样会内存超限。
综上所述，字典在两者之间作出了平衡。

## 3 代码实现
AC代码一：
```python
import sys

M, N, TOL = list(map(int, input().split()))
fill_lst = [0 for _ in range(M + 2)]
input_list = []
input_dict = {}
result_list = []
for k in range(N):
    temp_lst = list(map(int, sys.stdin.readline().split()))
    for k in range(M):
        if temp_lst[k] in input_dict:
            input_dict[temp_lst[k]] += 1
        else:
            input_dict[temp_lst[k]] = 1
    temp_lst.append(0)              # 在两端填充零
    temp_lst.insert(0, 0)
    input_list.append(temp_lst)
input_list.insert(0, fill_lst)      # 在上下填充零
input_list.append(fill_lst)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if input_dict[input_list[i][j]] == 1:
            low, high = i + 1, i - 1
            right, left = j + 1, j - 1
            length1 = abs(input_list[i][j] - input_list[low][left])     # 计算周围八个元素的差值绝对值
            length2 = abs(input_list[i][j] - input_list[low][j])
            length3 = abs(input_list[i][j] - input_list[low][right])
            length4 = abs(input_list[i][j] - input_list[i][left])
            length5 = abs(input_list[i][j] - input_list[i][right])
            length6 = abs(input_list[i][j] - input_list[high][left])
            length7 = abs(input_list[i][j] - input_list[high][j])
            length8 = abs(input_list[i][j] - input_list[high][right])
            if length1 > TOL and length2 > TOL and length3 > TOL and length4 > TOL and length5 > TOL and length6 > TOL and length7 > TOL and length8 > TOL:
                result_list.append('({}, {}): {}'.format(
                    j, i, input_list[i][j]))

length = len(result_list)
if length == 1:
    print(result_list[0])
elif length == 0:
    print('Not Exist')
else:
    print('Not Unique')
```

AC代码二：
```python
import sys
import numpy as np

# 计算3*3矩阵中心元素和周围元素差值的最小值
def min_matrix(matrix):
    mid = matrix[1][1]
    distance = 16777215
    for i in range(0, 3):
        for j in range(0, 3):
            if i != 1 and j != 1:
                temp = abs(matrix[i][j] - mid)
                if temp < distance:
                    distance = temp
    return distance


def main():
    M, N, TOL = list(map(int, input().split()))
    input_list = []
    input_dict = {}
    result_list = []
    for _ in range(N):
        temp_lst = list(map(int, sys.stdin.readline().split()))
        input_list.append(temp_lst)
        for k in range(M):
            if temp_lst[k] in input_dict:
                input_dict[temp_lst[k]] += 1
            else:
                input_dict[temp_lst[k]] = 1

    input_array = np.array(input_list)
    input_array = np.pad(input_array, (1, 1), 'constant')   # 使用数组在外围填充一圈零

    for iter in input_dict:
        if input_dict[iter] == 1:
            index_i, index_j = np.where(input_array == iter)    # 返回所查找元素的索引，返回值为二维元组
            index_i, index_j = index_i[0], index_j[0]
            if min_matrix(input_array[index_i - 1:index_i + 2,
                                      index_j - 1:index_j + 2]) > TOL:
                result_list.append('({}, {}): {}'.format(
                    index_j, index_i, input_array[index_i][index_j]))

    length = len(result_list)
    if length == 1:
        print(result_list[0])
    elif length == 0:
        print('Not Exist')
    else:
        print('Not Unique')

main()
```

## 4 参考
- PAT 1068-万绿丛中一点红：[https://blog.csdn.net/jialchen/article/details/110674832](https://blog.csdn.net/jialchen/article/details/110674832)
- PAT 1068 万绿丛中一点红 思路解析：[https://blog.csdn.net/G0rgeoustray/article/details/105684208](https://blog.csdn.net/G0rgeoustray/article/details/105684208)