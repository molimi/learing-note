## 1 PyQt5 图形界面开发工具

Qt 库是跨平台的 C++ 库的集合，是最强大的 GUI 库之一，可以实现高级 API 来访问桌面和移动系统的各种服务。
PyQt5 是一套 Python 绑定 Digia QT5 应用的框架。PyQt5 实现了一个 Python模块集，有 620 个类，6000 个函数和方法。
PyQt5 的优点：简单好用，功能强大， 跨平台支持，文档齐全，稳定性高，生态支持，开源免费。


本文使用`Anaconda+VSCode`配置PyQt5环境，在开始之前新建Anaconda的虚拟环境，如果不需要虚拟环境可以直接使用默认的Base环境。详细安装过程请参考：[Anaconda 和 PyTorch安装](https://blog.csdn.net/xq151750111/article/details/125085757)


## 2 Anaconda+VSCode+QT Designer配置PyQt5环境
### 2.1 创建虚拟环境

虚拟环境的本质，就是在你电脑里安装了多个Python解释器（可执行程序），每个Python解释器又关联了很多个包、模块；项目代码在运行时，是使用特定路径下的那个Python解释器来执行。

```python
# 格式如下
conda create -n 虚拟环境名字 python=版本  # 创建虚拟环境，开始新项目时执行一次
conda activate 虚拟环境名字 # 进入虚拟环境，每次打开终端都需要执行
conda deactivate # 退出虚拟环境，一般很少使用
conda remove -n 虚拟环境名字 --all  # 删除虚拟环境，一般很少使用
# 示例
conda create -n test python=3.8
conda activate test
conda deactivate
conda remove -n test --all
```

### 2.2 安装PyQt5

**1. pip 安装 PyQt5**

在新创建的虚拟环境中安装PyQt5
```bash
pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

安装了 PyQt5 就可以用 Python 语言编写 Qt 程序。例如，可以用一个简单的例程，检测 PyQt5 的安装是否成功。

```python
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 初识化界面
    MainWindow = QtWidgets.QWidget()        # 生成一个主窗口
    MainWindow.show()                       # 显示主窗口
    sys.exit(app.exec_())                   # 在线程中退出  
```
运行程序，将弹出如下界面：

<img src ="https://img-blog.csdnimg.cn/bb3e6365b5994ac6a1c971aeb3f6ef79.png#pic_center" width = 36%>

**2. pip 安装 QtTools**

```bash
pip install PyQt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 2.3 VSCode安装插件





_______


## 参考
- vscode配置pyqt5全过程：[https://blog.csdn.net/qq_37080185/article/details/121616507](https://blog.csdn.net/qq_37080185/article/details/121616507)
- Python 小白从零开始 PyQt5 项目实战（8）汇总篇（完整例程）：[https://blog.csdn.net/youcans/article/details/120925109](https://blog.csdn.net/youcans/article/details/120925109)
- PyQt5 教程：[https://www.w3schools.cn/pyqt5/index.html](https://www.w3schools.cn/pyqt5/index.html)