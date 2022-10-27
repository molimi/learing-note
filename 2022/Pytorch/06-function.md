&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Torch中，张量的操作非常重要，为了便于学习，这里整理下来。

## 1 张量的拆分和拼接
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在 PyTorch 中，对张量 (Tensor) 进行拆分通常会用到两个函数：
- torch.split [按块大小拆分张量]
- torch.chunk [按块数拆分张量]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而对张量 (Tensor) 进行拼接通常会用到另外两个函数：
- torch.cat [按已有维度拼接张量]
- torch.stack [按新维度拼接张量]

**1. 张量的拆分**
(1) torch.split(tensor, split_size_or_sections, dim = 0)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;功能：按块大小拆分张量
- tensor 为待拆分张量
- dim 指定张量拆分的所在维度，即在第几维对张量进行拆分。dim=0是按照行拆分，dim=1是按照列拆分。如果是三维向量的话，可以按照dim=2在矩阵的方向上划分。
- split_size_or_sections 表示在 dim 维度拆分张量时每一块在该维度的尺寸大小 (int)，或各块尺寸大小的列表 (list)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;指定每一块的尺寸大小后，如果在该维度无法整除，则最后一块会取余数，尺寸较小一些。如：长度为 10 的张量，按单位长度 3 拆分，则前三块长度为 3，最后一块长度为 1
- 函数返回：所有拆分后的张量所组成的 tuple，函数并不会改变原 tensor
```python
In [1]: import torch
In [2]: t1 = torch.randn(6, 2)
In [3]: t2 = torch.split(t1, 2, dim = 0)    #返回一个元组tutle
Out[3]:
(tensor([[-0.0039, -0.1259],
        [-0.7630,  1.3833]]), 
 tensor([[-0.7960,  0.2523],
        [-0.5351, -0.5850]]), 
 tensor([[ 0.3403, -0.2898],
        [-0.3122, -0.7490]]))
In [4]: t3 = torch.split(t1, 4, dim = 0)    #除不尽的取余数
Out[4]:
(tensor([[ 1.4674,  0.7185],
        [ 0.4943,  1.4040],
        [-1.5243,  0.0566],
        [-1.2039, -0.3079]]), 
 tensor([[-2.9470, -1.6064],
        [-0.8393, -0.5528]]))
```

