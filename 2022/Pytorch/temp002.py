# -*- coding: utf-8 -*-
from turtle import shape
import torch
from torch import device, nn
import torch.nn.functional as F





'''
class MLP(nn.Module):
    def __init__(self, **kwargs) -> None:
        super(MLP, self).__init__(**kwargs)
        self.hidden = nn.Linear(784, 256)
        self.output = nn.Linear(256, 10)

    def forward(self, x):
        out = F.relu(self.hidden(x))
        out = self.output(out)
        return out

X = torch.rand(2, 784)
net = MLP()
print(net)
print(net(X))

class MyLayer(nn.Module):
    def __init__(self, **kwargs) -> None:
        super(MyLayer, self).__init__(**kwargs)
    def forward(self, x):
        return x - x.mean()

layer = MyLayer()
print(layer(torch.tensor([1, 2, 3, 4, 5], dtype=torch.float)))      # tensor([-2., -1.,  0.,  1.,  2.])

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

# 定义一个函数来计算卷积层。它对输入和输出做相应的升维和降维=
def comp_conv2d(conv2d, X):
    # (1, 1)代表批量大小和通道数
    X = X.view((1, 1) + X.shape)
    Y = conv2d(X)
    return Y.view(Y.shape[2:])  # 排除不关心的前两维:批量和通道

conv2d = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)

X = torch.rand(8, 8)
comp_conv2d(conv2d, X).shape        # torch.Size([8, 8])
'''

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

def initialize_weights(self):
    for m in self.modules():
        if isinstance(m, nn.Conv2d):
            torch.nn.init.constant_(m.weight.data)
            if m.bias is not None:
                torch.nn.init.constant_(m.bias.data, 0.3)
        elif isinstance(m, nn.Linear):
            torch.nn.init.normal_(m.weight.data, 0.1)
            if m.bias is not None:
                torch.nn.init.zeros_(m.bias.data)
        elif isinstance(m, nn.BatchNorm2d):
            m.weight.data.fill_(1)
            m.bias.data.zeros_()


criterion = nn.MSELoss()
optimizer = nn.optimize.SGD()
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