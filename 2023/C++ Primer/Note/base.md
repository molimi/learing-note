
C++ 语言是在优化 C 语言的基础上为支持面向对象的程序设计而研制的一个通用目的的程序设计语言。在后来的持续研究中，C++ 增加了许多新概念，例如虚函数、重载、继承、标准模板库、异常处理、命名空间等。

C++ 语言的特点主要表现在两个方面：全面兼容 C 语言 和 支持面向对象的方法。

## 1 基础知识
### 1.1 扩展名
C语言源文件的后缀非常统一，在不同的编译器下都是.c。C++ 源文件的后缀则有些混乱，不同的编译器支持不同的后缀，下表是一个简单的汇总：

<table><tbody><tr><th>编译器</th><td>Microsoft Visual C++</td><td>GCC（GNU C++）</td><td>Borland C++</td><td>UNIX</td></tr>
<tr><th>后缀</th><td>cpp、cxx、cc</td><td>cpp、cxx、cc、c++、C</td><td>cpp</td><td>C、cc、cxx</td></tr></tbody></table>

通常使用 `.cpp` 作为 C++ 源文件的后缀，这样更加通用和规范。


### 1.2 注释符

- 单行注释：//注释内容
```cpp
int x;   // 定义 x 的数据类型为 int
```
- 块注释：/* 注释内容 */
```cpp
if(x>y)return x;
else return y;
/* 如果 x 大于 y 则返回 x
否则返回 y */
```
注释符可以放置在代码的任何位置，且不参与代码运行。

### 1.3 头文件声明

最简单的C++程序往往是下面这样声明头文件：
```cpp
//C++中常用写法
#include < iostream >      //引用C++标准头文件库
using namespace std;      //使用名字空间
```
`#include` 为C/C++中包含头文件命令，用于将指定头文件嵌入源文件中。`#include`一般用在 C、C++ 等语系的编译环境（编程软件的编程代码）中，也即告诉你，在这个地方要插入一堆代码，而这堆代码在另一个文件里。

`iostream`是 C++ 的一个头文件库，在安装 C++ 环境的时候就已安装于电脑中，只需要用 include 将该它包含进来，就可以使用它的代码。

C++已把标准C++库的组件放在一个名位std的namespace里面中，如果include头文件的时候加上.h，默认有`using namespace`，否则需要自己加上 `using namespace std`。

因此若没有第二行语句，cout 就会没有定义，除非使用 cout 时写成 `std::cout`，即指明其来自空间std 。

按照 C 语言规则声明则是下面这样：
```c
#include < iostream. h >    //引用头文件，不需要声明名字空间
```
不加.h的是现在 C++ 中规定的标准，目的在于使C++代码用于移植和混合嵌入时不受扩展名 .h 的限制，避免因为.h而造成的额外的处理和修改。而加.h是c语言的用法，但是在c++中也支持这种用法，主要是为了向下兼容c 的内容，平时尽量不用这种方法 。

在C++程序中，头文件不再以“.h”结尾，一些在C语言中常用的头文件在C++中的名字变为去掉“.h”，并在开头增加字符 c 。例如：

```cpp
#include < cstdio >   //标准化后经过改造的C标准库，所有的组件都放在了std中
#include < cstring >  //C++标准库下，基于char* 的字符处理函数库
#include < string >   //增加了C++类的字符处理函数库
#include < cstdlib >  
#include < bits/stdc++.h>  //号称万能库，在大部分情况下使用这一行就可以省去其他库的生声明
```

<stdio.h>是以往 C 和 C++ 的头文件，<cstdio>是标准C++（STL）函数库中的头文件，且 cstdio 中的函数都定义在一个名称空间 std 里面，如果要调用这个名字空间的函数，须加`std::`或者在文件中声明 `using namespace std`。

<string.h> 是标准C提供的字符处理函数集。面向char *.。<cstring> 是C++为兼容C提供的 <string.h> 的C++版本，里面的主要改进有：将一些隐藏变量编入命名空间；修正一些C++编译器认为Bug的代码。

<stdlib.h>可以提供一些函数与符号常量，<cstdlib>是C++为兼容C提供的版本。


### 1.4 命名空间

命名空间里面包含了逻辑结构上相互关联的一组类、函数、模板等。命名空间像是一个容器，把某些在逻辑结构上相关的 “对象” 放在一起并与外界区分。特别的，命名空间里的变量名或类名可以和命名空间外的变量名或类名重名。

