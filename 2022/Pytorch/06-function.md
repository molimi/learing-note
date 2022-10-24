## 1 张量的拆分和拼接
在Torch中，张量的维数通常很重要，为了便于学习，这里整理下来。



## 2 torch.unsqueeze()/torch.squeeze()




## 3 torch.gather()
看了一些教程，觉得还是官网给的解释最容易理解。这个函数就是从从原tensor中获取指定`dim`和指定`index`的数据。
```python
out = torch.gather(input, dim, index, *, sparse_grad=False, out=None) → Tensor      # 函数原型
```
官方的解释：沿给定轴dim，将输入索引张量index指定位置的值进行聚合。对一个3维张量，输出可以定义为：

```python
out[i][j][k] = input[index[i][j][k]][j][k]  # if dim == 0
out[i][j][k] = input[i][index[i][j][k]][k]  # if dim == 1
out[i][j][k] = input[i][j][index[i][j][k]]  # if dim == 2
```
举个例子：
```python
In [1]: tensor01 = torch.tensor([[1, 2],
	                      [3, 4]])
In [1]: index = torch.tensor([[1],[0]])
In [1]: print(torch.gather(tensor01, dim=1, index=index))
Out[1]:
tensor([[2],
        [3]])
```

对于输入tensor01,我们希望在dim=1这个方向上（也就是行），按照index的下标取出某些值组成一个新的tensor，而index的第一行是1，也就是想取出tensor01的第一行里，下标为1的值，取出来就是2；同理，index的第二行是0，也就是想取出a的第二行里，下标为0的值，取出来就是3。

<font color=#9900CC><strong>也就是说，input和index这两个tensor，除了dim这个方向维度数可以不同，其余维度方向上的形状要一致。</strong></font>例如，如果输入为$4x10x15$，dim=0，则索引必须为$Nx10x15$。


