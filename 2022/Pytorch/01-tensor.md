&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Pytorch`中的计算最终都可以归结为`Tensor`即张量的计算，所以有必要详细学习`PyTorch`中张量属性与运算梯度。

## 1 张量
`Tensor`是`PyTorch`的基础计算单位，一个张量可以是一个数字、向量、矩阵或任何多维数组。

几何代数中定义的张量是基于向量和矩阵的推广，比如我们可以将标量视为零阶张量，向量可以视为一阶张量，矩阵就是二阶张量。

- 0维张量/标量 标量是一个数字
- 1维张量/向量 1维张量称为“向量”。
- 2维张量 2维张量称为矩阵
- 3维张量 公用数据存储在张量 时间序列数据 股价 文本数据 彩色图片(RGB)
张量是现代机器学习的基础。它的核心是一个数据容器，多数情况下，它包含数字，有时候它也包含字符串，但这种情况比较少。因此可以把它想象成一个数字的水桶。

例子：一个图像可以用三个字段表示：
> (width, height, channel) = 3D

但是，在机器学习工作中，我们经常要处理不止一张图片或一篇文档——我们要处理一个集合。我们可能有10,000张郁金香的图片，这意味着，我们将用到4D张量：
> (sample_size, width, height, channel) = 4D

在PyTorch中， torch.Tensor是存储和变换数据的主要工具。其实Tensor和NumPy的多维数组非常类似。然而，Tensor 提供GPU计算和自动求梯度等更多功能，这些使 Tensor 这一数据类型更加适合深度学习。第一步，先导入torch，
```pytorch
import torch
```

### 1.1 创建张量
1. 通过`torch.Tensor()`的方法，构造一个未初始化的矩阵：
```python
tensor00 = torch.Tensor(5, 3)
tensor01 = torch.tensor([1,2,3])
tensor02 = torch.Tensor([1,2,3])
tensor03 = torch.FloatTensor([1,2,3])
print(tensor01, tensor02, tensor03)
print(tensor01.dtype, tensor02.dtype, tensor03.dtype)
print(tensor01.type(), tensor02.type(), tensor03.type())

print(type(torch.FloatTensor()),type(torch.Tensor()))
'''
tensor([1, 2, 3]) tensor([1., 2., 3.]) tensor([1., 2., 3.])
torch.int64 torch.float32 torch.float32
torch.LongTensor torch.FloatTensor torch.FloatTensor
<class 'torch.Tensor'> <class 'torch.Tensor'>
'''
```
> `torch.Tensor()`和`torch.tensor()`区别
- `torch.Tensor()`是Python类，更明确的说，是默认张量类型`torch.FloatTensor()`的别名，`torch.Tensor([1, 2, 3])` 会调用Tensor类的构造函数`__init__`，生成单精度浮点类型的张量。
- `torch.tensor()`仅仅是Python的函数。函数原型为：
```python
torch.tensor(data, dtype=None, device=None, requires_grad=True) # data可以是：list, tuple, array, scalar等类型
```
- `torch.tensor()`可以从data中的数据部分做拷贝（而不是直接引用），根据原始数据类型生成相应的`torch.LongTensor`，`torch.FloatTensor`，`torch.DoubleTensor`。



2. 通过`torch.zeros()`构造一个矩阵全为 0，并且通过dtype设置数据类型为 long。
```python
tensor04 = torch.zeros(5, 3, dtype=torch.long)
```
3. 通过torch.tensor()直接使用数据，构造一个张量：
```python
tensor05 = torch.tensor([5.5, 3])
```
4. 在已有的张量(tensor)中构建一个张量(tensor). 这些方法将重用输入张量(tensor)的属性，例如， dtype，除非用户提供新值
```python
tensor06 = torch.ones(5, 3, dtype=torch.double)
tensor06 = torch.rand_like(tensor04, dtype=torch.float) # 重置数据类型
```
张量可以有任何维数。每个维度有不同的长度。我们可以用张量的.shape 属性来查看每个维度的长度。
```python
tensor06.shape      # torch.Size([5, 3])
```
5. numpy数组转换为torch张量
tensor张量转换为numpy数组
```python
tensor07 = torch.ones(5)
print(tensor07)        # tensor([1., 1., 1., 1., 1.])

arr01 = tensor07.numpy()
print(arr01)       # [1. 1. 1. 1. 1.]
type(arr01)        # numpy.ndarray

tensor07.add_(1)
print(tensor07)        # tensor([2., 2., 2., 2., 2.])
print(arr01)           # [2. 2. 2. 2. 2.]
```
numpy数组转换为torch张量
```python
import numpy as np
arr02 = np.ones(5)
tensor08 = torch.from_numpy(arr02)
np.add(arr02, 1, out=arr02)
print(arr02)    # [2. 2. 2. 2. 2.]
print(tensor08) # tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
```
### 1.2 张量运算
1. 加法操作
```python
tensor09 = torch.rand(4, 3)
tensor10 = torch.ones(4, 3)
print(tensor09+tensor10)    # 方式一
print(torch.add(tensor09, tensor10))    # 方式二

