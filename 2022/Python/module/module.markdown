`Python`提供了强大的模块支持，主要体现为不仅在`Python`标准库中包含了大量的模块（称为标准模块)，而且还有很多第三方模块，另外开发者自己也可以开发自定义模块。通过这些强大的模块支持将极大地提高我们的开发效率。

模块到底指的是什么呢？模块，英文为 Modules，至于模块到底是什么，可以用一句话总结：模块就是 Python 程序。换句话说，任何 Python 程序都可以作为模块，包括在前面章节中写的所有 Python 程序，都可以作为模块。

我们知道Python代码可以写到一个文件中，但随着程序功能的复杂，程序体积会不断变大，为了便于维护，通常会将其分为多个文件（模块），这样不仅可以提高代码的可维护性，还可以提高代码的可重用性。

> 代码的可重用性体现在，当编写好一个模块后，只要编程过程中需要用到该模块中的某个功能（由变量、函数、类实现），无需做重复性的编写工作，直接在程序中导入该模块即可使用该功能。

<img src="https://img-blog.csdnimg.cn/09fd3a41209547a294ad66748285a271.png#pic_center" width=36%>

## 1 自定义模块
在Python中，自定义模块有两个作用:一个是规范代码，让代码更易于阅读，另一个是方便其他程序使用己经编写好的代码，提高开发效率。

实现自定义模块主要分为两部分，一部分是创建模块，另一部分是导入模块。

### 1.1 创建模块
创建模块时，可以将模块中相关的代码（变量定义和函数定义等)编写在一个单独的文件中，并且将该文件命名为“模块名+.py”的形式。

代码如下所示：
```python
def foo():
    '''module1.py'''
    print("hello, world!')
```

