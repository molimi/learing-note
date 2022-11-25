&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在程序运行过程中，经常会遇到各种各样的错误，这些错误统称为“异常”。这些异常有的是由于开发者将关键字敲错导致的，这类错误多数产生的是`SyntaxError: invalid syntax`(无效的语法)，这将直接导致程序不能运行。这类异常是显式的，在开发阶段很容易被发现。还有一类是隐式的，通常和使用者的操作有关。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;异常处理在任何一门编程语言里都是值得关注的一个话题，良好的异常处理可以让你的程序更加健壮，清晰的错误信息更能帮助你快速修复问题。在`Python`中，和不部分高级语言一样，使用了`try/except/else/finally`语句块来处理异常。
<img src="https://img-blog.csdnimg.cn/3eb6c86cfd5e48d7a269953292c3a11f.png#pic_center" width=50%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`有两种错误很容易辨认：语法错误和异常。`Python`的语法错误或者称之为解析错，就是解析代码时出现的错误。当代码不符合`Python`语法规则时，`Python`解释器在解析时就会报出`SyntaxError`语法错误，与此同时还会明确指出最早探测到错误的语句。如少了冒号，或者混用中英文符号的等等。即便 `Python`程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。大多数的异常都不会被程序处理，都以错误信息的形式展现。例如除数为 0、年龄为负数、数组下标越界等。下图列出常见异常：

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/5d9f75e755aa45f4ae61cf0c50e09436.png#pic_center"> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1 Python中常见异常</div> </center>

## 1 异常处理
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当一个程序发生异常时，代表该程序在执行时出现了非正常的情况，无法再执行下去。默认情况下，程序是要终止的。如果要避免程序退出，可以使用捕获异常的方式获取这个异常的名称，再通过其他的逻辑代码让程序继续运行，这种根据异常做出的逻辑处理叫作<font color=#9900CC><strong>异常处理</font></strong>。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;开发者可以使用异常处理全面地控制自己的程序。异常处理不仅仅能够管理正常的流程运行，还能够在程序出错时对程序进行必的处理。大大提高了程序的健壮性和人机交互的友好性。
### 1.1 try/except
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;异常捕捉通常使用`try/except`语句，其基本语法结构如下图所示：
<img src="https://img-blog.csdnimg.cn/1557a05d805342b7b62b5e0db300021d.png#pic_center" width=50%>

```python
# Mutiple exception in one line
try:
    print(a / b)
except (ZeroDivisionError, TypeError) as e:
    print(e)
```
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`try`块有且仅有一个，但`except`代码块可以有多个，且每个`except`块都可以同时处理多种异常。当程序发生不同的意外情况时，会对应特定的异常类型，`Python`解释器会根据该异常类型选择对应的`except`块来处理该异常。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`try`语句的执行流程如下；
- 首先，执行`try`子句（在关键字`try`和关键字`except`之间的语句）。
- 如果没有异常发生，忽略`except`子句，`try`子句执行后结束。
- 如果在执行`try`子句的过程中发生了异常，那么`try`子句余下的部分将被忽略，系统会自动生成一个异常类型，并将该异常提交给 Python 解释器，此过程称为捕获异常。如果异常的类型和`except`之后的名称相符，那么对应的`except`子句将被执行，这个过程被称为处理异常。
- 如果一个异常没有与任何的`except`匹配，那么这个异常将会传递给上层的`try`中，且程序运行终止，Python 解释器也将退出。
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 不管程序代码块是否处于`try`块中，甚至包括 `except`块中的代码，只要执行该代码块时出现了异常，系统都会自动生成对应类型的异常。但是，如果此段程序没有用 `try`包裹，又或者没有为该异常配置处理它的`except`块，则`Python`解释器将无法处理，程序就会停止运行；反之，如果程序发生的异常经`try`捕获并由`except`处理完成，则程序可以继续执行。

### 1.2 try/except...else
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在原本的`try except`结构的基础上，`Python`异常处理机制还提供了一个`else`块，也就是原有`try except`语句的基础上再添加一个`else`块，即`try except else`结构。如果使用`else`块，那么必须放在所有的`except`子句之后。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`else`包裹的代码，只有当`try`块没有捕获到任何异常时，才会得到执行；反之，如果`try`块捕获到异常，即便调用对应的`except`处理完异常，`else`块中的代码也不会得到执行。

<img src="https://img-blog.csdnimg.cn/0c9db3cc01bd4b999303e60d669b98a1.png#pic_center" width=50%>

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`else`子句比把所有的语句都放在`try`子句里面要好，这样可以避免一些意想不到，而`except`又无法捕获的异常。

### 1.3 try-finally
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`异常处理机制还提供了一个`finally`语句，通常用来为`try`块中的程序做扫尾清理工作。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意，和`else`语句不同，`finally`只要求和`try`搭配使用，而至于该结构中是否包含`except`以及`else`，对于 `finally`不是必须的（`else`必须和`try except`搭配使用）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在整个异常处理机制中，`finally`语句的功能是：无论`try`块是否发生异常，最终都要进入`finally`语句，并执行其中的代码块。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;基于`finally`语句的这种特性，在某些情况下，当`try`块中的程序打开了一些物理资源（文件、数据库连接等）时，由于这些资源必须手动回收，而回收工作通常就放在`finally`块中。
`Python`垃圾回收机制，只能帮我们回收变量、类对象占用的内存，而无法自动完成类似关闭文件、数据库连接等这些的工作。
<img src="https://img-blog.csdnimg.cn/8408e33177c64dc18255bcf1e77bbd33.png#pic_center" width=50%>

