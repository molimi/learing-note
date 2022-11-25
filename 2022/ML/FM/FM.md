### 1 背景
#### 1.1 LR模型方程
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于监督学习，机器学习模型的预测是一个估计函数$\hat{y}$（映射$F$）
$$\hat{y}=F:\pmb{X}\to y\tag{1}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$\pmb{X}$属于$n$维特征向量，即$\pmb{X} \in\mathbb{R}^{n}$，$y$属于目标值，回归问题中$y\in \mathbb{R}$，二分类问题中$y\in\{ -1,+1 \}$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们首先回顾一般的线性回归方程`LR`，对于输入任意一个$n$维特征向量$\pmb{X} = (x_{1}, x_{2}, \cdots, x_{n})$，建模估计函数$\hat{y}(\pmb{X})$为
$$\hat y(\pmb{X}) = w_0 + \sum_{i=1}^{n}w_ix_i\tag{2}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LR模型的参数为：$w_{0} \in \mathbb{R}$，$w \in  \mathbb{R^{n}} = (w_{1}, w_{2}, \cdots, w_{n})$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从LR模型方程中我们可以看到：
> （1）各个特征分量$x_{i}和x_{j}(i \neq j)$彼此之间是独立的
> 
> （2）$\hat{y}(\pmb{X})$将单个特征分量线性的组合起来，却忽略了特征分量彼此之间的相互组合关系

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于特征的组合关系，我们定义：
>（1）一阶特征：即单个特征，不产生新特征，如$x_{1}$
>
>（2）二阶特征：即两个特征组合产生的新特征，如$x_{1}x_{2}$
>
>（3）高阶特征：即两个以上的特征组合产生的新特征，如$x_{1}x_{2}x_{3}$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上可知，<font color=#9900CC><strong>`LR`模型只考虑了一阶特征的线性组合关系。</font></strong>

#### 1.2  多项式模型方程
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了克服模型欠缺二阶特征组合因素，我们将`LR`模型改写为二阶多项式模型
$$\hat{y}(\pmb{X})=w_0\sum_{i=1}^{n}w_ix_i+\sum_{i=1}^{n-1}\sum_{j=i+1}^nw_{ij}x_ix_j\tag{3}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$x_ix_j$表示两个互异特征组合的二阶特征，$w_{ij}$表示二阶特征的交叉项系数

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;至此，该模型似乎已经加入了特征组合的因素，接下来只要学习参数即可

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;但是，上述二阶多项式模型却有一个致命的缺陷：

> 数据稀疏性普遍存在的实际应用场景中，二阶特征系数$w_{ij}$的训练是很困难的

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;造成学习困难的原因是：
>（1）$w_{ij}$的学习需要大量特征分量$x_{i}$和$x_{j}$都非零的样本
>
>（2）样本本身是稀疏的，同时满足$x_{i}x_{j} \neq 0$的样本非常稀少

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上，<font color=#9900CC><strong>多项式模型虽然加入了二阶特征组合，却受到数据稀疏的影响。</strong></font>

