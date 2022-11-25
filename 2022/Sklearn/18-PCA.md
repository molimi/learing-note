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
