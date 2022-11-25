&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Matplotlib是Python中令人惊叹的可视化库，用于数组的二维图。 Matplotlib是一个基于NumPy数组的多平台数据可视化库，旨在与更广泛的SciPy堆栈配合使用。
## 1 保存图形时坐标轴标签太长导致显示不全的问题
**1. 问题描述**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在使用`matplotlib`绘制图像并保存时，由于标签太长，导致坐标轴上的标签显示不全的问题。刚遇到问题时调整了一下图片大小，然鹅并没有卵用。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;查看一下matplotlib的文档：[`matplotlib.pyplot.savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html?highlight=savefig)，可以看到：

<img src="https://img-blog.csdnimg.cn/142d6c13a1d44a34a881d18bd177aa47.png#pic_center" width=50%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;默认情况下，仅保存图形给定的部分，如果设置为`tight`，将尝试保存更紧致的图形。

**2. 解决办法**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在保存图形是加入`bbox_inches`参数：
```python
# 设置tight bbox
fig.savefig('output.png', bbox_inches='tight')
```

___
## 2 contourf()函数的使用
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`contourf()`是来绘制等高线的，contour和contourf都是画三维等高线图的，不同点在于`contour()`是绘制轮廓线，`contourf()`会填充轮廓。除非另有说明，否则两个版本的函数是相同的。
```python
coutour([X, Y,] Z,[levels], **kwargs)
```
<table border="1" cellpadding="1" cellspacing="1"><tbody><tr><td style="width:119px;">参数：</td><td>X,Y：类似数组，可选</td></tr><tr><td style="width:119px;">&nbsp;</td><td>为Z中的坐标值</td></tr><tr><td style="width:119px;">&nbsp;</td><td>当&nbsp;X,Y,Z&nbsp;都是&nbsp;2&nbsp;维数组时，它们的形状必须相同。如果都是&nbsp;1&nbsp;维数组时，len(X)是&nbsp;Z&nbsp;的列数，而&nbsp;len(Y)&nbsp;是&nbsp;Z&nbsp;中的行数。（例如，经由创建<font face="monospace">numpy.meshgrid()</font>）</td></tr><tr><td style="width:119px;">&nbsp;</td><td>Z：类似矩阵</td></tr><tr><td style="width:119px;">&nbsp;</td><td>绘制轮廓的高度值</td></tr><tr><td style="width:119px;">&nbsp;</td><td>levels：int或类似数组，可选</td></tr><tr><td style="width:119px;">&nbsp;</td><td>确定轮廓线/区域的数量和位置</td></tr><tr><td style="width:119px;"> <p>&nbsp;</p> </td><td>&nbsp;</td></tr><tr><td style="width:119px;">其他参数：</td><td>aalpha：float ，可选</td></tr><tr><td style="width:119px;">&nbsp;</td><td>alpha混合值，介于0（透明）和1（不透明）之间。</td></tr><tr><td style="width:119px;">&nbsp;</td><td>cmap：str或colormap ，可选</td></tr><tr><td style="width:119px;">&nbsp;</td><td>Colormap用于将数据值（浮点数）从间隔转换为相应Colormap表示的RGBA颜色。用于将数据缩放到间隔中看&nbsp;。</td></tr></tbody></table>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要画出等高线，核心函数是`plt.contourf()`，但在这个函数中输入的参数是x,y对应的网格数据以及此网格对应的高度值，因此我们调用`np.meshgrid(x,y)`把x,y值转换成网格数据：
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x, y):
    return (1 + x**3 + y**5) * np.exp(-x**2-y**2)

a = np.linspace(-3, 3)
X, Y = np.meshgrid(a, a)	# 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值

plt.contourf(X, Y, f(X, Y))
plt.show()
```

<img src="https://img-blog.csdnimg.cn/42f85b0c93fe4d48b4322e6b23d3c92e.png#pic_center" width=36%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果想显示热力图，那只要在`plt.contourf()`函数中添加属性`cmap=plt.cm.hot`就能显示热力图，其中cmap代表为color map，我们把color map映射成hot(热力图)

```python
plt.contourf(X, Y, f(X, Y), cmap=plt.cm.hot)
```

<img src="https://img-blog.csdnimg.cn/fc5b659fbdf1485ca187b781afa365bb.png#pic_center" width=36%>

___

## 3 Matplotlib.colors.ListedColormap
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`matplotlib.colors.ListedColormap`类属于matplotlib.colors模块。 matplotlib.colors模块用于将颜色或数字参数转换为RGBA或RGB。此模块用于将数字映射到颜色或以一维颜色数组(也称为colormap)进行颜色规格转换。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`matplotlib.colors.ListedColormap`类用于从颜色列表创建colarmap对象。这对于直接索引到颜色表中很有用，也可以用于为法线贴图创建特殊的颜色表。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用法： `class matplotlib.colors.ListedColormap(colors, name=’from_list’, N=None)`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参数：
- 颜色：它是Matplotlib颜色规格的数组或列表，或等于N x 3或N x 4浮点数组(N rgb或rgba值)
- 名称：它是一个可选参数，它接受一个字符串来标识颜色图。
- N：它是一个可选参数，它接受表示映射中条目数的整数值。它的默认值为“无”，其中颜色列表中的每个元素都有一个颜色表条目。如果N小于len(colors)，则列表将在N处截断，而如果N大于len，则列表将重复进行扩展。
- 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;该类的方法：`reversed()`：这用于创建Colormap的反向实例。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用法： `reversed(self, name=None)`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参数：
- name：它是一个可选参数，表示反转的颜色图的名称。如果将其设置为“无”，则名称将为父色图的名称+ “_r”。
返回值：它返回颜色图的反向实例

**示例一：**
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

a = np.linspace(-3, 3)
A, B = np.meshgrid(a, a)    # 生成网格
X = np.exp(-(A**2 + B**2))
figure, (axes1, axes2) = plt.subplots(ncols = 2)

colors = ["green", "orange", "gold", "blue", "k", "#550011", "purple", "red"]

axes1.set_title("color list")
contour = axes1.contourf(A, B, X, colors = colors)      # 绘制等高线， contour() 是绘制轮廓线，contourf()会填充轮廓

axes2.set_title("with colormap")
cmap = ListedColormap(colors)
contour = axes2.contourf(A, B, X, cmap = cmap)
figure.colorbar(contour)

plt.show()
```
<img src="https://img-blog.csdnimg.cn/6b04aa517106409b80a9186c4e716490.png#pic_center" width=36%>

**示例二：**
```python
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.colors as colors 
from mpl_toolkits.axes_grid1 import make_axes_locatable 
  
res = np.array([[0, 2], [3, 4]], dtype = int) 
  
u = np.unique(res) 
bounds = np.concatenate(([res.min()-1], 
                         u[:-1]+np.diff(u)/2., 
                         [res.max()+1])) 
  
norm = colors.BoundaryNorm(bounds, len(bounds)-1) 
color_map1 = ['#7fc97f', '#ffff99', '#386cb0', '#f0027f'] 
color_map = colors.ListedColormap(color_map1)  
  
fig, axes = plt.subplots() 
img = axes.imshow(res, cmap = color_map, 
                  norm = norm) 
divider = make_axes_locatable(axes) 
cax = divider.append_axes("right", size ="5 %") 
  
color_bar = plt.colorbar(img, cmap = color_map,  
                         norm = norm, cax = cax) 
  
color_bar.set_ticks(bounds[:-1]+np.diff(bounds)/2.) 
color_bar.ax.set_yticklabels(color_map1) 
color_bar.ax.tick_params(labelsize = 10) 
  
plt.show()
```

<img src="https://img-blog.csdnimg.cn/ca72e6c10c1e486c8eef0ccfea1b99ca.png#pic_center" width=36%>

## 4 fillbetween()
`matplotlib.pyplot.fill_between()`用于填充两条水平曲线之间的区域。函数原型为：
```python
plt.fill_between(
                 x, y1, y2=0, where=None, 
                 interpolate=False, step=None,
                 hold=None, data=None,
                 **kwargs
)
```
- x - array( length N) 定义曲线的 x 坐标
- y1 - array( length N ) or scalar 定义第一条曲线的 y 坐标
- y2 - array( length N ) or scalar 定义第二条曲线的 y 坐标
- where - array of bool (length N), optional, default: None。排除一些区域被填充。

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
np.random.seed(1)
x = np.linspace(0, 8, 16)
y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))

# plot
fig, ax = plt.subplots()

ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, (y1 + y2)/2, linewidth=2)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
```

<img src ="https://img-blog.csdnimg.cn/1629775525c24e668b8805dca00a4bc9.png#pic_center" width = 36%>

## 5 plt.gca().set_aspect("equal")

在matplotlib中，整个图像为一个Figure对象。在Figure对象中可以包含一个或者多个Axes对象。每个Axes(ax)对象都是一个拥有自己坐标系统的绘图区域。所属关系如下：

当我们调用plot时，matplotlib会调用`gca()`获取当前的axes绘图区域，而且gca反过来调用`gcf()`来获得当前的figure。


在pyplot模块中，许多函数都是对当前的Figure或Axes对象进行处理，比如说：`plt.plot()`实际上会通过`plt.gca()`获得当前的Axes对象ax，然后再调用ax.`plot()`方法实现真正的绘图。

`ax=plt.gca()`之后通过ax可以设定主刻度和副刻度`ax.xaxis.set_major_locotor(MultipleLocator(float))`...set_minor_locator(y轴上的修改为y即可)；除了刻度，x轴和y轴上对于同一个区间，可能长度不同，即axes per unit length可能不等，这时需要一句话搞定ax.set_aspect("equal")。

[matplotlib.axes.Axes.set_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html)

> 后续会继续补充~
