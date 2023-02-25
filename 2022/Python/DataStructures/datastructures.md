&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;前面一篇简单介绍了`Python`的数据类型与运算符，这一节主要学习`Python`中5种常用序列结构：列表、元组、集合、字典和字符串的详细使用和一些技巧，下图概括了本篇的主要内容。
<img src="https://img-blog.csdnimg.cn/0d0256174504475586ca94ec3ac430b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width=75%>

### 1 序列
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在数学上，序列也称数列，按一定顺序排列的数。程序设计中序列是一种数据存储方式，如C，C++中的数组。`Python`中序列是最基本的数据结构，是一块用于存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号（称为索引）访问它们。`Python`中内置了5种常用序列结构：列表、元组、集合、字典和字符串。这些序列支持以下几种通用的操作，但比较特殊的是，集合和字典不支持索引、切片、相加和相乘操作。

#### 1.1 索引
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;序列中，每个元素都有属于自己的编号（索引）。从左向右，索引值从 0 开始递增，同时支持索引值是负数，此类索引是从右向左计数，换句话说，从最后一个元素开始计数，从索引值 -1 开始，如下图所示。
<img src="https://img-blog.csdnimg.cn/110dcd186a7441d9b8e49782c9394967.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" width=50%>

```python
>>> str = "Python"
>>> print(str[-1] = str[5])
True
```

#### 1.2 切片
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;切片操作是访问序列中元素的另一种方法，它可以访问一定范围内的元素，通过切片操作，可以生成一个新的序列。序列实现切片的语法格式如下：
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`序列名称[头下标:尾下标:步长]`，其中头下标可以指定开始索引的位置（包括该位置），可以是正数或负数，若不指定，则默认为0，从序列的开头进行切片；尾下标表示结束索引位置（不包括该位置），如果不指定，则默认为序列的长度；步长表示隔几个存储位置（包含当前位置）取一次元素，也就是说，如果步长的值大于 1，则在进行切片去序列元素时，会“跳跃式”的取元素。如果省略设置步长的值，则最后一个冒号就可以省略。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面用切片操作实现倒序：
```python
>>> str = "python"
>>> print(str[::-1])
nohtyp
```

#### 1.3 相加
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中，支持两种类型相同的序列使用`“+”`运算符做相加操作，它会将两个序列进行连接，但不会去除重复的元素。

