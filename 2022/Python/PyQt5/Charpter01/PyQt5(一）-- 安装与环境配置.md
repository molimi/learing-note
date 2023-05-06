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

虽然安装 PyQt5 就可以编程实现 GUI，但是学习、编程、调试、修改都是相当复杂和繁琐的。而 Qt Designer 基本是通过人机交互的排版方式进行界面设计，非常方便、直观。所以我在使用 Qt Designer 图形界面设计工具之后，就再也不愿意编写 Python 程序来实现 GUI 了。

Qt Tools 包含了两个重要的工具：
- 图形界面设计工具 Qt Designer，用于设计图形界面，生成 .ui文件，以 xml 格式存储界面和控件的属性；
- UI 文件转换工具 PyUic，用于将 .ui 文件解析为 .py 文件的工具。
Qt Tools 工具可以直接使用 pip 方式安装：

```bash
pip install PyQt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 2.3 VSCode安装插件

在vscode应用商店中安装PYQT Integration插件，安装完成后点击pyqt integration右下角的小齿轮，选择扩展设置extension settings，设置下面两个path（可以搜索anaconda和python的安装目录进行查找）

1. 运行调试选择Python解释器，我这里解释器是Python 3.8.16 (被命名为pyqt5)

<img src ="https://img-blog.csdnimg.cn/439434548095450c847c147eef51c838.png#pic_center" width = 48%>

2. Pyqt-integration › Qtdesigner: Path

我的路径为 `C:\Users\CarpeDiem\.conda\envs\pyqt5\Lib\site-packages\qt5_applications\Qt\bin\designer.exe`


1. Pyqt-integration › Pyuic: Cmd

我的路径为 `C:\Users\CarpeDiem\.conda\envs\pyqt5\Scripts\pyuic5.exe`


<img src ="https://img-blog.csdnimg.cn/29d99c38858f4dfb9e3a0c7bf4ac7b48.png#pic_center" width = 48%>

### 2.4 QtDesigner 和 PyUIC 的快速入门

1. 在VSCode工作区右击，选择 `PYQT:New Form`，会弹出 Qt Designer 设计器

<img src ="https://img-blog.csdnimg.cn/eba10d9449bd4604b483a327c1a3a73b.png#pic_center" width = 48%>

(1) 新建窗体

首次运行 QtDesigner 时可能会自动弹出 “新建窗体” 对话框，也可以通过菜单栏选择：“文件 -> 新建” 或快捷键 “Ctrl+N” 唤起 “新建窗体” 对话框。

在 “新建窗体” 窗口的左侧菜单选择 “MainWindow” 新建一个图形窗口。

<img src ="https://img-blog.csdnimg.cn/eb733e7cce114185a35956c3e6a2e413.png#pic_center" width = 48%>

(2) 设计图形界面

QtDesigner 的使用界面与 AutoCAD 等设计软件类似，很好上手。

主界面分左中右三部分，左侧是各种备选的控件对象，右侧上方的 “对象查看器” 显示控件的树状结构，右侧下方的 “属性编辑器” 显示控件的各种属性，中间部分用于显示所设计的界面。

新建的窗口 “MainWindow” 虽然是一个空白的图形窗口，但已经生成了 centralwidget、menubar、statusbar 三个基本控件，可以在右侧上方 “对象查看器” 查看这些控件及结构。

下面我们为新建的图形窗口添加几个图形控件：

<img src ="https://img-blog.csdnimg.cn/ad4e51f468184792a167d4cfef75c4c6.png#pic_center" width = 48%>

新建一个按钮控件：

- 从左侧控件栏的 Button 中选择 PushButton 按钮，鼠标左键点中 PushButton 按钮不放，移动鼠标将 PushButton 按钮拖动到中间的新建图形窗口内的任意位置，松开鼠标左键，就在图形窗口位置生成了一个 PushButton 按钮对象。
- 鼠标左键点击图形窗口中的这个 PushButton 按钮对象，拖动按钮可以调整控件的位置，对于其它控件也可以通过鼠标拖动来调整位置。
- 鼠标选中 PushButton 按钮对象，控件周围的边界位置上就出现 8个蓝色的点，表示控件被选中，这时可以在右侧的 “属性编辑器” 内对对象的属性进行编辑和修改，例如：
    - 将 PushButton 对象的高度修改为 120，宽度修改为 40；
    - 将 PushButton 对象的 “QAbstractButton->text” 修改为 “测试按钮”；

新建一个文本显示框控件：
- 从左侧控件栏的 InputWidget 中选择 TextEdit 按钮，鼠标左键选中 TextEdit 按钮拖动到新建图形窗口内的，松开鼠标左键就在图形窗口生成了一个 TextEdit 对象。
- 鼠标选中 TextEdit 对象，在右侧的 “属性编辑器” 内可以对对象的属性进行编辑和修改，例如：
    - 将 TextEdit 对象的高度修改为 300，宽度修改为 200；
    - 对于 TextEdit 对象的显示内容可以用 html、markdown 等格式编辑，也可以鼠标双击 TextEdit 对象唤出 html 编辑对话框，输入希望显示的内容。

现在，我们就已经用 QtDesigner 完成了一个基本的图形界面。


(3) 将设计的图形界面保存为 .ui文件

在设计器中进行控件设计，保存。命名为 `test03.ui`。回到VSCode，发下工作目录下多出 `*.ui` 文件


(4) 右键生成的 `test03.ui`，选择 `PYQT:Compile Form`，则会自动生成 `UI_test03.py` 文件

<img src ="https://img-blog.csdnimg.cn/71fcd1ec62954b3b91240baf86a57dac.png#pic_center" width = 48%>

2. 我们编写一个主程序调用设计的图形界面 UI_test03.py，就可以完成一个图形界面应用程序

```python
"""
@author: CarpeDiem
@date: 23/5/1
@version: 0.1
@description: PyQt5初步使用
@Idea: Demo of GUI by PyQt5
"""
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_test03 import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)        # 创建应用程序对象
    main_window = QMainWindow()         # 创建主窗口
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()                  # 显示主窗口
    sys.exit(app.exec_())               # 在主线程中退出 
