&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本篇主要用来学习使用，阈值函数包括软阈值和硬阈值的介绍及求解，详细内容可以参考文后文章。

## 1 硬阈值(Hard Thresholding)函数   
### 1.1 硬阈值(Hard Thresholding)函数的符号
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;硬阈值(Hard Thresholding)并没有软阈值(Soft Thresholding)那么常见，这可能是因为硬阈值解决的问题是非凸的原因吧。硬阈值与软阈值由同一篇文献提出，硬阈值公式参见文献【1】的式(11)：
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803150915186" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第一次邂逅硬阈值(HardThresholding)是在文献【2】中：

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803150924840" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在查询软阈值(Soft Thresholding)的过程中，搜到了文献【3】，进而看到了提到了文献【4】：

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803150937090" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;文献【4】中提到的Fig 1如图所示：

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803150945465" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;硬阈值的符号到底表示什么意思呢？以文献【1】符号为例，清晰一点来说就是这样的：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这里$w$是变量，$\lambda$是阈值。

### 1.2 硬阈值(HardThresholding)函数的作用

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;弄清楚了硬阈值(HardThresholding)的符号表示以后，接下来说一说它的作用。这里主要是参考了软阈值的推导过程，然后作者经过一番琢磨和推导而得。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;硬阈值(HardThresholding)可以求解如下优化问题：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中：
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151051532" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是求向是向量$X$的零范数，即向量$X$中非零元素的个数。根据范数的定义，可以将上面优化问题的目标函数拆开：

<p style="text-align:center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151102188" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中拆分项中符号$|x|_0$的意思是
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151120528" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;现在，我们可以通过求解$N$个独立的形如函数

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151132372" alt=""></span></p> 
<p><span style="font-family:Times New Roman">的优化问题，来求解这个问题。将<em>f</em>(<em>x</em>)进一步写为：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151141981" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于$x\not=0$部分，我们知道它的最小值在$x=b$处取得，最小值为$λ$。现在的问题是$λ$与$b^2$到底谁更小？最小者将是函数的最小值。求解不等式$b^2>λ$可得

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151152575" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时最小值在$x=0$处取得；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;求解不等式$b^2<λ$可得

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151204982" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时最小值在$x=b$处取得；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此

<p align="center"><img src="https://img-blog.csdn.net/20160806104022747" alt=""><br> </p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;与前面的硬阈值(Hard Thresholding)对比一下，发现了么？若将上式中的b视为变量，`sqrt(λ)`视为阈值，上式即为硬阈值(Hard Thresholding)的公式。

至此，我们可以得到优化问题

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151037340" alt=""></span></p> 
<p><span style="font-family:Times New Roman">的解为</span></p> 

<p align="center"><img src="https://img-blog.csdn.net/20160806104026410" alt=""><br> </p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**注：** 该式为硬阈值(Hard Thresholding)的矩阵形式，这里的$B$是一个向量，应该是逐个元素分别执行硬阈值函数。

### 1.3 硬阈值(HardThresholding)的变形

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当优化问题变为
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151323034" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因为对目标函数乘一个常系数不影响极值点的获得，所以可等价为优化问题

<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151335482" alt=""></span></p> 
<p><span style="font-family:Times New Roman">此时的解为<img src="https://img-blog.csdn.net/20160803151628039" alt="">。</span></p> 

### 1.4 硬阈值(Hard Thresholding)的MATLAB代码

<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>硬阈值(Hard Thresholding)的函数代码可以写成专门针对优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151037340" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>MATLAB函数代码如下（参考了文献【5】倒数第2页）：</span></p> 
<p><span style="font-family:Times New Roman"></span></p> 
<pre><code class="language-lua"><span class="hljs-function"><span class="hljs-keyword">function</span> [ <span class="hljs-title">hard_thresh</span> ] = <span class="hljs-title">hardthresholding</span><span class="hljs-params">( b,lambda )</span></span>
    sel = (<span class="hljs-built_in">abs</span>(b)&gt;<span class="hljs-built_in">sqrt</span>(lambda));
    hard_thresh = b.*sel;