(2) torch.chunk(input, chunks, dim = 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;功能：按块数拆分张量
- input 为待拆分张量
- dim 指定张量拆分的所在维度，即在第几维对张量进行拆分
- chunks 表示在 dim 维度拆分张量时最后所分出的总块数 (int)，根据该块数进行平均拆分

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;指定总块数后，如果在该维度无法整除，则每块长度向上取整，最后一块会取余数，尺寸较小一些，若余数恰好为 0，则会只分出 chunks - 1 块。如：长度为 6 的张量，按 4 块拆分，则只分出三块，长度为 2 (6 / 4 = 1.5 → 2)；长度为 10 的张量，按 4 块拆分，则前三块长度为 3 (10 / 4 = 2.5 → 3)，最后一块长度为 1
- 函数返回：所有拆分后的张量所组成的 tuple，函数并不会改变原 input
```python
In [5]: t8 = torch.randn(6, 2)
In [6]: t8
Out[6]:
tensor([[-0.3711,  0.7372],
        [ 0.2608, -0.1129],
        [-0.2785,  0.1560],
        [-0.7589, -0.8927],
        [ 0.1480, -0.0371],
        [-0.8387,  0.6233]])

In [7]: torch.chunk(t8, 2, dim = 0)
Out[7]:
(tensor([[-0.3711,  0.7372],
         [ 0.2608, -0.1129],
         [-0.2785,  0.1560]]),
 tensor([[-0.7589, -0.8927],
         [ 0.1480, -0.0371],
         [-0.8387,  0.6233]]))

In [8]: torch.chunk(t8, 3, dim = 0)
Out[8]:
(tensor([[-0.3711,  0.7372],
         [ 0.2608, -0.1129]]),
 tensor([[-0.2785,  0.1560],
         [-0.7589, -0.8927]]),
 tensor([[ 0.1480, -0.0371],
         [-0.8387,  0.6233]]))

In [9]: torch.chunk(t8, 4, dim = 0)
Out[9]:
(tensor([[-0.3711,  0.7372],
         [ 0.2608, -0.1129]]),
 tensor([[-0.2785,  0.1560],
         [-0.7589, -0.8927]]),
 tensor([[ 0.1480, -0.0371],
         [-0.8387,  0.6233]]))

In [10]: t9 = torch.randn(10, 2)
In [11]: t9
Out[11]:
tensor([[-0.9749,  1.3103],
        [-0.4138, -0.8369],
        [-0.1138, -1.6984],
        [ 0.7512, -0.3417],
        [-1.4575, -0.4392],
        [-0.2035, -0.2962],
        [-0.7533, -0.8294],
        [ 0.0104, -1.3582],
        [-1.5781,  0.8594],
        [ 0.0286,  0.7611]])

In [12]: torch.chunk(t9, 4, dim = 0)
Out[12]:
(tensor([[-0.9749,  1.3103],
         [-0.4138, -0.8369],
         [-0.1138, -1.6984]]),
 tensor([[ 0.7512, -0.3417],
         [-1.4575, -0.4392],
         [-0.2035, -0.2962]]),
 tensor([[-0.7533, -0.8294],
         [ 0.0104, -1.3582],
         [-1.5781,  0.8594]]),
 tensor([[0.0286, 0.7611]]))
```


**2. 张量的合并**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以用`torch.cat`和`torch.stack`方法将多个张量合并，但是torch.cat仅仅是张量的连接，不会增加维度，而torch.stack是堆叠，会增加维度。
(1) torch.cat(tensors, dim = 0, out = None)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;功能：在已有维度拼接张量
- tensors 为待拼接张量的序列，通常为 tuple
- dim 指定张量拼接的所在维度，即在第几维对张量进行拼接，除该拼接维度外，其余维度上待拼接张量的尺寸必须相同
- out 表示在拼接张量的输出，也可直接使用函数返回值
- 函数返回：拼接后所得到的张量，函数并不会改变原 tensors

```python
In [13]: t10 = torch.rand(2, 3)
In [14]: t10
Out[14]:
tensor([[0.1199, 0.9585, 0.4629],
        [0.0949, 0.6016, 0.1782]])
In [15]: torch.cat((t10, t10, t10), dim=0)
Out[15]:
tensor([[0.1199, 0.9585, 0.4629],
        [0.0949, 0.6016, 0.1782],
        [0.1199, 0.9585, 0.4629],
        [0.0949, 0.6016, 0.1782],
        [0.1199, 0.9585, 0.4629],
        [0.0949, 0.6016, 0.1782]])
In [16]: torch.cat((t10, t10, t10), dim=1)
Out[16]:
tensor([[0.1199, 0.9585, 0.4629, 0.1199, 0.9585, 0.4629, 0.1199, 0.9585, 0.4629],
        [0.0949, 0.6016, 0.1782, 0.0949, 0.6016, 0.1782, 0.0949, 0.6016, 0.1782]])
```


(2) torch.stack(tensors, dim = 0, out = None)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;功能：在新维度拼接张量
- tensors 为待拼接张量的序列，通常为 tuple
- dim 指定张量拼接的新维度对应已有维度的插入索引，即在原来第几维的位置上插入新维度对张量进行拼接，待拼接张量在所有已有维度上的尺寸必须完全相同
- out 表示在拼接张量的输出，也可直接使用函数返回值
- 函数返回：拼接后所得到的张量，函数并不会改变原 tensors
```python
In [17]: t14 = torch.randn(2, 3)
In [18]: t14
Out[18]:
tensor([[-0.0288,  0.6936, -0.6222],
        [ 0.8786, -1.1464, -0.6486]])

In [19]: torch.stack((t14, t14, t14), dim = 0)
Out[19]:
tensor([[[-0.0288,  0.6936, -0.6222],
         [ 0.8786, -1.1464, -0.6486]],

        [[-0.0288,  0.6936, -0.6222],
         [ 0.8786, -1.1464, -0.6486]],

        [[-0.0288,  0.6936, -0.6222],
         [ 0.8786, -1.1464, -0.6486]]])

In [20]: torch.stack((t14, t14, t14), dim = 0).shape
Out[20]: torch.Size([3, 2, 3])

In [21]: torch.stack((t14, t14, t14), dim = 1)
Out[21]:
tensor([[[-0.0288,  0.6936, -0.6222],
         [-0.0288,  0.6936, -0.6222],
         [-0.0288,  0.6936, -0.6222]],

        [[ 0.8786, -1.1464, -0.6486],
         [ 0.8786, -1.1464, -0.6486],
         [ 0.8786, -1.1464, -0.6486]]])

In [22]: torch.stack((t14, t14, t14), dim = 1).shape
Out[22]: torch.Size([2, 3, 3])
```

温馨提示：stack与cat的区别在于，`torch.stack()`函数要求输入张量的大小完全相同，得到的张量的维度会比输入的张量的大小多1，并且多出的那个维度就是拼接的维度，那个维度的大小就是输入张量的个数。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;借鉴自————[Pytorch张量的拆分与拼接](https://blog.csdn.net/weixin_43427721/article/details/107208470)

____

## 2 torch.unsqueeze()/torch.squeeze()
**1. 降维torch.squeeze(input, dim=None, out=None)**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;函数功能：<font color=#990CC><strong>去除size为1的维度，包括行和列。当维度大于等于2时，squeeze()无作用。</font></strong>
- 当给定dim时，那么挤压操作只在给定维度上。即若`tensor.size(dim) = 1`，则去掉该维度
      - 其中squeeze(0)代表若第一维度值为1则去除第一维度
      - squeeze(1)代表若第二维度值为1则去除第二维度
      - -1，去除最后维度值为1的维度
- 当不给定dim时，将输入张量形状中的1去除并返回。如果输入是形如($t15×1×t16×1×C×1×D$)，那么输出形状就为： ($t15×t16×C×D$)
例如，输入形状为: ($t15×1×t16$), squeeze(input, 0) 将会保持张量不变，只有用 squeeze(input, 1)，形状会变成 ($t15×t16$)。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意：返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。多维张量本质上就是一个变换，如果维度是 1 ，那么，1 仅仅起到扩充维度的作用，而没有其他用途，因而，在进行降维操作时，为了加快计算，是可以去掉这些 1 的维度。

**参数:**
- input (Tensor) – 输入张量
- dim (int, optional) – 如果给定，则input只会在给定维度挤压，维度的索引（从0开始）
- out (Tensor, optional) – 输出张量

**例子：**
```python
In [23]: t8 = torch.zeros(2, 1, 2, 1, 2)
In [24]: t8.size()        
Out[24]: torch.Size([2, 1, 2, 1, 2])
In [25]: t8.dim()         
Out[25]: 5

In [26]: t9 = torch.squeeze(t8)
In [27]: t9.size()        
Out[27]: 
torch.Size([2, 2, 2])
In [28]: t9.dim()        
Out[28]: 3

In [29]: t10 = torch.squeeze(t8, 0)   
In [30]: t10.size()            
Out[30]:
torch.Size([2, 1, 2, 1, 2])
In [31]: t10.dim()             
Out[31]: 5

In [32]: t14 = torch.squeeze(t8, 1)
In [33]: t14.size()            
Out[33]:
torch.Size([2, 2, 1, 2])
In [34]: t14.dim()             
Out[34]: 4

In [35]: t12 = torch.squeeze(t8, 2)
In [36]: t12.size()            
Out[36]:
torch.Size([2, 1, 2, 2])
In [37]: t12.dim()             
Out[37]: 4

In [38]: t13 = torch.squeeze(t8, 3)
In [39]: t13.size()            
Out[39]:
torch.Size([2, 1, 2, 2])
In [40]: t13.dim()             
Out[40]: 4

In [41]: t14 = torch.ones(2, 1, 1)
In [42]: t13                  
Out[42]:
tensor([[[1.]], [[1.]]])
In [43]: torch.squeeze(t13)   
Out[43]:
tensor([1., 1.])
```

____


**2. 增维 torch.unsqueeze(input, dim, out=None)**
<font color=#990CC><strong>增加大小为1的维度，也就是返回一个新的张量，对输入的指定位置插入维度1且必须指明维度。</strong></font>
```python
t14 = torch.unsqueeze(t14, 3) # 在第3个维度上扩展
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意： 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以使用范围[-input.dim()-1，input.dim()+1)内的dim值。负dim将对应于在dim=dim+input.dim()+1时应用的unqueze()。例如对于一个（3,2,4）的tensor，其dim可以选择为none，-1,0,1,2，含义如下：

- none：所有元素的max，得到一个max值
- -1：若dim为负，则将被转化为dim+input.dim()+1，即3-1+1
- 0：最粗粒度的方向，在第1维插入一个维度
- 1：在第2维插入一个维度
- 2：最细粒度的方向，在第3维插入一个维度
- -3：在倒数第3维插入一个维度，在本例子也就是第一维
- 一句话概括：dim越大，越深入，none即所有最小元素参与计算。
**参数:**
- tensor (Tensor) – 输入张量
- dim (int) – 插入维度的索引（从0开始）
- out (Tensor, optional) – 结果张量

**例子：**
```python
import torch

t14 = torch.Tensor([1, 2, 3, 4])  # torch.Tensor是默认的tensor类型（torch.Flt15otTensor）的简称。

print(t14)  # tensor([1., 2., 3., 4.])
print(t14.size())  # torch.Size([4])
print(t14.dim())  # 1
print(t14.numpy())  # [1. 2. 3. 4.]

print(torch.unsqueeze(t14, 0))  # tensor([[1., 2., 3., 4.]])
print(torch.unsqueeze(t14, 0).size())  # torch.Size([1, 4])
print(torch.unsqueeze(t14, 0).dim())  # 2
print(torch.unsqueeze(t14, 0).numpy())  # [[1. 2. 3. 4.]]

print(torch.unsqueeze(t14, 1))
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.]])
print(torch.unsqueeze(t14, 1).size())  # torch.Size([4, 1])
print(torch.unsqueeze(t14, 1).dim())  # 2

