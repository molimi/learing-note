在模型实现上，由于深度神经网络层数往往较多，同时会有一些用于实现特定功能的层（如卷积层、池化层、批正则化层、LSTM层等），因此深度神经网络往往需要“逐层”搭建，或者预先定义好可以实现特定功能的模块，再把这些模块组装起来。这种“定制化”的模型构建方式能够充分保证模型的灵活性，也对代码实现提出了新的要求。

## 1 网络构造
PyTorch中神经网络构造一般是基于 Module 类的模型来完成的，它让模型构造更加灵活。

Module 类是 nn 模块里提供的一个模型构造类，是所有神经⽹网络模块的基类，我们可以继承它来定义我们想要的模型。在nn工具箱中，可以直接引用的网络很多，有全连接层、卷积层、循环层、正则化层、激活层等等。

定义好每层后，最后还需要通过前向传播的方式把这些串起来。这就是涉及如何定义forward函数的问题。forward函数的任务需要把输入层、网络层、输出层链接起来，实现信息的前向传导。该函数的参数一般为输入数据，返回值为输出数据。

在forward函数中，有些层来自nn.Module,也可以使用nn.functional定义。来自nn.Module的需要实例化，而使用nn.functional定义的可以直接使用。

下面继承 Module 类构造多层感知机。这里定义的 MLP 类重载了 Module 类的 init 函数和 forward 函数。它们分别用于创建模型参数和定义前向计算。前向计算也即正向传播。
```python
import torch
from torch import nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, **kwargs) -> None:
        super(MLP, self).__init__()
        self.hidden = nn.Linear(784, 256)
        self.output = nn.Linear(256, 10)

    def forward(self, x):
        out = F.relu(self.hidden(x))
        out = self.output(out)
        return out
```
以上的 MLP 类中⽆须定义反向传播函数。系统将通过⾃动求梯度⽽自动⽣成反向传播所需的 backward 函数。

我们可以实例化 MLP 类得到模型变量 net 。下⾯的代码初始化 net 并传入输⼊数据 X 做一次前向计算。其中， net(X) 会调用 MLP 继承⾃自 Module 类的 __call__ 函数，这个函数将调⽤用 MLP 类定义的forward 函数来完成前向计算。

```python
X = torch.rand(2, 784)
net = MLP()
print(net)
print(net(X))
```
输出结果如下图所示：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/a0464009cce840c79702283bdb34f39a.png#pic_center" width=50%> </center>

注意，这里并没有将 Module 类命名为 Layer (层)或者 Model (模型)之类的名字，这是因为该类是一个可供⾃由组建的部件。它的子类既可以是⼀个层(如PyTorch提供的 Linear 类)，⼜可以是一个模型(如这里定义的 MLP 类)，或者是模型的⼀个部分。

______

## 2 常见的层
深度学习的一个魅力在于神经网络中各式各样的层，例如全连接层、卷积层、池化层与循环层等等。虽然PyTorch提供了⼤量常用的层，但有时候我们依然希望⾃定义层。这里我们会介绍如何使用 Module 来自定义层，从而可以被反复调用。

### 2.1 不含模型参数的层
先介绍如何定义一个不含模型参数的自定义层。下⾯构造的 MyLayer 类通过继承 Module 类自定义了一个**将输入减掉均值后输出**的层，并将层的计算定义在了 forward 函数里。这个层里不含模型参数。
```python
class MyLayer(nn.Module):
    def __init__(self, **kwargs) -> None:
        super(MyLayer, self).__init__(**kwargs)
    def forward(self, x):
        return x - x.mean()
```
测试，实例化该层，然后做前向传播
```python
layer = MyLayer()
print(layer(torch.tensor([1, 2, 3, 4, 5], dtype=torch.float)))      # tensor([-2., -1.,  0.,  1.,  2.])
```

### 2.2 含模型参数的层
我们还可以自定义含模型参数的自定义层。其中的模型参数可以通过训练学出。

Parameter 类其实是 Tensor 的子类，如果一 个 Tensor 是 Parameter ，那么它会⾃动被添加到模型的参数列表里。所以在⾃定义含模型参数的层时，我们应该将参数定义成 Parameter ，除了直接定义成 Parameter 类外，还可以使⽤ ParameterList 和 ParameterDict 分别定义参数的列表和字典。

```python
class MyListDense(nn.Module):
    def __init__(self) -> None:
        super(MyListDense, self).__init__()
        self.params = nn.ParameterList([nn.Parameter(torch.randn(4, 4)) for i in range(3)])
        self.params.append(nn.Parameter(torch.randn(4, 1)))

    def forward(self, x):
        for i in range(len(self.params)):
            x = torch.mm(x, self.params[i])
        return x

net = MyListDense()
print(net)
```
```python
class MyDictDense(nn.Module):
    def __init__(self):
        super(MyDictDense, self).__init__()
        self.params = nn.ParameterDict({
                'linear1': nn.Parameter(torch.randn(4, 4)),
                'linear2': nn.Parameter(torch.randn(4, 1))
        })
        self.params.update({'linear3': nn.Parameter(torch.randn(4, 2))}) # 新增

    def forward(self, x, choice='linear1'):
        return torch.mm(x, self.params[choice])

net = MyDictDense()
print(net)
```

