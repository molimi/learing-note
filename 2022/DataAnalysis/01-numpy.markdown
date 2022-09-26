NumPy(Numerical Python) 是科学计算基础库，提供大量科学计算相关功能，比如数据统计，随机数生成等。其提供最核心类型为多维数组类型（ndarray），支持大量的维度数组与矩阵运算，Numpy 支持向量处理 ndarray 对象，提高程序运算速度。

## 1 基础知识

先终端输入命令`pip install numpy -i https://pypi.doubanio.com/simple/`下载`numpy`，然后导入库：
```python
import numpy as np 
```

### 1.1 ndarray对象
NumPy 定义了一个 n 维数组对象，简称 ndarray 对象，它是一个一系列相同类型元素组成的数组集合。数组中的每个元素都占有大小相同的内存块。

ndarray 对象采用了数组的索引机制，将数组中的每个元素映射到内存块上，并且按照一定的布局对内存块进行排列，常用的布局方式有两种，即按行或者按列。
创建一个 ndarray 只需调用 NumPy 的 array 函数即可：
```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
'''
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
'''
```

### 1.2 数据类型
numpy 支持的数据类型比 Python 内置的类型要多很多，基本上可以和 C 语言的数据类型对应上，其中部分类型对应为 Python 内置的类型。下表列举了常用 NumPy 基本类型。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/00b68871e85f4f3b944910a803322e04.png#pic_center"> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1 NumPy数据类型</div> </center>
数据类型对象 (dtype)是使用以下语法构造的：

```python
numpy.dtype(object, align, copy)
```

- object - 要转换为的数据类型对象
- align - 如果为 true，填充字段使其类似 C 的结构体。
- copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用
下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
```python
import numpy as np
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)      # 输出结构化数据student
ex = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)    # 将其应用于ndarray对象
print(ex)
```
输出为：
> [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]
> [(b'abc', 21, 50.) (b'xyz', 18, 75.)]

提示：字节顺序是通过对数据类型预先设定 < 或 > 来决定的。 < 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。> 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。

### 1.3 数组属性
1. size属性：数组元素个数
```python
array_one = np.arange(1, 100, 2)
array_two = np.random.rand(3, 4)
print(array_one.size, array_two.size)       # 50, 12
```

2. shape属性：数组的形状
ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。比如，一个二维数组，其维度表示"行数"和"列数"。ndarray.shape 也可以用于调整数组大小。
```python
print(array_one.shape, array_two.shape)     # (50,) (3, 4)
```

3. dtype属性：数组元素的数据类型
```python
print(array_one.dtype, array_two.dtype)     # int32 float64
```

4. ndim属性：数组的维度
```python
print(array_one.ndim, array_two.ndim)       # 1 2
```

5. itemsize属性：数组单个元素占用内存空间的字节数
```python
array_three = np.arange(1, 100, 2, dtype=np.int8)
print(array_one.itemsize, array_two.itemsize, array_three.itemsize)     # 4 8 1
```

6. nbytes属性：数组所有元素占用内存空间的字节数
```python
print(array_one.nbytes, array_two.nbytes, array_three.nbytes)       # 200 96 50
```

7. flat属性：数组（一维化之后）元素的迭代器
```python
from typing import Iterable
print(isinstance(array_two.flat, np.ndarray), isinstance(array_two.flat, Iterable))     # False True
```

8. base属性：数组的基对象（如果数组共享了其他数组的内存空间）
```python
array_four = array_one[:]
print(array_four.base is array_one, array_one.base is array_three)      # True False
```

