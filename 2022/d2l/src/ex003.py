# -*- coding； utf-8 -*-
import os
import pandas as pd
import torch

os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'house_tiny.csv')
# 构造数据
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')   # 列名
    f.write('NA,Pave,127500\n')
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

# 读入数据
data = pd.read_csv(data_file)
# print(data)
# print(data['Alley'])
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, -1]   # 分割数据集

inputs = inputs.fillna(inputs.mean())       # 用均值填充
# print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True)
# print(inputs)

X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X)
print(y)