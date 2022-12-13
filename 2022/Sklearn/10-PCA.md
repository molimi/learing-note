## 1 引言
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;降维是对数据高维度特征的一种预处理方法。降维是将高维度的数据保留下最重要的一些特征，去除噪声和不重要的特征，从而实现提升数据处理速度的目的。在实际的生产和应用中，降维在一定的信息损失范围内，可以为我们节省大量的时间和成本。降维也成为了应用非常广泛的数据预处理方法。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;降维具有如下一些优点：1）使得数据集更易使用；2）降低算法的计算开销；3）去除噪声；4）使得结果容易理解。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PCA（Principal Component Analysis） 是一种常见的数据分析方式，常用于高维数据的降维，可用于提取数据的主要特征分量。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PCA 的数学推导可以从最大可分型和最近重构性两方面进行，前者的优化条件为划分后方差最大，后者的优化条件为点到划分平面距离最小，这里我将从最大可分性的角度进行证明。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;初学者建议先阅读这份教程，英文好的可以直接阅读[原文文献](https://faculty.iiit.ac.in/~mkrishna/PrincipalComponents.pdf)，其他小伙伴可以参考：[A tutorial on Principal Components Analysis | 主成分分析（PCA）教程](https://www.cnblogs.com/XMU-hcq/p/6353698.html)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;奇异值分解，可以参考这份教程，英文好的可以直接阅读[原文文献](https://cis.temple.edu/~latecki/Courses/AI-Fall10/Lectures/PCA-Tutorial-Intuition.pdf)，其他的小伙伴可以参考：[A Tutorial on Principal Component Analysis(译)](https://blog.csdn.net/zhouchangyu1221/article/details/103949967)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PCA是将数据投影到方差最大的几个相互正交的方向上，以期待保留最多的样本信息。样本的方差越大表示样本的多样性越好，在训练模型的时候，我们当然希望数据的差别越大越好。否则即使样本很多但是他们彼此相似或者相同，提供的样本信息将相同，相当于只有很少的样本提供信息是有用的。样本信息不足将导致模型性能不够理想。这就是PCA降维的目的：将数据投影到方差最大的几个相互正交的方向上。这种约束有时候很有用，比如在下面这个例子：


<img src="https://img-blog.csdnimg.cn/199995b5ae14494586dcf5b01cfd7dc2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" width=36%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于这个样本集我们可以将数据投影到 x 轴或者 y 轴，但这都不是最佳的投影方向，因为这两个方向都不能最好的反映数据的分布。很明显还存在最佳的方向可以描述数据的分布趋势，那就是图中红色直线所在的方向。也是数据样本作投影，方差最大的方向。向这个方向做投影，投影后数据的方差最大，数据保留的信息最多。

## 2 PCA的思想
PCA顾名思义，就是找出数据里最主要的方面，用数据里最主要的方面来代替原始数据。基本想法是将所有数据投影到一个子空间中，从而达到降维的目标，为了寻找这个子空间，我们基本想法是：
1.  所有数据在子空间中更为分散
2.  损失的信息最小，即：在补空间的分量少

PCA问题的优化目标：将一组$p$维向量降为$q$维$(0\lt q\le p)$，其目标是选择$q$个单位正交基，使得原始数据变换到该组基上后，各特征两两之间的协方差为$0$，而特征的方差则尽可能大，当在正交的约束下取最大的$q$个方差。

假设$m$个$n$维数据$(x^{(1)}, x^{(2)},\cdots,x^{(m)})$都已经进行了中心化，即$\sum\limits_{i=1}^{m}x^{(i)}=0$。经过投影变换后得到的新坐标系为$\{w_1,w_2,...,w_n\}$，其中$w$是标准正交基，即$||w||_2=1, w_i^Tw_j=0$。

如果我们将数据从$n$维降到$k$维，即丢弃新坐标系中的部分坐标，则新的坐标系为$\{w_1,w_2,...,w_{k}\}$，样本点$x^{(i)}$在$k$维坐标系中的投影为：$z^{(i)} = (z_1^{(i)}, z_2^{(i)},...,z_{n'}^{(i)})^T$。其中，$z_j^{(i)} = w_j^Tx^{(i)}$是$z_j^{(i)} = w_j^Tx^{(i)}$在低维坐标系里第$j$维的坐标。


## 3 PCA的推导：基于最小投影距离
如果我们用$z^{(i)}$来恢复原始数据$x^{(i)}$，则得到的恢复数据$\overline{x}^{(i)} = \sum\limits_{j=1}^{n'}z_j^{(i)}w_j = Wz^{(i)}$，其中，$W$为标准正交基组成的矩阵。

现在我们考虑整个样本集，我们希望所有的样本到这个超平面的距离足够近，即最小化下式：
$$\sum\limits_{i=1}^{m}||\overline{x}^{(i)} - x^{(i)}||_2^2$$

将这个式子进行整理，可以得到：

$$\begin{align} \sum\limits_{i=1}^{m}||\overline{x}^{(i)} - x^{(i)}||_2^2 & = \sum\limits_{i=1}^{m}|| Wz^{(i)} - x^{(i)}||_2^2 \\& = \sum\limits_{i=1}^{m}(Wz^{(i)})^T(Wz^{(i)}) - 2\sum\limits_{i=1}^{m}(Wz^{(i)})^Tx^{(i)} + \sum\limits_{i=1}^{m} x^{(i)T}x^{(i)} \\& = \sum\limits_{i=1}^{m}z^{(i)T}z^{(i)} - 2\sum\limits_{i=1}^{m}z^{(i)T}W^Tx^{(i)} +\sum\limits_{i=1}^{m} x^{(i)T}x^{(i)} \\& = \sum\limits_{i=1}^{m}z^{(i)T}z^{(i)} - 2\sum\limits_{i=1}^{m}z^{(i)T}z^{(i)}+\sum\limits_{i=1}^{m} x^{(i)T}x^{(i)}  \\& = - \sum\limits_{i=1}^{m}z^{(i)T}z^{(i)} + \sum\limits_{i=1}^{m} x^{(i)T}x^{(i)}  \\& =   -tr( W^T（\sum\limits_{i=1}^{m}x^{(i)}x^{(i)T})W)  + \sum\limits_{i=1}^{m} x^{(i)T}x^{(i)} \\& =  -tr( W^TXX^TW)  + \sum\limits_{i=1}^{m} x^{(i)T}x^{(i)}  \end{align}$$

其中第(1)步用到了$\overline{x}^{(i)}=Wz^{(i)}$，第二步用到了平方和展开，第(3)步用到了矩阵转置公式$(AB)^T =B^TA^T$和$W^TW=I$，第(4)步用到了$z^{(i)}=W^Tx^{(i)}$，第(5)步合并同类项，第(6)步用到了$z^{(i)}=W^Tx^{(i)}$和矩阵的迹，第7步将代数和表达为矩阵形式。

注意到$\sum\limits_{i=1}^{m}x^{(i)}x^{(i)T}$是数据集的协方差矩阵，$W$的每一个向量$w_j$是标准正交基。而$\sum\limits_{i=1}^{m} x^{(i)T}x^{(i)}$是一个常量。最小化上式等价于：
$$\underbrace{arg\;min}_{W}\;-tr( W^TXX^TW) \;\;s.t. W^TW=I$$

这个最小化不难，直接观察也可以发现最小值对应的W由协方差矩阵$XX^T$最大的$k$个特征值对应的特征向量组成。当然用数学推导也很容易。利用拉格朗日函数可以得到
$$J(W) = -tr( W^TXX^TW + \lambda(W^TW-I))$$

对$W$求导有$-XX^TW+\lambda W=0$, 整理下即为：
$$XX^TW=\lambda W$$

这样可以更清楚的看出，$W$为$XX^T$的$k$个特征向量组成的矩阵，而$\lambda$为$XX^T$的若干特征值组成的矩阵，特征值在主对角线上，其余位置为0。当我们将数据集从$n$维降到$k$维时，需要找到最大的$k$个特征值对应的特征向量。这$k$个特征向量组成的矩阵$W$即为我们需要的矩阵。对于原始数据集，我们只需要用$z^{(i)}=W^Tx^{(i)}$，就可以把原始数据集降维到最小投影距离的$k$维数据集。

## 4 PCA的推导：基于最大投影方差
对于任意一个样本$x^{(i)}$，在新的坐标系中的投影为$W^Tx^{(i)}$，在新坐标系中的投影方差为$x^{(i)T}WW^Tx^{(i)}$，要使所有的样本的投影方差和最大，也就是最大化$\sum\limits_{i=1}^{m}W^Tx^{(i)}x^{(i)T}W$的迹，即：
$$\underbrace{arg\;max}_{W}\;tr( W^TXX^TW) \;\;s.t. W^TW=I$$

观察上一节的基于最小投影距离的优化目标，可以发现完全一样，只是一个是加负号的最小化，一个是最大化。

利用拉格朗日函数可以得到
$$J(W) = tr( W^TXX^TW + \lambda(W^TW-I))$$

对$W$求导有$-XX^TW+\lambda W=0$, 整理下即为：
$$XX^TW=\lambda W$$

和上面一样可以看出，$W$为$XX^T$的$k$个特征向量组成的矩阵，而$-\lambda$为$XX^T$的若干特征值组成的矩阵，特征值在主对角线上，其余位置为0。当我们将数据集从$n$维降到$k$维时，需要找到最大的$k$个特征值对应的特征向量。这$k$个特征向量组成的矩阵$W$即为我们需要的矩阵。对于原始数据集，我们只需要用$z^{(i)}=W^Tx^{(i)}$，就可以把原始数据集降维到最小投影距离的$k$维数据集。

## 5 PCA算法流程
### 5.1 特征值分解算法
1. 观测数据规范化处理，得到规范化数据矩阵$X$
1. 计算相关矩阵$R$
$$
R=[r_{ij}]_{m\times m}=\frac{1}{n-1}XX^\mathrm{T}\\
r_{ij} = \frac{1}{n-1}\sum\limits_{l=1}^nx_{il}x_{lj}, i,j=1,2,\cdots,m
$$
3. 求$R$的特征值和特征向量
$$
|R-\lambda I|=0\\
\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_m
$$
求累计方差贡献率达到预定值的主成分个数$k$
$$
\sum_{i=1}^k\eta_i=\frac{\sum\limits_{i=1}^k\lambda_i}{\sum\limits_{i=1}^m\lambda_i}
$$
求前$k$个特征值对应的单位特征向量
$$
a_i=(a_{1i},a_{2i},\cdots,a_{mi})^\mathrm{T}
$$
4. 求$k$个样本主成分
$$
  y_i=a_i^\mathrm{T}\boldsymbol x
$$
  其实算法到这就完事了，剩下两部分是输出。**前面是fit部分，后面是transform部分。**具体可以看下$P_{319}$中的关于相关矩阵特征值分解算法部分内容，构造正交矩阵之后就得到了主成分。
5. 计算$k$个主成分$y_i$与原变量$x_i$的相关系数$\rho(x_i,y_i)$以及$k$个主成分对原变量$x_i$的贡献率$\nu_i$
$$
\nu_i=\rho^2(x_i,(y_1, y_2, \cdots,y_k))=\sum_{j=1}^k\rho^2(x_i,y_j)=\sum_{j=1}^k\lambda_ja_{ij}^2\\
i=1,2,\cdots,m
$$
6. 计算$n$个样本的$k$个主成分值
    第$j$个样本，$\boldsymbol{x}_j=(x_{1j},x_{2j},\cdots, x_{mj})^\mathrm{T}$的第$i$个主成分值是
$$
y_{ij}=(a_{1i},a_{2i},\cdots,a_{mi})(x_{1j},x_{2j},\cdots,x_{mj})^\mathrm{T}=\sum\limits_{l=1}^m a_{li}x_{lj}\\
i=1,2,\cdots,m, j=1,2,\cdots,n
$$

### 5.2 奇异值分解算法
输入：$m\times n$样本矩阵$X$，每一行元素均值为0。`这里每一行是一个特征`
输出：$k\times n$样本主成分矩阵$Y$
参数：主成分个数$k$
1. 构造新的$n\times m$矩阵
$$
X^\prime=\frac{1}{\sqrt{n-1}}X^\mathrm{T}
$$
$X^\prime$每一列均值为0，其实就是转置了。
2. 对矩阵$X^\prime$进行截断奇异值分解
$$
X^\prime=U\mit{\Sigma}V^\mathrm{T}
$$
矩阵$V$的前$k$列构成$k$个样本主成分
3. 求$k\times n$样本主成分矩阵
$$
Y=V^\mathrm{T}X
$$

## 6 代码实现
 Sklearn的PCA就是用SVD进行求解的，原因有以下几点：
- 当样本维度很高时，协方差矩阵计算太慢；
- 方阵特征值分解计算效率不高；
- SVD除了特征值分解这种求解方式外，还有更高效更准球的迭代求解方式，避免了$XX^T$的计算；
- 其实 PCA 与 SVD 的右奇异向量的压缩效果相同。



### 6.1 对cancer数据集应用PCA并进行可视化
PCA 最常见的应用之一就是将高维数据集可视化。但对于有两个以上特征的数据，很难绘制散点图。想要可视化乳腺癌数据集，即便用散点图矩阵也很困难。这个数据集包含30个特征，这就导致需要绘制30*14=420张散点图！我们永远不可能仔细观察所有这些图像，更不用说试图理解它们了。

不过我们可以使用一种更简单的可视化方法——对每个特征分别计算两个类别（良性肿瘤和恶性肿瘤）的直方图。

```python
# 乳腺癌数据的特征直方图，可以发现许多数据没有可分性
fig, axes = plt.subplots(15, 2, figsize=(10, 20))
malignant = cancer.data[cancer.target==0]
bengin = cancer.data[cancer.target==1]

ax = axes.ravel()       # 拉成一维数组

for i in range(30):
    _, bins = np.histogram(cancer.data[:, i], bins=50)          # bins指定统计的区间个数
    ax[i].hist(malignant[:, i], bins=bins, color=mglearn.cm3(0), alpha=0.5)
    ax[i].hist(bengin[:, i], bins=bins, color=mglearn.cm3(2), alpha=0.5)
    ax[i].set_title(cancer.feature_names[i])
    ax[i].set_yticks(())

ax[0].set_xlabel("Feature magnitude")
ax[0].set_ylabel("Frequency")
ax[0].legend(['malignant', 'bengin'], loc='best')
fig.tight_layout()
```

<img src ="https://img-blog.csdnimg.cn/56e6334c0ab943e19f6ac370bcbeb9ae.png#pic_center" width = 48%>

这里我们为每个特征创建一个直方图，计算具有某一特征的数据点在特定范围内（叫作bin）的出现频率。每张图都包含两个直方图，一个是良性类别的所有点（蓝色），一个是恶性类别的所有点（红色）。这样我们可以了解每个特征在两个类别中的分布情况，也可以猜测哪些特征能够更好地区分良性样本和恶性样本。例如，“smoothness error”特征似乎没有什么信息量，因为两个直方图大部分都重叠在一起，而“worst concave points”特征看起来信息量相当大，因为两个直方图的交集很小。

但是，这种图无法向我们展示变量之间的相互作用以及这种相互作用与类别之间的关系。利用PCA，我们可以获取到主要的相互作用，并得到稍为完整的图像。我们可以找到前两个主成分，并在这个新的二维空间中用散点图将数据可视化。

在应用PCA之前，我们利用StandardScaler缩放数据，使每个特征的方差均为1：

```python
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
# PCA 之前需要预处理数据
scaler = StandardScaler()
scaler.fit(cancer.data)
X_scaled = scaler.transform(cancer.data)
```
学习并应用PCA 变换与应用预处理变换一样简单。我们将PCA 对象实例化，调用fit 方
法找到主成分，然后调用transform 来旋转并降维。默认情况下，PCA 仅旋转（并移动）
数据，但保留所有的主成分。为了降低数据的维度，我们需要在创建PCA 对象时指定想要
保留的主成分个数：

```python
from sklearn.decomposition import PCA 

# 保留数据的前两个主成分
pca = PCA(n_components=2)
pca.fit(X_scaled)

# 将数据变换到前两个主成分的方向上
X_pca = pca.transform(X_scaled)
print("Original shape: {}".format(str(X_scaled.shape)))     # Original shape: (569, 30)
print("Reduced shape: {}".format(str(X_pca.shape)))         # Reduced shape: (569, 2)
```

现在我们可以对前两个主成分作图：

```python
# 对第一个和第二个主成分作图，按类别着色
plt.figure(figsize=(8, 8))
mglearn.discrete_scatter(X_pca[:, 0], X_pca[:, 1], cancer.target)
plt.legend(cancer.target_names, loc="best")
plt.gca().set_aspect("equal")       # 设置两轴尺度相同
plt.xlabel("第一主成分")
plt.ylabel("第二主成分")
```
<img src ="https://img-blog.csdnimg.cn/ac1946a76b3640a0b9d2eedb8b7ac687.png#pic_center" width = 48%>
PCA 是一种无监督方法，在寻找旋转方向时没有用到任何类别信息。它只是观察数据中的相关性。对于这里所示的散点图，我们绘制了第一主成分与第二主成分的关系，然后利用类别信息对数据点进行着色。你可以看到，在这个二维空间中两个类别被很好地分离。这让我们相信，即使是线性分类器（在这个空间中学习一条直线）也可以在区分这个两个类别时表现得相当不错。我们还可以看到，恶性点比良性点更加分散，这一点也可以在图3-4 的直方图中看出来。

PCA 的一个缺点在于，通常不容易对图中的两个轴做出解释。主成分对应于原始数据中的方向，所以它们是原始特征的组合。但这些组合往往非常复杂，这一点我们很快就会看到。在拟合过程中，主成分被保存在PCA 对象的components_属性中：


```python
print("PCA component shape: {}".format(pca.components_.shape))      # PCA component shape: (2, 30)
```
components_ 中的每一行对应于一个主成分，它们按重要性排序（第一主成分排在首位，以此类推）。列对应于PCA 的原始特征属性，在本例中即为“mean radius” “mean texture”等。我们来看一下components_的内容：

```python
print("PCA components: \n {}".format(pca.components_))
```
我们还可以用热图将系数可视化，这可能更容易理解：
```python
plt.matshow(pca.components_, cmap='viridis')
plt.yticks([0, 1], ["第一成分", "第二成分"])
plt.colorbar()
plt.xticks(range(len(cancer.feature_names)),
           cancer.feature_names, rotation=60, ha='left')
plt.xlabel("特征")
plt.ylabel("主成分")
```
<img src ="https://img-blog.csdnimg.cn/109e00f1dc864342a1b0d49198499431.png#pic_center" width = 48%>

可以看到，在第一个主成分中，所有特征的符号相同（均为正，但前面我们提到过，箭头指向哪个方向无关紧要）。这意味着在所有特征之间存在普遍的相关性。如果一个测量值较大的话，其他的测量值可能也较大。第二个主成分的符号有正有负，而且两个主成分都包含所有30个特征。这种所有特征的混合使得解释上图中的坐标轴变得十分困难。

### 6.2 特征提取的特征脸
特征提取是一种数据表示，比原始表示更适合于分析。特征提取很有用，它的一个很好的应用实例就是图像。图像由像素组成，通常存储为红绿蓝（RGB）强度。图像中的对象通常由上千个像
素组成，它们只有放在一起才有意义。

我们将给出用PCA对图像做特征提取的一个简单应用，即处理Wild 数据集Labeled Faces（标记人脸）中的人脸图像。这一数据集包含从互联网下载的名人脸部图像，它包含从21世纪初开始的政治家、歌手、演员和运动员的人脸图像。我们使用这些图像的灰度版本，并将它们按比例缩小以加快处理速度。你可以在下图中看到其中一些图像：

```python
from sklearn.datasets import fetch_lfw_people

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
image_shape = people.images[0].shape

# 显示原始人脸照片
fix, axes = plt.subplots(2, 5, figsize=(15, 8), subplot_kw={'xticks': (), 'yticks': ()})
for target, image, ax in zip(people.target, people.images, axes.ravel()):
    ax.imshow(image)
    ax.set_title(people.target_names[target])
```

<img src ="https://img-blog.csdnimg.cn/6a877a36f5a54ea4b7d5c4beb40102d8.png#pic_center" width = 48%>

```python
print("people.images.shape: {}".format(people.images.shape))        # people.images.shape: (3023, 87, 65)
print("Number of classes: {}".format(len(people.target_names)))     # Number of classes: 62
```

但这个数据集有些偏斜，其中包含George W. Bush（小布什）和Colin Powell（科林• 鲍威尔）的大量图像，正如你在下面所见：

```python
# # 计算每个目标出现的次数
counts = np.bincount(people.target)
print("出现次数不少于二十的人脸")
print('{0:25} {1:6}'.format("姓名", "照片数目"))
# 将次数与目标一起打印出来
for i, (count, name) in enumerate(zip(counts, people.target_names)):
    print("{0:25} {1:6}".format(name, count), end='   ')
    if (i + 1) % 3 == 0:
        print()
```

<img src ="https://img-blog.csdnimg.cn/203cd5cccaca4074b3f4c10bcb3dfee2.png#pic_center" width = 48%>

为了降低数据偏斜，我们对每个人最多只取50张图像（否则，特征提取将会被George W. Bush 的可能性大大影响）：

```python
mask = np.zeros(people.target.shape, dtype=np.bool)
for target in np.unique(people.target):
    # 将每个人的前50条数据设置为1，方便取出
    mask[np.where(people.target == target)[0][:50]] = 1

X_people = people.data[mask]
y_people = people.target[mask]

# 将灰度值缩放到0到1之间，而不是在0到255之间，以得到更好的数据稳定性
X_people = X_people / 255.
```
人脸识别的一个常见任务就是看某个前所未见的人脸是否属于数据库中的某个已知人物。这在照片收集、社交媒体和安全应用中都有应用。解决这个问题的方法之一就是构建一个分类器，每个人都是一个单独的类别。但人脸数据库中通常有许多不同的人，而同一个人的图像很少（也就是说，每个类别的训练样例很少）。这使得大多数分类器的训练都很困难。另外，通常你还想要能够轻松添加新的人物，不需要重新训练一个大型模型。

一种简单的解决方法是使用单一最近邻分类器，寻找与你要分类的人脸最为相似的人脸。这个分类器原则上可以处理每个类别只有一个训练样例的情况。下面看一下KNeighborsClassifier的表现如何：

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X_people, y_people, stratify=y_people, random_state=0)

# 使用 1 个邻居的 K近邻分类器
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("原始数据经过KNN训练后测试集的精度： {:.2f}".format(knn.score(X_test, y_test)))
# 原始数据经过KNN训练后测试集的精度： 0.27
```
得到的精度为26.6%。对于包含62个类别的分类问题来说，这实际上不算太差（随机猜测的精度约为1/62=1.5%），但也不算好。我们每识别四次仅正确识别了一个人。

这里就可以用到PCA。想要度量人脸的相似度，计算原始像素空间中的距离是一种相当糟糕的方法。用像素表示来比较两张图像时，我们比较的是每个像素的灰度值与另一张图像对应位置的像素灰度值。这种表示与人们对人脸图像的解释方式有很大不同，使用这种原始表示很难获取到面部特征。例如，如果使用像素距离，那么将人脸向右移动一个像素将会发生巨大的变化，得到一个完全不同的表示。我们希望，使用沿着主成分方向的距离可以提高精度。这里我们启用PCA的白化（whitening）选项，它将主成分缩放到相同的尺度。变换后的结果与使用StandardScaler相同。再次使用上图的数据，白化不仅对应于旋转数据，还对应于缩放数据使其形状是圆形而不是椭圆：

```python
# 白化（whitening）或者球面化(sphered)：变换后的向量 $\mathbfb{z}=[z_1,\cdots,z_n]^T$ 是零均值、单位方差，并且元素$z_i$是不相关的 $E{z_i z_j}=\delta_{ij}$
# StandScaler 变换后的信号为零均值、单位方差，但是不保证信号之间不相关，即不保证信号分布为圆形，但是可以保证信号分布为椭圆形
# 零均值、单位方差的多元高斯密度是符合白化标准的；反之则不成立，因为球面微量的密度不一定是径向对称的
mglearn.plots.plot_pca_whitening()
```
<img src ="https://img-blog.csdnimg.cn/49039149a9ce4d85939845e1e775af55.png#pic_center" width = 48%>

我们对训练数据拟合PCA对象，并提取前100个主成分。然后对训练数据和测试数据进行变换：

```python
pca = PCA(n_components=100, whiten=True, random_state=0).fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

print("X_train_pca.shape: {}".format(X_train_pca.shape))
# X_train_pca.shape: (1547, 100)
```

新数据有100个特征，即前100 个主成分。现在，可以对新表示使用单一最近邻分类器来将我们的图像分类：
```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_pca, y_train)
print("测试集精度： {:.2f}".format(knn.score(X_test_pca, y_test)))      # 测试集精度： 0.36
```
我们的精度有了相当显著的提高，从26.6%提升到35.7%，这证实了我们的直觉，即主成分可能提供了一种更好的数据表示。

对于图像数据，我们还可以很容易地将找到的主成分可视化。请记住，成分对应于输入空间里的方向。这里的输入空间是87像素×65像素的灰度图像，所以在这个空间中的方向也是87像素×65像素的灰度图像。

我们来看一下前几个主成分
```python
print("pca.components_.shape: {}".format(pca.components_.shape))
# pca.components_.shape: (100, 5655)
```


```python
fig, axes = plt.subplots(3, 5, figsize=(15, 12),subplot_kw={'xticks': (), 'yticks': ()})
for i, (component, ax) in enumerate(zip(pca.components_, axes.ravel())):
    ax.imshow(component.reshape(image_shape),cmap='viridis')
    ax.set_title("{}. component".format((i + 1)))
```

<img src ="https://img-blog.csdnimg.cn/72d05a66c4d743ce861f7c83a01f9f78.png#pic_center" width = 48%>

虽然我们肯定无法理解这些成分的所有内容，但可以猜测一些主成分捕捉到了人脸图像的哪些方面。第一个主成分似乎主要编码的是人脸与背景的对比，第二个主成分编码的是人脸左半部分和右半部分的明暗程度差异，如此等等。虽然这种表示比原始像素值的语义稍强，但它仍与人们感知人脸的方式相去甚远。由于PCA 模型是基于像素的，因此人脸的相对位置（眼睛、下巴和鼻子的位置）和明暗程度都对两张图像在像素表示中的相似程度有很大影响。但人脸的相对位置和明暗程度可能并不是人们首先感知的内容。在要求人们评价人脸的相似度时，他们更可能会使用年龄、性别、面部表情和发型等属性，而这些属性很难从像素强度中推断出来。重要的是要记住，算法对数据（特别是视觉数据，比如人们非常熟悉的图像）的解释通常与人类的解释方式大不相同。


不过让我们回到PCA 的具体案例。我们对PCA变换的介绍是：先旋转数据，然后删除方差较小的成分。另一种有用的解释是尝试找到一些数字（PCA旋转后的新特征值），使我们可以将测试点表示为主成分的加权求和。
<img src ="https://img-blog.csdnimg.cn/2888bdc80b3442779090c71d47a7fbab.png#pic_center" width = 48%>

我们还可以用另一种方法来理解PCA模型，就是仅使用一些成分对原始数据进行重建。在下图中，在去掉第二个成分并来到第三张图之后，我们反向旋转并重新加上平均值，这样就在原始空间中获得去掉第二个成分的新数据点，正如最后一张图所示。我们可以对人脸做类似的变换，将数据降维到只包含一些主成分，然后反向旋转回到原始空间。回到原始特征空间可以通过inverse_transform 方法来实现。这里我们分别利用10个、50个、100个和500个成分对一些人脸进行重建并将其可视化：
```python
mglearn.plots.plot_pca_faces(X_train, X_test, image_shape)
```

<img src ="https://img-blog.csdnimg.cn/856a6c17c8334d10960c57d5db350692.png#pic_center" width = 48%>

可以看到，在仅使用前10个主成分时，仅捕捉到了图片的基本特点，比如人脸方向和明暗程度。随着使用的主成分越来越多，图像中也保留了越来越多的细节。这对应于下图的求和中包含越来越多的项。如果使用的成分个数与像素个数相等，意味着我们在旋转后不会丢弃任何信息，可以完美重建图像。

我们还可以尝试使用PCA的前两个主成分，将数据集中的所有人脸在散点图中可视化，其类别在图中给出。

```python
mglearn.discrete_scatter(X_train_pca[:, 0], X_train_pca[:, 1], y_train)
plt.xlabel('第一个主成分')
plt.ylabel('第二个主成分')
```
<img src ="https://img-blog.csdnimg.cn/7dc6b7fa5783437989c5d781f3144399.png#pic_center" width = 48%>


如你所见，如果我们只使用前两个主成分，整个数据只是一大团，看不到类别之间的分
界。这并不意外，因为即使有10个成分，PCA 也仅捕捉到人脸非常粗略的特征。

____

小结：
作为一个非监督学习的降维方法，它只需要特征值分解，就可以对数据进行压缩，去噪。因此在实际场景应用很广泛。为了克服PCA的一些缺点，出现了很多PCA的变种，比如为解决非线性降维的KPCA，还有解决内存限制的增量PCA方法Incremental PCA，以及解决稀疏数据降维的PCA方法Sparse PCA、解决异常值的Stable Principle Component Pursuit (SPCP)等。

PCA算法的主要优点有：
- 仅仅需要以方差衡量信息量，不受数据集以外的因素影响。
- 各主成分之间正交，可消除原始数据成分间的相互影响的因素。
- 计算方法简单，主要运算是特征值分解，易于实现。
PCA算法的主要缺点有：
- 主成分各个特征维度的含义具有一定的模糊性，不如原始样本特征的解释性强。
- 方差小的非主成分也可能含有对样本差异的重要信息，因降维丢弃可能对后续数据处理有影响。

____

### 参考

- A tutorial on Principal Components Analysis：[https://faculty.iiit.ac.in/~mkrishna/PrincipalComponents.pdf](https://faculty.iiit.ac.in/~mkrishna/PrincipalComponents.pdf)
- A Tutorial on Principal Component Analysis. Derivation, Discussion and Singular Value Decomposition：
  [https://cis.temple.edu/~latecki/Courses/AI-Fall10/Lectures/PCA-Tutorial-Intuition.pdf](https://cis.temple.edu/~latecki/Courses/AI-Fall10/Lectures/PCA-Tutorial-Intuition.pdf)
- 降维之奇异值分解(SVD)：[https://www.cnblogs.com/XMU-hcq/p/6353698.html](https://www.cnblogs.com/XMU-hcq/p/6353698.html)
- 【机器学习】降维——PCA（非常详细）：[https://zhuanlan.zhihu.com/p/77151308](https://zhuanlan.zhihu.com/p/77151308)
- 如何理解主元分析（PCA）：[https://www.matongxue.com/madocs/1025/](https://www.matongxue.com/madocs/1025/)
- 主成分分析(PCA)原理总结：[https://www.cnblogs.com/pinard/p/6239403.html](https://www.cnblogs.com/pinard/p/6239403.html)
- 主成分分析：[https://gitee.com/ni1o1/pygeo-tutorial/blob/master/12-.ipynb](https://gitee.com/ni1o1/pygeo-tutorial/blob/master/12-.ipynb)
- PCA 理论分析及应用：[http://lanbing510.info/public/file/posts/pca.doc](https://view.officeapps.live.com/op/view.aspx?src=http://lanbing510.info/public/file/posts/pca.doc&wdOrigin=BROWSELINK)