### 2.3 二维卷积层

二维卷积层将输入和卷积核做互相关运算，并加上一个标量偏差来得到输出。卷积层的模型参数包括了卷积核和标量偏差。在训练模型的时候，通常我们先对卷积核随机初始化，然后不断迭代卷积核和偏差。
```python 
# 卷积运算（二维互相关）
def corr2d(X, K):
    h, w = K.shape
    X, K = X.float(), K.float()
    Y = torch.zeros((X.shape[0]-h+1, X.shape[1]-w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i: i+h, j: j+w] * K).sum()
    return Y

# 二维卷积层
class Conv2D(nn.Module):
    def __init__(self, kernel_size):
        super(Conv2D, self).__init__()
        self.weight = nn.Parameter(torch.randn(kernel_size))
        self.bias = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return corr2d(x, self.weight) + self.bias
```
卷积窗口形状为 $p \times q$ 的卷积层称为 $p \times q$  卷积层。同样，  $p \times q$ 卷积或 $p \times q$ 卷积核说明卷积核的高和宽分别为 $p$ 和 $q$。

填充(padding)是指在输⼊高和宽的两侧填充元素(通常是0元素)。

下面的例子里我们创建一个⾼和宽为3的二维卷积层，然后设输⼊高和宽两侧的填充数分别为1。给定一 个高和宽为8的输入，我们发现输出的高和宽也是8。
```python
# 定义一个函数来计算卷积层。它对输入和输出做相应的升维和降维=
def comp_conv2d(conv2d, X):
    # (1, 1)代表批量大小和通道数
    X = X.view((1, 1) + X.shape)
    Y = conv2d(X)
    return Y.view(Y.shape[2:])  # 排除不关心的前两维:批量和通道

conv2d = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)

X = torch.rand(8, 8)
comp_conv2d(conv2d, X).shape        # torch.Size([8, 8])
```
当卷积核的高和宽不同时，我们也可以通过设置高和宽上不同的填充数使输出和输入具有相同的高和宽。
```python
# 使用高为5、宽为3的卷积核。在⾼和宽两侧的填充数分别为2和1
conv2d = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(5, 3), padding=(2, 1))
comp_conv2d(conv2d, X).shape        # torch.Size([8, 8])
```

在二维互相关运算中，卷积窗口从输入数组的最左上方开始，按从左往右、从上往下 的顺序，依次在输⼊数组上滑动。我们将每次滑动的行数和列数称为步幅(stride)。

```python
conv2d = nn.Conv2d(1, 1, kernel_size=(3, 5), padding=(0, 1), stride=(3, 4))
comp_conv2d(conv2d, X).shape
```
```python
torch.Size([2, 2])
```

填充可以增加输出的高和宽。这常用来使输出与输入具有相同的高和宽。

步幅可以减小输出的高和宽，例如输出的高和宽仅为输入的高和宽的 ( 为大于1的整数)。


### 2.4 池化层
池化层每次对输入数据的一个固定形状窗口(⼜称池化窗口)中的元素计算输出。不同于卷积层里计算输⼊和核的互相关性，池化层直接计算池化窗口内元素的最大值或者平均值。该运算也 分别叫做最大池化或平均池化。在二维最⼤池化中，池化窗口从输入数组的最左上方开始，按从左往右、从上往下的顺序，依次在输⼊数组上滑动。当池化窗口滑动到某⼀位置时，窗口中的输入子数组的最大值即输出数组中相应位置的元素。

下面把池化层的前向计算实现在`pool2d`函数里。
```python
def pool2d(X, pool_size, mode='max'):
    p_h, p_w = pool_size
    Y = torch.zeros((X.shape[0]-p_h+1, X.shape[1]-p_w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode == 'max':
                Y[i, j] = X[i: i+p_h, j: j+p_w].max()
            elif mode == 'avg':
                Y[i, j] = X[i: i+p_h, j: j+p_w].mean()

    return Y

X = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=torch.float)
print(pool2d(X, (2, 2)))    # tensor([[4., 5.], [7., 8.]])
```
补充：
也可以采用`torch.nn.Sequential()`来构建网络层，这个有点类似Keras的models.Sequential(),使用起来就像搭积木一样，非常方便。不过，这种方法每层的编码是默认的数字，不易区分。
如果要对每层定义一个名称，我们可以采用Sequential的一种改进方法，在Sequential的基础上，通过`add_module()`添加每一层，并且为每一层增加一个单独的名字。
此外，还可以在Sequential基础上，通过字典的形式添加每一层，并且设置单独的层名称。
以下是采用字典方式构建网络的一个示例代码：
```python
class Net(nn.Module):
    def __init__(self) -> None:
        super(Net, self).__init__()
        self.conv = nn.Sequential(
            OrderedDict(
                [('conv1', nn.Conv2d(3, 32, 3, 1, 1)),
                ('norm1', nn.BatchNorm2d(32)),
                ('relu1', nn.ReLU()),
                ('pool1', torch.nn.MaxPool2d(2))]))
        self.dense = nn.Sequential(
            OrderedDict(
                [('dense1', nn.Linear(32*3*3, 128)),
                ('relu2', nn.ReLU()),
                ('dense2', nn.Linear(128, 10))]))
```
____