#### 1.3 FM模型方程
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了克服模型无法在稀疏数据场景下学习二阶特征系数$w_{ij}$，我们需要将$w_{ij}$表示为另外一种形式

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为此，针对样本$\pmb{X}$的第i维特征分量$x_{i}$，引入辅助隐向量$\pmb{v}_{i}$
$$\pmb{v}_i=(v_{i1}, v_{i2}, \cdots, v_{ik})^T\in\mathbb{R}^k\tag{4}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$k$为超参数，表示特征分量$x_{i}$对应一个$k$维隐向量$\pmb{v}_{i}$，则将$w_{ij}$表示为：
$$\hat{w}_{ij}=\pmb{v}_i^T\pmb{v}_j=<\pmb{v}_i, \pmb{v}_j>=\sum_{f=1}^{k}v_{if}v{jf}\tag{5}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上式引入隐向量的含义为：二阶特征系数$w_{ij}$等价于：特征分量$x_{i}$和$x_{j}$对应的隐向量$\pmb{v}_{i}$和$\pmb{v}_{j}$的内积$<\pmb{v}_{i}, \pmb{v}_{j}>$，这就是`FM`模型的核心思想

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则我们将二阶多项式模型改写为`FM`模型：
$$\tilde{y}(x)=w_{0}+\sum_{i=1}^{n}{w_{i}x_{i}}+\sum_{i=1}^{n-1}{\sum_{j=i+1}^{n}{<\pmb{v}_{i},\pmb{v}_{j}>x_{i}x_{j}}} \tag{6}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从FM模型方程可知，FM模型的参数为：
$w_0\in\mathbb{R}, \pmb{w}\in\mathbb{R}^n, \pmb{V}\in\mathbb{R}^{n\times k}$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;各个参数的含义为：
> （1）$w_0\in\mathbb{R}$表示FM模型的偏置
> 
> （2）$\pmb{w}\in\mathbb{R}^n$表示FM模型对一阶特征的建模
> 
> （3）$\pmb{V}\in\mathbb{R}^{n\times k}$表示FM模型对二阶特征的建模
参数的个数为：1+n+nk
模型的复杂度为：$O(n^2k)$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对比(3)式和(6)式可知，交叉项$x_ix_j$的系数，前者用的是$w_{ij}$，后者用的是$\hat{w}_{ij}$，为了弄清二者之间的关系，引入几个矩阵。

(1)每个特征$x_{i}$对应的隐向量$\pmb{v}_{i}$组成的矩阵$\pmb{V}$：
$$\pmb{V}=\begin{bmatrix}\pmb{v}_1^T \\ \pmb{v}_2^T \\ \vdots \\\pmb{v}_n^T\end{bmatrix} = \begin{bmatrix} v_{11} & v_{12} & \cdots & v_{1k}\\  v_{21} & v_{22} & \cdots & v_{2k}\\ \vdots & \vdots & \vdots & \vdots\\  v_{n1} & v_{n2} & \cdots & v_{nk}\end{bmatrix}_{n\times k} \tag{7}$$
(2)多项式模型的二阶特征系数$w_{ij}$组成的交互方阵$\pmb{W}$
$$\pmb{W}= \begin{bmatrix} w_{11} & w_{12} & \cdots & w_{1n}\\  w_{21} & w_{22} & \cdots & w_{2n}\\ \vdots & \vdots & \vdots & \vdots\\  w_{n1} & w_{n2} & \cdots & w_{nn}\end{bmatrix}_{n\times n} \tag{8}$$
(3) `FM`模型的二阶特征系数$<\pmb{v}_{i}, \pmb{v}_{j}>$组成的方阵$\hat{\pmb{W}}$ 
$$\begin{aligned} \hat{\pmb{W}}&=\pmb{V}\times\pmb{V}^T=\begin{bmatrix}\pmb{v}_1^T \\ \pmb{v}_2^T \\ \vdots \\\pmb{v}_n^T\end{bmatrix}\times\begin{bmatrix}\pmb{v}_1 & \pmb{v}_2 & \cdots & \pmb{v}_n\end{bmatrix}\\&= \begin{bmatrix}\pmb{v}_1^T\pmb{v}_1 & \pmb{v}_1^T\pmb{v}_2 & \cdots & \pmb{v}_1^T\pmb{v}_n \\ \pmb{v}_2^T\pmb{v}_1 & \pmb{v}_2^T\pmb{v}_2 & \cdots & \pmb{v}_2^T\pmb{v}_n \\ \vdots & \vdots & \vdots & \vdots\\ \pmb{v}_n^T\pmb{v}_1 & \pmb{v}_n^T\pmb{v}_2 & \cdots & \pmb{v}_n^T\pmb{v}_n \end{bmatrix}_{n\times n} \\&=\begin{bmatrix}\pmb{v}_1^T\pmb{v}_1 & \hat{w}_{12} & \cdots & \hat{w}_{1n} \\ \hat{w}_{21} & \pmb{v}_2^T\pmb{v}_2 & \cdots & \hat{w}_{2n}\\ \vdots & \vdots & \vdots & \vdots\\ \hat{w}_{n1} & \hat{w}_{n2} & \cdots & \pmb{v}_n^T\pmb{v}_n \end{bmatrix}_{n\times n}\end{aligned}\tag{9}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从上面三个矩阵，我们可以看到：
（1）方阵$\pmb{W}$的非对角线上三角的元素，即为多项式模型的二阶特征系数：$w_{ij}$
（2）方阵$\hat{\pmb{W}}$的非对角线上三角的元素，即为`FM`模型的二阶特征系数：$<v_{i}, v_{j}>$
由于$\hat{\pmb{W}}=\pmb{V}\pmb{V}^T$，即隐向量矩阵的相乘结果，这是一种矩阵分解的方法

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;引用线性代数中的结论：当$k$足够大时，对于任意对称正定的实矩阵$\hat{\pmb{W}}\in\mathbb{R}^{n\times n}$，均存在实矩阵$\pmb{V}\in\mathbb{R}^{n\times k}$，使得$\hat{\pmb{W}}=\pmb{V}\times\pmb{V}^T$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所以`FM`模型需要保证的正定性。由于`FM`只关心互异特征之间的关系（$i>j$），因此$\hat{\pmb{W}}$的对角线元素可以任意取值，只需将它们取足够大（保证行元素严格对角占优），就可以保证$\hat{\pmb{W}}$的正定性。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;理论分析中，我们要求参数$k$取得足够大，但是，在高度稀疏数据场景中，由于没有足够的样本来估计复杂的交互矩阵，因此$k$通常应取得很小。事实上，对参数$k$(亦即`FM`的表达能力)的限制，在一定程度上可以提高模型的泛化能力。这种能够利用$\hat{\pmb{W}}$的低秩近似的性质也是`FM`的一个优势。

