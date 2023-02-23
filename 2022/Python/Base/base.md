@[TOC]
# 1 Python简介
## 1.1 精通一门编程语言的必要性
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;随着信息技术的发展，计算机技术应用越来越广泛，目前主流领域如下：

* <font color=#9900CC><strong>科学计算：</strong></font>是现代计算机应用的一个重要领域；
* <font color=#9900CC><strong>数据处理：</strong></font>用计算机来加工、管理与操作任何形式的数据资料，主要包括数据的采集、转换、分组、组织、计算、排序、存储、检索等；
* <font color=#9900CC><strong>人工智能：</strong></font>用计算机来模仿人的智能，使计算机具有识别语言、文字、图形和进行推理、学习以及适应环境的能力；
* <font color=#9900CC><strong>网络应用：</strong></font>在信息共享、文件传输、电子商务等领域迅速发展。
* <font color=#9900CC><strong>辅助技术：</strong></font>用计算机辅助进行工程设计、产品制造、性能测试，可以使设计工作半自动化或自动化；
* <font color=#9900CC><strong>过程控制：</strong></font>用计算机作为控制部件对单台设备或整个生产过程进行控制；


## 1.2 Python是什么
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。== Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字和一些标点符号，它具有比其他语言更有特色的语法结构。

* Python 是一种 <font color=#9900CC><strong>解释型语言：</strong></font>开发过程中没有了编译这个环节，类似于PHP和Perl语言；

* Python 是 <font color=#9900CC><strong>交互式语言：</strong></font>可以在一个 Python 提示符 >>> 后直接执行代码；

* Python 是 <font color=#9900CC><strong>面向对象语言：</strong></font>Python支持面向对象的风格或代码封装在对象的编程技术；

* Python 是 <font color=#9900CC><strong>初学者的语言：</strong></font>Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到浏览器再到游戏。

