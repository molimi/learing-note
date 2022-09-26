&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

## 1 正则表达式
### 1.1 定位符

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;行定位符就是用来描述字符串的边界，`“^”`表示行的开始，`“$”`表示行的结尾。
```python
^tm     # 表示要匹配字符串tm的开始位置是行头
tm$     # 表示要匹配字符串tm的结束位置是行尾
```

### 1.2 元字符


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;除了上一节介绍的元字符`“^”`和`“$”`外，正则表达式还有更多的元字符，见下图。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/66438f8aa08f4adbbd6ff166b6d0ef25.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center"> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1 常用元字符</div> </center>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;假设你在一篇英文小说里查找hi，你可以使用正则表达式hi。不幸的是，很多单词里包含hi这两个连续的字符，比如him,history,high等等。用hi来查找的话，这里边的hi也会被找出来。如果要精确地查找hi这个单词的话，我们应该使用`\bhi\b`。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`\b`是正则表达式规定的一个特殊代码（某些地方叫它元字符，metacharacter），代表着单词的开头或结尾，也就是单词的分界处。虽然通常英文的单词是由空格，标点符号或者换行来分隔的，但是`\b`并不匹配这些单词分隔字符中的任何一个，它只匹配一个位置。

### 1.3 限定符


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们知道，使用(`\w*`)匹配任意数量的字母或数字，如果想匹配特定数量的数字，就需要使用限定符(指定数量的字符)来实现该功能，如果匹配8位QQ号可用如下表达式：
```pyhton
^\d{8}$
```
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/0fe4797973ed48c49e8f116543cc482d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center"> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图2 常用限定符</div> </center>

### 1.4 字符类

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;正则表达式查找数字和字母是很简单的，因为已经有了对应这些字符集合的元字符（如`\d`、`\w`)，但是如果要匹配没有预定义元字符的字符集合(比如元音字母`a, e, i, o, u`)，应该怎么办？


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;很简单，只需要在方括号里列出它们就行了，像`[aeiou]`可以匹配任何一个英文元音字母，`[.?!]`匹配标点符号(“.” “?”或“!”)。也可以轻松地指定一个字符范围，像`[0-9]`代表的含义与`\d`就是完全一致的：一位数字；同理，`[a-z0-9A-Z_]`完全等同于`\w`(如果只考虑英文的话)。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;说明：要想匹配给定字符串中任意一个汉字，可以使用`[\u4e00-\u9fa5]`；如果要匹配连续多个汉字，可以使用`[\u4e00-\u9fa5]+`。


### 1.5 排除字符

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在1.1小节列出的是匹配符合指定字符集合的字符串。现在反过来，匹配不符合指定字符集合的字符串。正则表达式提供了`^`字符。这个元字符在1.1小节中出现过，表示行的开始。而这里将会放到方括号中，表示排除的意思。例如:
```python
[^a-zA-Z]
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;该表达式用于匹配一个不是字母的字符串。

### 1.6 选择字符


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;试想一下，如何匹配身份证号码？首先需要了解一下身份证号码的规则。身份证号码长度为15位或者18位。如果为15位时，则全为数字；如果为18位时，前17位为数字，最后一位是校验位，可能为数字或字符X。
在上面的描述中，包含着条件选择的逻辑，这就需要使用选择字符(|)来实现。该字符可以理解为‘或’，匹配身份证的表达式可以写成如下方式：
```python
(^\d{15}$)|(^\d{18}$)|(^\d{17})(\d|X|x)$
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;该表达式的意思是以匹配15位数字，或者18位数字，或者17位数字和最后一位。最后一位可以是数字，也可以是`X`或者`x`。


