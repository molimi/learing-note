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