```python
```python
def foo():
    '''module2.py'''
    print("goodbye, world!')
```

**温馨提示：**创建模块时，设置的模块名不能是Python自带的标准模块名称。

### 1.2 使用import语句导入模块
创建模块后，就可以在其他程序中使用该模块了。要使用模块需要先以模块的形式加载模块中的代码，这可以使用`import`语句实现。创建一个`test.py`函数进行测试：
```python
from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()
```
如果模块名比较长不容易记住，可以在导入模块时，使用as关键字为其设置一个别名，然后就可以通过这个别名来调用模块中的变量、函数和类等。例如，将上面导入模块的代码修改为以下内容:
```python
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
```

**说明：**在调用模块中的变量、函数或者类时，需要在变量名、函数名或者类名前添加“模块名.”作为前缀。


一个模块只会被导入一次，不管你执行了多少次`import`。这样可以防止导入模块被一遍又一遍地执行。

当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？
(1) 在当前目录（即执行的 Python脚本文件所在目录）下查找。
(2)到PYTHONPATH(环境变量)下的每个目录中查找。
(3)到Python的默认安装目录下查找。

以上所有涉及到的目录，都保存在标准模块 sys 的 sys.path 变量中，通过此变量我们可以看到指定程序文件支持查找的所有目录。换句话说，如果要导入的模块没有存储在 sys.path 显示的目录中，那么导入该模块并运行程序时，Python 解释器就会抛出 ModuleNotFoundError（未找到模块）异常。了解更多可以参考：[http://c.biancheng.net/view/4645.html](http://c.biancheng.net/view/4645.html)

解决“Python找不到指定模块”的方法有 3 种，分别是：
(1)向`sys.path`中临时添加模块文件存储位置的完整路径；
(2)将模块放在`sys.path`变量中已包含的模块加载路径中；
(3)设置`path`系统环境变量。

在使用`import`语句导入模块时，每执行一条`import`语句都会创建一个新的命名空间(namespace)，并且在该命名空间中执行与.py文件相关的所有语句。在执行时，需在具体的变量、函数和类名前加上“模块名.”前缀。如果不想在每次导入模块时都创建一个新的命名空间，而是将具体的定义导入到当前的命名空间中，这时可以使用`from…import`语句。使用`from…import`语句导入模块后，不需要再添加前缀，直接通过具体的变量、函数和类名等访问即可。

说明：命名空间可以理解为记录对象名字和对象之间对应关系的空间。目前Python的命名空间大部分都是通过字典(dict)来实现的。其中，key是标识符; value是具体的对象，例如，key是变量的名字， value则是变量的值。


注意：在使用`from...import`语句导入模块中的定义时，需要保证所导入的内容在当前的命名空间中是唯一的，否则将出现冲突，后导入的同名变量、函数或者类会覆盖先导入的。这时就需要使用`import`语句进行导入。


## 2 Python中包

使用模块可以避免函数名和变量名重名引发的冲突。那么，如果模块名重复应该怎么办呢?在Python中，提出了包(Package)的概念。包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下。这样，既可以起到规范代码的作用，又能避免模块名重名引起的冲突。

说明：包简单理解就是“文件夹”，只不过在该文件夹下必须存在一个名称为`“__init__.py”`的文件，可以是一个空模块，可以写一些初始化代码，其作用就是告诉 Python 要将该目录当成包来处理。这是`Python 2.x`的规定，而在`Python 3.x`中，`__init__.py`对包来说，并不是必须的。

### 2.1 Python 程序的包结构
在实际项目开发时，通常情况下，会创建多个包用于存放不同类的文件。例如，开发一个网站时，可以创建如下图所示的包结构。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/8d895c83d3aa47b5a7722c10c0ae7f0f.png#pic_center"> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">一个Python项目的包结构</div> </center>

### 2.2 创建和使用包
**1. 创建包**
创建包实际上就是创建一个文件夹，并且在该文件夹中创建一个名称为`“__init__.py”`的Python文件。在`__init__.py`文件中，可以不编写任何代码，也可以编写一些Python 代码。在`__init__.py`文件中所编写的代码，在导入包时会自动执行。

说明：`__init__.py`文件是一个模块文件，模块名为对应的包名。例如，在settings包中创建的`__init__.py`文件，对应的模块名为settings。

例如，在E盘根目录下，创建一个名称为settings的包，可以按照以下步骤进行:(1）计算机的E盘根目录下，创建一个名称为settings的文件夹。
(2）在IDLE中，创建一个名称为`“__init__.py”`的文件，保存在`E:\settings`文件夹下，并且在该文件中不写任何内容，然后再返回到资源管理器中，效果如下图所示。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/653cf2fa337b405996eb526d80d92221.png#pic_center"><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">创建__init__.py文件后的效果</div> </center>

至此，名称为settings的包创建完毕了，创建完毕之后便可以在该包中创建所需的模块了。

**2. 使用包**
创建包以后，就可以在包中创建相应的模块，然后再使用`import`语句从包中加载模块。从包中加载模块通常有以下3种方式:
通过“import＋完整包名＋模块名”形式加载指定模块
通过“from＋完整包名+import＋模块名”形式加载指定模块
通过“from+完整包名＋模块名+ import＋定义名”形式加载指定模块



## 3 引用其他模块
在Python中，除了可以自定义模块外，还可以引用其他模块，主要包括使用标准模块和第三方模块。下面分别进行介绍。

### 3.1 导入和使用标准模块

在 Python中，自带了很多实用的模块，称为标准模块（也可以称为标准库)，对于标准模块，我们可以直接使用`import`语句导入到Python文件中使用。例如，导入标准模块`random`(用于生成随机数)，可以使用下面的代码:
```python
import random   # 导入标准模块random
```
**温馨提示：**在导入标准模块时，也可以使用as关键字为其指定别名。通常情况下，如果模块名比较长，则可以为其设置别名。

除了random模块外，Python还提供了大约200多个内置的标准模块，涵盖了Python运行时服务、文字模式匹配、操作系统接口、数学运算、对象永久保存、网络和Internet脚本和GUI构建等方面。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/b2db00c34ead4053a05a25f1d2b204c2.png#pic_center"> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">Python常用的内置标准模块</div> </center>


### 3.2 第三方模块的下载与安装
在使用第三方模块时，需要先下载并安装该模块，然后就可以像使用标准模块一样导入并使用了。本节主要介绍如何下载和安装。下载和安装第三方模块可以使用Python提供的 pip命令实现。pip命令的语法格式如下:
```python
pip <command> [modulename]
```
参数说明:
- command：用于指定要执行的命令。常用的参数值有install(用于安装第三方模块)、uninstall(用于卸载已经安装的第三方模块)、list（用于显示已经安装的第三方模块）等。
- modulename：可选参数，用于指定要安装或者卸载的模块名，当command为 install 或者uninstall时不能省略。


说明：在大型程序中可能需要导入很多模块，推荐先导入Python提供的标准模块，然后再导入第三方模块，最后导入自定义模块。

如果想要查看Python中都有哪些模块（包括标准模块和第三方模块)，可以在IDLE中输入以下命今:
```python
help('modules)
```

如果只是想要查看已经安装的第三方模块，可以在命令行窗口中输入以下命令:
```python
pip list
```