### 1.7 转义字符

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;正则表达式中的转义字符(\)和Python中的大同小异，都是将特殊字符（如“”“?”“|”等）变为普通的字符。举一个IP地址的实例，用正则表达式匹配诸如“127.0.0.1”格式的IP地址。如果直接使用点字符，格式为:
```python
[1-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这显然不对，因为“.”可以匹配一个任意字符。这时，不仅是127.0.0.1这样的IP，连127101011这样的字符串也会被匹配出来。所以在使用“.”时，需要使用转义字符\)。修改后上面的正则表达式格式为:
```python
[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
```

### 1.8 分组

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过1.6小节中的例子，相信读者已经对小括号的作用有了一定的了解。小括号字符的第一个作用就是可以改变限定符的作用范围，如“|”、“*”、“^”等。例如下面的表达式中包含小括号。
```python
(six|four)th
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这个表达式的意思是匹配单词`sixth`或`fourth`，如果不使用小括号，那么就变成了匹配单词`six`和`fourth`了。
小括号的第二个作用是分组，也就是子表达式。如`(\.[0-9]{1,3}){3}`，就是对分组`(\.[0-9]{1,3})`进行重复操作。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于模式字符串中可能包括大量的特殊字符和反斜杠，所以需要写为原生字符串，即在模式字符串前加r或R。例如，模式字符串采用原生字符串表示为:
```python
r`\bm\w*\b`
```


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;推荐几个正则表达式在线测试工具，
- 菜鸟工具：[https://c.runoob.com/front-end/854/](https://c.runoob.com/front-end/854/)
- Regulex：[https://jex.im/regulex/#!flags=&re=%5B0-9%5D%2B](https://jex.im/regulex/#!flags=&re=%5B0-9%5D%2B)
- RegExr：[https://regexr.com/](https://regexr.com/)

____


## 2 Re模块

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Python`提供了`re`模块，用于实现正则表达式的操作。在实现时，可以使用`re`模块提供的方法（如`search()`、`match()`、`findall()`等）进行字符串处理，也可以先使用`re`模块的`compile()`方法将模式字符串转换为正则表达式对象，然后再使用该正则表达式对象的相关方法来操作字符串。下面是`re`模块中的核心函数。

### 2.1 编译表达式

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`compile`函数用于编译正则表达式，生成一个正则表达式(`Pattern`)对象，供 `match()`和`search()`这两个函数使用。]
参数说明：
- pattern：表示模式字符串，由要匹配的正则表达式转换而来。
- flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。常用的标志如图3所示。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/2f53a1f2fdb746a588ea31c55c232559.png#pic_center" width=75%> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图3 常用标志</div> </center>


语法格式为：
```python
re.compile(pattern[, flags])
```


### 2.2 匹配字符串

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;匹配字符串可以使用re模块提供的match()、search()、findall()等方法
1. 使用match()方法进行匹配
`match()`方法用于从字符串的开始处进行匹配，如果在起始位置匹配成功，则返回`Match`对象，否则返回`None`。其语法格式如下:
```python
re.match(pattern, string, [flags])
```
参数说明：
- pattern：表示模式字符串，由要匹配的正则表达式转换而来。
- string：表示要匹配的字符串。
- flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。常用的标志如图3所示。

例如，匹配字符串是否以`mr_`开头，不区分字母大小写，代码如下:

```python
import re
pattern = re.compile(r'mr_\w+', re.I)   # 模式字符串，不区分大小写
string1 = 'MR_SHOP mr_shop'  # 要匹配的字符串
m1 = pattern.match(string1)
print(m1)   # <re.Match object; span=(0, 7), match='MR_SHOP'>
string2 = '项目名称 MR_SHOP mr_shop'   
m2 = pattern.match(string2)
print(m2)   # None
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由上面的结果我们可以看到，`match()`方法从字符串的开始位置开始匹配，如果匹配成功，则返回一个`Match`对象包含了匹配值的位置和匹配数据。其中，要获取匹配值的起始位置可以使用`Match`对象的`start()`方法；要获取匹配值的结束位置可以使用`end()`方法；通过`span()`方法可以返回匹配位置的元组；通过`string`属性可以获取要匹配的字符串。例如下面的代码:
```python
import re

pattern = re.compile(r'mr_\w+', re.I)  # 模式字符串，不区分大小写
string1 = 'MR_SHOP mr_shop'  # 要匹配的字符串
m1 = pattern.match(string1)

print('匹配值的起始位置：', m1.start())
print('匹配值的结束位置：', m1.end())
print('匹配位置的元组：', m1.span())
print('要匹配的字符串：', m1.string)
print('匹配数据：', m1.group())
```

执行结果如下：
匹配值的起始位置： 0
匹配值的结束位置： 7
匹配位置的元组： (0, 7)
要匹配的字符串： MR_SHOP mr_shop
匹配数据： MR_SHOP

2. 使用search()方法进行匹配

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`search()`方法用于在整个字符串中搜索第一个匹配的值，如果匹配成功，则返回Match对象，否则返回None。`search()`方法的语法格式如下:

```python
re.search(pattern, string, [flags])
```
参数说明：
- pattern：表示模式字符串，由要匹配的正则表达式转换而来。
- string：表示要匹配的字符串。
- flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;搜索第一个以`mr_`开头的字符串，不区分字母大小写，代码如下:

```python
import re

pattern = re.compile(r'mr_\w+', re.I)  # 模式字符串，不区分大小写
string1 = 'MR_SHOP mr_shop'  # 要匹配的字符串
match = pattern.search(string1)
print(match)
string2 = '项目名称 MR_SHOP mr_shop'  
match = pattern.search(string2)
print(match)
```



执行结果如下：
<re.Match object; span=(0, 7), match='MR_SHOP'> 
<re.Match object; span=(5, 12), match='MR_SHOP'>



3. 使用findall()方法进行匹配

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`findall()`方法用于在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回。如果匹配成功，则返回包含匹配结构的列表，否则返回空列表。`findall()`方法的语法格式如下:
```python
re.findall(pattern, string, [flags])
```
- pattern：表示模式字符串，由要匹配的正则表达式转换而来。
- string：表示要匹配的字符串。
- flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;搜索以`mr_`开头的字符串，不区分字母大小写，代码如下:
```python
import re

pattern = re.compile(r'mr_\w+', re.I)  # 模式字符串，不区分大小写
string1 = 'MR_SHOP mr_shop'  # 要匹配的字符串
m1 = pattern.match(string1)
string2 = '项目名称 MR_SHOP mr_shop'
m2 = pattern.match(string2)
match = pattern.findall(string1)
print(match)
match = pattern.findall(string2)
print(match)
```



执行结果如下：
['MR_SHOP', 'mr_shop']
['MR_SHOP', 'mr_shop']

### 2.3 替换字符串

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sub()`方法用于实现字符串替换，语法格式如下：
```python
re.sub(pattern, repl, string, count, flags)
```
参数说明：
- pattern：表示模式字符串，由要匹配的正则表达式转换而来。
- repl：表示替换的字符串。
- string：表示要被查找替换的原始字符串。
- count：可选参数，表示模式匹配后替换的最大次数，默认值为0，表示替换所有的匹配。
- flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。

替换敏感字符，代码如下：
```python
import re
pattern = re.compile(r'(黑客)|(抓包)|(监听)|(Trojan)')
string = "我是一名程序员，我喜欢看黑客方面的书，想研究一下Trojan。\n"
sub = pattern.sub('@_@', string)
print(sub)  # 输出为：我是一名程序员，我喜欢看@_@方面的书，想研究一下@_@。
```

### 2.4 分割字符串

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`split()`方法用于实现根据正则表达式分割字符串，并以列表的形式返回。其作用同字符串对象的`split()`方法类似，所不同的就是分割字符由模式字符串指定。`split()`方法的语法格式如下:
```python
re.split(pattern, string, [maxsplit], [flags])
```
参数说明：
- pattern：表示模式字符串，由要匹配的正则表达式转换而来。
- string：表示要匹配的字符串。
- maxsplit：可选参数，表示最大的拆分次数。
- flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;例如，从给定的URL地址中提取出请求地址和各个参数，代码如下:
```python
pattern = re.compile(r'[?|&]')
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = pattern.split(url)
print(result)   # 输出为：['http://www.mingrisoft.com/login.jsp', 'username="mr"', 'pwd="mrsoft"']
```

____

小结：
<table>
<thead>
<tr>
<th>函数</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>re.compile(pattern, flags=0)</td>
<td>编译正则表达式返回正则表达式对象</td>
</tr>
<tr>
<td>re.match(pattern, string, flags=0)</td>
<td>用正则表达式匹配字符串 成功返回匹配对象 否则返回None</td>
</tr>
<tr>
<td>re.search(pattern, string, flags=0)</td>
<td>搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回None</td>
</tr>
<tr>
<td>re.split(pattern, string, maxsplit=0, flags=0)</td>
<td>用正则表达式指定的模式分隔符拆分字符串 返回列表</td>
</tr>
<tr>
<td>re.sub(pattern, repl, string, count=0, flags=0)</td>
<td>用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数</td>
</tr>
<tr>
<td>re.fullmatch(pattern, string, flags=0)</td>
<td>match函数的完全匹配（从字符串开头到结尾）版本</td>
</tr>
<tr>
<td>re.findall(pattern, string, flags=0)</td>
<td>查找字符串所有与正则表达式匹配的模式 返回字符串的列表</td>
</tr>
<tr>
<td>re.finditer(pattern, string, flags=0)</td>
<td>查找字符串所有与正则表达式匹配的模式 返回一个迭代器</td>
</tr>
<tr>
<td>re.purge()</td>
<td>清除隐式编译的正则表达式的缓存</td>
</tr>
<tr>
<td>re.I / re.IGNORECASE</td>
<td>忽略大小写匹配标记</td>
</tr>
<tr>
<td>re.M / re.MULTILINE</td>
<td>多行匹配标记</td>
</tr>
</tbody>
</table>


## 参考
- 正则表达式30分钟入门教程：[https://deerchao.cn/tutorials/regex/regex.htm](https://deerchao.cn/tutorials/regex/regex.htm)
- 字符串和正则表达式：[https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15)
- Python3 正则表达式：[https://www.runoob.com/python3/python3-reg-expressions.html](https://www.runoob.com/python3/python3-reg-expressions.html)