#### 1.4 模型化简
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从上述`FM`模型方程看，模型的复杂度的确是：$O(n^2k)$，但我们通过一些技巧可以化简模型的二阶系数项，如下：
$$\begin{aligned} &\sum_{i=1}^{n}{\sum_{j=i+1}^{n}{<v_{i},v_{j}>x_{i}x_{j}}} \\ &=\frac{1}{2}\sum_{i=1}^{n}{\sum_{j=1}^{n}{<v_{i},v_{j}>x_{i}x_{j}}}-\frac{1}{2}\sum_{i=1}^{n}{<v_{i},v_{i}>x_{i}x_{i}} \\ &=\frac{1}{2}(\sum_{i=1}^{n}{\sum_{j=1}^{n}{\sum_{f=1}^{k}{v_{i,f}v_{j,f}x_{i}x_{j}}}}-\sum_{i=1}^{n}{\sum_{f=1}^{k}{v_{i,f}v_{i,f}x_{i}x_{i}}}) \\ &=\frac{1}{2}\sum_{f=1}^{k}{((\sum_{i=1}^{n}{v_{i,f}x_{i}})(\sum_{j=1}^{n}{v_{j,f}x_{j}})-\sum_{i=1}^{n}{v_{i,f}^2x_{i}^2})} \\ &=\frac{1}{2}\sum_{f=1}^{k}{((\sum_{i=1}^{n}{v_{i,f}x_{i}})^2-\sum_{i=1}^{n}{v_{i,f}^2x_{i}^2})} \end{aligned} \tag{10}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对上述化简过程做一些解释：
- 第1个等号：对称方阵$\hat{\pmb{W}}$的所有元素之和减去主对角线元素之和
- 第2个等号：$<v_{i}, v_{j}>$向量内积展开成累加形式
- 第3个等号：提出公共部分$\sum_{f=1}^{k}$
- 第4个等号：表示为“和平方”减去“平方和”

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将式子(10)的化简结果代入式子(6)，可以得到：
$$\begin{aligned} y = w_0+\sum_{i=1}^nw_ix_i+\frac{1}{2}*\sum_{f=1}^{k}\left\{\left(\sum_{i=1}^{n}v_{if}x_i\right)^{2}-\sum_{i=1}^{n}v_{if}^{2}x_{i}^2\right\} \end{aligned} \tag{11}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看到通过数学上的化简，参数个数为：$1+n+kn$，模型的复杂度为：$O(kn)$，`FM`模型的复杂度降低到了线性级别

