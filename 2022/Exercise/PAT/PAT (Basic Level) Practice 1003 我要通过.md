&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;最近主要在浙大PAT OJ平台刷题，本篇主要分析1003题的求解思路和Python实现。

## 1 题目介绍
**1. 题目背景**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。得到“答案正确”的条件是：
1. 字符串中必须仅有`P`、`A`、`T`这三种字符，不可以包含其它字符；
2. 任意形如`xPATx`的字符串都可以获得“答案正确”，其中`x`或者是空字符串，或者是仅由字母`A`组成的字符串；
3. 如果`aPbTc`是正确的，那么`aPbATca`也是正确的，其中`a`、`b`、`c`均或者是空字符串，或者是仅由字母`A`组成的字符串。

**2. 输入格式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;每个测试输入包含1个测试用例。第1行给出一个正整数$n$($n≤10$)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过100，且不包含空格。

**3. 输出格式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出`YES`，否则输出`NO`。

**4. 输入样例**
```python
10
PAT
PAAT
AAPATAA
AAPAATAAAA
xPATx
PT
Whatever
APAAATAA
APT
APATTAA
```

**5. 输出样例**
```python
YES
YES
YES
YES
NO
NO
NO
NO
NO
NO
```
## 2 思路分析
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在厘清题目条件后，就会有思路了，这个题目有点像数学里的找规律，条件是不断加强的，一开始我是卡在条件三的理解，下面一一分析：

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;条件一：符串中必须仅有`P`、`A`、`T`这三种字符，不可以包含其它字符；
条件一容易理解，就是字面意思。
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;条件二：任意形如`xPATx`的字符串都可以获得“答案正确”，其中`x`或者是空字符串，或者是仅由字母`A`组成的字符串；
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;条件2结合条件1，任意形如`xPATx`的字符串都是正确的（`x`为空串或仅由`A`组成的字符串），这里`PAT`的两边都是`x`，也就是两边是相同的字符串，那么可举例`PAT`、`APATA`、`AAPATAA`、`AAAPATAAA`……都是正确的。
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;条件三：如果`aPbTc`是正确的，那么`aPbATca`也是正确的，其中`a`、`b`、`c`均或者是空字符串，或者是仅由字母`A`组成的字符串。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第3点是在第2点的基础上定义的一个推导关系，即`aPbTc→aPbATca`，后者相比于前者：
-（1）在`P`和`T`之间多了一个固定字符`A`；
-（2）在末尾接了一个`P`左侧的`a`。对应第2点的例子可得：（以下将`P`左侧的A称为“左A”，P和T之间的A称为“中A”，T右侧的A称为“右A”，很好理解）

PAT→PAAT→PAAAT→PAAA…T；
（左无A，中间无限加A，右无A）

APATA→APAATAA→APAAATAAA→APAAA…TAAA…；
（左1A，中A和右A数量始终保持一致）

AAPATAA→AAPAATAAAA→AAPAAATAAAAAA→AAPAAA…TAAAAAA……；
（左2A，右A的数量一直是中A的两倍）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;依次类推，我们可以发现规律：左边n个`A`，右`A`的数量就是中`A`的n倍，即 左`A`的数量*中`A`的数量=右`A`的数量。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上，可以得到下面的规律：
- 只存在`'P'`, `'A'`, `'T'`三种字符；
- `'P'`, `'T'`只能出现一次并且按照该顺序先后出现；
- `P&T`之间不能没有`A`；
- `T`之后`A`的数量 = `P`之前`A`的数量 × `P&T`中间`A`的数量。

代码思路：
> 使用一个长度为3的列表记录`P`之前，`P&T`之间，`T`之后`A`的数量。
> 为了检测`'P'`, `'T'`的出现及次序，使用一个标记变量`pos`：
> > 其值在出现`P`之前为0（使用count[0]记录`P`之前的`A`）
> > 只有在出现`P`且其值为0时，将值变为1（使用count[1]记录`P&T`之间的`A`）
> > 只有在出现`T`且其值为1时，将其变为2（使用count[2]记录`T`之后的`A`）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这样即可保证除此之外出现非`'A'`字符的情况都是不符合要求的，`pos`顺便还能作为count[]的索引。

## 3 代码实现

```python
def is_format(test_str):
    count_list = [0, 0, 0]
    pos = 0                               # 刚开始默认从P之前开始记录
    for letter in test_str:
        if letter == 'A':
            count_list[pos] += 1          # 分别统计A在不同位置之间出现的次数
        elif letter == 'P' and pos == 0:  # 出现P之后，把pos置位1
            pos = 1
        elif letter == 'T' and pos == 1:  # 出现T之后，把pos置位2
            pos = 2
        else:
            return 'NO'
    # 判断T是否在P之后出现，P和T之间是否有A，以及T之后A的数量是否等于P&T之间A的数量乘以P前A的数量
    if pos == 2 and count_list[1] and count_list[2] == count_list[0] * count_list[1]:
        return 'YES'
    else:
        return 'NO'


num = int(input())
for i in range(num):
    print(is_format(input()))
```

## 参考
- PAT乙级 1003 我要通过：[https://blog.csdn.net/weixin_43382079/article/details/103226733](https://blog.csdn.net/weixin_43382079/article/details/103226733)
- PAT乙级 1003：[https://blog.csdn.net/qq_41071754/article/details/108562260](https://blog.csdn.net/qq_41071754/article/details/108562260)
- PAT Basic 1003. 我要通过：[https://www.jianshu.com/p/2700af335690](https://www.jianshu.com/p/2700af335690)