print(torch.unsqueeze(t14, -1))
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.]])
print(torch.unsqueeze(t14, -1).size())  # torch.Size([4, 1])
print(torch.unsqueeze(t14, -1).dim())  # 2

print(torch.unsqueeze(t14, -2))  # tensor([[1., 2., 3., 4.]])
print(torch.unsqueeze(t14, -2).size())  # torch.Size([1, 4])
print(torch.unsqueeze(t14, -2).dim())  # 2
```

**补充：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`unsqueeze_`和`unsqueeze`实现一样的功能，区别在于`unsqueeze_`是 in_place操作,即`unsqueeze`不会对使用`unsqueeze`的 tensor 进行改变,想要获取`unsqueeze`后的值必须赋予个新值, `unsqueeze_`则会对自己改变。

```python
t15 = torch.Tensor([1, 2, 3, 4])
print(t15)
# tensor([1., 2., 3., 4.])

t16 = torch.unsqueeze(t15, 1)
print(t16)
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.]])

print(t15)
# tensor([1., 2., 3., 4.])

t15 = torch.Tensor([1, 2, 3, 4])
print(t15)
# tensor([1., 2., 3., 4.])

print(t15.unsqueeze_(1))
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.]])

print(t15)
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.]])
```
<font color=#9900CC><strong>PyTorch中的 XXX_ 和 XXX 实现的功能都是相同的，唯一不同的是前者进行的是 in_plt15ce 操作。</strong></font>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参考：[torch.unsqueeze() 和 torch.squeeze()](https://zhuanlan.zhihu.com/p/86763381)

____

## 3 torch.gather()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;看了一些教程，觉得还是官网给的解释最容易理解。这个函数就是从从原tensor中获取指定`dim`和指定`index`的数据。

```python
out = torch.gather(input, dim, index, *, sparse_grad=False, out=None) → Tensor      # 函数原型
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;官方的解释：沿给定轴dim，将输入索引张量index指定位置的值进行聚合。对一个3维张量，输出可以定义为：