小结：
<table class="reference">
<thead><tr class="header"><th>属性</th><th>说明</th></tr></thead>
<tbody>
<tr><td>ndarray.ndim</td><td>秩，即轴的数量或维度的数量</td></tr>
<tr><td>ndarray.shape</td><td>数组的维度，对于矩阵，n 行 m 列</td></tr>
<tr><td>ndarray.size</td><td>数组元素的总个数，相当于 .shape 中 n*m 的值</td></tr>
<tr><td>ndarray.dtype</td><td>ndarray 对象的元素类型</td></tr>
<tr><td>ndarray.itemsize</td><td>ndarray 对象中每个元素的大小，以字节为单位</td></tr>
<tr><td>ndarray.flags</td><td>ndarray 对象的内存信息</td></tr>
<tr><td>ndarray.real</td><td>ndarray元素的实部</td></tr>
<tr><td>ndarray.imag</td><td>ndarray 元素的虚部</td></tr>
<tr><td>ndarray.data</td><td>包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。</td></tr>
</tbody>
</table>

## 2 基本操作
### 2.1 创建数组
**1. 一维数组**
方法一：使用`array`函数，通过`list`创建数组对象
```python
array1 = np.array([1, 2, 3, 4, 5])
array1      # array([1, 2, 3, 4, 5])
```
方法二：使用`arange`函数，指定取值范围创建数组对象
```python
array2 = np.arange(0, 20, 2)
array2      # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
```
方法三：使用`linspace`函数，用指定范围均匀间隔的数字创建数组对象
```python
array3 = np.linspace(-5, 5, 101)
array3      # array([-5., -4.9, -4.8, ..., 4.8, 4.9, 5.])
```
方法四：使用`numpy.random`模块的函数生成随机数创建数组对象
产生10个$[0, 1)$范围的随机小数，代码：
```python
array4 = np.random.rand(10)
array4  # 
```
产生10个$[1, 100)$范围的随机整数，代码：
```python
array5 = np.random.randint(1, 100, 10)
array5      # array([29, 97, 87, 47, 39, 19, 71, 32, 79, 34])
```
产生20个$\mu=50, \sigma=10$的正态分布随机数，代码：
```python
array6 = np.random.normal(50, 10, 20)
array6
```
**2. 二维数组**
方法一：使用`array`函数，通过嵌套的`list`创建数组对象
```python
array7 = np.array([[1, 2, 3], [4, 5, 6]])
array       # array([[1, 2, 3], [4, 5, 6]])
```
方法二：使用`zeros`、`ones`、`full`、`empty`函数指定数组的形状创建数组对象
```python
array8 = np.zeros((3, 4))      # 生成3×4的全零数组
array9 = np.ones((3, 4))       # 生成3×4的全一数组
array10 = np.full((3, 4), 6)   # 生成3×4的全6数组
array10 = np.empty((3, 4))     # 生成3×4未初始化的数组
```
提示：numpy.empty() 返回的数组带有随机值，但这些数值并没有实际意义。切记 empty 并非创建空数组。

方法三：使用`eye`函数创建单位矩阵
```python
array11 = np.eye(4) # # 生成4×4的单位矩阵
```
方法四：通过`reshape`将一维数组变成二维数组
```python
array12 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)        
```
温馨提示：`reshape`是`ndarray`对象的一个方法，使用`reshape`方法时需要确保调形后的数组元素个数与调形前数组元素个数保持一致，否则将会产生异常。

补充：
有时候会遇到`array_ex.reshape(c, -1)`，表示将此矩阵或者数组重组，以c行d列的形式表示，如下：
```python
arr.shape       # (a, b)
arr.reshape(m ,-1)  # 改变维度为m行、d列 （-1表示列数自动计算，d= a*b /m ）
arr.reshape(-1, m)  # 改变维度为d行、m列 （-1表示行数自动计算，d= a*b /m ）
```
-1的作用就在此: 自动计算d：d=数组或者矩阵里面所有的元素个数/c, d必须是整数，不然报错）

常用的reshape(1, -1) 转化成一行，reshape(-1, 1)转化成一列。

方法五：通过`numpy.random`模块的函数生成随机数创建数组对象

```python
array13 = np.random.rand(3, 4)      # [0,1)范围的随机小数构成的3行4列的二维数组
array14 = np.random.randint(1, 100, (3, 4))     # [1, 100)范围的随机整数构成的3行4列的二维数组
```
**3. 多维数组**
方法一：使用随机的方式创建多维数组
```python
array15 = np.random.randint(1, 100, (3, 4, 5))      # 3×4×5的数组
```