>  <font color=#9900CC><strong>编译型语言：</strong></font>通过专门的编译器，将所有源代码一次性转换成特定平台（Windows、Linux 等）执行的机器码（以可执行文件的形式存在）。
>  <font color=#9900CC><strong>解释型语言：</strong></font>由专门的解释器，根据需要将部分源代码临时转换成特定平台的机器码。
> 想要了解更多，请参考：[编译型语言和解释型语言的区别](http://c.biancheng.net/view/4136.html)

## 1.3 Python语言特点
**1、面向对象**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==Python语言具有很强的面向对象特性，简化了面向对象的实现，它消除了保护类型、抽象类、接口等面向对象的元素，使得面向对象的概念更容易理解。==


**2、内置的数据结构**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python提供了一些内置的数据结构，这些数据结构实现了类似Java中集合类的功能。内置数据结构的出现简化了程序设计。==Python的数据结构包括元组、列表、字典、集合等。== 元组相当于“只读”的数组，列表可以作为可变长度的数组使用，字典相当于Java中的HashTable类型。


**3、简洁**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python语言的关键字比较少，它没有分号、begin、 end等标记，代码块使用空格或Tab键缩进的方式来分隔。此外，==Python代码简洁、短小、易于阅读。== Python简化了循环语句，即使程序结构很复杂也能快速读懂。


**4、健壮**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==Python提供了异常处理机制，能捕获程序的异常情况。== 此外Python的堆栈跟踪对象能够指出程序出错的位置和出错的原因。异常机制能够避免不安全退出的情况，同时能够帮助程序员调试程序。


**5、跨平台**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python会先被编译为与平台相关的二进制代码，然后再解释执行。这种方式类似于Java，但Python的执行速度提高了。==Python编写的应用程序可以运行在Windows、Unix、Linux等不同的操作系统上。== 在一种操作系统上编写的Python代码只需做少量修改，就可移植到其他的操作系统上。

**6、可扩展**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python是采用C开发的语言，因此可以使用C扩展Python，可以给Python添加新的模块、新的类。同时Python可以嵌入C、C++语言开发项目中，使程序具备脚本语言的特性。因此，==Python 又常被称为“胶水”语言。==


**7、动态性**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 与JavaScript、PHP、Perl等语言类似，==它不需要另外声明变量、直接赋值即可创建一个新的变量。==


**8、强类型语言**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python的变量创建后会对应一种类型，它可根据赋值表达式的内容决定变量的类型。Python在内部建立了管理这些变量的机制，不同类型的变量需要类型转换。

**9、应用广泛**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==Python语言应用于数据库、网络、图形图像、数学计算、Web开发、操作系统扩展等领域。== 有许多第三方库支持Python，例如：PIL（图像处理库）、Tkinter（创建图形用户界面）、Django（交互式网站）、Pygame（2D动画）、SCIPy（科学计算）、Twisted（网络编程）等。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python的以上特性使得软件的代码大幅度减少，开发任务进一步简化，我们编程的关注点不再是语言特性，而是程序所要实现的任务。

<img src="https://img-blog.csdnimg.cn/20210415164313876.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hxMTUxNzUwMTEx,size_16,color_FFFFFF,t_70#pic_center" width="80%">


## 1.4 Python的应用领域
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 通常应用于编写下述应用程序：
* <font color=#9900CC><strong>脚本</strong></font>——这些简短的程序自动执行常见的管理任务，如在系统中新增用户、将文件上传到网站、在不使用浏览器的情况下下载网页等。
* <font color=#9900CC><strong>网站开发</strong></font>——作为快速创建动态网站的工具，Django、Bottle和Tope等Python项目深受开发人员欢迎。
* <font color=#9900CC><strong>文本处理</strong></font>——Python在字符串和文本文件处理方面提供了强大的支持。
* <font color=#9900CC><strong>图像处理</strong></font>——如PIL库(目前已不再维护，取而代之的有Pillow)科学计算。网上有许多卓越的Python科学计算库，提供了用以统计、数学计算和绘图的函数。如：NumPy 。
* <font color=#9900CC><strong>教育</strong></font>——鉴于Python简洁实用，越来越多的学习将其作为第一门编程教学语言。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python的主要运用领域有：
* <font color=#9900CC><strong>云计算：</strong></font>云计算最热的语言，典型的应用OpenStack；
 * <font color=#9900CC><strong> WEB应用开发：</strong></font>许多优秀的WEB框架，许多大型网站是Python开发、YouTube、Dropbox、Douban……典型的Web框架包括：Django、flask、TurboGears、web2py 等等；
 * <font color=#9900CC><strong>科学计算和人工智能：</strong></font>Python 在人工智能领域内的机器学习、神经网络、深度学习等方面，都是主流的编程语言， 此外，Python擅长进行科学计算和数据分析，支持各种数学运算，可以绘制出更高质量的 2D 和 3D 图像；
 * <font color=#9900CC><strong>自动化运维：</strong></font>系统操作和维护，通常情况下，Python 编写的系统管理脚本，无论是可读性，还是性能、代码重用度以及扩展性方面，都优于普通的 shell 脚本；
 * <font color=#9900CC><strong>金融：</strong></font>定量交易、金融分析，在金融工程领域，Python使用越来越广泛；
 * <font color=#9900CC><strong>图形 GUI：</strong></font>PyQT，WXPython，TkInter；
 * Python在<font color=#9900CC><strong>网络爬虫、游戏开发、机器人控制编程</strong></font>等领域也有广泛应用。

## 1.5 Python编程环境搭建
1. <font color=#9900CC><strong> Window 平台安装 Python：</strong></font>打开浏览器访问：[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) ，点击下载 executable installer，x86 表示是 32 位的安装程序，x86-64 表示 64 位的。详细安装过程，请参考：[http://c.biancheng.net/view/4161.html](http://c.biancheng.net/view/4161.html)

2.  <font color=#9900CC><strong>Unix & Linux 平台安装 Python3：</strong></font>打开浏览器访问：[https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)，选择适用于 Unix/Linux 的源码压缩包，然后解压缩并安装。详细安装过程，请参考：[http://c.biancheng.net/view/4162.html](http://c.biancheng.net/view/4162.html)

3.  <font color=#9900CC><strong>MAC平台安装Python3：</strong></font>打开浏览器访问：[https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)，下载最新版安装即可。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;安装完成之后，需要<font color=#9900CC><strong>配置环境变量，</strong></font>详细过程可以参考：[Python3 环境搭建](https://www.runoob.com/python3/python3-install.html)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此外，还推荐下载其他IDE进行Python编程，IDE 是 Intergreated Development Environment 的缩写，中文称为集成开发环境，用来表示辅助程序员开发的应用软件。换言之，==集成开发环境就是一系列开发工具的组合套装。== 一般情况下，程序员可选择的 IDE 类别是很多的，比如说，用 Python 语言进行程序开发，既可以选用 Python 自带的 IDLE，也可以选择使用 PyCharm 和 Notepad++ 作为 IDE。
* PyCharm下载和安装教程（包含Python解释器）：[http://c.biancheng.net/view/5804.html](http://c.biancheng.net/view/5804.html)
* Python Eclipse+PyDec下载和安装教程：[http://c.biancheng.net/view/5810.html](http://c.biancheng.net/view/5810.html)
* Python VS Code下载和安装教程：[http://c.biancheng.net/view/5813.html](http://c.biancheng.net/view/5813.html)

## 1.6 Python学习
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面推荐几篇内容不错的关于Python学习路线和不同方向的进阶教程，有时间可以对照一下，看看自己还有多长的路要走。

1. [Python学习路线（2021修正版）](https://blog.csdn.net/u014044812/article/details/88079011?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161843724916780261926748%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161843724916780261926748&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-88079011.pc_search_result_hbase_insert&utm_term=python&spm=1018.2226.3001.4187)
2. [致Python初学者](https://blog.csdn.net/xufive/article/details/102993570?ops_request_misc=&request_id=&biz_id=102&utm_term=python&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-4-102993570.pc_search_result_hbase_insert&spm=1018.2226.3001.4187)
3. [python系列文章(基础，应用，后端，运维，自动化测试，爬虫，数据分析，可视化，机器学习，深度学习系列内容)](https://blog.csdn.net/luanpeng825485697/article/details/78347433?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161843724916780271586245%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=161843724916780271586245&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-9-78347433.pc_search_result_hbase_insert&utm_term=python&spm=1018.2226.3001.4187)
4. [全网最全Python学习路线图+14张思维导图](https://blog.csdn.net/weixin_44318830/article/details/103739987?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161843724916780271586245%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=161843724916780271586245&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-18-103739987.pc_search_result_hbase_insert&utm_term=python&spm=1018.2226.3001.4187)

***

# 2 基础语法
## 2.1 标识符
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;标识符主要作用就是作为变量、函数、类、模块以及其他对象的名称，==Python 中标识符的命名不是随意的，而是要遵守一定的命令规则，== 如下：

1. 标识符对大小写敏感，且第一个字符必须是字母表中字母或下划线 _ 。
2. 标识符的其他的部分由字母、数字和下划线组成。
3. 标识符不能和 Python 中的保留字相同。
4. 标识符中不能包含空格、@、% 以及 $ 等特殊字符。

> 在Python中，以下划线开头的标识符有特殊含义，如下
> * 以单下划线开头的标识符（如 _width），表示不能直接访问的类属性，其无法通过 from...import* 的方式导入；
> * 以双下划线开头的标识符（如__add）表示类的私有成员；
> * 以双下划线作为开头和结尾的标识符（如 __init__），是专用标识符。
> 综上，除非特定场景需要，应避免使用以下划线开头的标识符。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了，但我们应尽量避免使用汉字作为标识符，容易遇到奇葩的错误。

> 不同场景中的标识符，其名称也有一定的规范可循，具体如下：
> * 当标识符用作模块名时，应尽量短小，并且全部使用小写字母，可以使用下划线分割多个字母，例如 game_mian、game_register 等。
> * 当标识符用作包的名称时，应尽量短小，也全部使用小写字母，不推荐使用下划线，例如 com.mr、com.mr.book 等。
> * 当标识符用作类名时，应采用单词首字母大写的形式。例如，定义一个图书类，可以命名为 Book。
> * 模块内部的类名，可以采用 "下划线+首字母大写" 的形式，如 _Book；
> * 函数名、类中的属性名和方法名，应全部使用小写字母，多个单词之间可以用下划线分割；
> * 常量命名应全部使用大写字母，单词之间可以用下划线分割；

## 2.2 关键字
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;关键字即保留字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 开发程序时，不能将保留字作为变量、函数、类、模块和其他对象的名称来使用。在`Python`中，所有保留字区分大小写。
## 2.3 字符编码
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了规范页面编码，方便他人了解文件所用编码，建议在文件中使用中文编码声明注释。默认情况下，==Python3源码文件以“可变长编码”的UTF-8编码，所有字符串都是unicode字符串。== UTF-8编码把一个`Unicode`字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。了解更多，可以参考：[ASCII、GB2312、Unicode、UTF-8编码](https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Linux下为源码文件指定编码方式：
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
```

## 2.4 代码规范
**1、注释**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注释（Comments）用来向用户提示或解释某些代码的作用和功能，它可以出现在代码中的任何位置。Python 解释器在执行代码时会忽略注释，不做任何处理，就好像它不存在一样。Python中单行注释以 `#` 开头，多行注释可以用多个`#`，也可以使用`''''` 或 `"""`，示例如下：

```python
#!/usr/bin/python3

# 第一个注释
print("Hello World!")	 # 第二个注释

'''
第三个注释
第四个注释
'''

"""
第五注释
第六注释
"""
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** Python 多行注释不支持嵌套。添加注释时，一定要有意义，即注释能充分解释代码的功能及用途。注释除了可以解释代码的功能与用途，也可以用于临时注释不想执行的代码。

**2、行与缩进**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`最具特色的就是使用缩进来表示代码块，不需要使用大括号`{ }`。`Python`对代码缩进要求非常严格，同一级别的代码块缩进必须相同。如果不采用合理的代码缩进，将抛出`SyntaxError`异常。==缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数，通常情况下是采用 4 个空格长度作为一个缩进量（默认情况下，一个 Tab 键就表示 4 个空格）。== 示例如下：

```python
if True：
	print("True")
else:
	print("False")
```

> 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。将首行及后面的代码组称为一个子句(clause)。

**3、多行语句**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python通常是一行写完一条语句，但如果语句很长，我们可以使用**右反斜杠（\）** 来实现多行语句，如下：

```python
total = item_one + \
		item_two + \
		item_three
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在[]，{}，或（）中的多行语句，不需要使用反斜杠（\），例如：

```python
total = ['item_one', 'item_two', 'item_three',
					'item_four', 'item_five']
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，如下：

```python
import math; print(math.pow(2, 4))
```
**4、空行**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。==

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;空行与代码缩进不同，空行并不是`Python`语法的一部分。书写时不插入空行，`Python`解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

> Python 采用 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 作为编码规范，其中 PEP 是 Python Enhancement Proposal（Python 增强建议书）的缩写，8 代表的是 Python 代码的样式指南。下面列出PEP 8 中初学者应严格遵守的一些编码规则：
> 1. 每个 import 语句只导入一个模块，尽量避免一次导入多个模块。
> 2. 不要在行尾添加分号，也不要用分号将两条命令放在同一行。
> 3. 建议每行不超过 80 个字符，如果超过，建议使用小括号将多行内容隐式的连接起来，而不推荐使用反斜杠 \ 进行连接。（例外：导入模块的语句过长；注释里的URL）
> 4. 使用必要的空行可以增加代码的可读性，通常在顶级定义（如函数或类的定义）之间空两行，而方法定义之间空一行，另外在用于分隔某些功能的位置也可以空一行。
> 5. 通常情况下，在运算符两侧、函数参数之间以及逗号两侧，都建议使用空格进行分隔。
> 6. 应该避免在循环中使用“+”和“=”运算符累加字符串。这是因为字符串是不可变的，这样做会创建不必要的临时对象。推荐将每个子字符串加入列表，然后在循环结束后使用`join()`方法连接列表。
> 7. 适当使用异常处理结构提高程序容错性，但不能过多依赖异常处理结构，适当的显式判断还是必要的。

**5、命名规范**

- 模块名尽量短小，并且全部使用小写字母，可以使用下划线分隔多个字母。例如，`game_main`、`game_register`、`bmiexponent`都是推荐使用的模块名称。
- 包名尽量短小，并且全部使用小写字母，不推荐使用下划线。例如，`com.mingrisoft`、`com.mr`、`com.mr.book`都是推荐使用的包名称，而`com_mingrisoft`就是不推荐的。
- 类名采用单词首字母大写形式(即`Pascal`风格)。例如，定义一个借书类，可以命名为BorrowBooke。
- 模块内部的类采用下划线“_”+`Pascal`风格的类名组成。例如，在`BorrowBook`类中的内部类，可以使用`_BorrowBook`命名。
- 函数、类的属性和方法的命名规则同模块类似，也是全部使用小写字母，多个字母间用下划线“_”分隔。
- 常量命名时全部使用大写字母，可以使用下划线。
- 使用单下划线“_”开头的模块变量或者函数是受保护的，在使用`from xxx import *`语句从模块中导入时这些变量或者函数不能被导入。
- 使用双下划线“_”开头的实例变量或方法是类私有的。



## 2.5 导入模块
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模块就是`Python`程序，==在`Python`中导入模块后，我们就可以使用该模块里定义的类、方法或者变量，这样既可以提高代码的可重用性，又可以避免变量冲突，我们通常用 `import` 或者 `from...import` 来导入相应的模块。== 像`def`一样，`import` 和 `from` 是可执行的语句，他们可以出现在 `if` 中，可以出现在函数中，执行到这些语句的时候才会进行解析，换句话说，被导入的模块和变量名只有在对应的 `import` 或 `from` 语句执行后才可以使用。

>   模块，可以理解为是对代码更高级的封装，即把能够实现某一特定功能的代码编写在同一个 .py 文件中，并将其作为一个独立的模块，这样既可以方便其它程序或脚本导入并使用，同时还能有效避免函数名和变量名发生冲突。


**1、import语句**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;既可以一行导入单个模块，也可以一行内导入多个模块，这里以常用的 `math` 和 `random` 模块为例，具体如下：

```python
import math				# 导入math整个模块
print(math.pi)			# 使用math模块名作为前缀来访问模块中的成员
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一次导入多个模块，多个模块之间用逗号隔开。

```python
import math,random			# 导入math、random两个模块
print(math.pi)				# 输出π的近似值，十五位小数
print(random.random())		# 生成一个[0, 1.0)的随机小数
```
> Python 不建议一行 import 所有模块，而是推荐用多行 import 来导入模块。更多的是出于操作便利性的原因，与代码本身无关，这样更易于阅读；更易于编辑；更易于维护。

> import工作方式：Python会在两个地方寻找这个模块，第一个地方是在sys.path（可以运行代码import sys	print(sys.path)查看），一般安装的Python库的目录都可以在sys.path中找到（要将Python的安装目录添加到电脑的环境变量），对于安装好的库，我们直接import即可。第二个地方就是运行文件所在的目录。如果在一个模块的顶层导入，那么它的作用域就是全局的；如果在函数中导入，那么它的作用域是局部的。 如果模块是被第一次导入，它将被加载并执行。

**2、import-as**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;导入整个模块时，也可以为模块指定别名。

```python
import math as m		# 导入math整个模块，并制定别名为m
print(m.pi)				# 使用m模块别名作为前缀来访问模块中的成员
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在导入多个模块时，也可以为模块指定别名

```python
import math as m, random as ran		# 导入math、random两个模块，并为math指定别名m，为random指定别名ran
print(m.pi)
print(ran.random())
```

**3、from-import**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面使用 `from...import` 导入指定成员，即把指定成员导入到当前作用域，
```python
from math import pi		# 导入math模块的pi成员
print(pi)				# 使用导入成员的语法，直接使用成员名访问
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;导入模块成员时，也可以为成员指定别名。

```python
from math import pi as P	# 导入math模块的pi成员，并指定别名P
print(P)					# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`form...import` 导入模块成员时，支持一次导入多个成员，如下：

```python
from math import pi, sqrt		# 导入math模块的pi，sqrt成员
print(pi)						# 使用导入成员的语法，直接使用成员名访问
print(sqrt(4))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一次导入多个模块成员时，也可指定别名，同样使用 as 关键字为成员指定别名，

```python
from math import pi as P, sqrt as sq		# 导入math模块的pi，sqrt成员，并为其指定别名P，sq
print(P)							# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
paint(sq(4)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在使用 `from...import` 语法时，可以一次导入指定模块内的所有成员（存在不同模块，相同成员名的情况，从而发生冲突，此方式不推荐），如下：

```python
from sys import *		# 导入math棋块内的所有成员
print(pi)				# 使用导入成员的语法，直接使用成员名访问
print(sqrt(4))
```
> 只在两种场合下建议使用这样的方法，一个场合是：目标模块中的属性非常多，反复键入模块名很不方便，例如 Tkinter (Python/Tk) 和 NumPy (Numeric Python) 模块，可能还有 socket 模块。另一个场合是在交互解释器下，这样可以减少输入次数。

## 2.6 输入输出
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`input()`是 Python 的内置函数，用于从控制台读取用户输入的内容。==`input()`函数总是以字符串的形式来处理用户输入的内容，所以用户输入的内容可以包含任何字符。==
```python
s = input("请输入：")							# 数据以字符串的形式返回
number1 = eval(input("请输入数字：")	# eval()去掉" "，将字符串转化为有效的表达式，来求值，并返回计算结果，和str()功能刚好相反
number2 = val(input("请输入："))		
'''val() 函数当识别到非数字，停止读入字符串,字符串中的空格和换行符会被去掉。即如果字符串内有字母或其他非数字字符，
val()函数只转换第一个非数字字符之前的数字。当字符串的首字符为非数字时，返回值为0。该函数也可以识别进制符号'''
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print()` 默认输出是换行的，如果要实现不换行，需要在变量末尾加上 `end=" "`，输出多个变量时，print() 函数默认以空格隔开多个变量，想要使用不同的分隔符，可以使用缺省参数`seq=':'`，可以通过`help("print")`了解更多。

```python
print("****************")
print('{}网站："{}"'.format('百度', 'www.baidu.com')	
# str.format()实现字符串格式化，大括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
print('{0} 和 {1}'.format('GitHub', 'CSDN'))	# 括号中的数字用于指向传入对象在format()中的位置
print("你是:%s, %d岁" % ("CSDN", 22)				# % 操作符也可以实现字符串格式化
# 推荐使用str.format()，{}里可以添加可选项：和格式标识符，这样可以对值进行更好的格式化
```
> %或者{}都可以看做转换说明符，转换说明符（Conversion Specifier）只是一个占位符，它会被后面表达式（变量、常量、数字、字符串、加减乘除等各种形式）的值代替。

**1、%使用**
<center><strong>表1 Python转换说明符</strong>

|转换说明符| 解释 |
|--|--|
| %d、%i | 转换为带符号的十进制整数 |
| %o | 转换为带符号的八进制整数 |
| %x、%X | 	转换为带符号的十六进制整数 |
| %e、%E | 转化为科学计数法表示的浮点数（输出e的大小写不一样） |
|  %f、%F | 	转化为十进制浮点数 |
| %g、%G | 	智能选择使用 %f 或 %e 格式 |
| %c | 格式化字符及其 ASCII 码 |
| %r | 使用 repr() 函数将表达式转换为字符串 |
| %s | 	使用 str() 函数将表达式转换为字符串 |

（1）整数的输出

```python
>>> print('%o' % 24)		# 转换为八进制输出
30
>>> print('%d' % 24）
24
```

（2）浮点数的输出
* %f ——默认保留小数点后面六位，例：%.3f，保留3位小数位
* %e ——保留小数点后面六位有效数字，指数形式输出，例：%.3e，保留3位小数位，使用科学计数法
* %g ——在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法，例：%.3g，保留3位有效数字，使用小数或科学计数法

```python
>>> print('%.2f' % 6.6666)		# 取3位小数
6.666
>>> print('%.3e' % 1.11)		# 取3位小数，用科学计数法
1.110e+00
```

（3）字符串输出
* %10s——右对齐，占位符10位
* %-10s——左对齐，占位符10位
* %.2s——截取2位字符串
* %10.2s——10位占位符，截取两位字符串

```python
print('%10s' % 'hello')		# 右对齐，取10位，不够则补位
print('%-10.2s' % 'hello')  # 左对齐，取10位，并截取两位字符串，并用空格补位
```
**2、format使用**

（1）位置匹配
* 不带编号，即“{}”
* 带数字编号，可调换顺序，即“{1}”、“{2}”
* 带关键字，即“{key1}”、“{key2}”

```python
>>> print('{0} {1} {0}'.format('hello', 'world'))						# 带数字编号，并打乱顺序
hello world hello
>>> print('{key1} {key2} {key1}'.format(key1='world', key2='hello'))	# 带关键字
world hello world
```

（2）格式转换

```python
>>> print('{:b}'.format(2))			# 转换为二进制输出
10
>>> print('{:%}'.format(0.2))		# 将数值乘以100，然后以小数点保留六位格式打印，值后面会有一个百分号
20.000000%
```

（3）进阶用法

* 指定小数精度和输出宽度

```python
from math import pi
print('{0:8.4f}'.format(pi))		# 位置为0，最小宽度为8，小数点后4位；:m.nf表示宽度为m，小数位为n，m和n都可以不指定
print('{:10s}'.format('Hello'))		# 输出字符串的宽度至少为10
```

* 指定对齐方式
<——左对齐，>——右对齐，^——居中
```python
print('{:^10s} and {:>10s}'.format('Github', 'CSDN'))		# 取10位居中，取10位右对齐
print('{:*^10}'.format('CSDN'))								# 使用*填充
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python格式化输出，了解更多，请参考：[%用法和format用法](https://www.cnblogs.com/fat39/p/7159881.html)

## 2.7 内建函数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 解释器自带的函数叫做内置函数，这些函数可以直接使用，不需要导入某个模块。

> 内置函数与标准库函数的对比：内置函数是解释器的一部分，它随着解释器的启动而生效；标准库函数是解释器的外部扩展，导入模块以后才能生效。一般来说，内置函数的执行效率要高于标准库函数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上一小节的 `print()` 函数就是内置函数，Python 解释器还提供了更多内置函数，以下按字母表顺序列出：
<center><strong>表2 Python3 内置函数</strong>
<table class="docutils align-default">
<colgroup>
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="row-even"><td><a class="reference internal" href="#abs" title="abs"><code class="xref py py-func docutils literal notranslate"><span class="pre">abs()</span></code></a></td>
<td><a class="reference internal" href="#delattr" title="delattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">delattr()</span></code></a></td>
<td><a class="reference internal" href="#hash" title="hash"><code class="xref py py-func docutils literal notranslate"><span class="pre">hash()</span></code></a></td>
<td><a class="reference internal" href="#func-memoryview"><code class="docutils literal notranslate"><span class="pre">memoryview()</span></code></a></td>
<td><a class="reference internal" href="#func-set"><code class="docutils literal notranslate"><span class="pre">set()</span></code></a></p></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#all" title="all"><code class="xref py py-func docutils literal notranslate"><span class="pre">all()</span></code></a></td>
<td><a class="reference internal" href="#func-dict"><code class="docutils literal notranslate"><span class="pre">dict()</span></code></a></td>
<td><a class="reference internal" href="#help" title="help"><code class="xref py py-func docutils literal notranslate"><span class="pre">help()</span></code></a></td>
<td><a class="reference internal" href="#min" title="min"><code class="xref py py-func docutils literal notranslate"><span class="pre">min()</span></code></a></td>
<td><a class="reference internal" href="#setattr" title="setattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">setattr()</span></code></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="#any" title="any"><code class="xref py py-func docutils literal notranslate"><span class="pre">any()</span></code></a></td>
<td><a class="reference internal" href="#dir" title="dir"><code class="xref py py-func docutils literal notranslate"><span class="pre">dir()</span></code></a></td>
<td><a class="reference internal" href="#hex" title="hex"><code class="xref py py-func docutils literal notranslate"><span class="pre">hex()</span></code></a></td>
<td><a class="reference internal" href="#next" title="next"><code class="xref py py-func docutils literal notranslate"><span class="pre">next()</span></code></a></td>
<td><a class="reference internal" href="#slice" title="slice"><code class="xref py py-func docutils literal notranslate"><span class="pre">slice()</span></code></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#ascii" title="ascii"><code class="xref py py-func docutils literal notranslate"><span class="pre">ascii()</span></code></a></p></td>
<td><a class="reference internal" href="#divmod" title="divmod"><code class="xref py py-func docutils literal notranslate"><span class="pre">divmod()</span></code></a></p></td>
<td><a class="reference internal" href="#id" title="id"><code class="xref py py-func docutils literal notranslate"><span class="pre">id()</span></code></a></p></td>
<td><a class="reference internal" href="#object" title="object"><code class="xref py py-func docutils literal notranslate"><span class="pre">object()</span></code></a></p></td>
<td><a class="reference internal" href="#sorted" title="sorted"><code class="xref py py-func docutils literal notranslate"><span class="pre">sorted()</span></code></a></p></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="#bin" title="bin"><code class="xref py py-func docutils literal notranslate"><span class="pre">bin()</span></code></a></p></td>
<td><a class="reference internal" href="#enumerate" title="enumerate"><code class="xref py py-func docutils literal notranslate"><span class="pre">enumerate()</span></code></a></p></td>
<td><a class="reference internal" href="#input" title="input"><code class="xref py py-func docutils literal notranslate"><span class="pre">input()</span></code></a></p></td>
<td><a class="reference internal" href="#oct" title="oct"><code class="xref py py-func docutils literal notranslate"><span class="pre">oct()</span></code></a></p></td>
<td><a class="reference internal" href="#staticmethod" title="staticmethod"><code class="xref py py-func docutils literal notranslate"><span class="pre">staticmethod()</span></code></a></p></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#bool" title="bool"><code class="xref py py-func docutils literal notranslate"><span class="pre">bool()</span></code></a></p></td>
<td><a class="reference internal" href="#eval" title="eval"><code class="xref py py-func docutils literal notranslate"><span class="pre">eval()</span></code></a></p></td>
<td><a class="reference internal" href="#int" title="int"><code class="xref py py-func docutils literal notranslate"><span class="pre">int()</span></code></a></p></td>
<td><a class="reference internal" href="#open" title="open"><code class="xref py py-func docutils literal notranslate"><span class="pre">open()</span></code></a></p></td>
<td><a class="reference internal" href="#func-str"><code class="docutils literal notranslate"><span class="pre">str()</span></code></a></p></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="#breakpoint" title="breakpoint"><code class="xref py py-func docutils literal notranslate"><span class="pre">breakpoint()</span></code></a></p></td>
<td><a class="reference internal" href="#exec" title="exec"><code class="xref py py-func docutils literal notranslate"><span class="pre">exec()</span></code></a></p></td>
<td><a class="reference internal" href="#isinstance" title="isinstance"><code class="xref py py-func docutils literal notranslate"><span class="pre">isinstance()</span></code></a></p></td>
<td><a class="reference internal" href="#ord" title="ord"><code class="xref py py-func docutils literal notranslate"><span class="pre">ord()</span></code></a></p></td>
<td><a class="reference internal" href="#sum" title="sum"><code class="xref py py-func docutils literal notranslate"><span class="pre">sum()</span></code></a></p></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#func-bytearray"><code class="docutils literal notranslate"><span class="pre">bytearray()</span></code></a></p></td>
<td><a class="reference internal" href="#filter" title="filter"><code class="xref py py-func docutils literal notranslate"><span class="pre">filter()</span></code></a></p></td>
<td><a class="reference internal" href="#issubclass" title="issubclass"><code class="xref py py-func docutils literal notranslate"><span class="pre">issubclass()</span></code></a></p></td>
<td><a class="reference internal" href="#pow" title="pow"><code class="xref py py-func docutils literal notranslate"><span class="pre">pow()</span></code></a></p></td>
<td><a class="reference internal" href="#super" title="super"><code class="xref py py-func docutils literal notranslate"><span class="pre">super()</span></code></a></p></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="#func-bytes"><code class="docutils literal notranslate"><span class="pre">bytes()</span></code></a></p></td>
<td><a class="reference internal" href="#float" title="float"><code class="xref py py-func docutils literal notranslate"><span class="pre">float()</span></code></a></p></td>
<td><a class="reference internal" href="#iter" title="iter"><code class="xref py py-func docutils literal notranslate"><span class="pre">iter()</span></code></a></p></td>
<td><a class="reference internal" href="#print" title="print"><code class="xref py py-func docutils literal notranslate"><span class="pre">print()</span></code></a></p></td>
<td><a class="reference internal" href="#func-tuple"><code class="docutils literal notranslate"><span class="pre">tuple()</span></code></a></p></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#callable" title="callable"><code class="xref py py-func docutils literal notranslate"><span class="pre">callable()</span></code></a></p></td>
<td><a class="reference internal" href="#format" title="format"><code class="xref py py-func docutils literal notranslate"><span class="pre">format()</span></code></a></p></td>
<td><a class="reference internal" href="#len" title="len"><code class="xref py py-func docutils literal notranslate"><span class="pre">len()</span></code></a></p></td>
<td><a class="reference internal" href="#property" title="property"><code class="xref py py-func docutils literal notranslate"><span class="pre">property()</span></code></a></p></td>
<td><a class="reference internal" href="#type" title="type"><code class="xref py py-func docutils literal notranslate"><span class="pre">type()</span></code></a></p></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="#chr" title="chr"><code class="xref py py-func docutils literal notranslate"><span class="pre">chr()</span></code></a></p></td>
<td><a class="reference internal" href="#func-frozenset"><code class="docutils literal notranslate"><span class="pre">frozenset()</span></code></a></p></td>
<td><a class="reference internal" href="#func-list"><code class="docutils literal notranslate"><span class="pre">list()</span></code></a></p></td>
<td><a class="reference internal" href="#func-range"><code class="docutils literal notranslate"><span class="pre">range()</span></code></a></p></td>
<td><a class="reference internal" href="#vars" title="vars"><code class="xref py py-func docutils literal notranslate"><span class="pre">vars()</span></code></a></p></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#classmethod" title="classmethod"><code class="xref py py-func docutils literal notranslate"><span class="pre">classmethod()</span></code></a></p></td>
<td><a class="reference internal" href="#getattr" title="getattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">getattr()</span></code></a></p></td>
<td><a class="reference internal" href="#locals" title="locals"><code class="xref py py-func docutils literal notranslate"><span class="pre">locals()</span></code></a></p></td>
<td><a class="reference internal" href="#repr" title="repr"><code class="xref py py-func docutils literal notranslate"><span class="pre">repr()</span></code></a></p></td>
<td><a class="reference internal" href="#zip" title="zip"><code class="xref py py-func docutils literal notranslate"><span class="pre">zip()</span></code></a></p></td>
</tr>
</tr>
<tr class="row-even"><td><a class="reference internal" href="#compile" title="compile"><code class="xref py py-func docutils literal notranslate"><span class="pre">compile()</span></code></a></p></td>
<td><a class="reference internal" href="#globals" title="globals"><code class="xref py py-func docutils literal notranslate"><span class="pre">globals()</span></code></a></p></td>
<td><a class="reference internal" href="#map" title="map"><code class="xref py py-func docutils literal notranslate"><span class="pre">map()</span></code></a></p></td>
<td><a class="reference internal" href="#reversed" title="reversed"><code class="xref py py-func docutils literal notranslate"><span class="pre">reversed()</span></code></a></p></td>
<td><a class="reference internal" href="#__import__" title="__import__"><code class="xref py py-func docutils literal notranslate"><span class="pre">__import__()</span></code></a></p></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="#complex" title="complex"><code class="xref py py-func docutils literal notranslate"><span class="pre">complex()</span></code></a></p></td>
<td><a class="reference internal" href="#hasattr" title="hasattr"><code class="xref py py-func docutils literal notranslate"><span class="pre">hasattr()</span></code></a></p></td>
<td><a class="reference internal" href="#max" title="max"><code class="xref py py-func docutils literal notranslate"><span class="pre">max()</span></code></a></p></td>
<td><a class="reference internal" href="#round" title="round"><code class="xref py py-func docutils literal notranslate"><span class="pre">round()</span></code></a></p></td>
<td></td>
</tr>
</tbody>
</table>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;各个内置函数的具体功能和用法，可以查看：[https://docs.python.org/zh-cn/3/library/functions.html](https://docs.python.org/zh-cn/3/library/functions.html)