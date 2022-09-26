由于深度学习所需的样本量很大，一次加载全部数据运行可能会超出内存容量而无法实现；同时还有批（batch）训练等提高模型表现的策略，需要每次训练读取固定数量的样本送入模型中训练，因此深度学习在数据加载上需要有专门的设计。

PyTorch数据读入是通过Dataset+DataLoader的方式完成的，Dataset定义好数据的格式和数据变换形式，DataLoader用iterative的方式不断读入批次数据。

本节内容主要学习自《Python深度学习基于PyTorch》第四章——[Pytorch数据处理工具箱](http://www.feiguyunai.com/index.php/2019/07/31/pytorch-04/)

___

## 1 基础知识
Pytorch涉及数据处理（数据装载、数据预处理、数据增强等）主要工具包及相互关系如图1所示。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/8c9573accb2a488392ed854250df93b6.png#pic_center"> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1 PyTorch主要数据处理工具</div> </center>

图1 的左边是torch.utils.data工具包，它包括以下三个类：
（1）Dataset：是一个抽象类，其它数据集需要继承这个类，并且覆写其中的两个方法(__getitem__、__len__)。
（2）DataLoader：定义一个新的迭代器，实现批量（batch）读取，打乱数据（shuffle）并提供并行加速等功能。
（3）random_split：把数据集随机拆分为给定长度的非重叠新数据集。
（4）*sampler：多种采样函数。
图1中间是Pytorch可视化处理工具（torchvision），Pytorch的一个视觉处理工具包，它包括4个类，各类的主要功能如下：
（1）datasets:提供常用的数据集加载，设计上都是继承torch.utils.data.Dataset，主要包括MMIST、CIFAR10/100、ImageNet、COCO等。
（2）models:提供深度学习中各种经典的网络结构以及训练好的模型(如果选择pretrained=True)，包括AlexNet, VGG系列、ResNet系列、Inception系列等。
（3）transforms:常用的数据预处理操作，主要包括对Tensor及PIL Image对象的操作。
（4）utils:含两个函数，一个是make_grid，它能将多张图片拼接在一个网格中；另一个是save_img，它能将Tensor保存成图片。

_____

## 2 utils.data简介
我们可以定义自己的Dataset类来实现灵活的数据读取，定义的类需要继承PyTorch自身的Dataset类。主要包含三个函数：
- `__init__`: 用于向类中传入外部参数，同时定义样本集
- `__getitem__`: 用于逐个读取样本集合中的元素，可以进行一定的变换，并将返回训练/验证所需的数据
- `__len__`: 用于返回数据集的样本数

`__getitem__`一次只能获取一个数据，所以通过torch.utils.data.DataLoader来定义一个新的迭代器，实现batch读取。首先我们来定义一个简单的数据集，然后具体使用Dataset及DataLoader，以便有个直观认识。
(1) 导入需要的模块
```Python
import torch
from torch.utils.data import Dataset
import numpy as np
```
（2）定义获取数据集的类
该类继承基类Dataset，自定义一个数据集及对应标签。
```python
class TestDataset(Dataset): # 继承Dataset
    def __init__(self):
        self.data = np.asarray([[1, 2], [3, 4], [2, 1], [3, 4], [4, 5]])    # 一些由2维向量表示的数据集
        self.label = np.asarray([0, 1, 0, 1, 2])     # 这是数据集对应的标签

    def __getitem__(self, index):
        inputs = torch.from_numpy(self.data[index])   # 把numpy转换为Tensor
        targets = torch.tensor(self.label[index])
        return inputs, targets
    
    def __len__(self):
        return len(self.data)
```

（3）获取数据集中数据
```python
Test = TestDataset()
print(Test[2])
print(Test.__len__())
# 输出：
# (tensor([2, 1]), tensor(0))
# 5
```
以上数据以tuple返回，每次只返回一个样本。实际上，Dateset只负责数据的抽取，一次调用__getitem__只返回一个样本。如果希望批量处理(batch)，同时还要进行shuffle和并行加速等操作，可选择DataLoader。DataLoader的格式为：
```python
DataLoader(
    dataset,             # dataset: 加载的数据集；
    batch_size=1,        # batch_size: 批大小；
    shuffle=False,       # shuffle：是否将数据打乱；
    sampler=None,        # sampler：样本抽样
    batch_sampler=None,  
    num_workers=0,       # num_workers：使用多进程加载的进程数，0代表不使用多进程；
    collate_fn=,         # collate_fn：如何将多个样本数据拼接成一个batch，一般使用默认的拼接方式即可；
    pin_memory=False,    # pin_memory：是否将数据保存在pin memory区，pin memory中的数据转到GPU会快一些；
    drop_last=False,     # drop_last：dataset 中的数据个数可能不是 batch_size的整数倍，drop_last为True会将多出来不足一个batch的数据丢弃。
    timeout=0,
    worker_init_fn=None,
)
```
对于`DataLoader(dataset, batch_size=2, shuffle=True)`的理解，可以参考下图：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/0de57c452dae498484495f9e31016fab.png#pic_center"> </center>



```python
test_loader = DataLoader(Test, batch_size=2, shuffle=False, num_workers=2)
for i, train_data in enumerate(test_loader):
    print('i: ', i)
    data, label = train_data
    print('data: ', data)
    print('label: ', label)
```
运行结果为：
> i:  0 
> data:  tensor([[1, 2],
>         				[3, 4]]) 
> label:  tensor([0, 1])
> i:  1
> data:  tensor([[2, 1],
>         				[3, 4]]) 
> label:  tensor([0, 1]) 
> i:  2 
> data:  tensor([[4, 5]]) 
> label:  tensor([2])

从这个结果可以看出，这是批量读取。我们可以像使用迭代器一样使用它,如对它进行循环操作。不过它不是迭代器，我们可以通过iter命令转换为迭代器。
```python
dataiter = iter(test_loader)
imgs, labels = next(dataiter)
```
一般用data.Dataset处理同一个目录下的数据。如果数据在不同目录下，不同目录代表不同类别（这种情况比较普遍），使用data.Dataset来处理就不很方便。不过，可以使用Pytorch另一种可视化数据处理工具（即torchvision）就非常方便，不但可以自动获取标签，还提供很多数据预处理、数据增强等转换函数。

____


## 3 torchvision简介
torchvision有4个功能模块，model、datasets、transforms和utils。本节我们将主要介绍如何使用datasets的ImageFolder处理自定义数据集，如何使用transforms对源数据进行预处理、增强等。下面我们重点介绍transforms及ImageFolder。

### 3.1 transforms
transforms提供了对PIL Image对象和Tensor对象的常用操作。
（1）对PIL Image的常见操作如下：
- Scale/Resize: 调整尺寸，长宽比保持不变；
- CenterCrop、RandomCrop、RandomSizedCrop：裁剪图片，CenterCrop和RandomCrop在crop时是固定size，RandomResizedCrop则是random size的crop；
- Pad: 填充；
- ToTensor: 把一个取值范围是[0,255]的PIL.Image 转换成 Tensor。形状为(H,W,C)的numpy.ndarray，转换成形状为[C,H,W]，取值范围是[0,1.0]的torch.FloatTensor。
- RandomHorizontalFlip:图像随机水平翻转，翻转概率为0.5;
- RandomVerticalFlip: 图像随机垂直翻转;
- ColorJitter: 修改亮度、对比度和饱和度。
（2）对Tensor的常见操作如下：
- Normalize: 标准化，即减均值，除以标准差；
- ToPILImage:将Tensor转为PIL Image。

如果要对数据集进行多个操作，可通过Compose将这些操作像管道一样拼接起来，类似于nn.Sequential。以下为示例代码

```python
13
transforms.Compose([
    # 将给定的 PIL.Image 进行中心切割，得到给定的 size，
    # size 可以是 tuple，(target_height, target_width)。
    # size 也可以是一个 Integer，在这种情况下，切出来的图片形状是正方形。            
    transforms.CenterCrop(10),
    # 切割中心点的位置随机选取
    transforms.RandomCrop(20, padding=0),
    # 把一个取值范围是 [0, 255] 的 PIL.Image 或者 shape 为 (H, W, C) 的 numpy.ndarray，
    # 转换为形状为 (C, H, W)，取值范围是 [0, 1] 的 torch.FloatTensor
    transforms.ToTensor(),
    # 规范化到[-1,1]
    transforms.Normalize(mean = (0.5, 0.5, 0.5), std = (0.5, 0.5, 0.5))
])
```

### 3.2 ImageFolder

当文件依据标签处于不同文件下时，如：
─── data
├── Cat
│ ├── 001.jpg
│ └── 002.jpg
├── Dog
│ ├── 001.jpg
│ └── 002.jpg
.................
我们可以利用 torchvision.datasets.ImageFolder 来直接构造出 dataset，代码如下：
```python
from torchvision import transforms, datasets
train_data = datasets.ImageFolder(train_path, transform=data_transform)
train_loader = DataLoader(train_data)
val_data = datasets.ImageFolder(val_path, transform=data_transform)
```

ImageFolder 会将目录中的文件夹名自动转化成序列，那么DataLoader载入时，标签自动就是整数序列了。
下面我们利用ImageFolder读取不同目录下图片数据，然后使用transorms进行图像预处理，预处理有多个，我们用compose把这些操作拼接在一起。然后使用DataLoader加载。

_____


## 4 案例分析
### 4.1 在线下载
直接输入以下代码即可：
```python
from torchvision.datasets import mnist

# 下载数据并对数据预处理
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.5,], [0.5,])])
train_dataset = mnist.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = mnist.MNIST(root='./data', train=False, transform=transform, download=True)
train_loader = DataLoader(train_dataset, batch_size=train_batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=test_batch_size, shuffle=False)
```
train=True 代表我们读入的数据作为训练集(如果为true则从training.pt创建数据集，否则从test.pt创建数据集)。download=True则是当我们的根目录（root）下没有数据集时，便自动下载。

### 4.2 本地导入MNIST数据集
首先需要自定义数据类来继承和重写Dataset抽象类。
```python
import gzip
import os
from random import shuffle
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

class MnistDataset(Dataset):
    def __init__(self, folder, data_name, label_name, transform=None):
        (train_set, train_labels) = load_data(folder, data_name, label_name)
        self.train_set = train_set
        self.train_labels = train_labels
        self.transform = transform

    def __getitem__(self, index):
        img, target = self.train_set[index], int(self.train_labels[index])
        if self.transform is not None:
            img = self.transform(img)
        return img, target
    
    def __len__(self):
        return len(self.train_set)

def load_data(data_folder, data_name, label_name):
    with gzip.open(os.path.join(data_folder, label_name), 'rb') as labpath:
        y_train = np.frombuffer(labpath.read(), np.int8, offset=8)
    with gzip.open(os.path.join(data_folder, data_name), 'rb') as imgpath:
        x_train = np.frombuffer(imgpath.read(), np.int8, offset=16).reshape(len(y_train), 28, 28)
    return x_train, y_train

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.5,], [0.5,])])
train_dataset = MnistDataset('./data/MNIST/raw', 'train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz', transform=transform)
train_loader = DataLoader(train_dataset, shuffle=True, batch_size=64)
```
至于offset为什么是8和16，可以看到官方对该数据集的介绍，offset的0000-0003是 magic number，所以跳过不读，offset的0004-0007是items数目

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/b43b15f6db934342b40d074d24a29c29.png#pic_center"> </center>




### 参考
- Pytorch数据处理全流程：[https://mp.weixin.qq.com/s/as_PdkErmSahoNmKpR7wvQ](https://mp.weixin.qq.com/s/as_PdkErmSahoNmKpR7wvQ)
- DataLoader源代码剖析：[https://blog.csdn.net/g11d111/article/details/81504637](https://blog.csdn.net/g11d111/article/details/81504637)
- Pytorch数据处理工具箱：[http://www.feiguyunai.com/index.php/2019/07/31/pytorch-04/](http://www.feiguyunai.com/index.php/2019/07/31/pytorch-04/)
- pytorch/torch/utils/data/：[https://github.com/pytorch/pytorch/tree/1.7/torch/utils/data](https://github.com/pytorch/pytorch/tree/1.7/torch/utils/data)
- PyTorch教程：[https://pytorch.org/docs/stable/data.html](https://pytorch.org/docs/stable/data.html)