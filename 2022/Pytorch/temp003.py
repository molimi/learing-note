# -*- coding: utf-8 -*-
import numpy as np
from loaddata import *
from model import *
from utils import *
from torchvision import transforms
from torch.utils.data import DataLoader
import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt

# device configuration
my_seed = 2022
np.random.seed(my_seed)
torch.manual_seed(my_seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
device = get_device(0.7, my_seed)
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# 超参数设置
num_epoches = 10
batch_size = 64
learning_rate = 0.001
in_start = 1000
in_end = 2000
data_num = 0     # 0--AV45  1--FGD 2--VBM
set_index = 48

train_set = SnpDataset('../../data', 'Data_common_Img_adjusted.mat', in_start, in_end, data_num, set_index)
train_loader = DataLoader(train_set, shuffle=True, batch_size=batch_size)

model = CFSNet(in_end-in_start).to(device)


# loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)


losses = []
for epoch in range(num_epoches):
    train_loss = 0
    model.train()
    for data, label in train_loader:
        data, label = data.to(device), label.to(device)

        # forward pass
        output = model(data)
        loss = criterion(output, label)

        # backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # 计算损失
        train_loss += loss.item()

    losses.append(train_loss/len(train_loader))

plt.figure()
plt.switch_backend('agg')
plt.plot(np.arange(len(losses)), losses)
plt.legend(['Train Loss'], loc='best')
plt.savefig('./figure/train_loss.png')