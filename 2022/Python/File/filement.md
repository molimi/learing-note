&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;实际开发中常常会遇到对数据进行持久化操作的场景，而实现数据持久化最直接简单的方式就是将数据保存到文件中。对文件的一般操作包括打开文件、读取和追加数据、插入和删除数据、关闭文件、删除文件等。

## 1 文件路径
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于文件，有两个关键属性，分别是“文件名”和“路径”，文件名指的是为每个文件设定的名称，而路径则用来指明文件在计算机上的位置。比如`Windows`系统下的：`D:\demo\exercise\project.docx`。

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：**在`Windows`上，路径书写使用反斜杠`\`作为文件夹之间的分隔符。但在`OSX`和`Linux`上，使用正斜杠`/`作为它们的路径分隔符。如果想要程序运行在所有操作系统上，在编写`Python`脚本时，就必须处理这两种情况。不过后面可以`os.path.join()`函数来处理这个问题。

### 1.1 绝对路径与相对路径

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;每个运行在计算机上的程序，都有一个“当前工作目录”（或`cwd`）。所有没有从根文件夹开始的文件名或路径，都假定在当前工作目录下。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;明确一个文件所在路径，有两种方式，分别是：
- 绝对路径：总是从根文件夹开始，`Window`系统中以盘符（C：、D：）作为根文件夹，而`OS X`或者`Linux`系统中以 / 作为根文件夹。
- 相对路径：指的是文件相对于当前工作目录所在的位置。例如，当前工作目录为 `"C:\Windows\System32"`，若文件`demo.txt`就位于这个`System32`文件夹下，则`demo.txt`的相对路径表示为`".\demo.txt"`（其中`.\`就表示当前所在目录）。后面会讲`os`模块怎么处理文件路径问题。

_____

## 2 基本操作
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中，对文件的操作有很多种，常见的操作包括创建、删除、修改权限、读取、写入等，这些操作可大致分为以下 2 类：
- 删除、修改权限：作用于文件本身，属于系统级操作。
- 写入、读取：是文件最常用的操作，作用于文件的内容，属于应用级操作。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中，<font color=#9900CC><strong>对文件的系统级操作功能单一，比较容易实现，可以借助`Python`中的专用模块（os、sys 等），并调用模块中的指定函数来实现</font></strong>。见下一节介绍。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=#9900CC><strong>对于文件的应用级操作</font></strong>，在`Python`中实现文件的读写操作其实非常简单，通过`Python`内置的`open`函数，我们可以指定文件名、操作模式、编码信息等来获得操作文件的对象；接下来就可以对文件进行读写操作了，读取文件内容可使用`read()`、`readline()`以及`readlines()`函数；向文件中写入内容，可以使用`write()`函数；最后，完成对文件的读/写操作之后，需要关闭文件，可以使用`close()`函数。这里所说的操作模式是指要打开什么样的文件（字符文件还是二进制文件）以及做什么样的操作（读、写还是追加），具体的如下表所示。
<center>表1 open函数支持的文件打开模式</center>

| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `r`      | 读取（默认）                     |
| `w`      | 写入（会先）                     |
| `x`      | 写入，如果文件已经存在会产生异常 |
| `a`      | 追加，将内容写入到已有文件的末尾 |
| `b`      | 二进制模式                       |
| `t`      | 文本模式（默认）                 |
| `+`      | 更新（即可以读又可以写）         |


### 2.1 读和写文件
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`中，如果想要操作文件，首先需要创建或者打开指定的文件，并创建一个文件对象，而这些工作可以通过内置的`open()`函数实现。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`open()`函数用于创建或打开指定文件，该函数的常用语法格式如下：
```python
file = open(file_name [, mode='r' [ , buffering=-1 [ , encoding = None ]]])
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此格式中，用`[]`括起来的部分为可选参数，即可以使用也可以缺省。其中，各个参数所代表的含义如下：
- file：表示要创建的文件对象。
- file_name：要创建或打开文件的文件名称，该名称要用引号（单引号或双引号都可以）括起来。需要注意的是，如果要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可；否则，此参数需要指定打开文件所在的完整路径。
- mode：可选参数，用于指定文件的打开模式。可选的打开模式如表 1 所示。如果不写，则默认以只读（r）模式打开文件。
- buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区（通常使用缓冲区，建议不需要修改 buffing 参数的值）。
- encoding：手动设定打开文件时所使用的编码格式，不同平台的`encoding`参数值也不同，以`Windows`为例，其默认为`cp936`（实际上就是 GBK 编码）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`open()`函数支持的文件打开模式，可以参考表1和下图1进行学习。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/a9eecc54f13f4b8eb28a822840b5e7ab.png#pic_center" width=75%> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1 常用模式</div> </center>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**注意**，手动修改`encoding`参数的值，仅限于文件以文本的形式打开，也就是说，以二进制格式打开时，不能对`encoding`参数的值做任何修改，否则程序会抛出`ValueError`异常，


### 2.2 文件对象
#### 2.2.1 文件对象的属性
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;成功打开文件之后，可以调用文件对象本身拥有的属性获取当前文件的部分信息，其常见的属性为：
- file.name：返回文件的名称；
- file.mode：返回打开文件时，采用的文件打开模式；
- file.encoding：返回打开文件时使用的编码格式；
- file.closed：判断文件是否己经关闭。


#### 2.2.2 文件对象的方法
**1. file.read()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了读取一个文件的内容，调用`file.read([size])`, 这将读取一定数目的数据, 然后作为字符串或字节对象返回。`size`是一个可选的数字类型的参数。 当 `size`被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果文件是以文本模式（非二进制模式）打开的，则`read()`函数会逐个字符进行读取；反之，如果文件以二进制模式打开，则`read()`函数会逐个字节进行读取。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**注意**，如果目标文件使用的编码格式和`open()`函数打开该文件时使用的编码格式不匹配，`Python`解释器会提示`UnicodeDecodeError`。要么将`open()`函数中的`encoding`参数值修改为和目标文件相同的编码格式，要么重新生成目标文件（即将该文件的编码格式改为和`open()`函数中的`encoding`参数相同）。还有一种方法：先使用二进制模式读取文件，然后调用`bytes`的`decode()`方法，使用目标文件的编码格式，将读取到的字节串转换成认识的字符串。
```python
# 以二进制形式打开指定文件，该文件编码格式为 utf-8
f = open('myfile.txt', 'rb+')
byt = f.read()
print(byt)
print("\n转换后：")
print(byt.decode('utf-8'))
f.close()
```

**2. file.readline()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`file.readline()`会从文件中读取单独的一行。对于读取以文本格式打开的文件，读取一行很好理解；对于读取以二进制格式打开的文件，它们会以`“\n”`作为读取一行的标志。`file.readline()`如果返回一个空字符串, 说明已经已经读取到最后一行。

**3. file.readlines()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`readlines()`函数用于读取文件中的所有行，它和调用不指定`size`参数的`read()`函数类似，只不过该函数返回是一个字符串列表，其中每个元素为文件中的一行内容。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以使用`for-in`循环逐行读取或者用`readlines`方法将文件按行读取到一个列表容器中，代码如下所示。
```python
# 通过for-in循环逐行读取
with open('myfile.txt', mode='r') as f:
    for line in f:
        print(line, end='')
        time.sleep(0.5)