<span class="hljs-keyword">end</span></code></pre> 
<p></p> 
<p></p> 
<p><span style="font-family:Times New Roman">一定要注意：这种写法是针对最开始的优化问题：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151037340" alt=""></span></p> 
<p><span style="font-family:Times New Roman">但我个人感觉更应该写成这种通用形式：</span></p> 
<span style="font-family:Times New Roman"></span>
<pre><code class="language-r"><span class="hljs-keyword">function</span> <span class="hljs-punctuation">[</span> x <span class="hljs-punctuation">]</span> <span class="hljs-operator">=</span> hard<span class="hljs-punctuation">(</span> b<span class="hljs-punctuation">,</span><span class="hljs-built_in">T</span> <span class="hljs-punctuation">)</span>
    sel <span class="hljs-operator">=</span> <span class="hljs-punctuation">(</span><span class="hljs-built_in">abs</span><span class="hljs-punctuation">(</span>b<span class="hljs-punctuation">)</span><span class="hljs-operator">&gt;</span><span class="hljs-built_in">T</span><span class="hljs-punctuation">)</span>;
    x <span class="hljs-operator">=</span> b.<span class="hljs-operator">*</span>sel;
end</code></pre> 
<p></p> 
<p><span style="font-family:Times New Roman">如此之后，若要解决优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151037340" alt=""><br> </span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;只需调用`hard(B, sqrt(λ))`即可；若要解决优化问题
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151323034" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;只需调用`hard(B, sqrt(2*λ))`即可。

### 1.5 硬阈值(HardThresholding)测试代码
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>硬阈值(Hard Thresholding)要解决的优化问题目标函数是非凸的，不太常见，手边目前没有其它函数求解这个问题，因此测试代码只能测一下这个函数编写的正确与否了：</span></p> 
<span style="font-family:Times New Roman"></span>
<pre><code class="language-sql">clear <span class="hljs-keyword">all</span>;<span class="hljs-keyword">close</span> <span class="hljs-keyword">all</span>;clc; 
b <span class="hljs-operator">=</span> [<span class="hljs-number">-0.8487</span>   <span class="hljs-number">-0.3349</span>    <span class="hljs-number">0.5528</span>    <span class="hljs-number">1.0391</span>   <span class="hljs-number">-1.1176</span>]<span class="hljs-string">';
lambda = 0.5;
x1=hardthresholding(b,lambda)
x2=hard(b,sqrt(lambda))
fprintf('</span>\nError <span class="hljs-keyword">between</span> hardthresholding <span class="hljs-keyword">and</span> hard <span class="hljs-operator">=</span> <span class="hljs-operator">%</span>f\n<span class="hljs-string">',norm(x1-x2))</span></code></pre> 
<p></p> 
<p><span style="font-family:Times New Roman">这里就不给出输出结果了。可以运行一下，从输出结果来看，函数的功能是正确的。</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>另外，可以在matlab里输入以下命令看一个软阈值的图像：</span></p> 
<p><span style="font-family:Times New Roman"></span></p> 
<pre><code class="language-r">x<span class="hljs-operator">=</span><span class="hljs-operator">-</span><span class="hljs-number">5</span><span class="hljs-operator">:</span><span class="hljs-number">0.01</span><span class="hljs-operator">:</span><span class="hljs-number">5</span>;<span class="hljs-built_in">T</span><span class="hljs-operator">=</span><span class="hljs-number">1</span>;y<span class="hljs-operator">=</span>hard<span class="hljs-punctuation">(</span>x<span class="hljs-punctuation">,</span><span class="hljs-built_in">T</span><span class="hljs-punctuation">)</span>;plot<span class="hljs-punctuation">(</span>x<span class="hljs-punctuation">,</span>y<span class="hljs-punctuation">)</span>;grid;</code></pre> 
<p></p> 
<div style="text-align:center">
 <span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803151654983" alt=""></span>
</div> 
<p></p> 

### 1.6 参考文献
<p align="left"><span style="font-family:Times New Roman">【1】<span style="color:rgb(34,34,34)">Donoho D L, JohnstoneJ M. Ideal spatial adaptation by wavelet shrinkage[J]. Biometrika, 1994, 81(3):425-455.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman"><span style="color:rgb(34,34,34)">【</span><span style="color:rgb(34,34,34)">2</span><span style="color:rgb(34,34,34)">】</span><span style="color:rgb(34,34,34)">Wright SJ, Nowak R D, Figueiredo M A T. Sparse reconstruction by separableapproximation[J]. IEEE Transactions on Signal Processing, 2009, 57(7):2479-2493.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman"><span style="color:rgb(34,34,34)">【</span><span style="color:rgb(34,34,34)">3</span><span style="color:rgb(34,34,34)">】</span><span style="color:rgb(34,34,34)">http://blog.sina.com.cn/s/blog_6d0e97bb01015vq3.html</span></span></p> 
<p align="left"><span style="font-family:Times New Roman"><span style="color:rgb(34,34,34)">【</span><span style="color:rgb(34,34,34)">4</span><span style="color:rgb(34,34,34)">】</span><span style="color:rgb(34,34,34)">Elad M,Figueiredo M A T, Ma Y. On the Role of Sparse and Redundant Representations inImage Processing[J]. Proceedings of the IEEE, 2010, 98(6):972-982.</span></span></p> 
<p><span style="font-family:Times New Roman">【5】http://www.docin.com/p-553314466.html</span></p>

