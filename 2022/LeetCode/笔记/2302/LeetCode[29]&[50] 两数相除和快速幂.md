##1 两数相除
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/f65d58df5dce4c3b9205c9df989e7569.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/divide-two-integers/description/](https://leetcode.cn/problems/divide-two-integers/description/)

### 1.2 思路分析



## 2 Pow(x, n)
### 2.1 题目描述
<img src ="https://img-blog.csdnimg.cn/23b4072eacf441fb98703be1349dc840.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/powx-n/](https://leetcode.cn/problems/powx-n/)


### 2.2 思路分析




补充知识：
Python位运算 ———— 左移操作（<<）右移操作>>

左移操作：
左移操作，左移一位相当于乘以 b，`a<<b, a' = a*(2^b)`

```python
print(2<<3)     # 2*2^3 = 16，2的二进制10，向左移动3位后10000
print(2<<1)     # 2*2^1 = 4
print(3<<4)     # 3*2^4 = 48,3的二进制为11，向左移动四位后110000
```

右移操作
右移操作，右移一位相当于除以 b，`a>>b, a' = a//(2^b)`注意这里是整除，当向右移动位数大于能移动的位数时，置为0【可以理解为会将尾巴截掉】

```python
print(2>>3)     # 2//2^3 = 0，2的二进制10，向右最多移动2位后，所以多移动无疑为 0
print(2>>1)     # 2//2^1 = 1，向右移动一位为 01,
print(3>>4)     # 3//2^4 = 0, 3 的二进制为11，向右移动四位后00
print(3>>1)     # 3//2^1 = 1, 3 的二进制为11，向右移动一位后为01
```

> $>>$ 和 $<<$ 都是位运算，对二进制数进行移位操作。
> $<<$ 是左移，末位补 0，类比十进制数在末尾添 0 相当于原数乘以 10，$x<<1$ 是将 $x$ 的二进制表示左移一位，相当于原数 $x$ 乘2。比如整数4在二进制下是100，$4<<1$ 左移1位变成1000(二进制)，结果是 8。
> $>>$ 是右移，右移1位相当于除以2。
> 而 $>>=$ 和 $<<=$，就是对变量进行位运算移位之后的结果再赋值给原来的变量，可以类比赋值运算符 $+=$ 和 $-=$ 可以理解。
> 比如 $x>>=2$， 就是把变量 $x$ 右移2位，再保留x操作后的值。
