本篇主要介绍Pytorch的安装和换源

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PyTorch的安装，一般常见的是Anaconda/miniconda+Pytorch+ (Pycharm/VS Code) 的工具，我们的安装分为以下几步
## 1 Anaconda的安装
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在DL和ML中，要用到大量成熟的package。一个个安装 package 很麻烦，而且容易出现奇奇怪怪的问题。而 Anaconda很好的解决了我们的问题，它集成了常用于科学分析（机器学习， 深度学习）的大量package。省略了我们安装一些package的过程。

### 1.1 安装Anaconda/miniconda
（1）登陆[Anaconda | Individual Edition](https://www.anaconda.com/products/individual)，选择相应系统DownLoad
<p><a class="has-card" href="https://www.anaconda.com/products/individual" title="Anaconda | Individual Edition"><span class="link-card-box"><span class="link-title">Anaconda | Individual Edition</span><span class="link-link"><img alt="" class="link-link-icon" src="https://csdnimg.cn/release/blog_editor_html/release2.0.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M1H3">https://www.anaconda.com/products/individual</span></span></a></p>

(2) 可以去清华镜像安装相应系统，Windows根据64位或者32位下载对应的.exe，Linux安装.sh，Mac安装.pkg。一般建议不要选择最新版的（不太稳定），这里建议选择前两年中的anaconda3随意一个版本。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这里以Linux为例，假设安装包已下载，可以直接在终端输入命令，首先cd到你有这个安装包的文件夹中（假设是Documents）
```bash
cd Documents
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;随后执行bash + 安装包名(文件夹路径名也行)
```bash
bash "/home/carpediem/Downloads/Anaconda3-5.3.1-Linux-x86_64.sh"
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详细安装步骤步骤可以参考一下各系统的安装教程：
<p><a class="has-card" href="https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/" title="Index of /anaconda/archive/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror"><span class="link-card-box"><span class="link-title">Index of /anaconda/archive/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror</span><span class="link-desc">Index of /anaconda/archive/ | 清华大学开源软件镜像站，致力于为国内和校内用户提供高质量的开源软件镜像、Linux 镜像源服务，帮助用户更方便地获取开源软件。本镜像站由清华大学 TUNA 协会负责运行维护。</span><span class="link-link"><img alt="" class="link-link-icon" src="https://mirrors.tuna.tsinghua.edu.cn/static/img/favicon.png">https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/</span></span></a>根据自己电脑选择对应版本：下载还是挺快的。</p>

- Anaconda超详细安装教程（Windows环境下）：[https://blog.csdn.net/fan18317517352/article/details/123035625](https://blog.csdn.net/fan18317517352/article/details/123035625)
- 在Linux服务器上安装Anaconda（超详细）:[https://blog.csdn.net/wyf2017/article/details/118676765](https://blog.csdn.net/wyf2017/article/details/118676765)
- Mac上安装Anaconda最全教程：[https://zhuanlan.zhihu.com/p/350828057](https://zhuanlan.zhihu.com/p/350828057)

### 1.2 检验是否安装成功
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Windows在开始页找到Anaconda Prompt，一般在Anaconda3的文件夹下,(Linux在终端输入anaconda就可以验证，

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输入之后是没有找到命令，很可能是因为环境变量还没有配置好。输入
```bash
vim ~/.bashrc
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;进入后在最后一行添加，其中username是你的账户名，这里根据你自己安装的Anacona的路径进行修改：
```python
export PATH=/home/username/anaconda3/bin:$PATH
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;加之后更新配置文件
```bash
source ~/.bashrc
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;重新输入anaconda，就可以验证是否安装成功。

### 1.3 创建虚拟环境
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linux在终端(Ctrl+Alt+T)进行，Windows在Anaconda Prompt进行

查看现存虚拟环境
```bash
conv info --env
conda env list
```
<img src="https://img-blog.csdnimg.cn/f2666c3f3eb9460581f7d0354183bbe7.png#pic_center" width=50%>

1. 创建虚拟环境
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在深度学习和机器学习中，我们经常会创建不同版本的虚拟环境来满足我们的一些需求。下面我们介绍创建虚拟环境的命令。在选择Python版本时，不要选择太高，建议选择3.6-3.8，版本过高会导致相关库不适配。
```bash
conda create -n env_name python==version
```

2. 删除虚拟环境命令
```bash
conda remove -n env_name --all
```

3. 激活环境命令
```bash
conda activate env_name
```

4. 退出当前环境
```bash
conda deactivate
```

### 1.4 换源
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在安装package时，我们经常会使用`pip install package_name`和`conda install package_name` 的命令，但是一些package下载速度会很慢，因此我们需要进行换源，换成国内源，加快我们的下载速度。以下便是两种对应方式的换源

#### 1.4.1 pip换源
**1. Linux**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linux下的换源，我们首先需要在用户目录下新建文件夹`.pip`，并且在文件夹内新建文件`pip.conf`，具体命令如下
```bash
cd ~
mkdir .pip/
vi pip.conf
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;随后，我们需要在`pip.conf`添加下方的内容:
```bash
[global]
index-url = http://pypi.douban.com/simple
[install]
use-mirrors =true
mirrors =http://pypi.douban.com/simple/
trusted-host =pypi.douban.com
```

**2. Windows**

1、文件管理器文件路径地址栏敲：`%APPDATA%` 回车，快速进入 `C:\Users\电脑用户\AppData\Roaming` 文件夹中
2、新建 pip 文件夹并在文件夹中新建 `pip.ini` 配置文件
3、我们需要在`pip.ini` 配置文件内容，我们可以选择使用记事本打开，输入以下内容，并按下ctrl+s保存，在这里我们使用的是豆瓣源为例子。

```bash
[global]
index-url = http://pypi.douban.com/simple
[install]
use-mirrors =true
mirrors =http://pypi.douban.com/simple/
trusted-host =pypi.douban.com
```

常用的镜像安装源网站
（1）阿里云 http://mirrors.aliyun.com/pypi/simple/
（2）豆瓣 http://pypi.douban.com/simple/
（3）中国科学院 http://pypi.mirrors.opencas.cn/simple/
（4）清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
（5）中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
（6）华中科技大学 http://pypi.hustunique.com/
（7）Python官方 https://pypi.python.org/simple/ 
（8）v2ex http://pypi.v2ex.com/simple/


#### 1.4.2 conda换源

- （清华源）[官方换源帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
- 阿里源，可以参考：阿里云镜像——https://developer.aliyun.com/mirror/anaconda

(1) 查看源
```bash
conda config --show-sources
```
(2) 切换源
```bash
conda config --add channels XXXX
conda config --set show_channel_urls yes
```

(3) 删除源
```bash
conda config --remove channels XXX
```

(4) 换回源
```bash
conda config --remove-key channels
```

**1. Windows系统**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TUNA 提供了 Anaconda 仓库与第三方源的镜像，各系统都可以通过修改用户目录下的 `.condarc` 文件。Windows 用户无法直接创建名为 `.condarc` 的文件，可先执行`conda config --set show_channel_urls yes`生成该文件之后再修改。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;完成这一步后，我们需要修改`C:\Users\User_name\.condarc`这个文件，打开后将文件里原始内容删除，将下面的内容复制进去并保存。

```bash
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这一步完成后，我们需要打开`Anaconda Prompt` 运行 `conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引。

##### Linux系统：
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Linux系统下，我们还是需要修改`.condarc`来进行换源
```bash
cd ~
vi .condarc
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`vim`下，我们需要输入`i`进入编辑模式，将上方内容粘贴进去，按`ESC`退出编辑模式，输入`:wq`保存并退出。

```bash
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/peterjc123/
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们可以通过`conda config --show default_channels`检查下是否换源成功。同时，我们仍然需要`conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引。


## 2 检查有无NVIDIA GPU
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;该部分如果仅仅只有CPU或者集显的小伙伴们可以跳过该部分。

1. windows
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们可以通过在`cmd/terminal中`输入`nvidia-smi`（Linux和Win命令一样）、使用NVIDIA控制面板和使用任务管理器查看自己是否有NVIDIA的独立显卡及其型号
<img src="https://img-blog.csdnimg.cn/0de4c927c29c43b6b1fa8490949eb032.png#pic_center" width=50%>

<img src="https://img-blog.csdnimg.cn/7c5e9e98012f4108b874a5294d3e4566.png#pic_center" width=50%>

2. linux
<img src="https://img-blog.csdnimg.cn/56e6b0f16c10480d83a130d0fc16d49b.png#pic_center" width=50%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们需要看下版本号，看自己可以兼容的CUDA版本，等会安装PyTorch时是可以向下兼容的。具体适配表如下图所示。
<img src="https://img-blog.csdnimg.cn/48f7dd8537464fbb86b019df486ab3bd.png#pic_center" width=50%>


## 3 PyTorch的安装
#### Step 1：登录[PyTorch官网](https://pytorch.org/)
<img src="https://img-blog.csdnimg.cn/905a382b4e3448b390ae4c7b05d79f85.png#pic_center" width=50%>

#### Step 2：Install

<img src="https://img-blog.csdnimg.cn/521a86fbe81444739ad1dded52a8791e.png#pic_center" width=50%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这个界面我们可以选择本地开始（Start Locally），云开发（Cloud Partners)，以前的Pytorch版本（Previous PyTorch Versions），移动端开发（Mobile），在此处我们需要进行本地安装。

#### Step 3：选择命令
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们需要结合自己情况选择命令并复制下来，然后使用conda下载或者pip下载（建议conda安装）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;打开`Terminal`，输入`conda activate env_name`，激活环境并切换到环境下面，我们就可以进行PyTorch的安装了

<img src="https://img-blog.csdnimg.cn/31565e8232884367a550906d9af66ae4.png#pic_center" width=50%>

**注**：

1. **Stable**代表的是稳定版本，**Preview**代表的是先行版本
2. 可以结合电脑是否有显卡，选择CPU版本还是CUDA版本，建议还是需要NVIDIA GPU
3. 官方建议我们使用**Anaconda**来进行管理
4. 关于安装的系统要求

   1. **Windows**：
      1. Windows 7及更高版本；建议使用Windows 10或者更高的版本
      2. Windows Server 2008 r2 及更高版本
   2. **Linux：以常见的CentOS和Ubuntu为例**
      1. CentOS, 最低版本7.3-1611
      2. Ubuntu, 最低版本 13.04，这里会导致cuda安装的最大版本不同
   3. **macOS**：
      1. macOS 10.10及其以上

5. 有些电脑所支持的cuda版本<10.2，此时我们需要进行手动降级，即就是cudatoolkit = 你所适合的版本，但是这里需要注意下一定要保持Pytorch和cudatoolkit的版本适配。查看[Previous PyTorch Versions | PyTorch](https://pytorch.org/get-started/previous-versions/)

#### Step 4：在线下载

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果我们使用的`Anaconda Prompt`进行下载的话，我们需要先通过`conda activate env_name`，激活我们的虚拟环境中去，再输入命令。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**注**: 我们需要要把下载指令后面的 -c pytorch 去掉以保证使用清华源下载，否则还是默认从官网下载。

#### Windows：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在安装的过程中，我们可能会出现一些奇奇怪怪的问题，导致在线下载不成功，我们也可以使用**离线下载**的方法进行。

**下载地址**：https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过上面下载地址，我们需要下载好对应版本的pytorch和 torchvision 包，然后打开`Anaconda Prompt`/`Terminal`中，进入我们安装的路径下。

```bash
cd package_location
conda activate env_name
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接下来输入以下命令安装两个包

```bash
conda install --offline pytorch压缩包的全称（后缀都不能忘记）
conda install --offline torchvision压缩包的全称（后缀都不能忘记）
```
#### Step 6：检验是否安装成功

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;进入所在的**虚拟环境**，紧接着输入`python`，在输入下面的代码。

```python
import torch

torch.cuda.is_available()
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这条命令意思是检验是否可以调用cuda，如果我们**安装的是CPU版本的话会返回False，能够调用GPU的会返回True**。一般这个命令不报错的话就证明安装成功。
____

## 参考
- PyTorch的安装：[https://github.com/datawhalechina/thorough-pytorch/blob/main/source/](https://github.com/datawhalechina/thorough-pytorch/blob/main/source/)
- [https://blog.csdn.net/Robin_Pi/article/details/107538672](https://blog.csdn.net/Robin_Pi/article/details/107538672)