____

## 2 软阈值函数

### 2.1 软阈值(Soft Thresholding)函数的符号

<p><span style="font-family:Times New Roman">&nbsp; &nbsp; &nbsp; &nbsp; 软阈值(Soft Thresholding)目前非常常见，文献【1】【2】最早提出了这个概念。软阈值公式的表达方式归纳起来常见的有三种，以下是各文献中的软阈值定义符号：</span></p> 
<p><span style="font-family:Times New Roman">文献【1】式(12)：</span></p> 
<p style="text-align:center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142647009" alt=""><br> </span></p> 
<p></p> 
<p><span style="font-family:Times New Roman">文献【2】：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142743956" alt=""></span></p> 
<p><span style="font-family:Times New Roman">文献【3】：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142752494" alt=""></span></p> 
<p><span style="font-family:Times New Roman">文献【4】式(8)：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142759160" alt=""></span></p> 
<p><span style="font-family:Times New Roman">文献【5】式(1.5)：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142808338" alt=""></span></p> 
<p><span style="font-family:Times New Roman">文献【6】式(12)注释：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142817119" alt=""></span></p> 
<p><span style="font-family:Times New Roman">文献【7】：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142832176" alt=""></span></p> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中文献【1】【2】【3】【5】是第一种，也是最常见的一种；文献【4】【6】是第二种，个人认为可读性比第一种要好；文献【7】是第三种，个人认为可读性最好。当然，它们表达的意思是一样的(<font color=#9900CC><strong>无论是sgn(x)还是sign(x)都是符号函数，即当$x>0$时为1，当$x<0$时为-1。</font></strong>)

&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; 以文献【1】符号为例解释第一种表示方式。这里$w$是变量，$λ$是阈值(非负值)，符号$(|w|-λ)_+$表示当$(|w|-λ)>0$时则等于$|w|-λ$，当$(|w|-λ)<0$时则等于0。那么分三种情况来讨论：第一种情况是$w>\lambda>0$，则$sgn(w)=1$，$|w|=w$，$(|w|-λ)$一定大于0，$(|w|-λ)_+=|w|-λ$，所以$η_S(w,λ)=w-λ$；第二种情况是$w<-λ<0$，则$sgn(w)=-1$，$|w|=-w$，$(|w|-λ)$也一定大于0，$(|w|-λ)_+=|w|-λ$，所以$η_S(w,λ)=-1*(-w-λ)= w+λ$；第三种情况是$|w|<λ$，此时$(|w|-λ)$一定小于0，则$(|w|-λ)_+=0$，所以$η_S(w,λ)=0$。因此

<span style="font-family:Times New Roman"></span> 
<div style="text-align:center">
 <img src="https://img-blog.csdn.net/20160809165935019" alt="">
</div> 
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;  以文献【6】符号为例解释第二种表示方式。这种表示方式中符号$max{|u|-a,0}$的作用与第一种表示方式中的符号$(|w|-λ)_+$的作用一样，即当$(|u|-a)>0$时$max{|u|-a,0}=(|u|-a)$，当$(|u|-a)<0$时，$max{|u|-a,0}=0$，知道了这一点剩下的分析与第一种表示方式相同。

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 综上，三种表示方式均是一致的。

### 2.2 软阈值(Soft Thresholding)函数的作用

<p><span style="font-family:Times New Roman">&nbsp; &nbsp; &nbsp; &nbsp; 弄清楚了软阈值(Soft Thresholding)的符号表示以后，接下来说一说它的作用。以下内容主要参考了文献【7】，这是一个非常棒的PPT！！！</span></p> 
<p><span style="font-family:Times New Roman">&nbsp; &nbsp; &nbsp; &nbsp; 软阈值(SoftThresholding)可以求解如下优化问题：</span></p> 
<span style="font-family:Times New Roman"></span> 
<div style="text-align:center">
 <img src="https://img-blog.csdn.net/20160803142929994" alt="">