```

运行程序 `GUI_Demo2.py`，将弹出如下的图形界面：
<img src ="https://img-blog.csdnimg.cn/c47b54b819f342d2805980c90e3a7f14.png#pic_center" width = 48%>

这里的按钮和点击之后并没有任何反应，这是因为我们还没有设置这些控件所触发的动作和应用。在以后的程序中，我们将不断增加和丰富这个图形界面应用程序。


**补充：**

常见错误：无法将*.ui文件转为py文件
将 `*.ui` 文件转为py文件使用的是 `pyuic5.exe` 程序，常用的命令为 `pyuic5 -o destination.py source.ui`，其中-o 是操作参数，表示要生成一个文件，即将 `source.ui` 转换成 `destination.py`。
在配置好PYQT Integration插件后，经常会遇到`ImportError: DLL load failed: 找不到指定的模块` 的错误。常见原因有两个：
1. python3.dll丢失：通过Anaconda安装的Python缺少了python3.dll，可以从网上下载python3.dll，然后放到 Anaconda中python36.dll所在目录中；
2. PyQT5包冲突（大部分是这个错误）

**原因2的解决方法：**
- 执行 `pip uninstall PyQt5` 再重新安装
- 如果还是不行，则使用 `pip list` 命令查看已安装的包，将里面有关 PyQt 和 Qt 的相关项全部卸载，然后重新执行上面的“PyQt5安装”步骤


_______


## 参考
- vscode配置pyqt5全过程：[https://blog.csdn.net/qq_37080185/article/details/121616507](https://blog.csdn.net/qq_37080185/article/details/121616507)
- Python 小白从零开始 PyQt5 项目实战（8）汇总篇（完整例程）：[https://blog.csdn.net/youcans/article/details/120925109](https://blog.csdn.net/youcans/article/details/120925109)
- PyQt5 教程：[https://www.w3schools.cn/pyqt5/index.html](https://www.w3schools.cn/pyqt5/index.html)