```python
out[i][j][k] = input[index[i][j][k]][j][k]  # if dim == 0
out[i][j][k] = input[i][index[i][j][k]][k]  # if dim == 1
out[i][j][k] = input[i][j][index[i][j][k]]  # if dim == 2
```

**例子：**
```python
In [44]: t17 = torch.tensor([[1, 2],
	                      [3, 4]])
In [45]: index = torch.tensor([[1],[0]])
In [46]: print(torch.gather(t17, dim=1, index=index))
Out[46]:
tensor([[2],
        [3]])
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于输入t17，我们希望在dim=1这个方向上（也就是行），按照index的下标取出某些值组成一个新的tensor，而index的第一行是1，也就是想取出t17的第一行里，下标为1的值，取出来就是2；同理，index的第二行是0，也就是想取出t17的第二行里，下标为0的值，取出来就是3。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=#9900CC><strong>也就是说，input和index这两个tensor，除了dim这个方向维度数可以不同，其余维度方向上的形状要一致。</strong></font>例如，如果输入为$N \times 10 \times 15$，dim=0，则索引必须为$N\times 10 \times 15$。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参考自官网文档：TORCH.GaTHER：[https://pytorch.org/docs/sttable/generated/torch.gather.html?highlight=gather#torch.gather](https://pytorch.org/docs/sttable/generated/torch.gather.html?highlight=gather#torch.gather)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;推荐一个讲的很详细的博客：Understanding indexing with pytorch gather：[https://medium.com/analytics-vidhya/understanding-indexing-with-pytorch-gather-33717a84ebc4](https://medium.com/analytics-vidhya/understanding-indexing-with-pytorch-gather-33717a84ebc4)

_____

## 4 torch.where()
```python
torch.where(condition, x, y) → Tensor
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据条件，返回从$x,y$中选择元素所组成的张量。如果满足条件，则返回t14中元素。若不满足，返回y中元素。
$$
\text { out }_i= \begin{cases}\mathrm{x}_i & \text { if condition } \\ \mathrm{y}_i & \text { otherwise }\end{cases}
$$