</div> 
<p></p> 
<p><span style="font-family:Times New Roman">其中：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143000495" alt=""></span></p> 
<p><span style="font-family:Times New Roman">&nbsp; &nbsp; &nbsp; &nbsp; 根据范数的定义，可以将上面优化问题的目标函数拆开：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143016510" alt=""></span></p> 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;也就是说，我们可以通过求解$N$个独立的形如函数
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143028042" alt=""><br> </span></p> 
<p><span style="font-family:Times New Roman">的优化问题，来求解这个问题。由中学时代学过的求极值方法知道，可以求函数<em>f</em>(<em>x</em>)导数：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143048448" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>这里要解释一下变量x绝对值的导数，当x&gt;0时，|x|=x，因此其导数等于1；当x&lt;0时，|x|=-x，因此其导数等于-1；综合起来，x绝对值的导数等于sgn(x)。令函数<em>f</em>(<em>x</em>)导数等于0，得：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143100948" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>这个结果等号两端都有变量x，需要再化简一下。下面分三种情况讨论：</span></p> 
<p><span style="font-family:Times New Roman">(1)当b&gt;λ/2时</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>假设x&lt;0，则sgn(x)=-1，所以x=b+λ/2&gt;0，与假设x&lt;0矛盾；</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>假设x&gt;0，则sgn(x)=1，所以x=b-λ/2&gt;0，成立；</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>所以此时在x=b-λ/2&gt;0处取得极小值：</span></p> 
<div style="text-align:center">
 <span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143124933" alt=""></span>
</div> 
<p></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>即此时极小值小于<em>f</em>(0)，而当x&lt;0时</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143205402" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>即当x&lt;0时函数<em>f</em>(<em>x</em>)为单调降函数（对任意△<em>x</em>&lt;0，<em>f</em>(0)&lt;<em>f</em>(△<em>x</em>)）。因此，函数在x=b-λ/2&gt;0处取得最小值。</span></p> 
<p><span style="font-family:Times New Roman">(2)当b&lt;-λ/2时</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>假设x&lt;0，则sgn(x)=-1，所以x=b+λ/2&lt;0，成立；</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>假设x&gt;0，则sgn(x)=1，所以x=b-λ/2&lt;0，与假设x&lt;0矛盾；</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>所以此时在x=b+λ/2&lt;0处取得极小值：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143230652" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>即此时极小值小于<em>f</em>(0)，而当x&gt;0时</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143241212" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>即当x&gt;0时函数<em>f</em>(<em>x</em>)为单调升函数（对任意△<em>x</em>&gt;0，<em>f</em>(△<em>x</em>)&gt;<em>f</em>(0)）。因此，函数在x=b+λ/2&lt;0处取得最小值。</span></p> 
<p><span style="font-family:Times New Roman">(3)当-λ/2&lt;b&lt;λ/2时(即|b|&lt;λ/2时)</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>假设x&lt;0，则sgn(x)=-1，所以x=b+λ/2&gt;0，与假设x&lt;0矛盾；</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>假设x&gt;0，则sgn(x)=1，所以x=b-λ/2&lt;0，与假设x&lt;0矛盾；</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>即无论x为大于0还是小于0均没有极值点，那么x=0是否为函数<em>f</em>(<em>x</em>)的极值点呢？</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>对于△<em>x</em>≠0，</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143323199" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>当△<em>x</em> &gt;0时，利用条件b&lt;λ/2可得</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143336198" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>当△<em>x</em> &lt;0时，利用条件b&lt;λ/2可得(注：此时|△<em>x</em> |=-△<em>x</em>)</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143355746" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>因此，函数在x=0处取得极小值，也是最小值。</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>综合以上三种情况，<em>f</em>(<em>x</em>)的最小值在以下位置取得：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143406042" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>与前面的软阈值(Soft Thresholding)对比一下，发现了么？若将上式中的b视为变量，λ/2视为阈值，上式即为软阈值(SoftThresholding)的公式。</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>至此，我们可以得到优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142929994" alt=""></span></p> 
<p><span style="font-family:Times New Roman">的解为</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143439637" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>注：该式为软阈值(Soft Thresholding)的矩阵形式。</span></p> 
### 2.3 软阈值(Soft Thresholding)的变形
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>当优化问题变为</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143452950" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>因为对目标函数乘一个常系数不影响极值点的获得，所以可等价为优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143508356" alt=""></span></p> 
<p><span style="font-family:Times New Roman">此时的解为<em>soft</em>(<em>B</em>, <em>λ</em>)。</span></p> 

