&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;迭代是`Python`最强大的功能之一，是访问集合元素的一种方式。在`Python`中可迭代(Iterable)、迭代器(Iterator)和生成器(Generator)这几个概念是经常用到的，本文主要介绍可迭代(Iterable)、迭代器(Iterator)和生成器(Generator)的定义和使用。

### 1 可迭代对象(Iterbale)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可迭代对象: 简单的说，一个对象(在`Python`里面一切都是对象)只要实现了只要实现了`iter()`方法，那么用`isinstance()`函数检查就是`Iterable`对象；
```python
class IterObj:
    def __iter__(self):
        return self
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上面定义了一个类`IterObj`并实现了`iter`方法，这个就是一个可迭代(Iterable)对象
```python
it = IterObj()
print(isinstance(it, Iterable))     # true
print(isinstance(it, Iterator))     # false
print(isinstance(it, Generator))    # false
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Python中有哪些常见的可迭代对象呢？
1. 集合或序列类型（如list、tuple、set、dict、str）
2. 文件对象
3. 在类中定义了`iter()`方法的对象，可以被认为是`Iterable`对象，但自定义的可迭代对象要能在`for`循环中正确使用，就需要保证`iter()`实现必须是正确的（即可以通过内置`iter()`函数转成`Iterator`对象。关于`Iterator`下文还会说明，这里留下一个坑，只是记住`iter()`函数是能够将一个可迭代对象转成迭代器对象，然后在`for`中使用）
4. 在类中实现了如果只实现`getitem()`的对象可以通过`iter()`函数转化成迭代器但其本身不是可迭代对象。所以当一个对象能够在`for`循环中运行，但不一定是`Iterable`对象。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面我们验证第1、2点，
```python
from typing import Iterable
import os.path

print(isinstance([], Iterable))     # True list是可迭代对象
print(isinstance({}, Iterable))     # True dict是可迭代对象
print(isinstance((), Iterable))     # True tuple是可迭代对象
print(isinstance(set(), Iterable))  # True set是可迭代对象
print(isinstance('', Iterable))     # True string是可迭代对象
Current_Path = os.path.dirname(os.path.abspath(__file__))
with open(Current_Path + '/iter.py') as file:
    print(isinstance(file, Iterable))  # True
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;再来看第3点，         
```python
print(hasattr([], "__iter__"))  # true
print(hasattr({}, "__iter__"))  # true
print(hasattr((), "__iter__"))  # true
print(hasattr('', "__iter__"))  # true
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这些内置集合或序列对象都有`__iter__`属性，即他们都实现了同名方法。但这个可迭代对象要在`for`循环中被使用，那么它就应该能够被内置的`iter()`函数调用并转化成`Iterator`对象。例如，我们看内置的可迭代对象
```python
print(iter([]))     # <list_iterator object at 0x110243f28>
print(iter({}))     # <dict_keyiterator object at 0x110234408>
print(iter(()))     # <tuple_iterator object at 0x110243f28>
print(iter(''))     # <str_iterator object at 0x110243f28>
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;它们都相应的转成了对应的迭代器(Iterator)对象。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;现在回过头再看看一开始定义的那个`IterObj`类
```python
class IterObj:
    
    def __iter__(self):
        return self 
        
it = IterObj()
print(iter(it))
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们使用了`iter()`函数，这时候将再控制台上打印出以下信息：
> TypeError: iter() returned non-iterator of type 'IterObj'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;出现了类型错误，意思是`iter()`函数不能将‘非迭代器’类型转成迭代器。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;那如何才能将一个可迭代(Iterable)对象转成迭代器(Iterator)对象呢？ 我们修改一下IterObj类的定义

