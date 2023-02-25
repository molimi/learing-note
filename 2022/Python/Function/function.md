&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;函数就是一段封装好的，可以重复使用的代码，它使得我们的程序更加模块化，不需要编写大量重复的代码。函数能提高应用的模块性，和代码的重复利用率。`Python`提供了许多内建函数，比如`print()`。但我们也可以自己创建函数，这被叫做用户自定义函数。

### 1 基础
#### 1.1 函数定义
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`中可以使用`def`关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的，但不建议读者使用`a、b、c`这类简单的标识符作为函数名，函数名最好能够体现出该函数的功能（如上面的`my_len`，即表示我们自定义的`len()`函数）。在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量。具体规则如下：
- 函数代码块以`def`关键词开头，后接函数标识符名称和圆括号`()`。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号 : 起始，并且缩进。
- `return` [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
<img src="https://img-blog.csdnimg.cn/ca249a24bffe46c5932c7367c67ea199.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=50%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;具体语法格式如下：
```python
def 函数名(参数列表):
    # 函数体
    [return [返回值]]	# [] 括起来的为可选择部分，即可以使用，也可以省略
```

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 在创建函数时，即使函数不需要参数，也必须保留一对空的`“()”`，否则`Python`解释器将提示`“invaild syntax”`错误。另外，如果想定义一个没有任何功能的空函数，可以使用`pass`语句作为占位符。

#### 1.2 函数调用
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要调用一个函数，需要知道函数的名称和参数，如果传入的参数数量不对，会报`TypeError`的错误；如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报`TypeError`的错误。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`中，函数的参数可以有默认值，也支持使用可变参数，所以`Python`并不需要像其他语言一样支持[函数的重载](https://baike.baidu.com/item/%E9%87%8D%E8%BD%BD%E5%87%BD%E6%95%B0/3280477)，因为我们在定义一个函数的时候可以让它有多种不同的使用方式，下面是两个小例子。

```python
from random import randint

def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c

# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上面的例子中两个函数的参数都设定了默认值，这也就意味着如果在调用函数的时候如果没有传入对应参数的值时将使用该参数的默认值，所以在上面的代码中我们可以用各种不同的方式去调用`add`函数，这跟其他很多语言中函数重载的效果是一致的。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其实上面的`add`函数还有更好的实现方案，因为我们可能会对0个或多个参数进行加法运算，而具体有多少个参数是由调用者来决定，我们作为函数的设计者对这一点是一无所知的，因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示。
```python
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
```
___
### 2 函数的参数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;定义函数时都会选择有参数的函数形式，函数参数的作用是传递数据给函数，令其对接收的数据做具体的操作处理。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在使用函数时，经常会用到形式参数（简称“形参”）和实际参数（简称“实参”），二者都叫参数，之间的区别是：
- 形式参数：在定义函数时，函数名后面括号中的参数就是形式参数。
- 实际参数：在调用函数时，函数名后面括号中的参数称为实际参数，也就是函数的调用者给函数的参数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中，根据实际参数的类型不同，参数传递分为两种情况：
- 不可变类型：类似`C++`的值传递，如整数、字符串、元组。如`fun(a)`，传递的只是`a`的值，没有影响`a`对象本身。如果在`fun(a)`内部修改`a`的值，则是新生成一个`a`的对象。
- 可变类型：类似`C++`的引用传递，如 列表，字典。如`fun(la)`，则是将`la`真正的传过去，修改后`fun`外部的`la`也会受影响。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在进行值传递时，改变形式参数的值后，实际参数的值不改变；在进行引用传递时，改变形式参数的值后，实际参数的值也发生改变。具体了解，请参考：[Python函数参数传递机制](http://c.biancheng.net/view/2258.html)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;调用函数时可使用的正式参数类型：位置参数、关键字参数、默认参数、不定长参数。
#### 2.1 位置参数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;位置参数，有时也称必需参数，指的是必须按照正确的顺序将实际参数传到函数中，换句话说，调用函数时传入实际参数的数量和位置都必须和定义函数时保持一致。

**1. 实参和形参数量必须一致**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在调用函数，指定的实际参数的数量，必须和形式参数的数量一致（传多传少都不行），否则`Python`解释器会抛出 `TypeError`异常，并提示缺少必要的位置参数。
```python
def girth(width, height):
    return 2 * (width + height)
    
# 调用函数时，必须传递2个参数，否则会引发错误
print(girth(3, 3))
```

**2. 实参和形参位置必须一致**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在调用函数时，传入实际参数的位置必须和形式参数位置一一对应，否则会产生以下 2 种结果：
（1）抛出`TypeError`异常
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当实际参数类型和形式参数类型不一致，并且在函数中，这两种类型之间不能正常转换，此时就会抛出`TypeError`异常。
```python
def area(height,width):
    return height*width/2
print(area("C语言中文网",3))
```

（2）产生的结果和预期不符
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;调用函数时，如果指定的实际参数和形式参数的位置不一致，但它们的数据类型相同，那么程序将不会抛出异常，只不过导致运行结果和预期不符。
```python
# 计一个求梯形面积的函数，并利用此函数求上底为 4cm，下底为 3cm，高为 5cm 的梯形的面积。
# 但如果交互高和下低参数的传入位置，计算结果将导致错误
def area(upper_base,lower_bottom,height):
    return (upper_base+lower_bottom)*height/2
print("正确结果为：",area(4,3,5))	# 17.5
print("错误结果为：",area(4,5,3))	# 13.5
```

#### 2.2 关键字参数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;关键字参数是指使用形式参数的名字来确定输入的参数值。通过此方式指定函数实参时，不再需要与形参的位置完全一致，只要将参数名写正确即可。
```python
def dis_str(str1,str2):
    print("str1:",str1)
    print("str2:",str2)

dis_str('Python', 'Java')	# 位置参数
dis_str(str1 = 'Python', str2 = 'Java')	# 关键字参数
dis_str('Python', str2 = 'Java')	# 混合参数
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在调用有参函数时，既可以根据位置参数来调用，也可以使用关键字参数来调用。在使用关键字参数调用时，可以任意调换参数传参的位置。==但需要注意，混合传参时关键字参数必须位于所有的位置参数之后。==
#### 2.3 默认参数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`允许为参数设置默认值，即在定义函数时，直接给形式参数指定一个默认值。这样的话，即便调用函数时没有给拥有默认值的形参传递参数，该参数可以直接使用定义函数时设置的默认值。

`Python`定义带有默认值参数的函数，其语法格式如下：
```python
def 函数名(...，形参名，形参名=默认值)：
    代码块
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==注意，在使用此格式定义函数时，指定有默认值的形式参数必须在所有没默认值参数的最后，否则会产生语法错误。==在`Python`中，可以使用`函数名.__defaults__`查看函数的默认值参数的当前值，其结果是一个元组。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用可变对象作为参数默认值，多次调用可能导致意外情况。如下面的例子：

```python
def demo(obj=[]):
    print('obj的值：', obj)
    obj.append(1)

demo()	# 第一次调用，输出[]
demo()	# 第二次调用，输出[1]
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从上面的结果看，这显然不是我们想要的结果。为了防止出现这种情况，最好使用`None`作为可变对象的默认值，这时还需要加上必要的检查代码。修改后的代码如下：
```python
def demo(obj=None):
    if obj == None:
        obj = []
    print('obj的值：', obj)
    obj.append(1)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;定义函数时，为形式参数设置默认值要牢记一点：==默认参数必须指向不可变对象。==


#### 2.4 不定长参数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;加了星号`*`的参数会以元组(`tuple`)的形式导入，存放所有未命名的变量参数。
```python
def printinfo( arg1, *vartuple ):
   """打印任何传入的参数"""
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )		# 70	（60， 50）
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;加了两个星号`**`的参数会以字典的形式导入。
```python
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, name='小明', 数学=90)	# 1	{'name': '小明', '数学': 90}
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;声明函数时，参数中星号`*`以单独出现，如果单独出现星号`*`后的参数必须用关键字传入。
```python
def f(a, b, *, c):
	return a + b + c