```python
In [47]: import torch
In [48]: t18 = torch.randn(3, 2)
In [49]: t19 = torch.ones(3, 2)
In [50]: t18
Out[50]: 
tensor([[ 0.3529, -1.0199],
        [ 1.2971,  0.0828],
        [ 0.9522, -1.3071]])
In [51]: torch.where(t18 > 0, t18, t19)
Out[51]: 
tensor([[0.3529, 1.0000],
        [1.2971, 0.0828],
        [0.9522, 1.0000]])
```

`torch.randperm(n)`：将0~n-1（包括0和n-1）随机打乱后获得的数字序列，函数名是`random permutation`缩写
```python
torch.randperm(10)      # tensor([3, 6, 2, 5, 1, 4, 0, 8, 7, 9])
```

_____

## 5 torch.norm()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于范数不了解的，可以看之前的文章，[向量范数与矩阵范数的认识](https://blog.csdn.net/xq151750111/article/details/120207697)，这里直接展示用法：

`torch.norm()`是对输入的Tensor求范数，函数原型如下：
<img src ="https://img-blog.csdnimg.cn/05c44417381249efad8ca9e1fff91aed.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;按文档的意思，就是这个求解范数的函数由于不严谨在以后可能会被弃用。不过现在还可以用，也先把用法在这里讲解一下吧。
- input(Tensor)：输入张量
- p (int, float, inf, -inf, 'fro', 'nuc', optional) 默认为F范数，一般情况下与2范数的求解结果相同。
- dim (int, tuple of python:ints, list of python:ints, optional)——指定要计算范数的输入维度。如果dim为None，则将跨输入的所有维度计算范数。如果由p表示的范数类型不支持指定的维数，则会发生错误。
- keepdim (bool, optional) ——输出张量是否保持dim。如果dim=None且out=None，则忽略。默认值：False
**1. 直接求张量范数**
```python
import torch
t20 = torch.arange(9, dtype=torch.float) - 4
t21 = t20.reshape((3, 3))

# 2范数
print(torch.norm(t20))     # tensor(7.7460)
print(torch.norm(t21))     # tensor(7.7460)

# 无穷范数
print(torch.norm(t20, float('inf')))       # tensor(4.)
print(torch.norm(t21, float('inf')))       # tensor(4.)

# 1范数
print(torch.norm(t20, p=1))       # tensor(20.)
print(torch.norm(t21, p=1))       # tensor(20.)

# 0范数
print(torch.norm(t20, p=0))       # tensor(8.)
print(torch.norm(t21, p=0))       # tensor(8.)
```