```python
class IterObj:

    def __init__(self):
        self.a = [3, 5, 7, 11, 13, 17, 19]

    def __iter__(self):
        return iter(self.a)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们在构造方法中定义了一个名为a的列表，然后还实现了`__iter__()`方法。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;修改后的类是可以被`iter()`函数调用的，即也可以在`for`循环中使用
```python
    it = IterObj()
    print(isinstance(it, Iterable))     # true
    print(isinstance(it, Iterator))     # false
    print(isinstance(it, Generator))    # false
    print(iter(it))     # <list_iterator object at 0x102007278>
    for i in it:
        print(i)        # 将打印3、5、7、11、13、17、19元素
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此在定义一个可迭代对象时，我们要非常注意`__iter__()`方法的内部实现逻辑，一般情况下，是通过一些已知的可迭代对象（例如，上文提到的集合、序列、文件等或其他正确定义的可迭代对象）来辅助我们来实现.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;关于第4点说明的意思是`iter()`函数可以将一个实现了`__getitem__()`方法的对象转成迭代器对象，也可以在`for`循环中使用，但是如果用`isinstance()`方法来检测时，它不是一个可迭代对象。
```python
class IterObj:
    
    def __init__(self):
        self.a = [3, 5, 7, 11, 13, 17, 19]
    
    def __getitem__(self, i):
        return self.a[i]
        
it = IterObj()
print(isinstance(it, Iterable))     # false
print(isinstance(it, Iterator))     # false
print(isinstance(it, Generator)) false
print(hasattr(it, "__iter__"))  # false
print(iter(it))     # <iterator object at 0x10b231278>

for i in it:
    print(i)        # 将打印出3、5、7、11、13、17、19
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这个例子说明了可以在`for`中使用的对象，不一定是可迭代对象。

**小结：**
- 一个可迭代的对象是实现了`__iter__()`方`法的对象
- 它要在`for`循环中使用，就必须满足`iter()`的调用(即调用这个函数不会出错，能够正确转成一个Iterator对象)
- 可以通过已知的可迭代对象来辅助实现我们自定义的可迭代对象
- 一个对象实现了`__getitem__()`方法可以通过`iter()`函数转成`Iterator`，即可以在`for`循环中使用，但它不是一个可迭代对象(可用isinstance方法检测())

____

### 2 迭代器(Iterator)
### 2.1 迭代器对象
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。迭代器有两个基本的方法：`iter()`和`next()`。一个对象实现了`__iter__()`和`__next__()`方法，那么它就是一个迭代器对象。 例如
```python
class IterObj:

    def __init__(self):
        self.a = [3, 5, 7, 11, 13, 17, 19]

        self.n = len(self.a)
        self.i = 0

    def __iter__(self):
        return iter(self.a)

    def __next__(self):
        while self.i < self.n:
            v = self.a[self.i]
            self.i += 1
            return v
        else:
            self.i = 0
            raise StopIteration()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`IterObj`中，构造函数中定义了一个列表a,列表长度n,索引i。
```python
it = IterObj()
print(isinstance(it, Iterable))     # true
print(isinstance(it, Iterator))     # true
print(isinstance(it, Generator))    # false
print(hasattr(it, "__iter__"))      # true
print(hasattr(it, "__next__"))      # true
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;集合和序列对象是可迭代的但不是迭代器，但文件对象是迭代器。
```python
print(isinstance([], Iterator))         # false
print(isinstance({}, Iterator))         # false
print(isinstance((), Iterator))         # false
print(isinstance(set(), Iterator))      # false
print(isinstance('', Iterator))         # false
currPath = os.path.dirname(os.path.abspath(__file__))
with open(currPath+'/model.py') as file:
    print(isinstance(file, Iterator)) # true
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个迭代器(Iterator)对象不仅可以在for循环中使用，还可以通过内置函数`next()`函数进行调用。
```python
# 可迭代对象转为迭代器对象的方法
s = "字符串"
s_iter = s.__iter__()  # 此时的s_iter含有__next__的内置方法，就转为了迭代器对象。

# __next__:从头一次取出迭代器对象中的值。
print(s_iter.__next__())
print(s_iter.__next__())
print(s_iter.__next__())

