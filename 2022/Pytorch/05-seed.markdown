&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;前面几篇整理了主要记录了PyTorch学习过程，详细目录如下：
- [PyTorch基础（一）-- Anaconda 和 PyTorch安装](https://blog.csdn.net/xq151750111/article/details/125085757?spm=1001.2014.3001.5501)
- [PyTorch基础（二）-- 张量与梯度](https://blog.csdn.net/xq151750111/article/details/123910443?spm=1001.2014.3001.5501)
- [PyTorch基础（三）-- 数据处理](https://blog.csdn.net/xq151750111/article/details/125249611?spm=1001.2014.3001.5501)
- [PyTorch基础（四）-- 模型构建](https://blog.csdn.net/xq151750111/article/details/125249622?spm=1001.2014.3001.5501)
- [PyTorch基础（五）-- 损失函数](https://blog.csdn.net/xq151750111/article/details/125286119?spm=1001.2014.3001.5501)
- [PyTorch基础（六）-- optim模块](https://blog.csdn.net/xq151750111/article/details/123602946?spm=1001.2014.3001.5501)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本节主要介绍初始化、训练与评估、可视化以及随机种子的使用，当然也会随着后面的学习，不断完善PyTorch的使用技巧。

## 1 权值初始化
### 1.1 初始化方法
- 全零初始化：网络中不同的神经元有相同的输出，进行同样的参数更新；因此，这些神经元学到的参数都一样，等价于一个神经元。
- 随机权值初始化，常采用权值采样自N(0,0.01) 的高斯分布
- `Xavier` 初始化适合双曲正切激活函数，不适合ReLU函数

<img src="https://img-blog.csdnimg.cn/0b694b744c004a4d827766c86de01604.png#pic_center" width=50%>

- HE初始化(MSRA)
<img src="https://img-blog.csdnimg.cn/5fcaf0a103c24a209226d80499d9622b.png#pic_center" width=50%>

>权值初始化小结
>- 好的初始化方法可以防止前向传播过程中的信息消失，也可以解决反向传递过程中的梯度消失。
>- 激活函数选择双曲正切或者`Sigmoid`时，建议使用`Xaizer` 初始化方法；
>- 激活函数选择`ReLU`或`Leakly ReLU`时，推荐使用He初始化方法。

### 1.2 torch.nn.init使用
PyTorch也在`torch.nn.init`中为我们提供了常用的初始化方法。通过访问torch.nn.init的官方文档[链接](https://pytorch.org/docs/stable/nn.init.html) ，我们发现`torch.nn.init`提供了以下初始化方法：
1 . `torch.nn.init.uniform_`(tensor, a=0.0, b=1.0)

2 . `torch.nn.init.normal_`(tensor, mean=0.0, std=1.0)

3 . `torch.nn.init.constant_`(tensor, val)

4 . `torch.nn.init.ones_`(tensor)

5 . `torch.nn.init.zeros_`(tensor)

6 . `torch.nn.init.eye_`(tensor)

7 . `torch.nn.init.dirac_`(tensor, groups=1)

8 . `torch.nn.init.xavier_uniform_`(tensor, gain=1.0)

9 . `torch.nn.init.xavier_normal_`(tensor, gain=1.0)

10 . `torch.nn.init.kaiming_uniform_`(tensor, a=0, mode='fan__in', nonlinearity='leaky_relu')

11 . `torch.nn.init.kaiming_normal_`(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')

12 . `torch.nn.init.orthogonal_`(tensor, gain=1)

13 . `torch.nn.init.sparse_`(tensor, sparsity, std=0.01)

14 .  `torch.nn.init.calculate_gain`(nonlinearity, param=None)
关于计算增益如下表：
|nonlinearity|gain|
| ---- | ---- |
|Linear/Identity|1|
|Conv{1,2,3}D|1|
|Sigmod|1|
|Tanh|5/3|
|ReLU|sqrt(2)|
|Leaky Relu|sqrt(2/1+neg_slop^2)|

我们可以发现这些函数除了`calculate_gain`，所有函数的后缀都带有下划线，意味着这些函数将会直接原地更改输入张量的值。

### 1.3 初始化函数的封装
定义为一个`initialize_weights()`的函数并在模型初始后进行使用。
```python
def initialize_weights(self):
    for m in self.modules():
        if isinstance(m, nn.Conv2d):
            torch.nn.init.xavier_normal_(m.weight.data)
            if m.bias is not None:
                torch.nn.init.constant_(m.bias.data, 0.3)
        elif isinstance(m, nn.Linear):
            torch.nn.init.normal_(m.weight.data, 0.1)
            if m.bias is not None:
                torch.nn.init.zeros_(m.bias.data)
        elif isinstance(m, nn.BatchNorm2d):
            m.weight.data.fill_(1)
            m.bias.data.zeros_()
```
这段代码流程是遍历当前模型的每一层，然后判断各层属于什么类型，然后根据不同类型层，设定不同的权值初始化方法。我们可以通过下面的例程进行一个简短的演示：
```python
# 模型的定义
class MLP(nn.Module):
  # 声明带有模型参数的层，这里声明了两个全连接层
  def __init__(self, **kwargs):
    # 调用MLP父类Block的构造函数来进行必要的初始化。这样在构造实例时还可以指定其他函数
    super(MLP, self).__init__(**kwargs)
    self.hidden = nn.Conv2d(1,1,3)
    self.act = nn.ReLU()
    self.output = nn.Linear(10,1)
    
   # 定义模型的前向计算，即如何根据输入x计算返回所需要的模型输出
  def forward(self, x):
    out = self.act(self.hidden(x))
    return self.output(out)

mlp = MLP()
print(list(mlp.parameters()))
print("-------初始化-------")

initialize_weights(mlp)
print(list(mlp.parameters()))
```

## 2 训练与评估
如果是训练状态，那么模型的参数应该支持反向传播的修改；如果是验证/测试状态，则不应该修改模型参数。在PyTorch中，模型的状态设置非常简便，如下的两个操作二选一即可：
```python
model.train()       # 训练状态
model.eval()        # 验证、测试状态
```
在DataLoader构建完成后介绍了如何从中读取数据，在训练过程中使用类似的操作即可，区别在于此时要用for循环读取DataLoader中的全部数据。

```python
for data, label in train_loader:
```

之后将数据放到GPU上用于后续计算，此处以.cuda()为例

```python
data, label = data.to(device), label.to(device) # 如果有GPU，可以使用data.cuda(),label.cuda()
```
开始用当前批次数据做训练时，应当先将优化器的梯度置零：

```python
optimizer.zero_grad()
```

之后将data送入模型中训练：

```python
output = model(data)
```

根据预先定义的criterion计算损失函数：

```python
loss = criterion(output, label)
```

将loss反向传播回网络：

```python
loss.backward()
```

使用优化器更新模型参数：

```python
optimizer.step()
```

这样一个训练过程就完成了，后续还可以计算模型准确率等指标，这部分会在下一节的图像分类实战中加以介绍。

验证/测试的流程基本与训练过程一致，不同点在于：

- 需要预先设置torch.no_grad，以及将model调至eval模式
- 不需要将优化器的梯度置零
- 不需要将loss反向回传到网络
- 不需要更新optimizer

一个完整的图像分类的训练过程如下所示：
```python
def train(epoch):
    model.train()
    train_loss = 0
    for data, label in train_loader:
        data, label = data.to(device), label.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, label)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
    print('Epoch: {} \tTraining Loss: {:.4f}'.format(epoch, train_loss/len(train_loader)))
```
对应的，一个完整图像分类的验证过程如下所示：
```python
def val(epoch):
    model.eval()
    val_loss = 0
    eval_acc = 0
    for data, label in test_loader:
        data, label = data.to(device), label.to(device)
        output = model(data)
        loss = criterion(output, label)
        _, pred = torch.max(output, dim=1)
        eval_loss += loss.item()
        num_correct = (pred==label).sum().item()
        acc = num_correct/data.shape[0]
        eval_acc += acc
    print('Epoch: {} \t Testing Loss: {:.4f} \t Testing Acc: {:.4f}'.format(epoch, eval_loss/len(test_loader), eval_acc/len(test_loader)))
```

## 3  使用技巧
### 3.1 随机种子
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在神经网络中，参数默认是进行随机初始化的。如果不设置的话每次训练时的初始化都是随机的，导致结果不确定。如果设置初始化，则每次初始化都是固定的。
```python
import torch
import numpy as np

np.random.seed(1)
torch.manual_seed(1)        # 为CPU设置种子用于生成随机数，以使得结果是确定的
torch.cuda.manual_seed(1)   # 为当前GPU设置随机种子
#如果使用多个GPU，应该使用torch.cuda.manual_seed_all()为所有的GPU设置种子。
torch.cuda.manual_seed_all(1)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为什么使用相同的网络结构，跑出来的效果完全不同，用的学习率，迭代次数，batch size 都是一样？固定随机数种子是非常重要的。但是如果你使用的是PyTorch等框架，还要看一下框架的种子是否固定了。还有，如果你用了cuda，别忘了cuda的随机数种子。这里还需要用到`torch.backends.cudnn.deterministic`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`torch.backends.cudnn.deterministic`是啥？顾名思义，将这个 flag 置为True的话，每次返回的卷积算法将是确定的，即默认算法。如果配合上设置 Torch 的随机种子为固定值的话，应该可以保证每次运行网络的时候相同输入的输出是固定的，代码大致这样
```python
def init_seeds(seed=0):
    torch.cuda.manual_seed_all(seed) 

    if seed == 0:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
```

### 3.2 显存设置
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pytorch 训练时有时候会因为加载的东西过多而爆显存，有些时候这种情况还可以使用cuda的清理技术进行修整。
```python
torch.cuda.empty_cache()
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PyTorch上限制GPU显存的函数
```python
# 限制0号设备的显存的使用量为0.5，就是半张卡那么多，比如12G卡，设置0.5就是6G。 
torch.cuda.set_per_process_memory_fracton(0.5, 0)
torch.cuda.empty_cache()
# 计算一下总内存有多少
total_memory = torch.cuda.get_device_paoperties(0).total_memory
# 使用0.499的显存:
tmp_tensor = torch.empty(int(total_memory * 0.499), dtype=torch.int8, device='cuda')

# 清空该显存
del tmp_tensor
torch.cuda.empty_cache()

# 下面这句话会触发显存OOM错误，因为刚好触碰到了上限:
torch.empty(total_empty//2, dtype=torch.int8, device='cuda')
"""
It raises an error as follows: 
RuntimeError: CUDA out of memory. Tried to allocate 5.59 GiB (GPU 0; 11.17 GiB total capacity; 0 bytes already allocated; 10.91 GiB free; 5.59 GiB allowed; 0 bytes reserved in total by PyTorch)
显存超标后，比不设置限制的错误信息多了一个提示，“5.59 GiB allowed;”
"""
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详细内容可以参考：[PyTorch上进行GPU显存限制/切分的函数](https://zhuanlan.zhihu.com/p/338044800)


**补充**
`torch.cuda`主要函数：
- 查看是否有可用GPU、可用GPU数量： `torch.cuda.is_available()`, `torch.cuda.device_count()`
- 查看当前使用的GPU序号：`torch.cuda.current_device()`
- 查看指定GPU的容量、名称：`torch.cuda.get_device_capability(device)`,  `torch.cuda.get_device_name(device)`
- 清空程序占用的GPU资源： `torch.cuda.empty_cache()`
- 为GPU设置随机种子：`torch.cuda.manual_seed(seed)`, `torch.cuda.manual_seed_all(seed)`

## 4 可视化