参考自官网文档：TORCH.GATHER：[https://pytorch.org/docs/stable/generated/torch.gather.html?highlight=gather#torch.gather](https://pytorch.org/docs/stable/generated/torch.gather.html?highlight=gather#torch.gather)

推荐一个讲的很详细的博客：Understanding indexing with pytorch gather：[https://medium.com/@mbednarski/understanding-indexing-with-pytorch-gather-33717a84ebc4](https://medium.com/@mbednarski/understanding-indexing-with-pytorch-gather-33717a84ebc4)


## 4 torch.where()
```python
torch.where(condition, x, y) → Tensor
```
根据条件，返回从x,y中选择元素所组成的张量。如果满足条件，则返回x中元素。若不满足，返回y中元素。
$$
\text { out }_i= \begin{cases}\mathrm{x}_i & \text { if condition } \\ \mathrm{y}_i & \text { otherwise }\end{cases}
$$

```python
In [1]: import torch
In [2]: x = torch.randn(3, 2)
In [3]: y = torch.ones(3, 2)
In [4]: x
Out[4]: 
tensor([[ 0.3529, -1.0199],
        [ 1.2971,  0.0828],
        [ 0.9522, -1.3071]])
In [5]: torch.where(x > 0, x, y)
Out[5]: 
tensor([[0.3529, 1.0000],
        [1.2971, 0.0828],
        [0.9522, 1.0000]])
```

`torch.randperm(n)`：将0~n-1（包括0和n-1）随机打乱后获得的数字序列，函数名是`random permutation`缩写
```python
torch.randperm(10)      # tensor([3, 6, 2, 5, 1, 4, 0, 8, 7, 9])
```


## 5 torch.norm()
对于范数不了解的，可以看之前的文章，[向量范数与矩阵范数的认识](https://blog.csdn.net/xq151750111/article/details/120207697)，这里直接展示用法：

`torch.norm()`是对输入的Tensor求范数，函数原型如下：
<img src ="https://img-blog.csdnimg.cn/05c44417381249efad8ca9e1fff91aed.png#pic_center" width = 48%>

按文档的意思，就是这个求解范数的函数由于不严谨在以后可能会被弃用。不过现在还可以用，也先把用法在这里讲解一下吧。
- input(Tensor)：输入张量
- p (int, float, inf, -inf, 'fro', 'nuc', optional) 默认为F范数，一般情况下与2范数的求解结果相同。
- dim (int, tuple of python:ints, list of python:ints, optional)——指定要计算范数的输入维度。如果dim为None，则将跨输入的所有维度计算范数。如果由p表示的范数类型不支持指定的维数，则会发生错误。
- keepdim (bool, optional) ——输出张量是否保持dim。如果dim=None且out=None，则忽略。默认值：False
**1. 直接求张量范数**
```python
import torch
tensor01 = torch.arange(9, dtype=torch.float) - 4
tensor02 = tensor01.reshape((3, 3))

# 2范数
print(torch.norm(tensor01))     # tensor(7.7460)
print(torch.norm(tensor02))     # tensor(7.7460)

# 无穷范数
print(torch.norm(tensor01, float('inf')))       # tensor(4.)
print(torch.norm(tensor02, float('inf')))       # tensor(4.)

# 1范数
print(torch.norm(tensor01, p=1))       # tensor(20.)
print(torch.norm(tensor02, p=1))       # tensor(20.)

# 0范数
print(torch.norm(tensor01, p=0))       # tensor(8.)
print(torch.norm(tensor02, p=0))       # tensor(8.)
```

**2. 求指定维度上的范数**
```python
tensor03 = torch.tensor([[1, 2, 3], [-1, 1, 4]], dtype=torch.float)
print(torch.norm(tensor03, dim=0))          # tensor([1.4142, 2.2361, 5.0000])
print(torch.norm(tensor03, dim=1))          # tensor([3.7417, 4.2426])
print(torch.norm(tensor03, p=1, dim=1))     # tensor([6., 6.])

tensor04 = torch.arange(8, dtype=torch.float).reshape(2, 2, 2)
print(torch.norm(tensor04, dim=(1, 2)))             # tensor([ 3.7417, 11.2250])
print(torch.norm(tensor04[0, :, :]), torch.norm(tensor04[1, :, :]))     # tensor(3.7417) tensor(11.2250)
```
可以看输出，dim=0是对0维度上的一个向量求范数，返回结果数量等于其列的个数，也就是说有多少个0维度的向量，将得到多少个范数。dim=1同理。

**3. 保持维度不变**
```python
tensor05 = torch.rand((2, 3, 4))
norm1 = torch.norm(tensor05, dim=1, keepdim=True)
norm2 = torch.norm(tensor05, dim=1, keepdim=False)
print(tensor05.shape)           # torch.Size([2, 3, 4])
print(norm1.shape)              # torch.Size([2, 1, 4])
print(norm2.shape)              # torch.Size([2, 4])
```

可以发现，当`keepdim=False`时，输出比输入少一个维度（就是指定的dim求范数的维度）。而`keepdim=True`时，输出与输入维度相同，仅仅是输出在求范数的维度上元素个数变为1。这也是为什么有时我们把参数中的dim称为缩减的维度，因为norm运算之后，此维度或者消失或者元素个数变为1。

[TORCH.NORM](https://pytorch.org/docs/stable/generated/torch.norm.html?highlight=torch%20norm#torch.norm)


## 6 Tensor、Numpy、list

**1. torch.Tensor 转 numpy**

```python
ndarray = tensor.numpy()
```
若是是在 gpu，命令如下：

```python
ndarray = tensor.cpu().numpy()
```
这是由于 gpu上的 tensor 不能直接转为 numpy

有时候会遇到`detach()`，返回一个新的Variable，从当前计算图中分离下来的，但是仍指向原变量的存放位置,不同之处只是requires_grad为false，得到的这个Variable永远不需要计算其梯度，不具有grad。
```python
ndarray = tensor.detach().cpu().numpy()  # 返回值为numpy.array()
 ```
当我们再训练网络的时候可能希望保持一部分的网络参数不变，只对其中一部分的参数进行调整；或者值训练部分分支网络，并不让其梯度对主网络的梯度造成影响，这时候我们就需要使用detach()函数来切断一些分支的反向传播。

**2. numpy 转 torch.Tensor**

```pyhton
tensor = torch.from_numpy(ndarray)
```

**3. torch.Tensor 转 list**

```python
list = tensor.numpy().tolist()
```

**4. list 转 numpy**

```python
ndarray = np.array(list)
```

**5. numpy 转 list**

```python
list = ndarray.tolist()
```