# 如果迭代器对象中的值被取完之后依然继续取，就会报错。
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;迭代器对象的值一旦被取完，就会“死亡”，不能再进行取值了，在想重新取值的话，就必须重新在赋值然后重新取。

#### 2.2 for循环作用机制
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这时候我们就可以了解一下`for`循环的工作机理了。
```python
# while循环取字典的值。
dic = {"1":2,"2":2}
dic_iter = dic_iter.__iter__()

while True:
    try:
        print(dic_iter.__next__())
    except StopIteration:
        break
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看出来，`while`循环也可以取出字典的值，但是比较麻烦，我们经常用的`for`循环更加的方便，那么`for`循环又是怎么工作的呢？
```python
for k in dic:
	print(k)

# 以上述为例。
# 第一步：首先会进行dic = dic.__iter__(),将可迭代对象转化为迭代器对象
# 第二步：进行dic.__next__的调用，得到返回值给k，然后进行代码块的操作
# 第三步：循环第二步，直到出现StopIteration错误，对错误进行捕捉，退出循环。
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过上面的例子，实际上`for`循环就是迭代器循环。


#### 2.3 迭代器的优点和缺点

**优点：**
- 为序列和非序列提供了一个统一的迭代取值的方式。
- 惰性计算：不管迭代器对象有多大，同一时刻只有一行数据存在。

**缺点：**
- 在取得时候我们并不知道这个迭代器的长度。
- 取值是一次性的，过去的就让它过去，永远无法回来，除非我们在定义一个新的迭代器对象。

**小结：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所有的迭代器对象都是可迭代对象，但是不是所有的可迭代对象都是迭代器对象。可迭代对象用`iter`之后会转化为迭代器对象，迭代器对象用`iter`转化依然是迭代器对象本身。

____

### 3 生成器(Generator)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个生成器既是可迭代的也是迭代器，定义生成器有两种方式：
- 列表(集合、字典)生成器
- 使用`yield`定义生成器函数

第一种方式：
```python
g = (x * 2 for x in range(10))      # 0～18的偶数生成器 
print(isinstance(g, Iterable))      # true
print(isinstance(g, Iterator))      # true
print(isinstance(g, Generator))     # true
print(hasattr(g, "__iter__"))       # true
print(hasattr(g, "__next__"))       # true
print(next(g))      # 0
print(next(g))      # 2
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过列表推导式，可以直接创建一个列表，但是受到内存限制，列表容量肯定是有限的而且，创建一个包含100万个元素的列表，占用很大的存储空间。如果我们仅仅需要访问前面几个元素，后面元素的占用存储空间就被浪费。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所以，如果列表元素可以按照某种算法算出来，那我们就可以再循环当中不断地推导它，生成元素，这样就不必创建完整的`list`，从而大大节省了存储空间。

第二种方式：
```python
def gen():
    for i in range(10):
        yield i 
```
这里`yield`的作用就相当于return,这个函数就是顺序地返回[0,10)的之间的自然数，可以通过`next()`或使用`for`循环来遍历。

当程序遇到`yield`关键字时，这个生成器函数就返回了，直到再次执行了`next()`函数，它就会从上次函数返回的执行点继续执行，即`yield`退出时保存了函数执行的位置、变量等信息，再次执行时，就从这个`yield`退出的地方继续往下执行。

在`Python`中利用生成器的这些特点可以实现协程。协程可以理解为一个轻量级的线程，它相对于线程处理高并发场景有很多优势。

____

### 参考
- 迭代器与生成器：[https://www.runoob.com/python3/python3-iterator-generator.html](https://www.runoob.com/python3/python3-iterator-generator.html)
- 一文彻底搞懂Python可迭代(Iterable)、迭代器(Iterator)和生成器(Generator)的概念：[https://juejin.cn/post/6844903834381189127](https://juejin.cn/post/6844903834381189127)