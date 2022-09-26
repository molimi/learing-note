
Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。
Pyplot 是常用的绘图模块，能很方便让用户绘制 2D 图表。

## 0 准备工作
先安装`matplotlib`库，在终端输入命令`pip install matplotlib -i https://pypi.doubanio.com/simple/`下载`matplotlib`，然后导入库，并使用别名`plt`。
```python
import matplotlib.pyplot as plt
import numpy as np 
```

____

## 1 基础入门
### 1.1 简单绘图

使用NumPy库中的`linspace()`函数获得0到2π之间角度的ndarray对象。
```python
x = np.linspace(0, math.pi*2, 100)
```
ndarray对象用作图的x轴上的值。通过以下语句获得在y轴上显示的x中的角度的相应正弦值
```python
y = np.sin(x)
```
使用`plot()`函数绘制两个数组的值。
```python
plt.plot(x,y)
```
可以设置绘图标题以及x和y轴的标签。
```python
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
```
`show()`函数调用绘图查看器窗口
```python
plt.show()
```

完整代码：
```python
import numpy as np
import matplotlib.pyplot as plt
import math

# 显示中文设置
plt.rcParams['font.sans-serif'] = ['SimHei']        # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False          # 解决坐标轴负数的负号显示问题

x = np.linspace(0, math.pi*2, 100)
y = np.sin(x)
plt.plot(x, y)

plt.xlabel('角度')
plt.ylabel('正弦值')
plt.title('正弦波')
plt.show()
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/769d6a84fd1f4d37978c4d3e47a69545.png#pic_center" width=50%> </center>


由上面的代码，我们可以看到使用`matplotlib.pyplot`模块很容易快速生成绘图，但建议使用面向对象的方法，因为它可以更好地控制和自定义绘图。`matplotlib.axes.Axes`类中也提供了大多数函数。
使用更正式的面向对象方法背后的主要思想是创建图形对象，然后只调用该对象的方法或属性。这种方法有助于更好地处理其上有多个绘图的画布。
在面向对象的界面中，Pyplot仅用于一些功能，如图形创建，用户显式创建和跟踪图形和轴对象。在此级别，用户使用Pyplot创建图形，通过这些图形，可以创建一个或多个轴对象。然后，这些轴对象用于大多数绘图操作。对Matplotlib Axes类的详细介绍，请阅读：[https://www.yiibai.com/matplotlib/matplotlib_axes_class.html](https://www.yiibai.com/matplotlib/matplotlib_axes_class.html)

首先，创建一个提供空画布的图形实例。
```python
fig = plt.figure()
```
将轴添加到图形中。`add_axes()`方法需要一个4个元素的列表对象，对应于图形的左侧，底部，宽度和高度。每个数字必须介于0和1之间。
```python
ax = fig.add_axes([0, 0, 1, 1])
```
设置x和y轴的标签以及标题
```python
ax.set_title('正弦波')
ax.set_xlabel('角度')
ax.set_ylabel('正弦值')
```
调用axes对象的plot()方法。
```python
ax.plot(x, y)
```


完整代码：
```python
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

# 显示中文设置
plt.rcParams['font.sans-serif'] = ['SimHei']        # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False          # 解决坐标轴负数的负号显示问题


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('正弦波')
ax.set_xlabel('角度')
ax.set_ylabel('正弦值')
ax.plot(x, y)
plt.show()
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/769d6a84fd1f4d37978c4d3e47a69545.png#pic_center" width=50%> </center>

温馨提示：在绘图代码里经常看到，有用plt.，有用ax.，至于怎么选用，我认为简单又适合自己的才是最好的，如果有多个子图，并每个子图都需要修饰，ax会比plt更方便，反之则使用plt就够用了。

