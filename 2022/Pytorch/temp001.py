"""
import torch
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

It raises an error as follows: 
RuntimeError: CUDA out of memory. Tried to allocate 5.59 GiB (GPU 0; 11.17 GiB total capacity; 0 bytes already allocated; 10.91 GiB free; 5.59 GiB allowed; 0 bytes reserved in total by PyTorch)
显存超标后，比不设置限制的错误信息多了一个提示，“5.59 GiB allowed;”
"""
import torch
from torch import nn 

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