#### 1.5 损失函数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;利用`FM`模型方程，可以进行各种机器学习预测的任务，包括：
- Regression：$\hat{y}(x)$可以直接用作预测，并且最小平方误差来优化。
- Binary classification：$\hat{y}(x)$作为目标函数并且使用`hinge loss`或者`logit loss`来优化。
- Ranking：向量$\pmb{x}$通过$\hat{y}(x)$的分数排序，并且通过pairwise的分类损失来优化成对的样本$(x^{(a)}, x^{(b)})$
对以上的任务中，正则化项参数一般加入目标函数中以防止过拟合。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于回归问题，损失函数可以取最小平方误差函数
$$loss(\hat{y},y)=\frac{1}{2}(\hat{y}-y)^2\tag{12}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于分类问题，损失函数可以取`logit`逻辑函数
$$loss(\hat{y},y)=log(1+e^{-\hat{y}y})\tag{13}$$

#### 1.6 目标函数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过损失函数构造出目标函数为
$$obj=\sum_{i=1}^{N}loss(\hat{y}_i,y_i)\tag{14}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中包含具体的损失函数`loss`和估计函数$\hat{y}(X)$。这里$\hat{y}$即`FM`模型方程，损失函数`loss`可以带入具体的可导函数（如`logit`函数）即可。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;最优化目标函数，即最优化模型方程的参数，即转化为下面最优化问题
$$\theta^*=argmin \sum_{i=1}^{N}loss(\hat{y}_i,y_i)\tag{15}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;目标函数对模型参数的偏导数通式为：
$$\frac{\partial}{\partial \theta}loss(\hat{y}_i,y_i)=\frac{\partial loss(\hat{y}_i,y_i)}{\partial \hat{y}_i}\frac{\partial \hat{y}_i}{\partial \theta}\tag{16}$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于$R^2$和或`logit`作为损失函数而言，`loss`对模型估计函数$\hat{y}(X)$的偏导数为：
$$\frac{\partial loss(\hat{y}_i,y_i)}{\partial \hat{y}_i}=\begin{cases}\hat{y}_i-y_i\qquad & loss=\frac{1}{2}(\hat{y}_i-y_i)^2 \\ \frac{-y_i}{1+e^{\hat{y}_iy_i}}\qquad & loss=log(1+e^{-\hat{y}_iy_i})\end{cases}\tag{17}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于`FM`模型而言，优化的参数为：$\theta^{*} = \{w_{0}, \pmb{w}, \pmb{V}\}$，则`FM`模型方程对各个参数$\theta^{*}$的偏导数为：
$$\frac{\partial{\hat{y}_i}}{\partial{\theta}} =  \begin{cases} 1, & \text{if } \theta \text{ is } w_0; \\ x_i, & \text{if } \theta \text{ is } w_i; \\ x_i\sum_{j=1}^{n}(v_{jf}x_j)-x_{i}^2v_{if}, & \text{if } \theta \text{ is } v_{if}. \end{cases}\tag{18}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;于是对于`FM`模型的优化问题，我们可以采用`SGD`优化目标函数

#### 1.7 优化算法




#### 1.8 总结
_____

**补充：**