f(1, 2, 3)	# 报错
f(1, 2, c=3)	# 6
```

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果想要使用一个已经存在的列表作为函数的可变参数，可以在列表的名称前加`*`。如果想要使用一个已经存在的字典作为函数的可变参数，可在字典的名称前加`**`。

```python
def printsign(**sign):
    print()
    for key, value in sign.items():
        print('[' + key + ']的星座是：' + value)

printsign(忆梦='水瓶座', 香凝='双子座')
dict1 = {'忆梦': '水瓶座', '香凝': '双子座'}
printsign(**dict1)
```
___
### 3 返回值和作用域
#### 3.1 函数返回值
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中，用`def`语句创建函数时，可以用`return`语句指定应该返回的值，该返回值可以是任意类型，作用是将函数的处理结果返回给调用它的程序。需要注意的是，`return`语句在同一函数中可以出现多次，但只要有一个得到执行，就会直接结束函数的执行。如果同时返回多个值，则返回的是一个元组，当函数中没有`return`语句时，或者省略了`return`语句的参数时，将返回`None`，即返回空值。

#### 3.2 变量作用域
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所谓作用域（Scope），就是变量的有效范围，就是变量可以在哪个范围以内使用。有些变量可以在整段代码的任意位置使用，有些变量只能在函数内部使用，有些变量只能在`for`循环内部使用。

**1. 局部变量**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在函数内部定义的变量，它的作用域也仅限于函数内部，出了函数就不能使用了，我们将这样的变量称为局部变量（Local Variable）。

**2. 全局变量**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;除了在函数内部定义变量，`Python`还允许在所有函数的外部定义变量，这样的变量称为全局变量（Global Variable）。和局部变量不同，全局变量的默认作用域是整个程序，即全局变量既可以在各个函数的外部使用，也可以在各函数内部使用。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;定义全局变量的方式有以下 2 种：
- 在函数体外定义的变量，一定是全局变量，
- 在函数体内定义全局变量。即使用`global`关键字对变量进行修饰后，该变量就会变为全局变量。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;获取指定作用域范围中的变量
- `globals()`函数为`Python`的内置函数，它可以返回一个包含全局范围内所有变量的字典，该字典中的每个键值对，键为变量名，值为该变量的值。
- `locals()`函数也是`Python`内置函数之一，通过调用该函数，我们可以得到一个包含当前作用域内所有变量的字典。这里所谓的“当前作用域”指的是，在函数内部调用`locals()`函数，会获得包含所有局部变量的字典；而在全局范文内调用`locals()`函数，其功能和`globals()`函数相同。
- `vars()`函数也是`Python`内置函数，其功能是返回一个指定`object`对象范围内所有变量组成的字典。如果不传入`object`参数，`vars()`和 `locals()`的作用完全相同。

**3. 局部函数**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`支持在函数内部定义函数，此类函数又称为局部函数。
```python
#全局函数
def outdef ():
    #局部函数
    def indef():
        print("I like programing")
    #调用局部函数
    indef()
#调用全局函数
outdef()
```

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意：尽管`Python`允许全局变量和局部变量重名，但是在实际开发时，不建议这么做，因为这样容易让代码混乱,很难分清哪些是全局变量，哪些是局部变量。