### 2.4 软阈值(Soft Thresholding)的MATLAB代码

<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>软阈值(Soft Thresholding)的函数代码可以写成专门针对优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142929994" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>软阈值(Soft Thresholding)是如此简单以至于可以用一句代码去实现它[8]：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143602091" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>当然，如果不习惯这种形式，也可以写成常见的函数形式：</span></p> 
<span style="font-family:Times New Roman"></span>
<pre><code class="language-lua"><span class="hljs-function"><span class="hljs-keyword">function</span> [ <span class="hljs-title">soft_thresh</span> ] = <span class="hljs-title">softthresholding</span><span class="hljs-params">( b,lambda )</span></span>
    soft_thresh = sign(b).*<span class="hljs-built_in">max</span>(<span class="hljs-built_in">abs</span>(b) - lambda/<span class="hljs-number">2</span>,<span class="hljs-number">0</span>);
<span class="hljs-keyword">end</span></code></pre> 
<p></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>一定要注意：这种写法是针对最开始的优化问题：</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142929994" alt=""></span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>但我个人感觉更应该写成这种通用形式：</span></p> 
<span style="font-family:Times New Roman"></span>
<pre><code class="language-r"><span class="hljs-keyword">function</span> <span class="hljs-punctuation">[</span> x <span class="hljs-punctuation">]</span> <span class="hljs-operator">=</span> soft<span class="hljs-punctuation">(</span> b<span class="hljs-punctuation">,</span><span class="hljs-built_in">T</span> <span class="hljs-punctuation">)</span>
    x <span class="hljs-operator">=</span> <span class="hljs-built_in">sign</span><span class="hljs-punctuation">(</span>b<span class="hljs-punctuation">)</span>.<span class="hljs-operator">*</span><span class="hljs-built_in">max</span><span class="hljs-punctuation">(</span><span class="hljs-built_in">abs</span><span class="hljs-punctuation">(</span>b<span class="hljs-punctuation">)</span> <span class="hljs-operator">-</span> <span class="hljs-built_in">T</span><span class="hljs-punctuation">,</span><span class="hljs-number">0</span><span class="hljs-punctuation">)</span>;
end</code></pre> 
<p></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>如此之后，若要解决优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803142929994" alt=""></span></p> 
<p><span style="font-family:Times New Roman">只需调用soft(B, λ/2)即可；若要解决优化问题</span></p> 
<p align="center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143452950" alt=""><br> </span></p> 
<p><span style="font-family:Times New Roman">只需调用soft(B, λ)即可。</span></p> 

### 2.5 软阈值(Soft Thresholding)测试代码

<p align="left"><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>用以下一小段代码测试一下软阈值，用来求解优化问题：</span></p> 
<p align="center"><img src="https://img-blog.csdn.net/20160803145313085" alt=""></p> 
<p align="left"><span style="font-family:Times New Roman">这里用的对比函数是基追踪降噪(BPDN_quadprog.m)，参见<a target="_blank">压缩感知重构算法之基追踪降噪(Basis PursuitDe-Noising, BPDN)</a> （http://blog.csdn.net/jbb0523/article/details/52013669），使用BPDN时，实际上就是观测矩阵为单位阵时的一种特殊情况：</span></p> 
<span style="font-family:Times New Roman"></span>
<pre><code class="language-sql">clear <span class="hljs-keyword">all</span>;<span class="hljs-keyword">close</span> <span class="hljs-keyword">all</span>;clc; 
b <span class="hljs-operator">=</span> [<span class="hljs-number">-0.8487</span>   <span class="hljs-number">-0.3349</span>    <span class="hljs-number">0.5528</span>    <span class="hljs-number">1.0391</span>   <span class="hljs-number">-1.1176</span>]<span class="hljs-string">';
lambda = 1;
x1=soft(b,lambda)
x2=BPDN_quadprog(b,eye(length(b)),lambda)
fprintf('</span>\nError <span class="hljs-keyword">between</span> soft <span class="hljs-keyword">and</span> BPDN <span class="hljs-operator">=</span> <span class="hljs-operator">%</span>f\n<span class="hljs-string">',norm(x1-x2))</span></code></pre> 
<p></p> 
<p><span style="font-family:Times New Roman">这里就不给出输出结果了。运行后，观察输出结果可知，soft函数与BPDN_quadprog函数的输结果相同。</span></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>另外，可以在matlab里输入以下命令看一个软阈值的图像：</span></p> 
<span style="font-family:Times New Roman"></span>
<pre><code class="language-r">x<span class="hljs-operator">=</span><span class="hljs-operator">-</span><span class="hljs-number">5</span><span class="hljs-operator">:</span><span class="hljs-number">0.1</span><span class="hljs-operator">:</span><span class="hljs-number">5</span>;<span class="hljs-built_in">T</span><span class="hljs-operator">=</span><span class="hljs-number">1</span>;y<span class="hljs-operator">=</span>soft<span class="hljs-punctuation">(</span>x<span class="hljs-punctuation">,</span><span class="hljs-built_in">T</span><span class="hljs-punctuation">)</span>;plot<span class="hljs-punctuation">(</span>x<span class="hljs-punctuation">,</span>y<span class="hljs-punctuation">)</span>;grid;</code></pre> 
<p style="text-align:center"><span style="font-family:Times New Roman"><img src="https://img-blog.csdn.net/20160803143835830" alt=""><br> </span></p> 
<p></p> 
### 2.6 总结
<p></p> 
<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>可以发现，软阈值解决的优化问题和基追踪降噪问题很像，但并不一样，而且需要格外说明的是，软阈值并能不解决基追踪降噪问题，文献【8】在最后明确说明了这一点：</span></p> 
<span style="font-family:Times New Roman"></span> 
<div style="text-align:center">
 <img src="https://img-blog.csdn.net/20160803143913753" alt="">
