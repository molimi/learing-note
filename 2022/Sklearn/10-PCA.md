## 1 引言

降维是对数据高维度特征的一种预处理方法。降维是将高维度的数据保留下最重要的一些特征，去除噪声和不重要的特征，从而实现提升数据处理速度的目的。在实际的生产和应用中，降维在一定的信息损失范围内，可以为我们节省大量的时间和成本。降维也成为了应用非常广泛的数据预处理方法。

　　降维具有如下一些优点：

（1）使得数据集更易使用

（2）降低算法的计算开销

（3）去除噪声

（4）使得结果容易理解

PCA（Principal Component Analysis） 是一种常见的数据分析方式，常用于高维数据的降维，可用于提取数据的主要特征分量。

PCA 的数学推导可以从最大可分型和最近重构性两方面进行，前者的优化条件为划分后方差最大，后者的优化条件为点到划分平面距离最小，这里我将从最大可分性的角度进行证明。

初学者建议先阅读这份教程，英文好的可以直接阅读[原文文献](https://faculty.iiit.ac.in/~mkrishna/PrincipalComponents.pdf)，其他小伙伴可以参考：[A tutorial on Principal Components Analysis | 主成分分析（PCA）教程](https://www.cnblogs.com/XMU-hcq/p/6353698.html)

奇异值分解，可以参考这份教程，英文好的可以直接阅读[原文文献](https://cis.temple.edu/~latecki/Courses/AI-Fall10/Lectures/PCA-Tutorial-Intuition.pdf)，其他的小伙伴可以参考：[A Tutorial on Principal Component Analysis(译)](https://blog.csdn.net/zhouchangyu1221/article/details/103949967)

PCA是将数据投影到方差最大的几个相互正交的方向上，以期待保留最多的样本信息。样本的方差越大表示样本的多样性越好，在训练模型的时候，我们当然希望数据的差别越大越好。否则即使样本很多但是他们彼此相似或者相同，提供的样本信息将相同，相当于只有很少的样本提供信息是有用的。样本信息不足将导致模型性能不够理想。这就是PCA降维的目的：将数据投影到方差最大的几个相互正交的方向上。这种约束有时候很有用，比如在下面这个例子：

<img src="https://img-blog.csdnimg.cn/199995b5ae14494586dcf5b01cfd7dc2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" width=36%>

　对于这个样本集我们可以将数据投影到 x 轴或者 y 轴，但这都不是最佳的投影方向，因为这两个方向都不能最好的反映数据的分布。很明显还存在最佳的方向可以描述数据的分布趋势，那就是图中红色直线所在的方向。也是数据样本作投影，方差最大的方向。向这个方向做投影，投影后数据的方差最大，数据保留的信息最多。

## 2 PCA的思想
PCA顾名思义，就是找出数据里最主要的方面，用数据里最主要的方面来代替原始数据。具体的，假如我们的数据集是n维的，共有m个数据(x(1),x(2),...,x(m))。我们希望将这m个数据的维度从n维降到n'维，希

## 3 PCA的推导：基于最小投影距离

## 4 PCA的推导：基于最大投影方差

## 5 PCA算法流程

## 6 PCA实例

## 7 核主成分分析KPCA介绍


## 8 sklearn实现
### 8.1 对cancer数据集应用PCA并进行可视化

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

```python
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
# PCA 之前需要预处理数据
scaler = StandardScaler()
scaler.fit(cancer.data)
X_scaled = scaler.transform(cancer.data)
```

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

```python
print("PCA component shape: {}".format(pca.components_.shape))      # PCA component shape: (2, 30)
```

```python
print("PCA components: \n {}".format(pca.components_))
```



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

### 8.2 特征提取的特征脸
特征提取是一种数据表示，比原始表示更适合于分析。
例如：提取的特征脸是脸部照片中变化最大的地方，即人脸的细节，那些细节代表着光影变化较大的地方，比如：轮廓、皱纹等等
某些类别的数据过多，会导致数据偏斜，可以通过限制每个类别的数据量来解决



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
print("people.images.shape: {}".format(people.images.shape))        # people.images.shape: (2749, 87, 65)
print("Number of classes: {}".format(len(people.target_names)))     # Number of classes: 52
```

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

```python
# 白化（whitening）或者球面化(sphered)：变换后的向量 $\mathbfb{z}=[z_1,\cdots,z_n]^T$ 是零均值、单位方差，并且元素$z_i$是不相关的 $E{z_i z_j}=\delta_{ij}$
# StandScaler 变换后的信号为零均值、单位方差，但是不保证信号之间不相关，即不保证信号分布为圆形，但是可以保证信号分布为椭圆形
# 零均值、单位方差的多元高斯密度是符合白化标准的；反之则不成立，因为球面微量的密度不一定是径向对称的
mglearn.plots.plot_pca_whitening()
```
<img src ="https://img-blog.csdnimg.cn/49039149a9ce4d85939845e1e775af55.png#pic_center" width = 48%>


```python
pca = PCA(n_components=100, whiten=True, random_state=0).fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

print("X_train_pca.shape: {}".format(X_train_pca.shape))
# X_train_pca.shape: (1341, 100)
```


```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_pca, y_train)
print("测试集精度： {:.2f}".format(knn.score(X_test_pca, y_test)))      # 测试集精度： 0.35
```


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


```python
mglearn.plots.plot_pca_faces(X_train, X_test, image_shape)
```

<img src ="https://img-blog.csdnimg.cn/856a6c17c8334d10960c57d5db350692.png#pic_center" width = 48%>

```python
mglearn.discrete_scatter(X_train_pca[:, 0], X_train_pca[:, 1], y_train)
plt.xlabel('第一个主成分')
plt.ylabel('第二个主成分')
```
<img src ="https://img-blog.csdnimg.cn/7dc6b7fa5783437989c5d781f3144399.png#pic_center" width = 48%>




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
