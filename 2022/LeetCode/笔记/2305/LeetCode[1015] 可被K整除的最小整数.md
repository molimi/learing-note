数学(三) -- LC[]

## 1 可被 K 整除的最小整数
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/a9a3d760350c44dea0e67be8b4fcb54a.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/smallest-integer-divisible-by-k/description/](https://leetcode.cn/problems/smallest-integer-divisible-by-k/description/)

### 1.2 思路分析

**模运算**

如果让你计算 $1234 \cdot 6789$ 的个位数，你会如何计算？

由于只有个位数会影响到乘积的个位数，那么 $4\cdot 9=36$ 的个位数 $6$ 就是答案。

对于 $1234+6789$ 的个位数，同理，$4+9=13$ 的个位数 $3$ 就是答案。

你能把这个结论抽象成数学等式吗？

一般地，涉及到取模的题目，通常会用到如下等式(上面计算的是 $m=10$):

$$
(a+b)\bmod m = ((a\bmod m) + (b\bmod m)) \bmod m \\ 
(a\cdot b) \bmod m=((a\bmod m)\cdot  (b\bmod m)) \bmod m
$$

证明：根据带余除法，任意整数 $a$ 都可以表示为 $a=km+r$，这里 $r$ 相当于 $a mod m$。那么设 $a=k_1m+r_1,\ b=k_2m+r_2$。

第一个等式：
$$
\begin{aligned}
&(a+b) \bmod m\\
=&((k_1+k_2) m+r_1+r_2)\bmod m\\
=&(r_1+r_2)\bmod m\\
=&((a\bmod m) + (b\bmod m)) \bmod m
\end{aligned}
$$

即：两个数相加对某个数求余等于两个数分别求余相加之后再求余。

第二个等式：
$$
\begin{aligned}
&(a\cdot b) \bmod m\\
=&(k_1k_2m^2+(k_1r_2+k_2r_1)m+r_1r_2)\bmod m\\
=&(r_1r_2)\bmod m\\
=&((a\bmod m)\cdot  (b\bmod m)) \bmod m
\end{aligned}
$$



**举例一: $k = 7$**

从小到大枚举$n$，第一个能被 $k$ 整除的数的长度即为答案。

$$1 \rightarrow 11 \rightarrow 111 \rightarrow 1111 \rightarrow 11111 \rightarrow 111111$$

根据前置知识，设 $x$ 是上一次运算的结果(初始为1)，则下一个 $n$ 模 $k$ 的结果为 $(10x + 1) mod k$，看它是否为0。
$$1 \rightarrow 4 \longrightarrow 6 \longrightarrow 5 \longrightarrow 2 \longrightarrow 0$$

**举例二: $k=24$**

如果计算结果和之前的某个数相同，由于计算规则不变，后面会无限重复下去，无法得到0。

<img src ="https://img-blog.csdnimg.cn/2488dc909ce542ac81fea3ae065aed29.png#pic_center" width = 48%>


**方法一：哈希表**

用哈希表记录计算结果。如果在算出0之前就遇到了在哈希表中的数字，则返回—1。

```python
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        x = 1 % k           #  x 为余数
        seen = set()        #  创建一个无序集合，用于存储余数
        while x and x not in seen:      # 当余数为0或者余数重复出现，退出循环
            seen.add(x)
            x = (10 * x + 1) % k
        return -1 if x else len(seen) + 1   # 余数不为0，返回-1，余数为0，返回len(seen)+1    
``` 

**复杂度分析**
- 时间复杂度：$\mathcal{O}(k)$。
- 空间复杂度：$\mathcal{O}(k)$。


**方法二：抽屉原理**

循环 $k$ 次，如果没有算出0，则返回—1。
为什么？模 $k$ 的结果在 $[0, k-1]$ 中，这有 $k$ 个数字。如果循环 $k$ 次还没有找到0,
根据[鸽巢原理(抽屉原理)](https://oi-wiki.org/math/number-theory/fermat/#%E6%AC%A7%E6%8B%89%E5%AE%9A%E7%90%86)，必然有重复的数字。这也同时说明算法一的时间复杂度为 $O(k)$。

```python
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        x = 1 % k
        for i in count(1):              # 一定有解
            if x == 0:
                return i
            x = (x * 10 + 1) % k

```

**复杂度分析**
- 时间复杂度：$\mathcal{O}(k)$。
- 空间复杂度：$\mathcal{O}(1)$，仅用到若干额外变量。


`itertools.count(start=0, step=1)`

创建一个迭代器，它从 start 值开始，返回均匀间隔的值。常用于 `map()` 中的实参来生成连续的数据点。此外，还用于 `zip()` 来添加序列号。大致相当于：

```python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) --> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
```

当对浮点数计数时，替换为乘法代码有时精度会更好，例如：`(start + step * i for i in count())`。

**方法三：数学推导**

设 $n$ 的长度为 $x$，那么 $n=\frac{10^x-1}{9}$。$n$ 是 $k$ 的倍数，等价于 $10^x-1$ 是 $9k$ 的倍数，即 $10^x \equiv 1(mod 9k)$ 。
结论：最小的 $x$ 必然是 $\phi(9k)$ 的因子。
反证：如果 $\phi(9k) = px + r (0 < r <x)$，根据欧拉定理，$10^{\phi(9k)}=(10)P﹒10”=10”= 1(mod 9k)$，这说明有一个比 $x$ 更小的 $r$，矛盾。
那么计算 $\phi(9k)$ 并枚举其因子 $d$，用快速幂判断 $10^d mod (9k)$ 是否等于1。这一做法只需要 $(\sqrt(k)log k )$ 的时间。

一点优化

由于 $n$ 的个位数是1，所以必然不是 2 的倍数和 5 的倍数。如果 $k$ 是 2 的倍数或 5 的倍数，那么必然无解，返回 —1。否则一定有解。
证明：根据算法二，在计算过程中必然会出现两个数模 $k$ 同余。设这两个数为 $a=\frac{10^x-1}{9}$ 和 $b=\frac{10^y-1}{9}$，且 $a > b$。那么 $a-b$ 是 $k$ 的倍数。
注意 $a-b=\frac{10^x-10^y}{9}=10^y\cdot\frac{10^{x-y}-1}{9}$。$k$在没有因子 2 和 5 的情况下，要想整除上式，必须要整除 $\frac{10^{x-y}-1}{9}$，这说明 $n$ 的长度可以是 $x-y$。


```python
# 计算欧拉函数（n 以内的与 n 互质的数的个数）
def phi(n: int) -> int:
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res = res // i * (i - 1)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res // n * (n - 1)
    return res

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        m = phi(k * 9)
        # 从小到大枚举不超过 sqrt(m) 的因子
        i = 1
        while i * i <= m:
            if m % i == 0 and pow(10, i, k * 9) == 1:
                return i
            i += 1
        # 从小到大枚举不低于 sqrt(m) 的因子
        i -= 1
        while True:
            if m % i == 0 and pow(10, m // i, k * 9) == 1:
                return m // i
            i -= 1
```

**复杂度分析**
- 时间复杂度：$\mathcal{O}(\sqrt{k}\log k)$。计算 $\phi(9k)$ 和枚举 $\phi(9k)$ 的因子都需要 $\mathcal{O}(\sqrt{k})$ 的时间，对每个因子计算快速幂需要 $\mathcal{O}(\log k)$ 的时间，所以时间复杂度为 $\mathcal{O}(\sqrt{k}\log k)$。
- 空间复杂度：$\mathcal{O}(1)$。仅用到若干额外变量。


## 2 总持续时间可被 60 整除的歌曲
### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/1ce920fffbd14c91a1464e6200acc5d3.png#pic_center" width = 48%>

题目链接：[https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/](https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/)

### 2.2 思路分析

**1. 组合数学**

遍历数组的同时用一个哈希表（或者数组）记录元素的出现次数。

遍历 $\textit{time}$：
- 举例，如果 $\textit{time}[i]=1$，那么需要知道左边有多少个模 60 余数是 59 的数。
- 举例，如果 $\textit{time}[i]=62$，那么需要知道左边有多少个模 60 余数是 58 的数。
- 一般地，对于 $\textit{time}[i]$，需要知道左边有多少个模 60 余数是 $60-\textit{time}[i] mod 60$ 的数。
特别地，如果 $\textit{time}[i]$ 模 60 的余数是 0，那么需要知道左边有多少个模 60 余数也是 0 的数。
这两种情况可以合并为：累加左边 $(60-\textit{time}[i] mod 60) mod 60$ 的出现次数。

代码实现时，用一个长为 60 的数组 $\textit{cnt}$ 维护 $\textit{time}[i] mod 60$ 的出现次数。

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        cnt = [0] * 60
        for t in time:
            # 先查询 cnt，再更新 cnt，因为题目要求 i<j
            # 如果先更新，再查询，就把 i=j 的情况也考虑进去了
            ans += cnt[(60 - t % 60) % 60]
            cnt[t % 60] += 1
        return ans
```

复杂度分析
时间复杂度：$\mathcal{O}(n+U)$，其中 $n$ 为 $\textit{nums}$ 的长度，$U=60$。
空间复杂度：$\mathcal{O}(U)$。


________

## 参考

- 三种算法+优化：[https://leetcode.cn/problems/smallest-integer-divisible-by-k/solutions/2263780/san-chong-suan-fa-you-hua-pythonjavacgo-tk4cj/](https://leetcode.cn/problems/smallest-integer-divisible-by-k/solutions/2263780/san-chong-suan-fa-you-hua-pythonjavacgo-tk4cj/)
- 「两数之和」的本质是什么？：[https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/2259343/liang-shu-zhi-he-de-ben-zhi-shi-shi-yao-bd0r1/](https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/solutions/2259343/liang-shu-zhi-he-de-ben-zhi-shi-shi-yao-bd0r1/)