使用命名空间的时候，我们可以用 花括号 把声明块括起来，再以关键字 namespace 开头并命名，其基本格式如下：

```cpp
namespace 命名空间的名字
{
    声明块
}
``

其中声明块中可以包含变量、类、函数等。例如：
```cpp
namespace S
{
    int x;
    void FunA()
    {
        ...
    }
}
```

在命名空间外使用命名空间内的成员：命名空间的名字加上作用域运算符 `::`。

参考上例 namespace S，若访问 x，可写成 `S::x`；访问 `FunA()` 则为 `S::FunA()`。

命名空间的嵌套， 具有分层屏蔽的作用。例如：

```cpp
namespace S1
{
    namespace S2
    {
        int x;
        void FunA()
        {
        ...
        }
    }
}
```

若要访问 x，则可写为 `S1::S2::x`，同理，访问 FunA() 则可写为 `S1::S2::FunA()`。

using 声明：若命名空间内的某个成员使用了 using 声明，那么这个成员在程序的后续使用中，可直接使用成员名，无需添加限定修饰名。使用 using 声明：以关键字 using 开头后跟命名空间内的成员名。参考上例嵌套的命名空间：

namespace S2 中 int x 的 using 声明为：`using S1::S2::x`;

注意： using namespace 后不能加类名或变量名。同上，若 namespace S2 中 int x 的 using 声明写为 `using namespace S1::S2::x` 便是错误的。

using 指示符可以一次性地使命名空间内的全体成员被直接使用。using 指示符的使用： 以关键字 `using namespace` 开头后跟命名空间名字。特别的，std 命名空间声明和定义了标准 C++ 库中的所有组件，使用 `using namespace std`; 则可使用标准 C++ 库中的所有成员。

### 1.5 输入与输出

C++ 标准 I/O 库包含 iostream、fstream 和 sstringstream。iostream、fstream 比较常用，一般操作于输入和输出，相较于前两者来说 sstringstream 的出现频率就低了许多，一般操作于数据的格式化。为了能更好的理解 C++ 语言的标准 I/O 库，我们参考 cplusplus 官网 的相关内容，整理注释了一份关于输入输出流类继承体系的关系图：

<img src ="https://img-blog.csdnimg.cn/0fd6204b58c04c68ac0c1efe15e5f03f.png#pic_center" width = 64%>

**1. 标准输出流对象 cout**
预定义的插入符 “ << ” 作用在流类对象 cout 上可实现最基本的屏幕输出，其格式为：
```cpp
cout << 表达式1 << 表达式2...;
```
在输出语句中，若串联多个插入符，则可输出多个数据项。例如：

cout << a << b << c;

则依次输出 a,b,c 三个数据项的值。

若插入符后面是复杂的表达式，则系统自动计算其表达式的值并传给插入符。例如：

```cpp
cout << "a+b=" << a+b;
```
依次输出字符串 “ a+b= ” 以及 a+b 的计算结果。

**2. 标准输入流对象 cin**

预定义的提取符 “ >> ” 作用在流类对象 cin 上可实现对键盘输入的提取操作，其格式为：

```cpp
cin >> 表达式1 >> 表达式2...
```

其中表达式通常用于存放输入值的变量。例如：

```cpp
int a,b;
cin >> a >> b;
```
即编译执行后，输入 a 和 b 的值，a 和 b 之间使用空格分隔。如输入：1 2，则给 a 赋值为 1，b 赋值为 2。

**3. 简单的 I/O 格式控制**

一般情况下，使用 cin 和 cout 进行数据的输入和输出时，会自动按照默认的格式进行处理。如若需要设定特殊的格式，可利用 C++ I/O 流类库提供的操纵符进行调整。这些操纵符可直接嵌入到输入输出语句中实现格式控制。常用的 I/O 流类库操纵符，请阅读：[C++ 基本的输入输出](https://www.runoob.com/cplusplus/cpp-basic-input-output.html)


### 1.6 编译和运行C++程序

C/C++ 代码生成可执行文件的过程：

<img src ="https://img-blog.csdnimg.cn/11085cee60b84514924f81aa57082721.jpeg#pic_center" width = 64%>

我们常见的编译器有两个：
- gcc 编译器
- g++ 编译器
gcc和g++都是GNU(组织)的编译器。


程序 g++ 是将 gcc 默认语言设为 C++ 的一个特殊的版本，链接时它自动使用 C++ 标准库而不用 C 标准库。通过遵循源码的命名规范并指定对应库的名字，用 gcc 来编译链接 C++ 程序是可行的，如下例所示：

```bash
$ gcc main.cpp -lstdc++ -o main
```
新建一个helloworld.cpp文件，最简单的编译方式：

```bash
$ g++ helloworld.cpp
```
由于命令行中未指定可执行程序的文件名，编译器采用默认的 a.out。程序可以这样来运行：
```bash
$ ./a.out
Hello, world!
```

通常我们使用 -o 选项指定可执行程序的文件名，以下实例生成一个 helloworld 的可执行文件：
```bash
$ g++ helloworld.cpp -o helloworld
```

执行 helloworld:
```bash
$ ./helloworld
Hello, world!
```

如果是多个 C++ 代码文件，如 runoob1.cpp、runoob2.cpp，编译命令如下：
```bash
$ g++ runoob1.cpp runoob2.cpp -o runoob
```

生成一个 runoob 可执行文件。

g++ 有些系统默认是使用 C++98，我们可以指定使用 C++11 来编译 main.cpp 文件：

```bash
g++ -g -Wall -std=c++11 main.cpp
```
g++ 常用命令选项：请阅读：[g++ 常用命令选项](https://www.runoob.com/cplusplus/cpp-environment-setup.html)


> gcc和g++编译器的区别
> g++：会把.c和.cpp的文件都当作是C++的源程序进行编译。
> gcc：会把.c的程序当作是C的源程序进行编译，.cpp 的程序当作是C++的源程序进行编译

_____

### 参考
- C++语言：[https://www.lanqiao.cn/courses/2752/learning/?id=47676&compatibility=false](https://www.lanqiao.cn/courses/2752/learning/?id=47676&compatibility=false)
- 从C到C++：[http://c.biancheng.net/view/2191.html](http://c.biancheng.net/view/2191.html)
- C++基础：[https://www.runoob.com/cplusplus/cpp-environment-setup.html](https://www.runoob.com/cplusplus/cpp-environment-setup.html)
- 头文件声明：[https://blog.csdn.net/weixin_39737764/article/details/](https://blog.csdn.net/weixin_39737764/article/details/113052835#:~:text=C%2B%2B%E5%B7%B2%E6%8A%8A%E6%A0%87%E5%87%86C%2B%2B%E5%BA%93%E7%9A%84%E7%BB%84%E4%BB%B6%E6%94%BE%E5%9C%A8%E4%B8%80%E4%B8%AA%E5%90%8D%E4%BD%8Dstd%E7%9A%84namespace%E9%87%8C%E9%9D%A2%E4%B8%AD%EF%BC%8C%E5%A6%82%E6%9E%9Cinclude%E5%A4%B4%E6%96%87%E4%BB%B6%E7%9A%84%E6%97%B6%E5%80%99%E5%8A%A0%E4%B8%8A.h%EF%BC%8C%E9%BB%98%E8%AE%A4%E6%9C%89using%20namespace%EF%BC%8C%E5%90%A6%E5%88%99%E9%9C%80%E8%A6%81%E8%87%AA%E5%B7%B1%E5%8A%A0%E4%B8%8A%20using%20namespace%20std%E3%80%82,%E5%9B%A0%E6%AD%A4%E8%8B%A5%E6%B2%A1%E6%9C%89%E7%AC%AC%E4%BA%8C%E8%A1%8C%E8%AF%AD%E5%8F%A5%EF%BC%8Ccout%E5%B0%B1%E4%BC%9A%E6%B2%A1%E6%9C%89%E5%AE%9A%E4%B9%89%EF%BC%8C%E9%99%A4%E9%9D%9E%E4%BD%BF%E7%94%A8cout%E6%97%B6%E5%86%99%E6%88%90%20std%20%3A%3A%20cout%EF%BC%8C%E5%8D%B3%E6%8C%87%E6%98%8E%E5%85%B6%E6%9D%A5%E8%87%AA%E7%A9%BA%E9%97%B4std%20%E3%80%82)
- gcc编译：[https://blog.csdn.net/weixin_41010198/article/details/117523288](https://blog.csdn.net/weixin_41010198/article/details/117523288)