**2. 求指定维度上的范数**
```python
t22 = torch.tensor([[1, 2, 3], [-1, 1, 4]], dtype=torch.float)
print(torch.norm(t22, dim=0))          # tensor([1.4142, 2.2361, 5.0000])
print(torch.norm(t22, dim=1))          # tensor([3.7417, 4.2426])
print(torch.norm(t22, p=1, dim=1))     # tensor([6., 6.])

t23 = torch.arange(8, dtype=torch.float).reshape(2, 2, 2)
print(torch.norm(t23, dim=(1, 2)))             # tensor([ 3.7417, 11.2250])
print(torch.norm(t23[0, :, :]), torch.norm(t23[1, :, :]))     # tensor(3.7417) tensor(11.2250)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看输出，dim=0是对0维度上的一个向量求范数，返回结果数量等于其列的个数，也就是说有多少个0维度的向量，将得到多少个范数。dim=1同理。

**3. 保持维度不变**
```python
t24 = torch.rand((2, 3, 4))
norm1 = torch.norm(t24, dim=1, keepdim=True)
norm2 = torch.norm(t24, dim=1, keepdim=False)
print(t24.shape)                # torch.Size([2, 3, 4])
print(norm1.shape)              # torch.Size([2, 1, 4])
print(norm2.shape)              # torch.Size([2, 4])
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以发现，当`keepdim=False`时，输出比输入少一个维度（就是指定的dim求范数的维度）。而`keepdim=True`时，输出与输入维度相同，仅仅是输出在求范数的维度上元素个数变为1。这也是为什么有时我们把参数中的dim称为缩减的维度，因为norm运算之后，此维度或者消失或者元素个数变为1。

