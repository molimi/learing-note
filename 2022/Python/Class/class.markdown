&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 语言在设计之初，就定位为一门面向对象的编程语言，而面向对象编程（Object-oriented Programming，简称 OOP），是一种封装代码的方法。比较正式的说法，“把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。”
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代码封装，其实就是隐藏实现功能的具体代码，仅留给用户使用的接口，就好像使用计算机，用户只需要使用键盘、鼠标就可以实现一些功能，而根本不需要知道其内部是如何工作的。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“Python 中一切皆对象”就是对 Python 这门编程语言的完美诠释。在 Python 中，所有的变量其实也都是对象，包括整形（int）、浮点型（float）、字符串（str）、列表(list)、元组(tuple)、字典（dict）和集合（set）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;类和对象是 Python 的重要特征，相比其它面向对象语言，Python 很容易就可以创建出一个类和对象。同时，Python 也支持面向对象的三大特征：封装、继承和多态。
> 面向对象相关术语：
> - 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
> - 方法：类中定义的函数。
> - 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
> - 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
> - 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
> - 局部变量：定义在方法中的变量，只作用于当前实例的类。
> - 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用`self`修饰的变量。详细了解[类变量、实例变量、局部变量](http://c.biancheng.net/view/2283.html)
> - 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
> - 实例化：创建一个类的实例，类的具体对象。
> - 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

### 1 类和对象
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;类是对象的模板，而对象是类的实例。从这个解释我们可以看出，类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。
#### 1.1 定义类
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在`Python`中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。
```python
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    def __init__(self, name):
        self.name = name

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`class`后面紧接着的是类名，类名通常是大写开头的单词，然后是(object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用`object`类，这是所有类最终都会继承的类。最后，要跟有冒号(:)，表示告诉`Python`解释器，下面要开始设计类的内部功能了，也就是编写类属性和类方法。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和变量名一样，类名本质上就是一个标识符，因此我们在给类起名字时，必须让其符合 Python 的语法，同时应考虑程序的可读性。如果由单词构成类名，建议每个单词的首字母大写，其它字母小写。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`__init__()`方法是一个特殊的类实例方法，称为构造方法(或构造函数)。构造方法用于创建对象时使用，每当创建一个类的实例对象时，`Python`解释器都会自动调用它。`__init__()`方法可以包含多个参数，但必须包含一个名为 `self`的参数，且必须作为第一个参数。

#### 1.2 创建和使用对象
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。在类的实例化，如果没有手动添加`__init__()`构造方法，又或者添加的 `__init__()`中仅有一个`self`参数，则创建类对象时的参数可以省略不写。
```python
stu1 = Student('CarpeDiem')
stu1.study('math')
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;实例化后的类对象可以执行以下操作：
- 访问或修改类对象具有的实例变量，甚至可以添加新的实例变量或者删除已有的实例变量；
- 调用类对象的方法，包括调用现有的方法，以及给类对象动态添加方法。具体了解，请阅读：[类对象的使用](http://c.biancheng.net/view/2265.html)
#### 1.3 self用法
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`self`代表实际调用该方法的对象，而非类。类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是`self`。事实上，`Python`只是规定，无论是构造方法还是实例方法，最少要包含一个参数，并没有规定该参数的具体名称。之所以将其命名为`self`，只是程序员之间约定俗成的一种习惯，遵守这个约定，可以使我们编写的代码具有更好的可读性。无论是类中的构造函数还是普通的类方法，实际调用它们的谁，则第一个参数`self`就代表谁。
#### 1.4 访问可见性
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在很多面向对象编程语言中，我们通常会将对象的属性设置为私有的（private）或受保护的（protected），简单的说就是不允许外界访问，而对象的方法通常都是公开的（public），因为公开的方法就是对象能够接受的消息。在`Python`中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，下面的代码可以验证这一点。

```python
class Demo:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

demo = Demo('hello')
# AttributeError: 'Demo' object has no attribute '__bar'
demo.__bar()
# AttributeError: 'Demo' object has no attribute '__foo'
print(demo.__foo)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们。
```python
demo = Demo('hello')
demo._Demo__bar()       # hello __bar
print(demo._Demo__foo)  # hello
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。所以大多数`Python`程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻。

### 2 进阶
#### 2.1 静态方法和类方法
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在类的内部，使用`def`关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数`self`, 且为第一个参数，`self`代表的是类的实例。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`还可以在类中定义类方法，类方法的第一个参数约定名为`cls`，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
```python
class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）。
```python
clock = Clock.now()  # 通过类方法创建对象并获取系统时间
print(clock.now())   # <__main__.Clock object at 0x000002C6BAC256A0>
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。静态方法没有类似`self`、`cls`这样的特殊参数，因此`Python`解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。静态方法需要使用`＠staticmethod`修饰，例如：
```python
class Triangle(object):
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;静态方法的调用，既可以使用类名，也可以使用类对象。
```python
#使用类名直接调用静态方法
Triangle.is_valid(3, 4, 5)
#使用类对象调用静态方法
triangle = Triangle()
triangle.is_valid(3, 4, 5)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于刚接触这一块来说，区分这 3 种类方法是非常简单的，即采用`@classmethod`修饰的方法为类方法；采用`@staticmethod`修饰的方法为静态方法；不用任何修改的方法为实例方法。在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替它们实现想要的功能，但在一些特殊的场景中（例如工厂模式中），使用类方法和静态方法也是很不错的选择。

#### 2.2 @property装饰器
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的`getter`（访问器）和`setter`（修改器）方法进行对应的操作。如果要做到这点，就可以考虑使用`@property`包装器来包装`getter`和`setter`方法，使得对属性的访问既安全又方便，代码如下所示。
```python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


person = Person('香凝', 12)
person.play()
person.age = 22
person.play()
# person.name = '兰花'  # AttributeError: can't set attribute
```

#### 2.3 __slots__方法
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义`__slots__`变量来进行限定。需要注意的是`__slots__`的限定只对当前类的对象生效，对子类并不起任何作用。
```python
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


person = Person('香凝', 22)
person.play()
person._gender = '男'
# AttributeError: 'Person' object has no attribute '_is_gay'
# person._is_gay = True
```

#### 2.4 类之间的关系
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;类和类之间的关系有三种：`is-a`、`has-a`和`use-a`关系。
- `is-a`关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
- `has-a`关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
- `use-a`关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。


#### 2.5 封装、继承和多态
1. 封装
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;封装机制保证了类内部数据结构的完整性，因为使用类的用户无法直接看到类中的数据结构，只能使用类允许公开的数据，很好地避免了外部对内部数据的影响，提高了程序的可维护性。对类进行良好的封装，还可以提高代码的复用性。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;前面已经讲过属性的访问可见性，默认情况下，`Python`类中的变量和方法都是公有（public）的，它们的名称前都没有下划线（_）；如果类中的变量和函数，其名称以双下划线`__`开头，则该变量（函数）为私有变量（私有函数），其属性等同于`private`。还可以定义以单下划线`_`开头的类属性或者类方法（例如 _name、_display(self)），这种类属性和类方法通常被视为私有属性和私有方法，虽然它们也能通过类对象正常访问，但这是一种约定俗称的用法。

> 注意，`Python`类中还有以双下划线开头和结尾的类方法（例如类的构造函数__init__(self)），这些都是`Python`内部定义的，用于`Python`内部调用。我们自己定义类属性或者类方法时，不要使用这种格式。


2. 继承
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。下面我们先看一个继承的例子：
```python
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def meet(self):
        print('我是 %s, 很高兴认识你！' % self._name)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s同学正在学习%s。' % (self._name, course))

stu1 = Student('忆梦', 18, '初一')
stu1.meet()
stu1.study('数学')
```
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;大部分面向对象的编程语言，都只支持单继承，即子类有且只能有一个父类。而`Python`却支持多继承（C++也支持多继承）。和单继承相比，多继承容易让代码逻辑复杂、思路混乱。虽然`Python`在语法上支持多继承，但逼不得已，建议不要使用多继承。关于继承，了解更多：[子类继承父类构造函数](https://www.runoob.com/w3cnote/python-extends-init.html)和[父类方法重写](http://c.biancheng.net/view/2289.html)

3. 多态
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
```python
from abc import ABCMeta, abstractmethod
class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Cat(Pet):
    def make_voice(self):
        print('%s: 喵喵喵...' % self._nickname)

class Dog(Pet):
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
for pet in pets:
    pet.make_voice()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。`Python`从语法层面并没有像`Java`或`C#`那样提供对抽象类的支持，但是我们可以通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voice`抽象方法进行了重写并给出了不同的实现版本，当我们在`main`函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;补充内容：[type()函数：动态创建类](http://c.biancheng.net/view/2292.html)、[MetaClass元类](http://c.biancheng.net/view/2293.html)、[枚举类定义和使用](http://c.biancheng.net/view/2305.html)、[类特殊成员](http://c.biancheng.net/python/special_member/)

### 参考
- 面向对象进阶：[09.面向对象进阶.md](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/09.面向对象进阶.md)
- Python面向对象：[https://www.runoob.com/python3/python3-class.html](https://www.runoob.com/python3/python3-class.html)
- Python类和对象：[http://c.biancheng.net/python/class_object/](http://c.biancheng.net/python/class_object/)