### 1.2 图和子图
我们不能在一个空白的figure上绘图，必须要创建一个或更多的subplots（子图），用add_subplot:
```python
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
```
这行代码的意思是，figure是2x2（这样一共有4幅图），而且我们选中4个subplots（数字从1到4）中的第1个。如果要创建另外两个子图，可以输入：
```python
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
```
我们可以直接在空白的subplot上绘图，直接在对应的AxesSubplot对象上调用方法即可，如果输入`plt.plot([1.5, 3.5, -2, 1.6])`这样的命令，matplotlib会把图画在最后一个figure的最后一个子图上。
```python
plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/deced44058d345a0876b77f4cbed7d44.png#pic_center" width=50%> </center>

因为创建一个带有多个subplot的figure是很常见的操作，所以matplotlib添加了一个方法，plt.subplots，来简化这个过程。这个方法会创建一个新的figure，并返回一个numpy数组，其中包含创建的subplot对象：

```python
fig, axes = plt.subplots(2, 3)
```

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/d45c256cc5254e6e806345bc8ffbf886.png#pic_center" width=50%> </center>

这个操作是很有用的。axes能用一个二位数据来索引，例如，axes[0, 1]。我们可以使用sharex和sharey来指定不同subplot有相同的x-或y-axis（其实就是令坐标轴的范围相同），这能让我们在同一范围内进行数据之间的比较。不然的话，matplotlib会自动绘图的范围不一定是一样的。

默认情况下，matplotlib会在subplot之间留下一定间隔的边距，这取决于绘图的高度和跨度。所以如果我们调整绘图的大小，它会自动调整。我们可以用Figure对象下的subplots_adjust方法来更改间隔，当然，也可以用第一层级的函数：
```python
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
```    
wspace和hspace控制figure宽度和长度的百分比，可以用来控制subplot之间的间隔。这里有一个例子，我们让间隔为0：

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/6a4381879c7540c7b0be00e830a19dc1.png#pic_center" width=50%> </center>

注意到轴上有些标签重叠了。matplotlib不会检查标签是否重叠，所以我们需要直接规定明确的tick location（记号位置）和tick labels（记号标签），这部分会稍后介绍。

### 1.3 颜色，标记物，线样式
matplotlib的plot主函数能接受x和y坐标，在可选项中，字符串能指定颜色和线样式。例如，画出x和y，用绿色的点线：
```python
ax.plot(x, y, 'g--')
```

这种方法可以很方便的同时指定颜色和线样式；不过有些用户可能不喜欢直接把规定颜色和样式的字符串写在一起，当然，我们也可以写得更明确一些：
```python
ax.plot(x, y, linestyle='--', color='g')
```

有很多可供选择的颜色缩写，当然，我们也可以使用任意的颜色，通过制定hex code(十六进制码，比如'#CECECE')。通过查看plot的字符串文档，我们可以看到可供选择的所有线样式（直接输入`plot?`）。

另外还可以用markers（标记物）来高亮实际的数据点。因为matplotlib创建一个continuous line plot（连续线条图）的话，如果想要插入，可能看不清楚哪里可以插入数据点。而marker可以作为样式的一部分，字符串必须按颜色，标记物类型，样式这样的顺序：
```python
plt.plot(np.random.randn(30).cumsum(), 'ko--')
```
也可以分开写：
```python
plt.plot(np.random.randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
```
对于点线图，我们注意到，默认情况下，后续点是通过线性添加上的。这个可以通过drawstyle来更改：
```python
data = np.random.randn(30).cumsum()
plt.plot(data, 'ko--', label='Default')
plt.plot(data, 'g*-', drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/c801c15fed3545f4913df598581299dd.png#pic_center" width=50%> </center>

### 1.4 标记，标签，图例
对于大部分绘图的装饰，有两种主要的方法：使用pyplot（matplotlib.pyplot）和用更对象导向的简单的matplotlib API。

pyplot界面是为交互式使用而设计的，它包含很多方法，比如xlim, xticks, xticklabels。这些方法控制绘图的范围，标记位置，标记标签。有两种使用方法：

- 调用的时候不传入参数，使用当前的参数设置（例如，plt.xlim()返回当前X轴的范围）
- 调用的时候传入参数，使用传入的参数设置（例如，plt.xlim([0, 10]), 令X轴的范围从0到10）

所有这些方法，作用于激活的或最新创建的AxesSubplot对象上。每一个都在subplot有对应的两个方法；比如对于xlim，就有对应的ax.get_xlim和ax.set_xlim。这里使用subplot的方法，这样会更清晰。
```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
```
为了改变x-axis tick（x轴标记），使用set_xticks和set_xticklabels。前者告诉matplotlib沿着x轴的范围，把标记放在哪里；默认会把所在位置作为标签，但我们可以用set_xticklabels来设置任意值作为标签：
```python
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
```
rotation选项让x轴上的标记标签有一个30度的旋转。set_xlabel给x轴一个名字，而set_title给subplot一个标题：
```python
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
```
用相同的流程来更改y轴，把上面代码里的x变为y。axes类有一个set方法，能让我们一次设置很多绘图特性。对于上面的例子，我们可以写成下面这样：
```python
props = {
    'title': 'My first matplotlib plot',
    'xlabel': 'Stage'
}

ax.set(**props)
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/a7528219db1e4bac9162db1c74b4867a.png#pic_center" width=50%> </center>

图例对于绘图很重要。有很多方式可以添加图例。最简单的方法是用label参数：
```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(30).cumsum(), 'k', label='one')
ax.plot(np.random.randn(30).cumsum(), 'k--', label='two')
plt.legend(loc='best')
plt.show()
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/37d3855ffcb94384aa9600a15424f2df.png#pic_center" width=50%> </center>

legend方法有一些选项，比如用loc参数设定位置。更多信息，可以参考字符串文档（ax.legend?）

loc告诉matplotlib把图例放在哪里。如果不挑剔的话，直接设定'best'就可以了，它会自动选择一个合适的位置。如果想要从图例中排除一个或更多的元素，那就不要传入label，或设置`label='_nolegen_'`。

### 1.5 注释

除了标准的绘图类型，我们可能希望画出自己的绘图注释，包括文本，箭头或其他形状。我们可以添加注释和文本，通过text，arrow，和annotate函数。text能在指定的坐标(x, y)上写出文本，还可以自己设定样式：
```python
ax.text(x, y, 'Hello world!', family='monospace', fontsize=10)
```

注释可以画出文本和箭头。下面举个例子：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

ax = plt.gca()  # 设置边框/坐标轴

ax.spines['right'].set_color('none')    # spines就是脊梁，即四个边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', -0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 绘制特定散点
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')

# k--表示黑色虚线，k代表黑色，--表示虚线,lw表示线宽， 绘制(x0,y0)垂直于x轴的线
plt.plot([x0, x0], [0, y0], 'k--', lw=2.5)

'''
其中参数xycoords='data' 是说基于数据的值来选位置, xytext=(+30, -30) 和 textcoords='offset points'
对于标注位置的描述 和 xy 偏差值, arrowprops是对图中箭头类型的一些设置.
'''
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# 其中-3.7, 3,是选取text的位置, 空格需要用到转字符\ ,fontdict设置文本字体
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\mu\ \sigma_i\ \alpha_t$', fontdict={'size':'16', 'color':'red'})
plt.show()
```

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/7da1c9355a0f432db35745ea819cefc2.png#pic_center" width=50%> </center>



### 1.6 保存为文件

我们可以用plt.savefig来保存图。这个方法等同于直接在figure对象上调用savefig方法。例如，想要保存一个SVG版本的图片，键入：
```python
plt.savefig('figpath.svg)
```

保存的文件类型通过文件名后缀来指定。即如果使用 .pdf做为后缀，就会得到一个PDF文件。这里有一些重要的设置，作者经常用来刊印图片：

- dpi，控制每英寸长度上的分辨率
- bbox_inches, 能删除figure周围的空白部分

比如我们想要得到一幅PNG图，有最小的空白，400 DPI，键入：
```python
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
```  


### 1.7 matplotlib设置

matplotlib很多默认的设置是可以自己定义的，通过修改一些全局设定，比如图大小，subplot间隔，颜色，字体大小，网格样式等等。一种设定的方式是用rc方法，例如，想要设置全局的图大小为10 x 10，键入：
```python
plt.rc('figure', figsize=(10, 10))
``` 
rc中的第一个参数是我们想要自定义的组件，比如'figure', 'axes', 'xtick', 'ytick', 'grid', 'legend'，或其他。然后添加一个关键字来设定新的参数。一个比较方便的写法是把所有的设定写成一个dict：

    font_options = {'family': 'monospace',
                    'weight': 'bold',
                    'size'  : 'small'}
    plt.rc('font', **font_options)
    
更详细的设定可以去看一下文档，matplotlib下的设置文件*matplotlibrc*，位于*matplotlib/mlp-data*文件夹下。如果按自己的方式修改这个文件，并把这个文件放在主目录下，更名为*.matplotlibrc*的话，在每次启动matplotlib的时候，会自动加载这个文件。

___

## 参考
- 官方教程：[https://matplotlib.org/](https://matplotlib.org/)
- Matplotlib 教程：[https://www.runoob.com/matplotlib/matplotlib-tutorial.html](https://www.runoob.com/matplotlib/matplotlib-tutorial.html)
- Matplotlib教程：[https://www.yiibai.com/matplotlib](https://www.yiibai.com/matplotlib)
- Python--Matplotlib（基本用法）：[https://blog.csdn.net/qq_34859482/article/details/80617391](https://blog.csdn.net/qq_34859482/article/details/80617391)
- matplotlib.pyplot的使用总结大全：[https://zhuanlan.zhihu.com/p/139052035](https://zhuanlan.zhihu.com/p/139052035)