方法二：将一维二维的数组调形为多维数组
```python
array16 = np.arange(1, 25).reshape((2, 3, 4))       # 一维数组调形为多维数组
array17 = np.random.randint(1, 100, (4, 6)).reshape((4, 3, 2))      # 二维数组调形为多维数组
```

方法三：读取图片获得对应的三维数组
```python
from matplotlib import pyplot as plt        # 导入库
array18 = plt.imread('01.jpg')              # 任意加载一张图片
```
### 2.2 索引和切片
NumPy 的ndarray对象可以进行索引和切片操作，通过索引可以获取或修改数组中的元素，通过切片可以取出数组的一部分。

1. 索引运算
一维数组
```python
array19 = np.arange(10)
print(array19[0], array19[array19.size-1])      # 0 9
print(array19[-array19.size], array19[-1])      # 0 9
```
二维数组位置可以参考下图：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/0e3a819a976d4ef48975c3413dd72abe.png#pic_center" width=50%> </center>
```python
array20 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array20[2])       # [7 8 9]
print(array20[0][0], array20[-1][-1])       # 1 9
```
2. 切片运算
切片是形如[开始索引:结束索引:步长]的语法，通过指定开始索引（默认值无穷小）、结束索引（默认值无穷大）和步长（默认值1），从数组中取出指定部分的元素并构成新的数组。因为开始索引、结束索引和步长都有默认值，所以它们都可以省略，如果不指定步长，第二个冒号也可以省略。一维数组的切片运算跟 Python 中的list类型的切片非常类似，可以参考列表切片操作，二维数组的切片可以参考下面的图片。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/e92aeaa1b601498485e383e2995b9e42.png#pic_center" width=50%> </center>

```python
print(array20[:2, 1:])      # [[2 3] [5 6]]
print(array20[2])           # [7 8 9]
print(array20[2, :])        # [7 8 9]
print(array20[2:, :])       # [[7 8 9]]
print(array20[:, :2])       # [[1 2] [4 5] [7 8]]
print(array20[1, :2])       # [4 5]
print(array20[1:2, :2])     # [[4 5]]
print(array20[::2, ::2])    # [[1 3] [7 9]]
print(array20[::-2, ::-2])  # [[9 7] [3 1]]
```

3. 花式索引
花式索引（Fancy indexing）是指利用整数数组进行索引，这里所说的整数数组可以是 NumPy 的ndarray，也可以是 Python 中list、tuple等可迭代类型，可以使用正向或负向索引。
```python
array22 = np.array([[30, 20, 10], [40, 60, 50], [10, 90, 80]])
array22[[0, 2]]         # 取二维数组的第1行和第3行
array22[[0, 2], [1, 2]] # 取二维数组第1行第2列，第3行第3列的两个元素 array([20, 80])
array22[[0, 2], 1]      # 取二维数组第1行第2列，第3行第2列的两个元素 array([20, 90])
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/88078c48e296480b931ed0e60ecbe988.png#pic_center" width=50%> </center>

4. 布尔索引
布尔索引就是通过布尔类型的数组对数组元素进行索引，布尔类型的数组可以手动构造，也可以通过关系运算来产生布尔类型的数组。
```python
array23 = np.arange(1, 10)
array23[[True, False, True, True, False, False, False, False, True]]    # array([1, 3, 4, 9])
array23 >= 5    # array([False, False, False, False,  True,  True,  True,  True,  True])
~(array23 >= 5) # ~运算符可以实现逻辑变反，array([ True,  True,  True,  True, False, False, False, False, False])
array23[array23 >= 5]   # array([5, 6, 7, 8, 9])
```


温馨提示：<font color=#9900CC><strong>切片操作虽然创建了新的数组对象，但是新数组和原数组共享了数组中的数据，</strong></font>简单的说，如果通过新数组对象或原数组对象修改数组中的数据，其实修改的是同一块数据。花式索引和布尔索引也会创建新的数组对象，而且新数组复制了原数组的元素，新数组和原数组并不是共享数据的关系，这一点通过前面讲的数组的base属性也可以了解到，在使用的时候要引起注意。

### 2.3 广播机制
广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。

如果两个数组 array38 和 array25 形状相同，即满足 array38.shape == array25.shape，那么 array38*array25 的结果就是 array38 与 array25 数组对应位相乘。这要求维数相同，且各维度的长度相同。
```python
array38 = np.array([1, 2, 3, 4])
array25 = np.array([10, 20, 30, 40])
array26 = array38 * array25
print(array26)        # [10 40 90 160]
```
当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。如：
```python
array27 = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
array28 = np.array([1,2,3])
print(array27 + array28)
```
运算结果如下图所示：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/1ece32961dd8436587151c164aa807bd.png#pic_center" width=50%> </center>

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/44ffa3ea6a43498fadc30301c08a8239.png#pic_center" width=50%> </center>

### 2.4 遍历数组
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式，可以配合 for 循环完成对数组元素的遍历。示例一：
```python
array29 = np.arange(0,60,5)
array29 = array29.reshape(3,4)
for x in np.nditer(array26):      # 使用nditer迭代器,并使用for进行遍历
   print(x)     # 0 5 10 15 20 25 30 35 40 45 50 55