## 3 模型示例
### 3.1 LeNet
1998年的诞生的LeNet(LeCun et al. [Gradient-Based Learning Applied to Document Recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf))可谓是现在各种卷积神经网络的始祖了，其网络结构虽然只有5层，却包含了卷积神经网络的基本组件（卷积层，池化层，全连接层）

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/0478664b7d1d489495ec23b394228d8f.png#pic_center" width=50%> </center>

LeNet是一个简单的前馈神经网络(feed-forward network）（LeNet）。它接受一个输入，然后将它送入下一层，一层接一层的传递，最后给出输出。
```python
import torch
from torch import nn 
import torch.nn.functional as F

class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool1 = nn.AvgPool2d(2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool2 = nn.AvgPool2d(2)
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
    
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)

        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)

        return x

net = LeNet5()

print(net)
params = list(net.parameters())    # 返回模型可学习参数
print(len(params))
print(params[0].size()) # conv1的权重
# 随机的 32x32 的输入，如果使用Mnist数据集，需要填充 padding=2
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)
```
输出结果为：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/eab2bdd64533454aac2fb7df39f5a985.png#pic_center" width=50%> </center>


注意：`torch.nn`只支持小批量处理 (mini-batches）。整个 `torch.nn` 包只支持小批量样本的输入，不支持单个样本的输入。比如，`nn.Conv2d` 接受一个4维的张量，即`nSamples x nChannels x Height x Width `如果是一个单独的样本，只需要使用`input.unsqueeze(0)` 来添加一个“假的”批大小维度。

- `torch.Tensor` - 一个多维数组，支持诸如`backward()`等的自动求导操作，同时也保存了张量的梯度。

- `nn.Module `- 神经网络模块。是一种方便封装参数的方式，具有将参数移动到GPU、导出、加载等功能。

- `nn.Parameter `- 张量的一种，当它作为一个属性分配给一个`Module`时，它会被自动注册为一个参数。

- `autograd.Function` - 实现了自动求导前向和反向传播的定义，每个`Tensor`至少创建一个`Function`节点，该节点连接到创建`Tensor`的函数并对其历史进行编码。


### 3.2 Alexnet
Alex等人在2012年提出的AlexNet网络结构模型在ILSVRC-2012上以巨大的优势获得第一名，引爆了神经网络的应用热潮，使得卷积神经网络CNN成为在图像分类上的核心算法模型。下图是该模型的网络结构。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/8d62f5fbcc3a4f1587f4151e59fa4bd8.png#pic_center" width=50%> </center>


```python
class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 96, 11, 4), # in_channels, out_channels, kernel_size, stride, padding
            nn.ReLU(),
            nn.MaxPool2d(3, 2), # kernel_size, stride
            # 减小卷积窗口，使用填充为2来使得输入与输出的高和宽一致，且增大输出通道数
            nn.Conv2d(96, 256, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(3, 2),
            # 连续3个卷积层，且使用更小的卷积窗口。除了最后的卷积层外，进一步增大了输出通道数。
            # 前两个卷积层后不使用池化层来减小输入的高和宽
            nn.Conv2d(256, 384, 3, 1, 1),
            nn.ReLU(),
            nn.Conv2d(384, 384, 3, 1, 1),
            nn.ReLU(),
            nn.Conv2d(384, 256, 3, 1, 1),
            nn.ReLU(),
            nn.MaxPool2d(3, 2)
        )
         # 这里全连接层的输出个数比LeNet中的大数倍。使用丢弃层来缓解过拟合
        self.fc = nn.Sequential(
            nn.Linear(256*5*5, 4096),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Dropout(0.5),
            # 输出层。由于这里使用Fashion-MNIST，所以用类别数为10，而非论文中的1000
            nn.Linear(4096, 10),
        )

    def forward(self, img):
        feature = self.conv(img)
        output = self.fc(feature.view(img.shape[0], -1))
        return output
```

```python
net = AlexNet()
print(net)
```
```python
AlexNet(
  (conv): Sequential(
    (0): Conv2d(1, 96, kernel_size=(11, 11), stride=(4, 4))
    (1): ReLU()
    (2): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(96, 256, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
    (4): ReLU()
    (5): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(256, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU()
    (8): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU()
    (10): Conv2d(384, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (11): ReLU()
    (12): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (fc): Sequential(
    (0): Linear(in_features=6400, out_features=4096, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.5)
    (3): Linear(in_features=4096, out_features=4096, bias=True)
    (4): ReLU()
    (5): Dropout(p=0.5)
    (6): Linear(in_features=4096, out_features=10, bias=True)
  )
)
```


## 参考
- Pytorch神经网络工具箱：[http://www.feiguyunai.com/index.php/2019/09/11/pytorch-char03/](http://www.feiguyunai.com/index.php/2019/09/11/pytorch-char03/)