</div> 
<p></p> 

<p><span style="font-family:Times New Roman"><span style="font-family:'Times New Roman'">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>最后，非常感谢文献【7】的PPT，看了之后让我有一种醍醐灌顶的感觉……</span></p> 
### 2.7 参考文献
<p align="left"><span style="font-family:Times New Roman">【1】<span style="color:rgb(34,34,34)">Donoho D L, JohnstoneJ M. Ideal spatial adaptation by wavelet shrinkage[J]. Biometrika, 1994, 81(3):425-455.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman">【2】<span style="color:rgb(34,34,34)">Donoho D L.De-noising by soft-thresholding[J]. IEEE transactions on information theory,1995, 41(3): 613-627.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman">【3】<span style="color:rgb(34,34,34)">Bredies K, Lorenz D.Iterative soft-thresholding converges linearly[R]. Zentrum fürTechnomathematik, 2007.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman">【4】<span style="color:rgb(34,34,34)">Bioucas-Dias J M,Figueiredo M A T. A new TwIST: two-step iterative shrinkage/thresholdingalgorithms for image restoration[J]. IEEE Transactions on Image processing,2007, 16(12): 2992-3004.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman">【5】<span style="color:rgb(34,34,34)">Beck A, Teboulle M. Afast iterative shrinkage-thresholding algorithm for linear inverse problems[J].SIAM journal on imaging sciences, 2009, 2(1): 183-202.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman">【6】<span style="color:rgb(34,34,34)">Wright S J, Nowak RD, Figueiredo M A T. Sparse reconstruction by separable approximation[J]. IEEETransactions on Signal Processing, 2009, 57(7): 2479-2493.</span></span></p> 
<p align="left"><span style="font-family:Times New Roman">【7】谷鹄翔.IteratedSoft-Thresholding Algorithm[Report,slides]. http://www.sigvc.org/bbs/thread-41-1-2.html</span></p> 
<p><span style="font-family:Times New Roman">【8】http://www.simonlucey.com/soft-thresholding/</span></p> 
<p><span style="font-family:Times New Roman">【9】http://blog.sina.com.cn/s/blog_6d0e97bb01015vq3.html</span></p>

____

### 参考文章
- 硬阈值(Hard Thresholding)函数解读：[https://blog.csdn.net/jbb0523/article/details/52103819](https://blog.csdn.net/jbb0523/article/details/52103819)
- 软阈值(Soft Thresholding)函数解读：[https://blog.csdn.net/jbb0523/article/details/52103257](https://blog.csdn.net/jbb0523/article/details/52103257)
- 软阈值函数学习笔记：[https://blog.csdn.net/SignalProc8848/article/details/107418070](https://blog.csdn.net/SignalProc8848/article/details/107418070)
- 软阈值迭代算法(ISTA）和快速软阈值迭代算法(FISTA):[https://www.cnblogs.com/louisanu/p/12045861.html](https://www.cnblogs.com/louisanu/p/12045861.html)