```

在内存中，Numpy 数组提供了两种存储数据的方式，分别是 C-order（行优先顺序）与 Fortrant-order（列优先顺序）。nditer 迭代器选择了一种与数组内存布局一致的顺序，之所以这样做，是为了提升数据的访问效率。

在默认情况下，当我们遍历数组中元素的时候，不需要考虑数组的存储顺序，这一点可以通过遍历上述数组的转置数组来验证。示例二：
```python
array30 = np.arange(0,60,5)
array30 = array30.reshape(3,4)
array31 = array30.T     # a的转置数组
for x in np.nditer(array31):      
   print(x，end=",")        # a转置后的遍历输出 0 5 10 15 20 25 30 35 40 45 50 55
```
下面以 C 样式访问转置数组的副本。示例 3 如下：
```python
array32 = np.arange(0,60,5).reshape(3,4)
for x in np.nditer(array32.T.copy(order='C')):        # copy方法生成数组副本
    print (x, end=", " )        # 0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,
```
控制遍历顺序
- for x in np.nditer(array, order='F'):Fortran order，即是列序优先；
- for x in np.nditer(array30.T, order='C'):C order，即是行序优先；

```python
array33 = np.arange(0,60,5)
array33 = array33.reshape(3,4)
print(array33)
for x in np.nditer(array33, order = 'C'):
   print (x,end=",")    # C-order行顺序 0,5,10,15,20,25,30,35,40,45,50,55,
for x in np.nditer(array33, order = 'F'):
   print (x,end=",")    # F-order列顺序 0,20,40,5,25,45,10,30,50,15,35,55,