对称矩阵上三角求和，设矩阵为$\pmb{M}$：
$$M=\left( 	\begin{matrix} 	m_{11} & m_{12} & \cdots & m_{1n} \\ 	m_{21} & m_{22} & \cdots & m_{1n} \\ 	\vdots & \vdots & \ddots & \vdots \\ 	m_{n1} & m_{n2} & \cdots & m_{nn} \\ 	\end{matrix} \right)_{n*n}\tag{19}$$
其中，$m_{ij}=m_{ji}$
令上三角元素和为$\pmb{A}$，即$\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}m_{ij}=A$，那么，$\pmb{M}$的所有元素之和等于$2*\pmb{A}+tr(\pmb{M})$，$tr(\pmb{M})$为矩阵的迹。
$$\sum_{i=1}^n\sum_{j=1}^nm_{ij}=2*\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}m_{ij} + \sum_{i=1}^{n}m_{ii}\tag{20}$$
于是，可以得到：
$$A=\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}m_{ij}=\frac{1}{2}*\left\{\sum_{i=1}^n\sum_{j=1}^nm_{ij}-\sum_{i=1}^{n}m_{ii}\right\}\tag{21}$$

当参数为$v_{if}$时，只需要关注模型高阶项，当计算参数$v_{if}$的梯度时，其余无关参数可看做常数。
$$\begin{aligned} \frac{\partial{y}}{\partial{v_{if}}} ={} & \partial{\frac{1}{2}\left\{\left(\sum_{i=1}^{n}v_{if}x_i\right)^{2}-\sum_{i=1}^{n}v_{if}^{2}x_{i}^2\right\}}/\partial{v_{if}}  \\ ={} & \frac{1}{2}* \left\{ \frac{ 	\partial{ 		\left\{ \sum_{i=1}^{n}v_{if}x_i 		\right\}^2 	} }{\partial{v_{if}}} - \frac{ 	\partial{ 		\left\{ 			\sum_{i=1}^{n}v_{if}^{2}x_{i}^2 		\right\} 	} }{\partial{v_{if}}} \right\}  \\ \end{aligned} \tag{22}$$
其中，
$$\frac{ 	\partial{ 		\left\{ 			\sum_{i=1}^{n}v_{if}^{2}x_{i}^2 		\right\} 	} }{\partial{v_{if}}} =  2x_{i}^2v_{if} \tag{23}$$
令$\lambda=\sum_{i=1}^{n}v_{if}x_i$，则：
$$\begin{aligned} \frac{ 	\partial{ 		\left\{ \sum_{i=1}^{n}v_{if}x_i 		\right\}^2 	} }{\partial{v_{if}}} ={} & \frac{\partial{\lambda^2}}{\partial{v_{if}}}  \\ ={} & \frac{\partial{\lambda^2}}{\partial{\lambda}} \frac{\partial{\lambda}}{\partial{v_{if}}}  \\ ={} & 2\lambda*\frac{\partial{\sum_{i=1}^{n}v_{if}x_i}}{\partial{v_{if}}}  \\ ={} & 2\lambda*x_i  \\ ={} & 2*x_i*\sum_{j=1}^{n}v_{jf}x_j  \\ \end{aligned} \tag{24}$$
结合公式（22~24），可得：
$$\frac{\partial{y}}{\partial{v_{if}}} = x_i\sum_{j=1}^{n}v_{jf}x_j-x_{i}^2v_{if}  \tag{25}$$

___

### 参考
- Factorization Machines：[https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)
- FM模型的算法思想：[https://www.jianshu.com/p/8d792422e582](https://www.jianshu.com/p/8d792422e582)
- Factorization Machines 学习笔记：[https://blog.csdn.net/itplus/article/details/40534885?spm=1001.2014.3001.5501](https://blog.csdn.net/itplus/article/details/40534885?spm=1001.2014.3001.5501)
- 因子分解机（Factorization Machine）详解：[https://blog.csdn.net/lijingru1/article/details/88623136](https://blog.csdn.net/lijingru1/article/details/88623136)
- FM理论与实践：[https://zhuanlan.zhihu.com/p/89639306](https://zhuanlan.zhihu.com/p/89639306)