___
###  4 函数式编程
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`对函数式编程提供部分支持。由于`Python`允许使用变量，因此，`Python`不是纯函数式编程语言。

#### 4.1 高阶函数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order function）。

**1. 变量可以指向函数**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个变量指向了一个函数，那么可以通过该变量来调用这个函数。
```python
>>> f = abs
>>> f(-10)
10
```

**2. 函数名也是变量**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;函数名其实就是指向函数的变量，对于abs()这个函数，完全可以把函数名`abs`看成变量，它指向一个可以计算绝对值的函数！

```python
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;把`abs`指向10后，就无法通过`abs(-10)`调用该函数了！因为`abs`这个变量已经不指向求绝对值函数而是指向一个整数10！要恢复`abs`函数，请重启`Python`交互环境。

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注：由于`abs`函数实际上是定义在`import builtins`模块中的，所以要让修改`abs`变量的指向在其它模块也生效，要用`import builtins; builtins.abs = 10`。

**3. 传入函数**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。举一个例子：

```python
def add(x, y, f):
	return f(x) + f(y)
print(add(-5, 6, abs)	# 11
```
**4. map() 和 reduce()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。

```python
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))	# [1, 4, 9, 16, 25, 36, 49, 64, 81]
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于结果`r`是一个`Iterator`，`Iterator`是惰性序列，因此通过`list()`函数让它把整个序列都计算出来并返回一个`list`。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f((x1, x2), x3), x4)
```

```python
>>> from functools import reduce
>>> reduce(lambda x,y: x+y, [1, 2, 3, 4,5])
15
```

**5. filter()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`内建的`filter()`函数用于过滤序列。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;把一个序列中的空字符串删掉，可以这么写：
```python
def not_empty(s):
    return s and s.strip()


new_list = list(filter(not_empty, ['A', ' ', 'B', None, 'C', '']))
print(new_list)		# ['A', 'B', 'C']
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可见用`filter()`这个高阶函数，关键在于正确实现一个“筛选”函数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**注意：** 到`filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回`list`。

**6. sorted()**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`内置的`sorted()`函数也是一个高阶函数，它还可以接收一个`key`函数来实现自定义的排序，例如按绝对值大小排序：

```python
>>> soretd([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
>>> soretd([36, 5, -12, 9, -21], key=abs)
>[5, 9, -12, -21, 36]
```

#### 4.2 匿名函数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=#9900C><strong>关键字`lambda`表示匿名函数，冒号前面表示函数参数，参数可以有多个，使用逗号","分隔。匿名函数有个限制，就是只能有一个表达式，不用写`return`，返回值就是该表达式的结果且只有一个，也不能出现其他非表达式语句（如`for`或`while`）。</font></strong>
- `lambda`只是一个表达式，函数体比`def`简单很多。
- `lambda`的主体是一个表达式，而不是一个代码块。仅仅能在`lambda`表达式中封装有限的逻辑进去。
- `lambda`函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
- 虽然`lambda`函数看起来只能写一行，却不等同于`C`或`C++`的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
```python
>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x101c6ef28>
>>> f(5)
25
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同样，也可以把匿名函数作为返回值返回，比如：

```python
def build(x, y):
    return lambda: x * x + y * y
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;了解更多，可以阅读[返回函数与闭包](https://www.liaoxuefeng.com/wiki/1016959663602400/1017434209254976)、[装饰器](https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584)和[偏函数](https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145929440)


___

### 参考
- Python3 函数：[https://www.runoob.com/python3/python3-function.html](https://www.runoob.com/python3/python3-function.html)
- 函数式编程：[https://www.liaoxuefeng.com/wiki/1016959663602400/1017328525009056](https://www.liaoxuefeng.com/wiki/1016959663602400/1017328525009056)
- Python函数和lambda表达式：[http://c.biancheng.net/python/function/](http://c.biancheng.net/python/function/)