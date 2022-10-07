&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从 Python3.7 版本开始，引入了一个新的模块`dataclasses`，该模块主要提供了一种数据类的实现方式。基于[PEP-557](https://peps.python.org/pep-0557/)实现。 所谓数据类，类似 C++里的 `plain struct`，Java 语言中的 `Bean`。通过一个容器类(class)，继而使用对象的属性访问数据。

## 1 为什么需要数据类
### 1.1 内置数据类型的局限
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面用tuple、dict、namedtuple分别实现一个学生的数据类型，包括姓名(name)，年龄(age)，性别(gender)，学号(student_ID)。
**1. 使用tuple**
```python
In [1]: stu01 = ('KK', 'M', 23, 2201)

In [2]: stu01[0]
Out[2]: 'KK'
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;缺点：创建和取值基于位置, 需要记住坐标对应的信息。

**2. 使用dict**
```python
In [3]: stu01 = {'name': 'KK', 'gender': 'M', 'age': 23, 'number': 2021}
In [4]: stu01['gender']
Out[4]: 'M'
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用字典之后, 获取信息时会相对直观, 但是相较于字典的括号语法 `stu01['gender']` 我们更希望可以用类似获取属性一样使用`stu01.gender`。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;缺点：无法对数据属性名进行控制。

**3. 使用namedtuple**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python 中的`collections`模块提供一个命名元组, 可以使用点表示法和字段名称访问给定命名元组中的值. 使用`namedtuple`代码如下:
```python
In [5]: from collections import namedtuple

In [6]: Student = namedtuple("Student", ['name', 'gender', 'age', 'number'])

In [7]: stu01 = Student('KK', 'M', 23, 2021)

In [8]: stu01
Out[8]: Student(name='KK', gender='M', age=23, number=2021)

In [9]: stu01.age
Out[9]: 23
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用namedtuple之后
- （1）可以使用 '.'语法获取数据的属性, 可以限制数据的属性名称,
- （2）创建对象时数据不匹配会报错。
```python
In [10]: stu02 = Student('MM', 'F', 20)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-cef5297a0148> in <module>()
----> 1 stu02 = Student('MM', 'F', 20)

TypeError: __new__() missing 1 required positional argument: 'number'
```


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;缺点：数据无法修改；无法自定义数据比较, 没有默认值, 没有函数支持。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;小结：对于一些字段比较少的数据结构，`namedtuple`是一个非常好的解决方案. 但面对一些复杂的数据的时候，需要更多的功能时，`namedtuple`就无法满足了.

```python
In [11]: stu02 = Student('MM', 'F', 20, 2202)

In [12]: stu02.age = 21
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-15-ea75eb45d83f> in <module>()
----> 1 stu02.age = 21

AttributeError: can't set attribute
```
### 1.2 自定义类 Class
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了支持数据修改, 默认值, 比较等功能. 更加好一些的方法是, 使用自定义类来实现数据类. 一个最简单的数据类代码如下:
```python
In [13]: class Student:
    ...:     def __init__(self, name, gender, age, number):
    ...:         self.name = name
    ...:         self.gender = gender
    ...:         self.age = age
    ...:         self.number = number

In [14]: stu01 = Student(name='KK', gender='M', age=23, number=2201)

In [15]: stu02 = Student('MM', 'F', 20, 2202)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以使用位置参数或者键值参数创建对象，下面修改对象的属性。
```python
In [16]: stu02.age = 21

In [17]: stu02.age
Out[17]: 21
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;目前的实现，对于对象的描述不太友好，不知道对象的属性。
```python
In [18]: stu01
Out[18]: <__main__.Student at 0x14609b84cf8>
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此外，数据还不支持比较。
```python
In [19]: stu01 > stu02
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-22-56a188870353> in <module>()
----> 1 stu01 > stu02

TypeError: '>' not supported between instances of 'Student' and 'Student'
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了解决上面两个问题，可以通过实现`repr`方法来自定义描述, 实现`gt`方法来支持比较的功能. 更新代码如下:

```python
In [20]: class Student:
    ...:     def __init__(self, name, gender, age, number):
    ...:         self.name = name
    ...:         self.gender = gender
    ...:         self.age = age
    ...:         self.number = number
    ...:     def __repr__(self):
    ...:         return f'Student: \n {self.name}\t {self.gender}\t {self.age}\t {self.number}'
    ...:     def __eq__(self, other):
    ...:         return self.age == other.age
    ...:     def __gt__(self, other):
    ...:         return self.age > other.age
    ...:

In [21]: stu01 = Student(name='KK', gender='M', age=23, number=2201)

In [22]: stu02 = Student(name='MM', gender='F', age=20, number=2202)

In [23]: stu01
Out[23]:
Student:
 KK      M       23      2201

In [24]: stu01 > stu02
Out[24]: True
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看到数据对象有了更直观的描述, 支持了对比 (若要支持`>=`的对比, 还需要自定义`__ge__`方法). 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;缺点：
- (1) `__init__`方法中重复代码
- (2) 需要自己实现`__repr__`方法, 和比较方法`__eq__`, `__gt__`等

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这部分内容主要借鉴自：[Python中的数据类dataclass详解](https://www.cnblogs.com/hanfe1/p/16720178.html)


____

## 2 使用dataclass

### 2.1 定义一个dataclass
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dataclasses`模块提供了一个装饰器帮助我们定义自己的数据类：
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    gender: str
    age: int
    number: int
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在数据类被定义后，会根据给出的类型注解生成一个如下的初始函数：
```python
class Student:
    def __init__(self, name: str, gender: str, age: int, number: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.number = number
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看到初始化操作都已经自动生成了，下面让我们试用一下：
```python
stu01 = Student('KK', 'F', 23, 2201)
print(stu01)                # Student(name='KK', gender='F', age=23, number=2201)
stu02 = Student('MM', 'M', 20, 2202)
print(stu02 == stu01)       # False
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;例子中可以看出`__repr__`和`__eq__`方法也已经为我们生成了，如果没有其他特殊要求的话这个dataclass已经具备了投入生产环境的能力，是不是很神奇？

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`dataclass`装饰器带来的变化：
1. 无需定义__init__，然后将值赋给self，dataclass负责处理它
2. 我们以更加易读的方式预先定义了成员属性，以及类型提示。我们现在立即能知道number是int类型。这无疑比一般定义类成员的方式更具可读性。


### 2.2 深入dataclass装饰器
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dataclass`的魔力源泉都在`dataclass`这个装饰器中，如果想要完全掌控dataclass的话那么它是你必须了解的内容。
装饰器的原型如下：
```python
dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dataclass`装饰器将根据类属性生成数据类和数据类需要的方法。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们的关注点集中在它的kwargs上：
<div class="table-wrapper"><table>
<thead>
<tr>
<th>key</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td>init</td>
<td>指定是否自动生成<code>__init__</code>，如果已经有定义同名方法则忽略这个值，也就是指定为True也不会自动生成</td>
</tr>
<tr>
<td>repr</td>
<td>同init，指定是否自动生成<code>__repr__</code>；自动生成的打印格式为<code>class_name(arrt1:value1, attr2:value2, ...)</code></td>
</tr>
<tr>
<td>eq</td>
<td>同init，指定是否生成<code>__eq__</code>；自动生成的方法将按属性在类内定义时的顺序逐个比较，全部的值相同才会返回True</td>
</tr>
<tr>
<td>order</td>
<td>自动生成<code>__lt__</code>，<code>__le__</code>，<code>__gt__</code>，<code>__ge__</code>，比较方式与eq相同；如果order指定为True而eq指定为False，将引发<code>ValueError</code>；如果已经定义同名函数，将引发<code>TypeError</code></td>
</tr>
<tr>
<td>unsafehash</td>
<td>如果是False，将根据eq和frozen参数来生成<code>__hash__</code>:<br> 1. eq和frozen都为True，<code>__hash__</code>将会生成<br>2. eq为True而frozen为False，<code>__hash__</code>被设为<code>None</code><br>3. eq为False，frozen为True，<code>__hash__</code>将使用超类（object）的同名属性（通常就是基于对象id的hash）<br>当设置为True时将会根据类属性自动生成<code>__hash__</code>，然而这是不安全的，因为这些属性是默认可变的，这会导致hash的不一致，所以除非能保证对象属性不可随意改变，否则应该谨慎地设置该参数为True</td>
</tr>
<tr>
<td>frozen</td>
<td>设为True时对field赋值将会引发错误，对象将是不可变的，如果已经定义了<code>__setattr__</code>和<code>__delattr__</code>将会引发<code>TypeError</code></td>
</tr>
</tbody>
</table></div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有默认值的属性必须定义在没有默认值的属性之后，和对kw参数的要求一样。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上面我们偶尔提到了`field`的概念，我们所说的数据类属性，数据属性实际上都是被`field`的对象，它代表着一个数据的实体和它的元信息，下面我们了解一下`dataclasses.field`。


### 2.3 dataclasses.field
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;先看下field的原型： 
```python 
dataclasses.field(*, default=MISSING, default_factory=MISSING, repr=True, hash=None, init=True, compare=True, metadata=None) 
``` 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通常我们无需直接使用，装饰器会根据我们给出的类型注解自动生成`field`，但有时候我们也需要定制这一过程，这时`dataclasses.field`就显得格外有用了。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`default`和`default_factory`参数将会影响默认值的产生，它们的默认值都是None，意思是调用时，如果为指定，则产生一个为None的值。其中default是field的默认值，而`default_factory`控制如何产生值，它接收一个无参数或者全是默认参数的`callable`对象，然后用调用这个对象获得field的初始值，之后再将default（如果值不是MISSING）复制给`callable`返回的这个对象。

<img src="https://img-blog.csdnimg.cn/142d6c13a1d44a34a881d18bd177aa47.png#pic_center" width=50%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当我们尝试使用可变的数据类型, 给数据类中做默认值时, 触发了python中的大坑之一————使用可变默认参数, 导致多个实例公用一个数据从而引发bug。`dataclass`默认阻止使用可变数据做默认值。举个例子，对于list，当复制它时只是复制了一份引用，所以像`dataclass`里那样直接复制给实例的做法的危险而错误的，为了保证使用list时的安全性，应该这样做：
```python
@dataclass
class C:
     # 引入field后， 改动下面这行，使用默认工厂函数来初始化默认值
    mylist: List[int] = field(default_factory=list)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当初始化C的实例时就会调用`list()`而不是直接复制一份list的引用：
```python
>>> c1 = C()
>>> c1.mylist += [1,2,3]
>>> c1.mylist
[1, 2, 3]
>>> c2 = C()
>>> c2.mylist
[]
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数据污染得到了避免。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`init`参数如果设置为`False`，表示不为这个`field`生成初始化操作，`dataclass`提供了`__post_init__`供我们利用这一特性：
```python
@dataclass
class C:
    a: int
    b: int
    c: int = field(init=False)
 
    def __post_init__(self):
        self.c = self.a + self.b
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`__post_init__`在`__init__`后被调用，我们可以在这里初始化那些需要前置条件的`field`。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`repr`参数表示该`field`是否被包含进`repr`的输出，`compare`和`hash`参数表示`field`是否参与比较和计算`hash`值。`metadata`不被`dataclass`自身使用，通常让第三方组件从中获取某些元信息时才使用，所以我们不需要使用这一参数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果指定一个`field`的类型注解为`dataclasses.InitVar`，那么这个`field`将只会在初始化过程中（`__init__`和`__post_init__`）可以被使用，当初始化完成后访问该`field`会返回一个`dataclasses.Field`对象而不是`field`原本的值，也就是该`field`不再是一个可访问的数据对象。举个例子，比如一个由数据库对象，它只需要在初始化的过程中被访问：
```python
@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None
 
    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')
 
c = C(10, database=my_database)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这个例子中会返回c.i和c.j的数据，但是不会返回c.database的。

**补充：**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要使数据类不可变，需要在创建类时设置frozen=True。
```python
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Data:
    name: Any
    value: Any = 42

data = Data("myname", 99)
data.name = "other"             # FrozenInstanceError: cannot assign to field 'name'
```


### 2.4 一些常用函数
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dataclasses`模块中提供了一些常用函数供我们处理数据类。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`dataclasses.asdict`和`dataclasses.astuple`我们可以把数据类实例中的数据转换成字典或者元组：
```python
from dataclasses import asdict, astuple
asdict(stu01)       # {'name': 'KK', 'gender': 'F', 'age': 23, 'number': 2201}
astuple(stu01)      # ('KK', 'F', 23, 2201)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`dataclasses.is_dataclass`可以判断一个类或实例对象是否是数据类：
```python
from dataclasses import is_dataclass
is_dataclass(stu01) # True
```

### 2.5 dataclass继承
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python3.7引入`dataclass`的一大原因就在于相比`namedtuple`，`dataclass`可以享受继承带来的便利。&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`dataclass`装饰器会检查当前class的所有基类，如果发现一个`dataclass`，就会把它的字段按顺序添加进当前的class，随后再处理当前class的field。所有生成的方法也将按照这一过程处理，因此如果子类中的field与基类同名，那么子类将会无条件覆盖基类。子类将会根据所有的field重新生成一个构造函数，并在其中初始化基类。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;看个例子：
```python
from dataclasses import field
from typing import List

@dataclass
class Student:
    name: str
    gender: str
    age: int
    number: int

@dataclass
class Group:
    name: str
    students: List[Student] = field(default_factory=list)

stu01 = Student('KK', 'F', 23, 2201)
stu02 = Student('MM', 'M', 20, 2202)
group_first = Group('To be number one', [stu01, stu02])
group_first
# Group(name='To be number one', students=[Student(name='KK', gender='F', age=23, number=2201), Student(name='MM', gender='M', age=20, number=2202)])
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C中的x则覆盖了Base中的定义。


```python
@dataclass
class Base:
    x: float = 25.0
    y: int = 0
 
@dataclass
class C(Base):
    z: int = 10
    x: int = 15
 
C()         # C(x=15, y=0, z=10)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;没错，数据类的继承就是这么简单。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这部分内容主要借鉴自：[Python dataclass使用指南](https://www.cnblogs.com/apocelipes/p/10284346.html)


________


**小结：**
合理使用`dataclass`将会大大减轻开发中的负担，将我们从大量的重复劳动中解放出来，这既是`dataclass`的魅力，不过魅力的背后也总是有陷阱相伴，最后我想提几点注意事项： 
- `dataclass`通常情况下是`unhashable`的，因为默认生成的`__hash__`是`None`，所以不能用来做字典的key，如果有这种需求，那么应该指定你的数据类为`frozen dataclass` 
- 小心当你定义了和`dataclass`生成的同名方法时会引发的问题 
- 当使用可变类型（如list）时，应该考虑使用`field`的`default_factory` 
- 数据类的属性都是公开的，如果你有属性只需要初始化时使用而不需要在其他时候被访问，请使用`dataclasses.InitVar`



## 参考
- dataclass---数据类：[https://docs.python.org/zh-cn/3/library/dataclasses.html](https://docs.python.org/zh-cn/3/library/dataclasses.html)
- 理解 Python 的 Dataclasses：[https://zhuanlan.zhihu.com/p/59657729](https://zhuanlan.zhihu.com/p/59657729)
- Python中的数据类dataclass详解：[https://www.cnblogs.com/hanfe1/p/16720178.html](https://www.cnblogs.com/hanfe1/p/16720178.html)
- dataclass——数据类——Python 文档：[https://cainiaojiaocheng.com/Python/docs/3.7/library/dataclasses](https://cainiaojiaocheng.com/Python/docs/3.7/library/dataclasses)