result = torch.empty(4, 3)
torch.add(tensor09, tensor10, out=result)   # 方式三 提供一个输出 tensor 作为参数
# 这里的 out 不需要和真实的运算结果保持维数一致，但是会有警告提示！
print(result)
tensor10.add_(tensor09)  # 方式4 in-place
print(tensor10)
```
温馨提示：任何在原地(in-place)改变张量的操作都有一个`_`后缀。例如`x.copy_(y)`, `x.t_()`操作将改变x.

2. 索引操作
这里的索引操作和numpy类似，需要注意的是：索引出来的结果与原数据共享内存，修改一个，另一个会跟着修改。如果不想修改，可以考虑使用copy()等方法
```python
tensor11 = torch.rand(4, 3)
print(tensor11[:, 1])   # 获取第二列
```
调整大小：如果要调整张量/重塑张量，可以使用`torch.view`：
```python
tensor12 = torch.ones(4, 4)
tensor13 = tensor12.view(16)
tensor14 = tensor12.view(-1, 8) # -1是指这一维的维数由其他维度决定
print(tensor12.size(), tensor13.size(), tensor14.size())    # torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])
```


注意 view() 返回的新tensor与源tensor共享内存(其实是同一个tensor)，也即更改其中的一个，另 外一个也会跟着改变。(顾名思义，view仅仅是改变了对这个张量的观察⻆度)


> 如果我们想返回一个真正新的副本(即不共享内存)该怎么办呢？Pytorch还提供了一 个 reshape() 可以改变形状，但是此函数并不能保证返回的是其拷贝，所以不推荐使用。推荐先用 clone 创造一个副本然后再使用 view 。
> 注意：使用 clone 还有一个好处是会被记录在计算图中，即梯度回传到副本时也会传到源 Tensor 。

3. 广播机制
当对两个形状不同的 Tensor 按元素运算时，可能会触发广播(broadcasting)机制：先适当复制元素使这两个 Tensor 形状相同后再按元素运算。
```python
tensor15 = torch.arange(1, 3).view(1, 2)
tensor16 = torch.arange(1, 4).view(3, 1)
print(tensor15+tensor16)
```


## 2 梯度运算
### 2.1 基本运算
张量的几大属性
| 属性 | 说明 |
|--|--|
| data | 存放该张量的值 |
| grad | 存放该张量的梯度值 |
| requires_grad | 是否需要为该张量计算梯度 |
| grad_fn | 记录该张量的运算信息 |
下面定义一个基本的张量运算z = x + y，下面看x/y/z三个张量的相关属性值。
```bash
>>> x = torch.randn(1, 1)
>>> y = torch.rand(1, 1, requires_grad=True)
>>> z = x + y
>>> print(x.data, x.grad, x.requires_grad, x.grad_fn)
tensor([[0.1760]]) None False None
>>> print(y.data, y.grad, y.requires_grad, y.grad_fn)
tensor([[0.2602]]) None True None
>>> print(z.data, z.grad, z.requires_grad, z.grad_fn)
tensor([[0.4362]]) None True <AddBackward0 object at 0x7ff07a0f2910>
>>> z.backward()
>>> print(x.grad, y.grad)
None tensor([[1.]])
```
通过上面的运行结果，可以发现在调用`backward()`进行反向传播后，requires_grad为True的张量y的grad里面就有相应的梯度值了，而张量x的grad依然为None。

除此以外，直接创建的张量x/y的grad_fn均为None。另一方面，z是torch.add函数的输出（由x和y计算而来的），所以z的反向传播函数为AddBackward。

通过这个例子中，我们初步对这几大属性和梯度运算有一个直观的认识：

- 在用Pytorch创建张量时，属性requires_grad默认值为False；
- 仅当张量的requires_grad=True时，才会为该张量计算梯度；
- 由用户直接创建的张量的grad_fn为None，而由某些运算操作产生的张量的grad_fn则有相应的用于计算梯度的反向传播函数。

如果我们继续对z反向传播一次，
```python
>>> z.backward()
>>> print(x.grad, y.grad)
None tensor([[2.]])
```
可以发现x的梯度依旧为None，而y的梯度却累加了。为了避免梯累加造成问题，<font color=#9900CC><strong>一般训练模型时我们在每次进行反向传播之前都要将梯度清零。</strong></font>
____

## 参考
- PyTorch张量：[https://github.com/datawhalechina/thorough-pytorch/blob/main/source/第二章](https://github.com/datawhalechina/thorough-pytorch/blob/main/source/%E7%AC%AC%E4%BA%8C%E7%AB%A0/2.1%20%E5%BC%A0%E9%87%8F.md)
- PyTorch进阶之路（一）：张量与梯度：[https://zhuanlan.zhihu.com/p/59081057](https://zhuanlan.zhihu.com/p/59081057)
- Pytorch张量属性与梯度计算那些事儿：[https://mp.weixin.qq.com/s/JPEccTeg5ejcEbk46mqbkg](https://mp.weixin.qq.com/s/JPEccTeg5ejcEbk46mqbkg)