[TORCH.NORM](https://pytorch.org/docs/stable/generated/torch.norm.html?highlight=torch%20norm#torch.norm)

## 6 torch.cumsum()
函数原型：

```python
torch.cumsum(input, dim, *, dtype=None, out=None) → Tensor
```

返回维度dim中输入元素的累计和。【功能：累加】例如，如果输入是大小为N的向量，则结果也将是大小为N的带有元素的向量。【运算后维度不变】
一维数据：
```python
In [52]: t25 = torch.arange(0, 6)
In [53]: t25                          
Out[53]:
tensor([0, 1, 2, 3, 4, 5])
In [54]: t26 = torch.cumsum(t25, dim=0)
In [55]: t26                          
Out[55]:
tensor([ 0,  1,  3,  6, 10, 15])
In [56]: t27 = torch.cumsum(t25, dim=-1)
In [57]: t27                          
Out[57]: tensor([ 0,  1,  3,  6, 10, 15])
```
二维数据：

```python
In [58]: t28 = t25.view(2, 3)
In [59]: t28         
Out[60]:
tensor([[0, 1, 2], 
        [3, 4, 5]])

In [61]: t29 = torch.cumsum(t28, dim=0)      
In [62]: t31 = torch.cumsum(t28, dim=1)
In [63]: t32 = torch.cumsum(t28, dim=-1)
In [64]: t29          
Out[64]:
tensor([[0, 1, 2], 
        [3, 5, 7]])
In [65]: t31          
Out[65]:
tensor([[ 0,  1,  3], 
        [ 3,  7, 12]])
In [66]: t32          
Out[66]: 
tensor([[ 0,  1,  3], 
        [ 3,  7, 12]])
```

三维数据：

```python
In [67]: t33 = torch.arange(0, 16).view(2, 2, 4)
In [68]: t33
Out[68]:
tensor([[[ 0,  1,  2,  3],
         [ 4,  5,  6,  7]],

        [[ 8,  9, 10, 11],
         [12, 13, 14, 15]]])

In [69]: t34 = torch.cumsum(t33, dim=0)
In [70]: t34
Out[70]:
tensor([[[ 0,  1,  2,  3],
         [ 4,  5,  6,  7]],

        [[ 8, 10, 12, 14],
         [16, 18, 20, 22]]])

In [71]: t35 = torch.cumsum(t33, dim=1)
In [72]: t35
Out[72]:
tensor([[[ 0,  1,  2,  3],
         [ 4,  6,  8, 10]],

        [[ 8,  9, 10, 11],
         [20, 22, 24, 26]]])

In [73]: t36 = torch.cumsum(t33, dim=2)
In [74]: t36
Out[74]:
tensor([[[ 0,  1,  3,  6],
         [ 4,  9, 15, 22]],

        [[ 8, 17, 27, 38],
         [12, 25, 39, 54]]])

In [75]: t37 = torch.cumsum(t33, dim=-1)
In [76]: t37
Out[76]:
tensor([[[ 0,  1,  3,  6],
         [ 4,  9, 15, 22]],

        [[ 8, 17, 27, 38],
         [12, 25, 39, 54]]])
```
结果分析：

三维数据规模计算后有三个数据，我们可以理解为层、行、列。这里的规模是：2,2,4，表示2层，2行，4列的数据。

- (dim=0)表示层不变，也就是第一层不变，后面的层依次累加。这里一共就2层，第一层不变，那就只需要计算第二层就可以了。
- (dim=1)表示行不变，也就是第一行不变，后面的行依次累加，这里一共2层，每层有两行，所以，这每层中的首行都不变。
- (dim=2)表示列不变，后面的列依次累加。
- (dim=-1)其实就是反向查找维度，也就是等于最后一个维度。

参考自：[torch.cumsum维度详解](https://blog.csdn.net/songxiaolingbaobao/article/details/114580364
)
官方对函数的解释：[TORCH.CUMSUM](https://pytorch.org/docs/stable/generated/torch.cumsum.html?highlight=cumsum#torch.cumsum)

## 7 torch.sort()
函数原型：
```python
torch.sort(input, dim=None, descending=False, out=None) -> (Tensor, LongTensor)
```
返回值：
返回一个元组（sorted_tensor，sorted_indices），其中sorted_ indices是原始输入张量中元素的索引。

参数
- input (Tensor) – the input tensor
形式上与 numpy.narray 类似
- dim (int, optional) – the dimension to sort along
维度，对于二维数据：dim=0 按列排序，dim=1 按行排序，默认 dim=1
- descending (bool, optional) – controls the sorting order (ascending or descending)
降序，descending=True 从大到小排序，descending=False 从小到大排序，默认 descending=Flase

例子：
```python
In [77]: t38 = torch.randn(3,4)
In [78]: t38  
Out[78]:
tensor([[-0.9950, -0.6175, -0.1253,  1.3536],
        [ 0.1208, -0.4237, -1.1313,  0.9022],
        [-1.1995, -0.0699, -0.4396,  0.8043]])
In [79]: sorted, indices = torch.sort(x)  #按行从小到大排序
In [80]: sorted
Out[81]:
tensor([[-0.9950, -0.6175, -0.1253,  1.3536],
        [-1.1313, -0.4237,  0.1208,  0.9022],
        [-1.1995, -0.4396, -0.0699,  0.8043]])
In [82]: indices
Out[82]:
tensor([[0, 1, 2, 3],
        [2, 1, 0, 3],
        [0, 2, 1, 3]])
In [83]: sorted, indices = torch.sort(x, descending=True)  #按行从大到小排序 (即反序)
In [84]: sorted
Out[84]:
tensor([[ 1.3536, -0.1253, -0.6175, -0.9950],
        [ 0.9022,  0.1208, -0.4237, -1.1313],
        [ 0.8043, -0.0699, -0.4396, -1.1995]])
In [85]: indices
Out[85]:
tensor([[3, 2, 1, 0],
        [3, 0, 1, 2],
        [3, 1, 2, 0]])
In [86]: sorted, indices = torch.sort(x, dim=0)  #按列从小到大排序
In [87]: sorted
Out[87]:
tensor([[-1.1995, -0.6175, -1.1313,  0.8043],
        [-0.9950, -0.4237, -0.4396,  0.9022],
        [ 0.1208, -0.0699, -0.1253,  1.3536]])
In [88]: indices
Out[88]:
tensor([[2, 0, 1, 2],
        [0, 1, 2, 1],
        [1, 2, 0, 0]])
In [89]: sorted, indices = torch.sort(x, dim=0, descending=True)  #按列从大到小排序
In [90]: sorted
Out[90]:
tensor([[ 0.1208, -0.0699, -0.1253,  1.3536],
        [-0.9950, -0.4237, -0.4396,  0.9022],
        [-1.1995, -0.6175, -1.1313,  0.8043]])
In [91]: indices
Out[91]:
tensor([[1, 2, 0, 0],
        [0, 1, 2, 1],
        [2, 0, 1, 2]])
```