```python
>>> print("人生苦短"+"，"+"我用"+"python")
人生苦短，我用python
>>> num = [1, 2, 3]
>>> word = ['python', 'php', 'java', 'C++']
>>> print(num + word)
[1, 2, 3, 'python', 'php', 'java', 'C++']
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 序列相加时，相同类型序列指同为列表、元组、集合等，序列中的元素类型可以不同。

#### 1.4 相乘
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中，使用数字`n`乘以一个序列会生成新的序列，其内容为原来序列被重复`n`次的结果。例如：

```python
>>> str = "Python"
>>> print(str*3)
PythonPythonPython
```

#### 1.5 检察元素
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中使用`in`关键字检查某元素是否为序列的成员，用`not in`关键字用来检查某个元素是否不包含在指定的序列中，其语法格式为：

```python
>>> str = "python"
>>> print('p' in str)
True
>>> print('p' not in str)
False
```

#### 1.6 内置函数
<table>
	<caption>
		表 1 序列相关的内置函数</caption>
	<tbody><tr><th>函数</th><th>功能</th></tr>
		<tr><td>len()</td><td>计算序列的长度，即返回序列中包含多少个元素。</td></tr>
		<tr><td>max()</td><td>找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。</td></tr>
		<tr><td>min()</td><td>找出序列中的最小元素。</td></tr>
		<tr><td>list()</td><td>将序列转换为列表。</td></tr>
		<tr><td>str()</td><td>将序列转换为字符串。</td></tr>
		<tr><td>sum()</td><td>计算元素和。</td></tr>
		<tr><td>sorted()</td><td>对元素进行排序。</td></tr>
		<tr><td>reversed()</td><td>反向序列中的元素。</td></tr>
		<tr><td>enumerate()</td><td>将序列组合为一个索引序列，多用在 for 循环中。</td></tr>
	</tbody>
</table>


### 2 列表 list
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中没有数组，但是加入了更加强大的列表。如果把数组看做是一个集装箱，那么`Python`的列表就是一个工厂的仓库。列表会将所有元素都放在一对中括号`[ ]`里面，相邻元素之间用逗号`,`分隔。列表的元素可以是整数、小数、字符串、列表、元组等任何类型的数据，并且同一个列表中元素的类型也可以不同。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 在使用列表时，虽然可以将不同类型的数据放入到同一个列表中，但通常情况下不这么做，同一列表中只放入同一类型的数据，这样可以提高程序的可读性。

#### 2.1 创建、删除列表
1. 使用`[ ]`直接创建列表

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用此方式创建列表时，列表中元素可以有多个，也可以一个都没有，例如：
```python
>>> name = ["jack", "jane", "marry"]
>>> age = [16, 18, 15]
>>> emptylist = []
```

3. 使用`list()`函数创建列表

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;内置函数`list()`可以将其它数据类型转换为列表类型

```python
>>> print(list("hello")
['h', 'e', 'l', 'l', 'o']
>>> print(list({'a':1, 'b':2, 'c':3}))
['a', 'b', 'c']
```
4. 拼接列表

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`+`运算符可以将多个序列连接起来；列表是序列的一种，所以也可以使用`+`进行连接，这样就相当于在第一个列表的末尾添加了另一个列表。使用`+`会生成一个新的列表，原有的列表不会被改变。

```python
>>> language = ["Python", "C++", "Java"]
>>> date = [1991, 1998, 1995]
>>> info = language + date
>>> print(info)
['Python', 'C++', 'Java', 1991, 1998, 1995]
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于已经创建的列表，如果不再使用，可以使用`del`关键字将其删除。在实际开发中并不经常使用`del`来删除列表，因为`Python`自带的垃圾回收机制会自动销毁无用的列表，即使开发者不手动删除，`Python`也会自动将其回收。语法格式为：`del listname`。


#### 2.2 访问元素
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;列表是顺序存储，可以使用索引（Index）访问列表中的某个元素（得到的是一个元素的值），也可以使用切片访问列表中的一组元素（得到的是一个新的子列表）。

```python
>>> numberlist = [1, 2, 3, 4]
>>> print(numberlist[::2])
[1, 3]
```

#### 2.3 添加元素
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在C++学习列表时，添加和删除元素，需要通过指针的方式实现，而Python里面提供了更加简单的方式对列表的元素进行增删。
**1. append()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`append()`方法用于在列表的末尾追加元素，语法格式如下：
> `listname.append(obj)`
> `listname`表示要添加元素的列表；`obj`表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。

```python
program = ["Python", "C++", "Java"]
# 追加元素
program.append("PHP")
print(program)

# 追加元组，整个元组被当成一个元素
other = ("JavaScript", "C#", "Go")
program.append(other)
print(program)

# 追加列表，整个列表也被当成一个元素
data = ["Ruby", "SQL"]
program.append(data)
print(program)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输出结果为：
> ['Python', 'C++', 'Java', 'PHP']
['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go')]
['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go'), ['Ruby', 'SQL']]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 当给`append()`方法传递列表或者元组时，会将它们视为一个整体，作为一个元素添加到列表中，从而形成包含列表和元组的新列表。

**2. extend()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`extend()`不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。语法格式如下：

> `listname.extend(obj)`
> `listname`指的是要添加元素的列表；`obj`表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等，但不能是单个的数字。
```python
program = ["Python", "C++", "Java"]
# 追加元素
program.extend("C")
print(program)

# 追加元组，元祖被拆分成多个元素
other = ("JavaScript", "C#", "Go")
program.extend(other)
print(program)

# 追加列表，列表也被拆分成多个元素
data = ["Ruby", "SQL"]
program.extend(data)
print(program)
```
输出结果为：
> ['Python', 'C++', 'Java', 'C']
['Python', 'C++', 'Java', 'C', 'JavaScript', 'C#', 'Go']
['Python', 'C++', 'Java', 'C', 'JavaScript', 'C#', 'Go', 'Ruby', 'SQL'] 

**3. insert()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果希望在列表中间某个位置插入元素，那么可以使用`insert()`方法。语法格式如下：

> `listname.insert(index, obj)`
> 其中，`index`表示指定位置的索引值。`insert()`会将`obj`插入到`listname`列表第`index`个元素的位置。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当插入列表或者元组时，`insert()`也会将它们视为一个整体，作为一个元素插入到列表中，这一点和`append()`是一样的。

```python
program = ["Python", "C++", "Java"]
# 追加元素
program.insert(1, "C")
print(program)

# 追加元组，整个元组被当成一个元素
other = ("JavaScript", "C#", "Go")
program.insert(0, other)
print(program)

# 追加列表，整个列表也被当成一个元素
data = ["Ruby", "SQL"]
program.insert(2, data)
print(program)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输出结果为：
> ['Python', 'C', 'C++', 'Java']
[('JavaScript', 'C#', 'Go'), 'Python', 'C', 'C++', 'Java']
[('JavaScript', 'C#', 'Go'), 'Python', ['Ruby', 'SQL'], 'C', 'C++', 'Java']

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** `insert()`主要用来在列表的中间位置插入元素，如果仅仅希望在列表的末尾追加元素，更建议使用 `append()`和`extend()`。

#### 2.4 删除元素
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`列表中删除元素主要分为以下 3 种场景：
- 根据目标元素所在位置的索引进行删除，可以使用`del`关键字或者`pop()`方法；
- 根据元素本身的值进行删除，可使用列表（list类型）提供的`remove()`方法；
- 将列表中所有元素全部删除，可使用列表（list类型）提供的`clear()`方法。

**1. del()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`del`是`Python`中的关键字，专门用来执行删除操作，它不仅可以删除整个列表，还可以删除列表中的某些元素。

```python
>>> language = ["Python", "C++", "Java", "PHP"]
>>> del laguage[-1]
>>> print(laguage)
["Python", "C++", "Java"]
>>> del laguage[-3:-1]
>>> print(laguage)
["Java"]
```

**2. pop()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pop()`方法用来删除列表中指定索引处的元素，具体格式如下：

> `listname.pop(index)`
> `listname`表示列表名称，`index`表示索引值。如果不写`index`参数，默认会删除列表中的最后一个元素，类似于数据结构中的“出栈”操作。

```python
>>> numbers = [12, 15, 16, 18]
>>> numbers.pop(2)
>>> print(numbers)
[12, 15, 18]
>>> numbers.pop()
[12, 15]
```

**3. remove()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`remove()`方法会根据元素本身的值来进行删除操作。但`remove()`方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 `ValueError`错误。

```python
>>> numbers = [12, 15, 16, 18]
>>> numbers.remove(18)
>>> print(numbers)
[12, 15, 16]
```
**4. clear()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`clear()`用来删除列表的所有元素，也即清空列表。例如：`listname.clear()`。

#### 2.5 修改元素
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;修改单个元素可以直接对元素赋值即可，`Python`支持通过切片语法给一组元素赋值。在进行这种操作时，如果不指定步长（step 参数），Python 就不要求新赋值的元素个数与原来的元素个数相同；这意味，该操作既可以为列表添加元素，也可以为列表删除元素。使用切片语法时也可以指定步长（step 参数），但这个时候就要求所赋值的新元素的个数与原有元素的个数相同。

```python
program = ["Python", "C++", "Java"]

# 修改单个元素
program[1] = "C"
print(program)

# 修改后两个元素，对空切片（slice）赋值，就相当于插入一组新的元素：
other = ("JavaScript", "C#", "Go")
program[1:3] = other
print(program)

# 使用步长
program[::2] = ["Ruby", "SQL"]
print(program)
```

```python
['Python', 'C', 'Java']
['Python', 'JavaScript', 'C#', 'Go']
['Ruby', 'JavaScript', 'SQL', 'Go']
```

#### 2.6 查找元素
**1. index()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`index()`方法用来查找某个元素在列表中出现的位置（也就是索引），如果该元素不存在，则会导致`ValueError`错误，所以在查找之前最好使用`count()`方法判断一下。语法格式为：
> `listname.index(obj, start, end)`
> `listname`表示列表名称，`obj`表示要查找的元素，`start`表示起始位置，`end`表示结束位置。

```python
>>> numbers = [12, 16, 20, 25]
>>> print(numbers.index(20))
2
>>> print(numbers.index(12,2))
ValueError
```

**2. count()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`count()`方法用来统计某个元素在列表中出现的次数，如果`count()`返回 0，就表示列表中不存在该元素，所以`count()`也可以用来判断列表中的某个元素是否存在。
```python
>>> numbers = [1, 2, 3, 2, 4, 6, 8]
>>> print(numbers.count(2))
2
```

#### 2.7 遍历列表
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;直接使用`for`循环遍历列表，只能输出元素值。

```python
for item in listname:
	# 输出item
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`for`循环和`enumerate()`函数实现同时输出索引值和元素内容。

```python
for index,item in enumerate(listname):
	# index：用于保存元素的索引
	# item：用于保存获取到的元素值，要输出元素内容时，直接输出该变量即可
	# listname：列表名称
```

#### 2.8 列表推导式
使用列表推导式可以快速生成一个列表，或者根据某个列表生成满足指定需求的列表。
（1）生成指定范围的数值列表
> list = [Expression for var in range]
> list：表示生成的列表名称；Expression：表达式，用于计算新列表的元素；var：循环变量；range：采用`range()`函数生成的range对象。

（2）根据列表生成指定需求的列表
> newlist = [Expression for var in list]
> newlist：表示新生成的列表名称；Expression：表达式，用于计算新列表的元素；var：变量，值为后面列表的每个元素值；list：用于生成新列表的原列表。

（3）从列表中选择符合条件的元素组成新的列表
> newlist = [Expression for var in list if condition]
> newlist：表示新生成的列表名称；Expression：表达式，用于计算新列表的元素；var：变量，值为后面列表的每个元素值；list：用于生成新列表的原列表；conditon：条件表达式，用于指定筛选条件


<table class="reference">
	<caption>
		表 2 Python 列表包含的方法</caption>
<tbody><tr>
<th style="width:5%">序号</th><th style="width:35%">方法</th><th style="width:60%">描述</th></tr>
<tr><td>1</td><td><a href="https://www.runoob.com/python3/python3-att-list-append.html">list.append(obj)</a></td><td>在列表末尾添加新的对象</td></tr>
<tr><td>2</td><td><a href="https://www.runoob.com/python3/python3-att-list-count.html">list.count(obj)</a></td><td>统计某个元素在列表中出现的次数</td></tr>
<tr><td>3</td><td><a href="https://www.runoob.com/python3/python3-att-list-extend.html">list.extend(seq)</a></td><td>在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）</td></tr>
<tr><td>4</td><td><a href="https://www.runoob.com/python3/python3-att-list-index.html">list.index(obj)</a></td><td>从列表中找出某个值第一个匹配项的索引位置</td></tr>
<tr><td>5</td><td><a href="https://www.runoob.com/python3/python3-att-list-insert.html">list.insert(index, obj)</a></td><td>将对象插入列表</td></tr>
<tr><td>6</td><td><a href="https://www.runoob.com/python3/python3-att-list-pop.html">list.pop([index=-1])</a></td><td>移除列表中的一个元素（默认最后一个元素），并且返回该元素的值</td></tr>
<tr><td>7</td><td><a href="https://www.runoob.com/python3/python3-att-list-remove.html">list.remove(obj)</a></td><td>移除列表中某个值的第一个匹配项</td></tr>
<tr><td>8</td><td><a href="https://www.runoob.com/python3/python3-att-list-reverse.html">list.reverse()</a></td><td>反向列表中元素</td></tr>
<tr><td>9</td><td><a href="https://www.runoob.com/python3/python3-att-list-sort.html">	list.sort( key=None, reverse=False)</a></td><td>对原列表进行排序</td></tr>
<tr><td>10</td><td><a href="https://www.runoob.com/python3/python3-att-list-clear.html">list.clear()</a></td><td>清空列表</td></tr>
<tr><td>11</td><td><a href="https://www.runoob.com/python3/python3-att-list-copy.html">list.copy()</a></td><td>复制列表</td></tr>
</tbody></table>


___

### 3 元组 tuple
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;元组可以看做不可变的列表，通常情况下，元组用于保存无需修改的内容。从存储内容上看，元组可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且在同一个元组中，元素的类型可以不同。
**1. 创建元组**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`()`直接创建元组，元组通常都是使用一对小括号将所有元素包围起来的，但小括号不是必须的，只要将各元素用逗号隔开，`Python`就会将其视为元组，如下：

```python
>>> content = ("math", 90, [1, 2], ('c', 2)) 
>>> course = "C++", "Matlab"
>>> print(course)
('C++', 'Matlab')
>>> tuple1 = ("python")
>>> type(tuple1)
<class 'str'>
>>> tuple2("python",)
>>> type(tuple2)
<class 'tuple'>
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号，否则`Python`解释器会将它视为字符串。当使用多个字符串，没有`()`时，如`course = "C++", "Matlab"`，若中间没有逗号，`Python`会将其视为字符串，反之视为元组。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;也可以使用内置的函数`tuple()`将其它数据类型转换为元组类型，语法格式：`tuple(data)`，其中，data 表示可以转化为元组的数据，包括字符串、元组、range 对象等。

**2. 访问元素**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和列表一样，我们可以使用索引（Index）访问元组中的某个元素（得到的是一个元素的值），也可以使用切片访问元组中的一组元素（得到的是一个新的子元组）。

```python
>>> program = tuple("python")
>>> print(program[-2])
o
>>> print(program[::2])
('p', 't', 'o')
```

**3. 修改元组**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;元组是不可变序列，元组中的元素不能被修改，所以只能创建一个新的元组去替代旧的元组。

**4. 删除元组**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当创建的元组不再使用时，可以通过`del`关键字将其删除。`Python`自带垃圾回收功能，会自动销毁不用的元组，所以一般不需要通过`del`来手动删除。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用元组推导式可以快速生成元组。其形式与列表推导式类似，只是将`[]`修改为`()`。元组推导式的结果并不是一个元组，而是一个生成器对象。要使用该生成器对象，可以将其转换为元组或者列表。
<table>
	<caption>
		表 3 Python 字典特征</caption>
	<tbody>
		<tr>
			<th>
				主要特征</th>
			<th>
				解释</th>
		</tr>
		<tr>
			<td>
				通过键而不是通过索引来读取元素</td>
			<td>
				字典类型有时也称为关联数组或者散列表（hash）。它是通过键将一系列的值联系起来的，这样就可以通过键从字典中获取指定项，但不能通过索引来获取。</td>
		</tr>
		<tr>
			<td>
				字典是任意数据类型的无序集合</td>
			<td>
				和列表、元组不同，通常会将索引值 0 对应的元素称为第一个元素，而字典中的元素是无序的。</td>
		</tr>
		<tr>
			<td>
				字典是可变的，并且可以任意嵌套</td>
			<td>
				字典可以在原处增长或者缩短（无需生成一个副本），并且它支持任意深度的嵌套，即字典存储的值也可以是列表或其它的字典。</td>
		</tr>
		<tr>
			<td>
				字典中的键必须唯一</td>
			<td>
				字典中，不支持同一个键出现多次，否则只会保留最后一个键值对。</td>
		</tr>
		<tr>
			<td>
				字典中的键必须不可变</td>
			<td>
				字典中每个键值对的键是不可变的，只能使用数字、字符串或者元组，不能使用列表。</td>
		</tr>
	</tbody>
</table>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;列表（list）和元组（tuple）比较相似，它们都按顺序保存元素，所有的元素占用一块连续的内存，每个元素都有自己的索引，因此列表和元组的元素都可以通过索引（index）来访问。它们的区别在于：列表是可以修改的，而元组是不可修改的。字典（dict）和集合（set）存储的数据都是无序的，每份元素占用不同的内存，其中字典元素以`key-value`的形式保存。


### 4 字典 dict
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;字典（dict）是一种无序的、可变的序列，它的元素以“键值对（key-value）”的形式存储。字典中的键是惟一的（其他类型的映射也是如此），但值并不唯一。键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行。字典是支持无限极嵌套的。

#### 4.1 基本操作
1. 使用`{}`创建字典

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;每个键和它的值之间用冒号`(:)` 隔开，项之间用逗号`(,)`隔开，而整个字典是由一对大括号括起来。空字典(不包括任何项)由大括号组成，像这样: `{}`。语法格式如下：
> dictname = {"key":"value1", 'key2':'value2', ..., 'keyn':valuen}
> dictname 表示字典变量名，keyn : valuen 表示各个元素的键值对。需要注意的是，同一字典中的各个键必须唯一，不能重复。

3. 通过`fromkeys()`方法创建字典

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;字典类型提供的`fromkeys()`方法创建带有默认值的字典，具体格式为：
> dictname = dict.fromkeys(list, value=None) 
> `list`参数表示字典中所有键的列表（list）；`value`参数表示默认值，如果不写，则为空值`None`。

5. 通过`dict()`映射函数创建字典

```python
# 创建空字典
emptyDict = {} # empythDict = dict()
# str 表示字符串类型的键，value 表示键对应的值。使用此方式创建字典时，字符串不能带引号
newdict1 = dict(str1=value1, str2=value2, str3=value3)

# 向 dict() 函数传入列表或元组，而它们中的元素又各自是包含 2 个元素的列表或元组，其中第一个元素作为键，第二个元素作为值
demo1 = [('a',97), ('b',98), ('c',99)]
demo2 = [['a',97], ['b',98], ['c',99]]
demo3 = (('a',97), ('b',98), ('c',99))
demo4 = (['a',97], ['b',98], ['c',99])
newdict2 = dict(demo)

# 通过应用 dict() 函数和 zip() 函数，可将前两个列表转换为对应的字典
keys = ['a', 'b', 'c']
values = [87, 98, 99]
newdict3 = dict(zip(keys, values))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 无论采用以上哪种方式创建字典，字典中各元素的键都只能是字符串、元组或数字，不能是列表。列表是可变的，不能作为键。

4. 访问字典

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;列表和元组是通过下标来访问元素的，而字典不同，它通过键来访问对应的值。因为字典中的元素是无序的，每个元素的位置都不固定，所以字典也不能像列表和元组那样，采用切片的方式一次性访问多个元素。可以通过键名（key）访问，该键是必须存在的，否则会抛出异常。

```python
>>> letter_code = {"A":65, "B":66, "C":67}
>>> print(letter_code['A'])
65
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;除了上面这种方式外，`Python`更推荐使用`dict`类型提供的`get()`方法来获取指定键对应的值。当指定的键不存在时，`get()`方法不会抛出异常，默认返回`None`。

```python
>>> letter_code = {"A":65, "B":66, "C":67}
>>> print(letter_code.get('D'))
None
>>> print(letter_code.get('D', "此键不存在"))
此键不存在
```
5. 删除字典

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和删除列表、元组一样，手动删除字典也可以使用`del`关键字，`Python`自带垃圾回收功能，会自动销毁不用的字典，所以一般不需要通过`del`来手动删除。

```python
letter_code = {"A":65, "B":66, "C":67}
del letter_code['B']  # 删除键"B"
letter_code.clear()	  # 清空字典
del letter_code  	  # 删除字典 
```

6. 添加键值对

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为字典添加新的键值对很简单，直接给不存在的 key 赋值即可。

8. 修改键值对

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`字典中键（key）的名字不能被修改，只能修改值（value）。字典中各元素的键必须是唯一的，因此，如果新添加元素的键与已存在元素的键相同，那么键所对应的值就会被新的值替换掉，以此达到修改元素值的目的。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果要删除字典中的键值对，还是可以使用`del`语句。如果要判断字典中是否存在指定键值对，首先应判断字典中是否有对应的键。判断字典是否包含指定键值对的键，可以使用`in`或`not in`运算符。

#### 4.2 常用方法
**keys()、values()、items()**

 - `keys()`方法用于返回字典中的所有键（key）； 
 - `values()`方法用于返回字典中所有键对应的值（value）； 
 - `items()`用于返回字典中所有的键值对（key-value）。

```python
>>> letter_code = {"A":65, "B":66, "C":67}
>>> print(letter_code.keys())
dict_keys(['A', 'B', 'C'])
>>> print(letter_code.values())
dict_values([65, 66, 67])
>>> print(letter_code.items()) 
dict_items([('A', 65), ('B', 66), ('C', 67)])
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`keys()`、`values()`和`items()`返回值的类型分别为`dict_keys`、`dict_values`和`dict_items`。为了操作这些返回值，我们可以使用`list()`函数，将返回的数据转换成列表，也可以使用`for...in...`循环遍历返回值。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同样可以使用字典推导式可以快速生成字典。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python字典包含的其他内置方法如下表所示：
<table class="reference">
	<caption>
		表 4 Python 字典包含的方法</caption>
<tbody><tr>
<th style="width:5%">序号</th><th style="width:35%">函数</th><th style="width:60%">描述</th></tr>
<tr><td>1</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-clear.html">radiansdict.clear()</a></td><td>删除字典内所有元素 </td></tr>
<tr><td>2</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-copy.html">radiansdict.copy()</a></td><td>返回一个字典的浅复制</td></tr>
<tr><td>3</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-fromkeys.html">radiansdict.fromkeys()</a></td><td> 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值</td></tr>
<tr><td>4</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-get.html">radiansdict.get(key, default=None)</a></td><td>返回指定键的值，如果键不在字典中返回 default 设置的默认值</td></tr>
<tr><td>5</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-in.html">key in dict</a></td><td>如果键在字典dict里返回true，否则返回false</td></tr>
<tr><td>6</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-items.html">radiansdict.items()</a></td><td>以列表返回一个视图对象</td></tr>
<tr><td>7</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-keys.html">radiansdict.keys()</a></td><td>返回一个视图对象</td></tr>
<tr><td>8</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-setdefault.html">radiansdict.setdefault(key, default=None)</a></td><td>   
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default</td></tr>
<tr><td>9</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-update.html">radiansdict.update(dict2)</a></td><td>把字典dict2的键/值对更新到dict里</td></tr>
<tr><td>10</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-values.html">radiansdict.values()</a></td><td>返回一个视图对象</td></tr>
<tr><td>11</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-pop.html">radiansdict.pop(key[,default])</a></td><td>删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。
否则，返回default值。</td></tr>
<tr><td>12</td><td><a href="https://www.runoob.com/python3/python3-att-dictionary-popitem.html"> radiansdict.popitem()</a></td><td>随机返回并删除字典中的最后一对键和值。</td></tr>
</tbody></table>

### 5 集合 set
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 中的集合，和数学中的集合概念一样，用来保存不重复的元素，即集合中的元素都是唯一的，互不相同。从形式上看，和字典类似，Python 集合会将所有元素放在一对大括号`{}`中，相邻元素之间用`“,”`分隔。从内容上看，同一集合中，只能存储不可变的数据类型，包括整形、浮点型、字符串、元组，无法存储列表、字典、集合这些可变的数据类型，否则`Python`解释器会抛出`TypeError`错误。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 集合对于每种数据元素，只会保留一份。在`Python`中集合是无序的，每次输出时元素的排序顺序可能都不相同。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`中有两种集合类型，一种是`set`类型的集合，另一种是`frozenset`类型的集合，它们唯一的区别是，`set`类型集合可以做添加、删除元素的操作，而`forzenset`类型集合不行。

#### 5.1 基本操作
**1. 创建集合**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`{}`创建，直接将集合赋值给变量，也可以使用内置函数`set()`，其功能是将字符串、列表、元组、range 对象等可迭代对象转换成集合。
```python
>>> newSet = {1, 'a', (1, 2, 3), [1, 2]}
>>> set1 = set("python")
>>> set2 = set([1, 2, 3, 4])
>>> set3 = set((1, 2, 3, 4))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 如果要创建空集合，只能使用`set()`函数实现。因为直接使用一对`{}`，`Python`解释器会将其视为一个空字典。
**2. 访问元素**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于集合中的元素是无序的，因此无法向列表那样使用下标访问元素。`Python`中，访问集合元素最常用的方法是使用循环结构，将集合中的数据逐一读取出来。

```python
setNew = {1, 2, 'a', (1, 2, 3), [1, 2]}
for element in setNew:
	print(element, end=' ')
```

**3. 删除集合**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和其他序列类型一样，也可以使用`del()`语句。

**4. 添加元素**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`s.add(x)`将元素 $x$ 添加到集合 $s$ 中，如果元素已存在，则不进行任何操作。`s.update(x)`也可以添加元素，且参数可以是列表，元组，字典等。

```python
>>> set1 = set(("Python", "C++", "PHP"))
>>> set1.add("SQL")
>>> print(set1)
{'C++', 'PHP', 'SQL', 'Python'}
>>> set1.update(["C#", "Go"], ["Java'])
>>>print(set1)
{'Go', 'PHP', 'SQL', 'C#', 'C++', 'Java', 'Python'}
```

**5. 删除元素**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`s.remove(x)`将元素 $x$ 从集合 $s$ 中移除，如果元素不存在，则会发生错误。`s.discard(x)`也可以移除集合中的元素，且如果元素不存在，不会发生错误。`s.pop()`可以设置随机删除集合中的一个元素。

```python
>>> program_set = {"Python", "Java", "C++", "PHP"}
>>> program_set.remove("C++")
>>> print(program_set)
{'PHP', 'Java', 'Python'}
>>> program_set.discard("C++")
>>> program_set.pop()
'PHP'
```
**6. 集合运算**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;集合最常做的操作就是进行交集、并集、差集以及对称差集运算。

|操作符及应用| 描述 |
|--|--|
| `set1 | set2` | 并，返回一个新集合，包括在集合`set1`和`set2`中的所有元素 |
| `set1 - set2` |  差,返回一个新集合，包括在集合`set1`但不在`set2`中的元素  |
| `set1 & set2` | 交，返回一个新集合，包括同时在集合`set1`和`set2`中的元素 |
| `set1 ^ set2` | 补，返回一个新集合，包括集合`set1`和`set2`中的非相同元素 |
| `set1<=set2`或`set1 < set2` | 返回`True/False`，判断`set1`和`set2`的子集关系 |
| `set1 >= set2`或`set1>set2` | 返回`True/False`，判断`set1`和`set2`的包含关系 |
| `set1 |= set2` |  并，更新集合`set1`，包括在集合`set1`和`set2`中的所有元素 |
| `set1 -= set2` | 差，更新集合`set1`，包括在集合`set1`但不在`set2`中的元素 |
| `set1 &= set2` | 交，更新集合`set1`，包括同时在集合`set1`和`set2`中的元素 |
| `set1 ^= set2` | 补，更新集合`set1`，包括集合`set1`和`set2`中的非相同元素 |


#### 5.2 常用方法
<table class="reference">
	<caption>
		表 5 Python 集合包含的方法</caption>
<tbody><tr>
<th>方法</th>
<th>描述</th>
</tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-add.html" target="_blank" rel="noopener noreferrer">add()</a></td><td>为集合添加元素</td></tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-clear.html" target="_blank" rel="noopener noreferrer">clear()</a></td><td>移除集合中的所有元素</td></tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-copy.html" target="_blank" rel="noopener noreferrer">copy()</a></td><td>拷贝一个集合</td></tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-difference.html" target="_blank" rel="noopener noreferrer">difference()</a></td><td>返回多个集合的差集</td>
  </tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-difference_update.html" target="_blank" rel="noopener noreferrer">difference_update()</a></td><td>移除集合中的元素，该元素在指定的集合也存在。</td>
  </tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-discard.html" target="_blank" rel="noopener noreferrer">discard()</a></td><td>删除集合中指定的元素</td></tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-intersection.html" target="_blank" rel="noopener noreferrer">intersection()</a></td><td>返回集合的交集</td>
  </tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-intersection_update.html" target="_blank" rel="noopener noreferrer">intersection_update()</a></td><td>
  返回集合的交集。</td></tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-isdisjoint.html" target="_blank" rel="noopener noreferrer">isdisjoint()</a></td><td>判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。</td>
  </tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-issubset.html" target="_blank" rel="noopener noreferrer">issubset()</a></td><td>判断指定集合是否为该方法参数集合的子集。</td>
  </tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-issuperset.html" target="_blank" rel="noopener noreferrer">issuperset()</a></td><td>判断该方法的参数集合是否为指定集合的子集</td></tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-pop.html" target="_blank" rel="noopener noreferrer">pop()</a></td><td>随机移除元素</td></tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-remove.html" target="_blank" rel="noopener noreferrer">remove()</a></td><td>移除指定元素</td></tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-symmetric_difference.html" target="_blank" rel="noopener noreferrer">symmetric_difference()</a></td><td>返回两个集合中不重复的元素集合。</td>
  </tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-symmetric_difference_update.html" target="_blank" rel="noopener noreferrer">symmetric_difference_update()</a></td><td>
  移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。 </td></tr>
  <tr>
    <td><a href="https://www.runoob.com/python3/ref-set-union.html" target="_blank" rel="noopener noreferrer">union()</a></td><td>返回两个集合的并集</td>
  </tr>
<tr><td><a href="https://www.runoob.com/python3/ref-set-update.html" target="_blank" rel="noopener noreferrer">update()</a></td><td>给集合添加元素</td></tr>
</tbody></table>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** `set`集合是可变序列，程序可以改变序列中的元素；`frozenset`集合是不可变序列，程序不能改变序列中的元素。当集合的元素不需要改变时，我们可以使用`fronzenset`替代`set`，这样更加安全。有时候程序要求必须是不可变对象，这个时候也要使用`fronzenset`替代`set`。比如，字典（dict）的键（key）就要求是不可变对象。

### 6 字符串 str
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;字符串是`Python`中最常用的数据类型。我们可以使用引号(`'`或`"`)来创建字符串。`Python`不支持单字符类型，单字符在`Python`中也是作为一个字符串使用。

#### 6.1 拼接
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`中拼接（连接）字符串很简单，可以直接将两个字符串紧挨着写在一起，会自动将两个字符串拼接在一起。具体格式为：
```python
>>> word = "Hello" "World"
>>> print(word)
HelloWorld
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上面的写法主要针对字符串常量，如果需要使用变量，就得借助`+`运算符来拼接。在很多应用场景中，我们需要将字符串和数字拼接在一起，而`Python`不允许直接拼接数字和字符串，所以我们必须先将数字转换成字符串。可以借助`str()`和`repr()`函数将数字转换为字符串。
- str()： 函数返回一个用户易读的表达形式。
- repr()： 产生一个解释器易读的表达形式。
```python
>>>  name = "python"
>>> str(name)
'python'
>>> repr(name)
"'python'"
```

#### 6.2 切片
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;字符串是由多个字符构成的，字符之间是有顺序的，这个顺序号就称为索引（index）。`Python`允许通过索引来操作字符串中的单个或者多个字符，比如获取指定索引处的字符，返回指定字符的索引值等。可以参考第一部分序列的切片。

```python
>>> var1 = "Hello World!"
>>> print("var1[0]:", var1[0])
var1[0]:H
>>> var2 = "no"
>>> print("reverse order：", var2[::-1])
on
```

#### 6.3 常用函数
**1. len()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;想知道一个字符串有多少个字符（获得字符串长度），或者一个字符串占用多少个字节，可以使用`len()`函数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在实际开发中，除了常常要获取字符串的长度外，有时还要获取字符串的字节数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`中，不同的字符所占的字节数不同，数字、英文字母、小数点、下划线以及空格，各占一个字节，而一个汉字可能占2~4个字节，具体占多少个，取决于采用的编码方式。例如，汉字在`GBK/GB2312`编码中占用 2 个字节，而在`UTF-8`编码中一般占用 3 个字节。

**2. split()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`split()`方法可以实现将一个字符串按照指定的分隔符切分成多个子串，这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来。该方法的基本语法格式如下：
> `str.split(seq, maxsplit)`
> - str： 表示要进行分割的字符串；
> - sep：用于指定分隔符，可以包含多个字符。此参数默认为`None`，表示所有空字符，包括空格、换行符`“\n”`、制表符`“\t”`等。
> - maxsplit：可选参数，用于指定分割的次数，最后列表中子串的个数最多为`maxsplit+1`。如果不指定或者指定为 -1，则表示分割次数没有限制。

```python
>>> string = " I $ love $ Python"
>>> print(string.split())
['I', '$', 'love', '$', 'Python']
>>> print(string.split('$'))
[' I ', ' love ', ' Python']
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 在未指定`sep`参数时，也不能指定`maxsplit`参数，`split()`方法默认采用空字符进行分割，但当字符串中有连续的空格或其他空字符时，都会被视为一个分隔符对字符串进行分割。
**3. jion()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`join()`方法也是非常重要的字符串方法，它是`split()`方法的逆方法，用来将列表（或元组）中多个字符串采用固定的分隔符连接在一起。语法格式如下：
> `newstr = str.join(iterable)`
> - newstr：表示合并后生成的新字符串；
> - str：用于指定合并时的分隔符；
> - iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。

```python
>>> list = ["www", "baidu", "com"]
>>> print('.'.join(list))
www.baidu.com
>>> dir = '', 'usr', 'bin', 'env'
>>> type(dir)
<class 'tuple'>
>>> print('/'.join(dir))
/usr/bin/env
```
**4. count()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`count()`方法用于检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。语法格式如下：
> `str.count(sub[,start[,end]])`
> - str：表示原字符串；
> - sub：表示要检索的字符串；
> - start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
> - end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。
```python
>>> var1 = "/usr/bin/env"
>>> var1.count('/')
3
```

**5. find()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`find()`方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。语法格式如下：

> sr.find(sub[,start[,end]])` 
> - str：表示原字符串； 
> - sub：表示要检索的目标字符串；
> - start：表示开始检索的起始位置。如果不指定，则默认从头开始检索； 
> - end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。
```python
>>> var1 = "python"
>>> var1.find('n')
5
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** `Python`还提供了`rfind()`方法，与`find()`方法最大的不同在于，`rfind()`是从字符串右边开始检索。

**6. index()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同`find()`方法类似，`index()`方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，`index()`方法会抛出异常。语法格式如下：
> `str.index(sub[,start[,end]])`
> - str：表示原字符串； 
> - sub：表示要检索的子字符串； 
> - start：表示检索开始的起始位置，如果不指定，默认从头开始检索；
> - end：表示检索的结束位置，如果不指定，默认一直检索到结尾。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 同`find()`和`rfind()`一样，字符串变量还具有`rindex()`方法，其作用和`index()`方法类似，不同之处在于它是从右边开始检索。

**7. ljust()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ljust()`方法的功能是向指定字符串的右侧填充指定字符，从而达到左对齐文本的目的。基本格式如下：

> `str.ljust(width[,fillchar])`
> - str：表示要进行填充的字符串；
> - width：表示包括`str`本身长度在内，字符串要占的总长度；
> - fillchar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。
`rjust()`和`ljust()`方法类似，唯一的不同在于，`rjust()`方法是向字符串的左侧填充指定字符，从而达到右对齐文本的目的。`center()`字符串方法与`ljust()`和`rjust()`的用法类似，但它让文本居中，而不是左对齐或右对齐。
```python
>>> var1 = "python"
>>> print(var1.rjust(10, '-'))
----python
>>> print(var1.ljust(10, '-'))
python----
>>> print(var1.center(10, '-'))
--python--
```

**8. 格式检查**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`startswith()`方法用于检索字符串是否以指定字符串开头，如果是返回`True`；反之返回`False`。`endswith()`方法用于检索字符串是否以指定字符串结尾，如果是则返回`True`；反之则返回`False`。语法格式如下：
> `str.startswith(sub[,start[,end]])`
> - str：表示原字符串；
> - sub：要检索的子串；
> - start：指定检索开始的起始位置索引，如果不指定，则默认从头开始检索；
> - end：指定检索的结束位置索引，如果不指定，则默认一直检索在结束。

```python
>>> var1 = "www.baidu.com"
>>> var1.startswith("http")
False
>>> var1.endswith("com")
True
```

**9. 大小写转换**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了方便对字符串中的字母进行大小写转换，字符串变量提供了 3 种方法，分别是`title()`、`lower()`和`upper()`。
- `title()`方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写，转换完成后，此方法会返回转换得到的字符串。如果字符串中没有需要被转换的字符，此方法会将字符串原封不动地返回。
- `lower()`方法用于将字符串中的所有大写字母转换为小写字母，转换完成后，该方法会返回新得到的字符串。如果字符串中原本就都是小写字母，则该方法会返回原字符串。
- `upper()`的功能和`lower()`方法恰好相反，它用于将字符串中的所有小写字母转换为大写字母，和以上两种方法的返回方式相同，即如果转换成功，则返回新字符串；反之，则返回原字符串。

```python
>>> var1 = "l like python"
>>> var1.title()
'L Like Python'
>>> var1.lower()
'l like python'
>>> var1.upper()
'L LIKE PYTHON'
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 以上 3 个方法都仅.限于将转换后的新字符串返回，而不会修改原字符串。


**10. 去空格** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用户输入数据时，很有可能会无意中输入多余的空格，或者在一些场景中，字符串前后不允许出现空格和特殊字符，此时就需要去除字符串中的空格和特殊字符。（特殊字符，指的是制表符（\t）、回车符（\r）、换行符（\n）等）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;字符串变量提供了 3 种方法来删除字符串中多余的空格和特殊字符，它们分别是：
- strip()：删除字符串前后（左右两侧）的空格或特殊字符。
- lstrip()：删除字符串前面（左边）的空格或特殊字符。
- rstrip()：删除字符串后面（右边）的空格或特殊字符。

```python
>>> var1 = "\r python \t is so easy \n"
>>> var1.strip()
'python \t is so easy'
>>> var1.lstrip()
'python \t is so easy \n'
>>> var1.rstrip()
'\r python \t is so easy'
>>> var1.strip('\r')
' python \t is so easy \n'
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**温馨提示：** 注意，`Python`的`str`是不可变的（不可变的意思是指，字符串一旦形成，它所包含的字符序列就不能发生任何改变），因此这三个方法只是返回字符串前面或后面空白被删除之后的副本，并不会改变字符串本身。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`python3.6`之后版本添加了`f-string`，称之为字面量格式化字符串，是新的格式化字符串的语法。`f-string`格式化字符串以`f`开头，后面跟着字符串，字符串中的表达式用大括号`{}`包起来，它会将变量或表达式计算后的值替换进去，实例如下：
```python
>>> name = "python"
>>> f'hello {name}'
'hello python'
>>> x = 1 
>>> print(f'{x+1=}')
x+1=2
```


Python 的字符串常用内建函数如下：
<table class="reference">
	<caption>
		表 6 Python 字符串包含的方法</caption>
<tbody><tr>
<th style="width:5%">序号</th><th>方法</th><th>描述</th></tr>
<tr><td>1</td><td><p><a href="https://www.runoob.com/python3/python3-string-capitalize.html">capitalize()</a></td><td>将字符串的第一个字符转换为大写</p></td></tr>
<tr><td>2</td><td><p><a href="https://www.runoob.com/python3/python3-string-center.html">center(width, fillchar)</a></p></td><td>
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。</td>
</tr>
<tr><td>3</td><td><p><a href="https://www.runoob.com/python3/python3-string-count.html">count(str, beg= 0,end=len(string))</a></p></td><td>返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数</td></tr>
<tr><td>4</td><td><p><a href="https://www.runoob.com/python3/python3-string-decode.html">bytes.decode(encoding="utf-8", errors="strict")</a></p></td><td>Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。</td></tr>
<tr><td>5</td><td><p><a href="https://www.runoob.com/python3/python3-string-encode.html">encode(encoding='UTF-8',errors='strict')</a></p></td><td>以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'</td></tr>
<tr><td>6</td><td><p><a href="https://www.runoob.com/python3/python3-string-endswith.html">endswith(suffix, beg=0, end=len(string))</a></td><td>检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.</p></td></tr>
<tr><td>7</td><td><p><a href="https://www.runoob.com/python3/python3-string-expandtabs.html">expandtabs(tabsize=8)</a></p></td><td>把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。</td></tr>
<tr><td>8</td><td><p><a href="https://www.runoob.com/python3/python3-string-find.html">find(str, beg=0, end=len(string))</a></p></td><td>检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1</td></tr>
<tr><td>9</td><td><p><a href="https://www.runoob.com/python3/python3-string-index.html">index(str, beg=0, end=len(string))</a></p></td><td>跟find()方法一样，只不过如果str不在字符串中会报一个异常。</td></tr>
<tr><td>10</td><td><p><a href="https://www.runoob.com/python3/python3-string-isalnum.html">isalnum()</a></p></td><td>如果字符串至少有一个字符并且所有字符都是字母或数字则返
回 True，否则返回 False</td></tr>
<tr><td>11</td><td><p><a href="https://www.runoob.com/python3/python3-string-isalpha.html">isalpha()</a></p></td><td>如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True,
否则返回 False</td></tr>
<tr><td>12</td><td><p><a href="https://www.runoob.com/python3/python3-string-isdigit.html">isdigit()</a></p></td><td>如果字符串只包含数字则返回 True 否则返回 False..</td></tr>
<tr><td>13</td><td><p><a href="https://www.runoob.com/python3/python3-string-islower.html">islower()</a></p></td><td>如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False</td></tr>
<tr><td>14</td><td><p><a href="https://www.runoob.com/python3/python3-string-isnumeric.html">isnumeric()</a></p></td><td>如果字符串中只包含数字字符，则返回 True，否则返回 False</td></tr>
<tr><td>15</td><td><p><a href="https://www.runoob.com/python3/python3-string-isspace.html">isspace()</a></p></td><td>如果字符串中只包含空白，则返回 True，否则返回 False.</td></tr>
<tr><td>16</td><td><p><a href="https://www.runoob.com/python3/python3-string-istitle.html">istitle()</a></p></td><td>	
如果字符串是标题化的(见 title())则返回 True，否则返回 False</td></tr>
<tr><td>17</td><td><p><a href="https://www.runoob.com/python3/python3-string-isupper.html">isupper()</a></p></td><td>如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False</td></tr>
<tr><td>18</td><td><p><a href="https://www.runoob.com/python3/python3-string-join.html">join(seq)</a></p></td><td>以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串</td></tr>
<tr><td>19</td><td><p><a href="https://www.runoob.com/python3/python3-string-len.html">len(string)</a></p></td><td>返回字符串长度</td></tr>
<tr><td>20</td><td><p><a href="https://www.runoob.com/python3/python3-string-ljust.html">ljust(width[, fillchar])</a></p></td><td>返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。</td></tr>
<tr><td>21</td><td><p><a href="https://www.runoob.com/python3/python3-string-lower.html">lower()</a></p></td><td>转换字符串中所有大写字符为小写.</td></tr>
<tr><td>22</td><td><p><a href="https://www.runoob.com/python3/python3-string-lstrip.html">lstrip()</a></p></td><td>截掉字符串左边的空格或指定字符。</td></tr>
<tr><td>23</td><td><p><a href="https://www.runoob.com/python3/python3-string-maketrans.html">maketrans()</a></p></td><td>创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。</td></tr>
<tr><td>24</td><td><p><a href="https://www.runoob.com/python3/python3-string-max.html">max(str)</a></p></td><td>返回字符串 str 中最大的字母。</td></tr>
<tr><td>25</td><td><p><a href="https://www.runoob.com/python3/python3-string-min.html">min(str)</a></p></td><td>返回字符串 str 中最小的字母。</td></tr>
<tr><td>26</td><td><p><a href="https://www.runoob.com/python3/python3-string-replace.html">replace(old, new [, max])</a></p></td><td>把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。</td></tr>
<tr><td>27</td><td><p><a href="https://www.runoob.com/python3/python3-string-rfind.html">rfind(str, beg=0,end=len(string))</a></p></td><td>类似于 find()函数，不过是从右边开始查找.</td></tr>
<tr><td>28</td><td><p><a href="https://www.runoob.com/python3/python3-string-rindex.html">rindex( str, beg=0, end=len(string))</a></p></td><td>类似于 index()，不过是从右边开始.</td></tr>
<tr><td>29</td><td><p><a href="https://www.runoob.com/python3/python3-string-rjust.html">rjust(width,[, fillchar])</a></p></td><td>返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串</td></tr>
<tr><td>30</td><td><p><a href="https://www.runoob.com/python3/python3-string-rstrip.html">rstrip()</a></p></td><td>删除字符串末尾的空格或指定字符。</td></tr>
<tr><td>31</td><td><p><a href="https://www.runoob.com/python3/python3-string-split.html">split(str="", num=string.count(str))</a></p></td><td>
以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串</td></tr>
<tr><td>32</td><td><p><a href="https://www.runoob.com/python3/python3-string-splitlines.html">splitlines([keepends])</a></p></td><td>按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。</td></tr>
<tr><td>33</td><td><p><a href="https://www.runoob.com/python3/python3-string-startswith.html">startswith(substr, beg=0,end=len(string))</a></p></td><td>检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。</td></tr>
<tr><td>34</td><td><p><a href="https://www.runoob.com/python3/python3-string-strip.html">strip([chars])</a></p></td><td>在字符串上执行 lstrip()和 rstrip()</td></tr>
<tr><td>35</td><td><p><a href="https://www.runoob.com/python3/python3-string-swapcase.html">swapcase()</a></p></td><td>将字符串中大写转换为小写，小写转换为大写</td></tr>
<tr><td>36</td><td><p><a href="https://www.runoob.com/python3/python3-string-title.html">title()</a></p></td><td>返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())</td></tr>
<tr><td>37</td><td><p><a href="https://www.runoob.com/python3/python3-string-translate.html">translate(table, deletechars="")</a></p></td><td>根据 str 给出的表(包含 256 个字符)转换 string 的字符，要过滤掉的字符放到 deletechars 参数中</td></tr>
<tr><td>38</td><td><p><a href="https://www.runoob.com/python3/python3-string-upper.html">upper()</a></p></td><td>	
转换字符串中的小写字母为大写</td></tr>
<tr><td>39</td><td><p><a href="https://www.runoob.com/python3/python3-string-zfill.html">zfill (width)</a></p></td><td>返回长度为 width 的字符串，原字符串右对齐，前面填充0</td></tr>
<tr><td>40</td><td><p><a href="https://www.runoob.com/python3/python3-string-isdecimal.html">isdecimal()</a></p></td><td>
检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。</td></tr>
</tbody></table>

___

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于上面这么多函数记不住怎么办，可以使用`dir()`函数用来列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等；`help()`函数用来查看某个函数或者模块的帮助文档。用`dir(str)`查看字符串类型（str）支持的所有方法，用`help(str.lower)`查看`str`类型中`lower()`函数的用法，注意使用`help()`查看某个函数的用法时，函数名后边不能带括号。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于上面序列的操作，了解各个函数的时间复杂度，可以参考：[https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

<table>
<caption>表7 列表、元组、字典、集合和字符串的区别</caption>
<tr><th>数据结构</th><th>是否可变</th><th>是否重复</th><th>是否有序</th><th>定义符号</th></tr>
<tr><td>列表（list）</td><td>可变</td><td>可重复</td><td>有序</td><td>[]</td></tr>
<tr><td>元组（tuple）</td><td>不可变</td><td>可重复</td><td>有序</td><td>()</td></tr>
<tr><td>字典（dictionary）</td><td>可变</td><td>可重复</td><td>无序</td><td>{key:value}</td></tr>
<tr><td>集合（set）</td><td>可变</td><td>不可重复</td><td>无序</td><td>{}</td></tr>
<tr><td>字符串（string）</td><td>不可变</td><td>可重复</td><td>有序</td><td>""</td></tr>
</table>