```python
def main():
    f = None
    try:
        f = open('myfile.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    except Exception as e:
        print('Unexpected Error: {}'.format(e))
    finally:
        if f:
            f.close()
main()
```
### 1.4  抛出异常
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果你需要自主抛出异常一个异常，可以使用`raise`关键字，等同于C#和Java中的`throw`，有如下三种常用的用法：
- `raise`：单独一个`raise`。该语句引发当前上下文中捕获的异常（比如在`except`块中），或默认引发`RuntimeError`异常。
- `raise`异常类名称：`raise`后带一个异常类名称，表示引发执行类型的异常。
 - `raise`异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。

```python
try:
    a = input("输入一个数：")
    if(not a.isdigit()):
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：",repr(e))
    raise
```
<img src="https://img-blog.csdnimg.cn/ee1770b7970b4b6296ca51f7e46d7a8b.png#pic_center" width=50%>

### 1.5 自定义异常
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中自定义自己的异常类型非常简单，只需要要从`Exception`类继承即可(直接或间接)：
```python
class SomeCustomException(Exception):
    pass

class AnotherException(SomeCustomException):
    pass
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一般你在自定义异常类型时，需要考虑的问题应该是这个异常所应用的场景。如果内置异常已经包括了你需要的异常，建议考虑使用内置的异常类型。比如你希望在函数参数错误时抛出一个异常，你可能并不需要定义一个`InvalidArgumentError`，使用内置的`ValueError`即可。

**补充：**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在实际调试程序的过程中，有时只获得异常的类型是远远不够的，还需要借助更详细的异常信息才能解决问题。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;捕获异常时，有 2 种方式可获得更多的异常信息，分别是：
- 使用`sys`模块中的`exc_info`方法；
- 使用`traceback`模块中的相关函数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;了解更多请参考，[Python sys.exc_info()方法：获取异常信息](http://c.biancheng.net/view/4611.html)和[traceback模块：获取异常信息](http://c.biancheng.net/view/2362.html)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python assert`（断言）用于判断一个表达式，在表达式条件为`false`的时候触发异常。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况。

```python
assert 1 == 2   # 判断条件为False，抛出异常
```


## 参考
- Python中的异常处理：[https://segmentfault.com/a/1190000007736783](https://segmentfault.com/a/1190000007736783)
- Python异常处理机制：[http://c.biancheng.net/python/try_except/](http://c.biancheng.net/python/try_except/)
- Python3 错误和异常：[https://www.runoob.com/python3/python3-errors-execptions.html](https://www.runoob.com/python3/python3-errors-execptions.html)
- Built-in Exceptions：[https://docs.python.org/3/library/exceptions.html#exception-hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