print()

# 读取文件按行读取到列表中
with open('myfile.txt') as f:
    lines = f.readlines()
print(lines)
```

**4. file.write()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f.write(string)`将`string`写入到文件中, 然后返回写入的字符数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`的文件对象中，不仅提供了`write()`函数，还提供了`writelines()`函数，可以实现将字符串列表写入文件中。


**5. file.tell()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f.tell()`返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。


**6. file.seek()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果要改变文件当前的位置, 可以使用`f.seek(offset, from_what)`函数。`from_what`的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
- seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
- seek(x,1) ： 表示从当前位置往后移动x个字符
- seek(-x,2)：表示从文件的结尾往前移动x个字符

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 注意，当`offset`值非 0 时，`Python`要求文件必须要以二进制格式打开，否则会抛出`io.UnsupportedOperation`错误。

**7. file.close()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;前面一直强调打开的文件最后一定要关闭，否则会程序的运行造成意想不到的隐患。但是，即便使用`close()`做好了关闭文件的操作，如果在打开文件或文件操作过程中抛出了异常，还是无法及时关闭文件。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了更好地避免此类问题，不同的编程语言都引入了不同的机制。在`Python`中，对应的解决方式是使用`with as`语句操作[上下文管理器](http://c.biancheng.net/view/5319.html)（context manager），它能够帮助我们自动分配并且释放资源。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`with as`操作已经打开的文件对象（本身就是上下文管理器），无论期间是否抛出异常，都能保证`with as`语句执行完毕后自动关闭已经打开的文件。
```python
with open('myfile.txt', 'r') as f:
    read_data = f.read()
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**补充：**`file.isatty()`表示如果文件连接到一个终端设备返回`True`，否则返回 `False`。

### 2.3 常用模块
#### 2.3.1 os.path模块
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果将单个文件和路径上的文件夹名称的字符串传递给它，`os.path.join()` 就会返回一个文件路径的字符串，包含正确的路径分隔符。
```python
import os
os.path.join('demo', 'exercise')
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此程序是在`Windows`上运行的，所以`os.path.join('demo', 'exercise')`返回 'demo\\exercise'（请注意，反斜杠有两个，因为每个反斜杠需要由另一个反斜杠字符来转义）。如果在`OS X`或`Linux`上调用这个函数，该字符串就会是 'demo/exercise'。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`os`模块提供了非常丰富的方法用来处理文件和目录。常用的方法可以参考[OS 文件/目录方法](https://www.runoob.com/python3/python3-os-file-methods.html)


#### 2.3.2 pickle模块

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中有个序列化过程叫作`pickle`，它能够实现任意对象与文本之间的相互转化，也可以实现任意对象与二进制之间的相互转化。也就是说，`pickle`可以实现 `Python`对象的存储及恢复。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pickle`模块提供了以下 4 个函数供我们使用：
- dumps()：将 Python 中的对象序列化成二进制对象，并返回；
- loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；
- dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
- load()：读取指定的序列化数据文件，并返回对象。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;以上这 4 个函数可以分成两类，其中`dumps`和`loads`实现基于内存的 Python 对象与二进制互转；`dump`和`load`实现基于文件的 Python 对象与二进制互转。
```python
import pickle

tup1 = ('Python', {1, 2, 3}, None)
p1 = pickle.dumps(tup1)  # 序列化成二进制对象
t2 = pickle.loads(p1)  # 发序列化成Python对象
with open("a.txt", 'wb') as f:  # 打开文件
    pickle.dump(tup1, f)  # 用 dump 函数将 Python 对象转成二进制对象文件
with open("a.txt", 'rb') as f:  # 打开文件
    t3 = pickle.load(f)  # 将二进制文件对象转换成 Python 对象
```
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;看似强大的`pickle`模块，其实也有它的短板，即`pickle`不支持并发地访问持久性对象，在复杂的系统环境下，尤其是读取海量数据时，使用`pickle`会使整个系统的I/O读取性能成为瓶颈。这种情况下，可以使用`ZODB`。
> 
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ZODB`是一个健壮的、多用户的和面向对象的数据库系统，专门用于存储 Python 语言中的对象数据，它能够存储和管理任意复杂的 Python 对象，并支持事务操作和并发控制。并且`ZODB`也是在 Python 的序列化操作基础之上实现的，因此要想有效地使用`ZODB`，必须先学好`pickle`。

#### 2.3.3 fileinput模块

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`提供了`fileinput`模块，通过该模块中的`input()`函数，我们能同时打开指定的多个文件，还可以逐个读取这些文件中的内容。和`open()`函数返回单个的文件对象不同，`fileinput`对象无需调用类似`read()`、`readline()`、`readlines()`这样的函数，直接通过`for`循环即可按次序读取多个文件中的数据。
```python
import fileinput
# 使用for循环遍历fileinput对象
for line in fileinput.input(file=('myfile.txt', 'file.txt')):
    print(line)  # 输出读取到的内容
fileinput.close()  # 关闭文件流
```
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意，和`open()`函数不同，`input()`函数不能指定打开文件的编码格式，这意味着使用该函数读取的所有文件，除非以二进制方式进行读取，否则该文件编码格式都必须和当前操作系统默认的编码格式相同，不然 Python 解释器可能会提示`UnicodeDecodeError`错误。

#### 2.3.4 linecache模块

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果我们想读取某个文件中指定行包含的数据，可以使用`linecache`模块。`linecache`模块常用来读取`Python`源文件中的代码，它使用的是`UTF-8`编码格式来读取文件内容。这意味着，使用该模块读取的文件，其编码格式也必须为 `UTF-8`，否则要么读取出来的数据是乱码，要么直接读取失败（`Python`解释器会报`SyntaxError`异常）。
```python
import linecache
import string

print(linecache.getline(string.__file__, 3))  # 读取string模块中的第三行数据
print(linecache.getline('myfile.txt', 2))  # 读取普通文件的第二行
```

**补充：**
- `pathlib`模块的操作对象是各种操作系统中使用的路径（例如指定文件位置的路径，包括绝对路径和相对路径）。详细了解，请阅读：[pathlib模块用法详解](http://c.biancheng.net/view/2541.html)
- `fnmatch`模块主要用于文件名称的匹配，其能力比简单的字符串匹配更强大，但比使用正则表达式相比稍弱。如果在数据处理操作中，只需要使用简单的通配符就能完成文件名的匹配，则可以考虑使用`fnmatch`模块。
- `tempfile`模块专门用于创建临时文件和临时目录，它既可以在`UNIX`平台上运行良好，也可以在`Windows`平台上运行良好。

____

## 3 代码实现
### 3.1 读写文本文件

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;读取文本文件时，需要在使用`open`函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为`'r'`（如果不指定，默认值也是`'r'`），然后通过`encoding`参数指定编码（如果不指定，默认值是`None`，那么在读取文件时使用的是操作系统默认的编码），如果不能保证保存文件时使用的编码方式与`encoding`参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取失败。下面的例子演示了如何读取一个纯文本文件。
```python
f = open('myfile.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;温馨提示，如果`open`函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。为了让代码有一定的健壮性和容错性，我们可以使用`Python`的异常机制对可能在运行时发生状况的代码进行适当的处理，如下所示。
```python
f = None
try:
    f = open('myfile.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
finally:
    if f:
        file.close()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果不愿意在`finally`代码块中关闭文件对象释放资源，也可以使用上下文语法，通过`with`关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示。
```python
try:
    with open('myfile.txt', 'r', encoding='utf-8') as f:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要将文本信息写入文件文件也非常简单，在使用`open`函数时指定好文件名并将文件模式设置为`'w'`即可。注意如果需要对文件内容进行追加式写入，应该将模式设置为`'a'`。如果要写入的文件不存在会自动创建文件而不是引发异常。



### 3.2  读写二进制文件
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;读写二进制文件和读写文本文件类似，下面的代码实现了复制图片文件的功能。
```python
try:
    with open('001.jpg', 'rb') as fs1:
        data = fs1.read()
        print(type(data))  # <class 'bytes'>
    with open('002.jpg', 'wb') as fs2:
        fs2.write(data)
except FileNotFoundError as e:
    print('指定的文件无法打开.')
except IOError as e:
    print('读写文件时出现错误.')
print('程序执行结束.')
```

### 3.3 读写JSON文件

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？答案是将数据以`JSON`格式进行保存。`JSON`是`JavaScript Object Notation`的缩写，它本来是`JavaScript`语言中创建对象的一种字面量语法，现在已经被广泛的应用于跨平台跨语言的数据交换，原因很简单，因为`JSON`也是纯文本，任何系统任何编程语言处理纯文本都是没有问题的。了解更多可以参考：[JSON的官方网站](https://www.json.org/json-en.html)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们使用`Python`中的`json`模块就可以将字典或列表以`JSON`格式保存到文件中，代码如下所示。

```python
import json
mydict = {
    'name': 'carpediem',
    'age': 38,
    'qq': 957658,
    'friends': ['Tom', 'David'],
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}
try:
    with open('data.json', 'w', encoding='utf-8') as fs:
        json.dump(mydict, fs)
except IOError as e:
    print(e)
print('保存数据完成!')
```
`json`模块主要有四个比较重要的函数，分别是：
- dump - 将Python对象按照JSON格式序列化到文件中
- dumps - 将Python对象处理成JSON格式的字符串
- load - 将文件中的JSON数据反序列化成对象
- loads - 将字符串的内容反序列化成Python对象


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;了解序列化和反序列化，可以参考：[https://mp.weixin.qq.com/s/0EfIUB9E-0Oh_Clwuxswuw](https://mp.weixin.qq.com/s/0EfIUB9E-0Oh_Clwuxswuw)

_____

## 4 目录操作

目录也称文件夹，用于分层保存文件。通过目录可以分门别类地存放文件。也可以通过目录快速找到想要的文件。在Python中，并没有提供直接操作目录的函数或者对象，而是需要使用内置的`os`和`os.path`模块实现。下面代码的演示主要以Windows系统为例。

> `os`模块是Python内置的与操作系统功能和文件系统相关的模块。该模块中的语句的执行结果通常与操作系统有关，在不同操作系统上运行，可能会得到不一样的结果。常用的目录操作主要有判断目录是否存在、创建目录、删除目录和遍历目录等。


### 4.1 os和os.path模块
1. os.name
用于获取操作系统类型，如果`os.name`的输出结果为nt，则表示是Windows操作系统；如果是posix，则表示是Linux、Unix或 Mac OS操作系统。

2. os.linesep
用于获取当前操作系统的换行符。

3. os.sep
用于获取当前系统所使用的路径分隔符。

### 4.2 路径
第一部分已经介绍了绝对路径和相对路径，
<center>os模块提供的与目录相关的函数</center>
| 函数                               | 说明                                                                          |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| getcwd()                           | 返回当前工作目录                                                              |
| listdir(path)                      | 返回指定路径下的文件和目录信息                                                |
| mkdir(path [,mode])                | 创建目录                                                                      |
| makedirs(path1/path2······[,mode]) | 创建多级目录                                                                  |
| rmdir(path)                        | 删除目录                                                                      |
| removedirs(path1/path2······）     | 删除多级目录                                                                  |
| chdir(path)                        | 把path设置为当前工作目录                                                      |
| walk(top[,topdown[,onerror]])      | 遍历目录树，该方法返回一个元组，包括所有路径名、所有目录列表和文件列表3个元素 |

<center>os.path模块提供的与目录相关的函数</center>
| 函数             | 说明                                                            |
| ---------------- | --------------------------------------------------------------- |
| abspath(path)    | 用于获取文件或目录的绝对路径                                    |
| exists(path)     | 用于判断目录或者文件是否存在，如果存在则返回True，否则返回False |
| join(path, name) | 将目录与目录或者文件名拼接起来                                  |
| splitext()       | 分离文件名和扩展名                                              |
| basename(path)   | 从一个目录中提取文件名                                          |
| dirname(path)    | 从一个路径中提取文件路径，不包括文件名                          |
| isdir(path)      | 用于判断是否为有效路径                                          |


**1. 相对路径**


**2. 绝对路径**


**3. 拼接路径**


### 4.3 判断目录是否存在



### 4.4 创建目录




### 4.5 删除目录


### 4.6 遍历目录


## 5 高级文件操作
### 5.1 删除文件



### 5.2 重命名文件和目录


### 5.3 获取文件基本信息


______

## 参考
- Python文件操作：[http://c.biancheng.net/python/file/](http://c.biancheng.net/python/file/)
- I/O编程：[https://www.liaoxuefeng.com/wiki/1016959663602400/1017606916795776](https://www.liaoxuefeng.com/wiki/1016959663602400/1017606916795776)
- 文件操作：[https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15)