```

### 2.5 其他

<table><caption>数组变维操作</caption>
   <thead><tr><th>函数名称</th><th>函数介绍</th></tr></thead>
   <tbody>
<tr><td>reshape</td><td>在不改变数组元素的条件下，修改数组的形状。</td></tr>
<tr><td>flat</td><td>返回是一个迭代器，可以用 for 循环遍历其中的每一个元素。</td></tr>
<tr><td>flatten</td><td>以一维数组的形式返回一份数组的副本，对副本的操作不会影响到原数组。</td></tr>
<tr><td>ravel</td><td>返回一个连续的扁平数组（即展开的一维数组），与 flatten不同，它返回的是数组视图（修改视图会影响原数组）。</td></tr></tbody></table>

<table>
	<caption>数组转置操作</caption>
   <thead><tr><th>函数名称</th><th>函数介绍</th></tr></thead>
	<tbody><tr><td>transpose</td><td>将数组的维度值进行对换，比如二维数组维度(2,4)使用该方法后为(4,2)</td></tr>
		<tr><td>ndarray.T</td><td>与 transpose 方法相同</td></tr>
		<tr><td>rollaxis</td><td>沿着指定的轴向后滚动至规定的位置</td></tr>
		<tr><td>swapaxes</td><td>对数组的轴进行对换</td></tr></tbody></table>

<table class="reference">
<caption>数组转置操作</caption>
<thead>
<tr><th>函数名称</th><th>函数介绍</th></tr>
</thead><tbody><tr><td><code>resize</code></td><td> 返回指定形状的新数组</td></tr>
<tr><td><code>append</code></td><td> 将值添加到数组末尾</td></tr>
<tr><td><code>insert</code></td><td> 沿规定的轴将元素值插入到指定的元素前</td>
</tr>
<tr><td><code>delete</code></td><td> 删掉某个轴的子数组，并返回删除后的新数组</td></tr>
<tr><td><code>unique</code> </td><td>用于删除数组中重复的元素，并按元素值由大到小返回一个新数组</td></tr></tbody></table>

注：resize 仅对原数组进行修改，没有返回值，而 reshape 不仅对原数组进行修改，同时返回修改后的结果。

Numpy 数组操作：修改数组形状、翻转数组、修改数组维度、连接数组、分割数组、数组元素的添加与删除，了解更多请阅读：[https://www.runoob.com/numpy/numpy-array-manipulation.html](https://www.runoob.com/numpy/numpy-array-manipulation.html)


## 3 常用函数
### 3.1 通用一元函数

通用函数是对ndarray中的数据执行元素级运算的函数。你可以将其看做普通函数（接收一个标量值作为参数，返回一个标量值）的矢量化包装器，如下所示。

**表1：通用一元函数**
| 函数                             | 说明                                          |
| -------------------------------- | --------------------------------------------- |
| `abs` / `fabs`                   | 求绝对值的函数                                |
| `sqrt`                           | 求平方根的函数，相当于`array ** 0.5 `         |
| `square`                         | 求平方的函数，相当于`array ** 2`              |
| `exp`                            | 计算$e^x$的函数                               |
| `log` / `log10` / `log2`         | 对数函数（`e`为底 / `10`为底 / `2`为底）      |
| `sign`                           | 符号函数（`1` - 正数；`0` - 零；`-1` - 负数） |
| `ceil` / `floor`                 | 上取整 /  下取整                              |
| `isnan`                          | 返回布尔数组，NaN对应`True`，非NaN对应`False` |
| `isfinite` / `isinf`             | 判断数值是否为无穷大的函数                    |
| `cos` / `cosh` / `sin`           | 三角函数                                      |
| `sinh` / `tan` / `tanh`          | 三角函数                                      |
| `arccos` / `arccosh` / `arcsin`  | 反三角函数                                    |
| `arcsinh` / `arctan` / `arctanh` | 反三角函数                                    |
| `rint` / `round`                 | 四舍五入函数                                  |
```python
array34 = np.array([0, 30, 45, 60, 90])
print(np.sin(array34*np.pi/180))    # [0. 0.5 0.70710678 0.8660254  1.]
```

### 3.2 通用二元函数

**表2：通用二元函数**
| 函数                              | 说明 |
| --------------------------------- | ---- |
| `add(x, y)` / `substract(x, y)` | 加法函数 / 减法函数 |
|`multiply(x, y)` / `divide(x, y)`|乘法函数 / 除法函数|
| `floor_divide(x, y)` / `mod(x, y)` | 整除函数 / 求模函数 |
|`allclose(x, y)`|检查数组`x`和`y`元素是否几乎相等|
| `power(x, y)`                     | 数组$x$的元素$x_i$和数组$y$的元素$y_i$，计算$x_i^{y_i}$ |
| `maximum(x, y)` / `fmax(x, y)`   | 两两比较元素获取最大值 / 获取最大值（忽略NaN） |
| `minimum(x, y)` / `fmin(x, y)`    | 两两比较元素获取最小值 / 获取最小值（忽略NaN） |
| `inner(x, y)` | 内积运算 |
| `cross(x, y) `/ `outer(x, y)` | 叉积运算 / 外积运算 |
| `intersect1d(x, y)` | 计算`x`和`y`的交集，返回这些元素构成的有序数组        |
| `union1d(x, y)`     | 计算`x`和`y`的并集，返回这些元素构成的有序数组        |
| `in1d(x, y)`        | 返回由判断`x` 的元素是否在`y`中得到的布尔值构成的数组 |
| `setdiff1d(x, y)`   | 计算`x`和`y`的差集，返回这些元素构成的数组            |
| `setxor1d(x, y)`    | 计算`x`和`y`的对称差，返回这些元素构成的数组          |

>**补充说明**：在二维空间内，两个向量$\boldsymbol{A}=\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$和$\boldsymbol{B}=\begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$的叉积是这样定义的：$\boldsymbol{A}\times \boldsymbol{B}=\begin{vmatrix} a_1 \quad a_2 \\ b_1 \quad b_2 \end{vmatrix}=a_1b_2 - a_2b_1$，其中$\begin{vmatrix} a_1 \quad a_2 \\ b_1 \quad b_2 \end{vmatrix}$称为行列式。但是一定要注意，叉积并不等同于行列式，行列式的运算结果是一个标量，而叉积运算的结果是一个向量。如果不明白，我们可以看看三维空间两个向量，$\boldsymbol{A}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix}$和$\boldsymbol{B}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$的叉积是$\left< \hat{i} \begin{vmatrix} a_2 \quad a_3 \\ b_2 \quad b_3 \end{vmatrix}, -\hat{j} \begin{vmatrix} a_1 \quad a_3 \\ b_1 \quad b_3 \end{vmatrix}, \hat{k} \begin{vmatrix} a_1 \quad a_2 \\ b_1 \quad b_2 \end{vmatrix} \right>$，其中$\hat{i}, \hat{j}, \hat{k}$代表每个维度的单位向量。
```python
array36 = np.array([10, 20, 30])
array37 = np.array([3, 5, 7])
print(np.mod(array36, array37))  # [1 0 2]
```

### 3.3 统计函数
统计方法主要包括：sum()、mean()、std()、var()、min()、max()、argmin()、argmax()、cumsum()等，分别用于对数组中的元素求和、求平均、求标准差、求方差、找最大、找最小、求累积和等，请参考下面的代码。
```python
array38 = np.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
print(array38.sum())        # 30
print(array38.mean())       # 3.0
print(array38.max())        # 5
print(array38.min())        # 1
print(array38.std())        # 1.4142135623730951
print(array38.var())        # 2.0
print(array38.cumsum())     # [ 1  3  6 10 15 20 24 27 29 30]
```

all() / any()方法：判断数组是否所有元素都是True / 判断数组是否有为True的元素。
astype()方法：拷贝数组，并将数组中的元素转换为指定的类型。
dot()方法：实现一个数组和另一个数组的点积运算。


## 4 其他
### 4.1 矩阵库
NumPy 中提供了专门用于线性代数（linear algebra）的模块和表示矩阵的类型matrix，当然我们通过二维数组也可以表示一个矩阵，官方并不推荐使用matrix类而是建议使用二维数组，而且有可能在将来的版本中会移除matrix类。NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。
<table>
	<caption>Matrix矩阵库</caption>
   <thead><tr><th>函数名称</th><th>函数介绍</th></tr></thead>
	<tbody><tr><td>matlib.empty()</td><td>返回一个空矩阵，所以它的创建速度非常快</td></tr>
		<tr><td>numpy.matlib.zeros()</td><td>创建一个以 0 填充的矩阵</td></tr>
		<tr><td>numpy.matlib.ones()</td><td>创建一个以 1 填充的矩阵</td></tr>
		<tr><td>numpy.matlib.eye() </td><td>返回一个对角线元素为 1，而其他元素为 0 的矩阵</td></tr>
      <tr><td>numpy.matlib.identity()</td><td>返回一个给定大小的单位矩阵，矩阵的对角线元素为 1，而其他元素均为 0</td></tr>
      <tr><td>numpy.matlib.rand()</td><td> 创建一个以随机数填充，并给定维度的矩阵</td></tr></tbody></table>

### 4.2 线性代数

NumPy 提供了 numpy.linalg 模块，该模块中包含了一些常用的线性代数计算方法

| 函数            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| `diag`          | 以一维数组的形式返回方阵的对角线元素或将一维数组转换为方阵（非对角元素元素为0） |
| `vdot` | 向量的点积                                      |
| `dot`  | 数组的点积                                      |
| `inner`  | 数组的内积                                      |
| `outer`  | 数组的叉积                                      |
| `trace`         | 计算对角线元素的和                                           |
| `norm`  | 求模（范数）运算                                  |
| `det`           | 计算行列式的值（在方阵上计算会得到一个标量）             |
| `matrix_rank`   | 计算矩阵的秩                                      |
| `eig`           | 计算矩阵的特征值（eigenvalue）和特征向量（eigenvector）      |
| `inv`           | 计算非奇异矩阵（$n$阶方阵）的逆矩阵                          |
| `pinv`          | 计算矩阵的摩尔-彭若斯（Moore-Penrose）广义逆                 |
| `qr`            | QR分解（把矩阵分解成一个正交矩阵与一个上三角矩阵的积）       |
| `svd`           | 计算奇异值分解（singular value decomposition）               |
| `solve`         | 解线性方程组$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$，其中$\boldsymbol{A}$是一个方阵 |
| `lstsq`         | 计算$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$的最小二乘解 |




重要概念
副本和视图
副本是一个数据的完整的拷贝，如果我们对副本进行修改，它不会影响到原始数据，物理内存不在同一位置。

视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。

视图一般发生在：

1、numpy 的切片操作返回原数据的视图。
2、调用 ndarray 的 view() 函数产生一个视图。
副本一般发生在：

Python 序列的切片操作，调用deepCopy()函数。
调用 ndarray 的 copy() 函数产生一个副本。

字节交换‘
在几乎所有的机器上，多字节对象都被存储为连续的字节序列。字节顺序，是跨越多字节的程序对象的存储规则。

大端模式：指数据的高字节保存在内存的低地址中，而数据的低字节保存在内存的高地址中，这样的存储模式有点儿类似于把数据当作字符串顺序处理：地址由小向大增加，而数据从高位往低位放；这和我们的阅读习惯一致。

小端模式：指数据的高字节保存在内存的高地址中，而数据的低字节保存在内存的低地址中，这种存储模式将地址的高低和数据位权有效地结合起来，高地址部分权值高，低地址部分权值低。

补充：
NumPy 通常处理实数多一些，对于字符串、二进制运算、IO操作，可以参考：NumPy 字符串函数：[https://www.runoob.com/numpy/numpy-string-functions.html](https://www.runoob.com/numpy/numpy-string-functions.html)、NumPy 位运算[https://www.runoob.com/numpy/numpy-binary-operators.html](https://www.runoob.com/numpy/numpy-binary-operators.html)、IO操作[https://www.runoob.com/numpy/numpy-linear-algebra.html](https://www.runoob.com/numpy/numpy-linear-algebra.html)




## 参考
- Python之numpy详细教程：[https://blog.csdn.net/qq_46092061/article/details/118410838](https://blog.csdn.net/qq_46092061/article/details/118410838)
- Numpy教程：[https://www.runoob.com/numpy/numpy-tutorial.html](https://www.runoob.com/numpy/numpy-tutorial.html)
- Numpy：[http://c.biancheng.net/numpy/what-is-numpy.html](http://c.biancheng.net/numpy/what-is-numpy.html)
- 最全的NumPy教程：[https://blog.51cto.com/python3/2950582](https://blog.51cto.com/python3/2950582)