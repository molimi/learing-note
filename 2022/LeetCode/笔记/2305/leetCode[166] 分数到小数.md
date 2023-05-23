数学(三) -- LC[]

## 1 分数到小数

### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/fa19349f323049898ab1a341c099487b.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/fraction-to-recurring-decimal/description/](https://leetcode.cn/problems/fraction-to-recurring-decimal/description/)

### 1.2 思路分析

**1. 长除法**

题目要求根据给定的分子和分母，将分数转成整数或小数。由于给定的分子和分母的取值范围都是 $[-2^{31}, 2^{31}-1]$，为了防止计算过程中产生溢出，需要将分子和分母转成 64 位整数表示。

将分数转成整数或小数，做法是计算分子和分母相除的结果。可能的结果有三种：整数、有限小数、无限循环小数。

如果分子可以被分母整除，则结果是整数，将分子除以分母的商以字符串的形式返回即可。

如果分子不能被分母整除，则结果是有限小数或无限循环小数，需要通过模拟长除法的方式计算结果。为了方便处理，首先根据分子和分母的正负决定结果的正负（注意此时分子和分母都不为 0），然后将分子和分母都转成正数，再计算长除法。

计算长除法时，首先计算结果的整数部分，将以下部分依次拼接到结果中：
1. 如果结果是负数则将负号拼接到结果中，如果结果是正数则跳过这一步；
2. 将整数部分拼接到结果中；
3. 将小数点拼接到结果中。

完成上述拼接之后，根据余数计算小数部分。

计算小数部分时，每次将余数乘以 10，然后计算小数的下一位数字，并得到新的余数。重复上述操作直到余数变成 0 或者找到循环节。
- 如果余数变成 0，则结果是有限小数，将小数部分拼接到结果中。
- 如果找到循环节，则找到循环节的开始位置和结束位置并加上括号，然后将小数部分拼接到结果中。

如何判断是否找到循环节？注意到对于相同的余数，计算得到的小数的下一位数字一定是相同的，因此如果计算过程中发现某一位的余数在之前已经出现过，则为找到循环节。为了记录每个余数是否已经出现过，需要使用哈希表存储每个余数在小数部分第一次出现的下标。

假设在计算小数部分的第 $i$ 位之前，余数为 $\textit{remainder}_i$，则在计算小数部分的第 $i$ 位之后，余数为 $\textit{remainder}_{i+1}$。

假设存在下标 $j$ 和 $k$，满足 $j \le k$ 且 $\textit{remainder}_j = \textit{remainder}_{k+1}$，则小数部分的第 $k+1$ 位和小数部分的第 $j$ 位相同，因此小数部分的第 $j$ 位到第 $k$ 位是一个循环节。在计算小数部分的第 $k$ 位之后就会发现这个循环节的存在，因此在小数部分的第 $j$ 位之前加上左括号，在小数部分的末尾（即第 $k$ 位之后）加上右括号。

<img src ="https://img-blog.csdnimg.cn/f511862661584b15bcee0ca183f1b66e.png#pic_center" width = 64%>

<img src ="https://img-blog.csdnimg.cn/e7fa5f96097a4c91bd638aba9bd556e2.png#pic_center" width = 64%>


```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 如果本身能够整除，直接返回计算结果
        if numerator % denominator == 0: return str(numerator//denominator)
        res = []
        if numerator * denominator < 0:             # 如果其一为负数，先追加负号
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator//denominator))     #  计算整数部分，并将余数赋值给 remainder
        res.append('.')
        remainder = numerator % denominator
        index_map = dict()
        while remainder and remainder not in index_map:
            index_map[remainder] = len(res)         # 记录当前余数所在答案的位置，并继续模拟除法运算
            remainder *= 10
            res.append(str(remainder//denominator))
            remainder %= denominator
        if remainder:                   # 当前余数之前出现过，则将出现位置和最后位置添加'()'
            ind = index_map[remainder]
            res.insert(ind, '(')
            res.append(')')
        return ''.join(res)
```

**复杂度分析**
- 时间复杂度：$O(l)$，其中 $l$ 是答案字符串的长度，这道题中 $l \le 10^4$。对于答案字符串中的每一个字符，计算时间都是 $O(1)$。
- 空间复杂度：$O(l)$，其中 $l$ 是答案字符串的长度，这道题中 $l \le 10^4$。空间复杂度主要取决于答案字符串和哈希表，哈希表中的每个键值对所对应的下标各不相同，因此键值对的数量不会超过 $l$。


## 2 两数相除

### 2.1 题目描述

<img src ="https://img-blog.csdnimg.cn/d8231735d9d84898baa6c13dd417d27d.png#pic_center" width = 64%>

题目链接：[https://leetcode.cn/problems/divide-two-integers/description/](https://leetcode.cn/problems/divide-two-integers/description/)

### 2.2 思路分析

**1. 二分查找**

如果除法结果溢出，那么我们需要返回 $2^{31}-1$ 作为答案。因此在编码之前，我们可以首先对于溢出或者容易出错的边界情况进行讨论：

- 当被除数为 32 位有符号整数的最小值 $-2^{31}$ 时：
    - 如果除数为 1，那么我们可以直接返回答案 $-2^{31}$；
    - 如果除数为 −1，那么答案为 $2^{31}$，产生了溢出。此时我们需要返回 $2^{31} - 1$。
- 当除数为 32 位有符号整数的最小值 $s-2^{31}$ 时：
    - 如果被除数同样为 $-2^{31}$，那么我们可以直接返回答案 111；
    - 对于其余的情况，我们返回答案 0。
- 当被除数为 0 时，我们可以直接返回答案 0。

对于一般的情况，根据除数和被除数的符号，我们需要考虑 444 种不同的可能性。因此，为了方便编码，我们可以将被除数或者除数取相反数，使得它们符号相同。

如果我们将被除数和除数都变为正数，那么可能会导致溢出。例如当被除数为 $-2^{31}$ 时，它的相反数 $2^{31}$ 产生了溢出。因此，我们可以考虑将被除数和除数都变为负数，这样就不会有溢出的问题，在编码时只需要考虑 1 种情况了。


如果我们将被除数和除数的其中（恰好）一个变为了正数，那么在返回答案之前，我们需要对答案也取相反数。

方法一：二分查找
思路与算法

根据「前言」部分的讨论，我们记被除数为 X，除数为 Y，并且 X 和 Y 都是负数。我们需要找出 X/Y 的结果 Z。Z 一定是正数或 0。

根据除法以及余数的定义，我们可以将其改成乘法的等价形式，即：

$$Z\times Y \geq X \geq (Z+1) \times Y$$

因此，我们可以使用二分查找的方法得到 ZZZ，即找出最大的 ZZZ 使得 Z×Y≥XZ \times Y \geq XZ×Y≥X 成立。

由于我们不能使用乘法运算符，因此我们需要使用「快速乘」算法得到 $Z \times Y$ 的值。

由于我们只能使用 32 位整数，因此二分查找中会有很多细节。

首先，二分查找的下界为 1，上界为 $2^{31} - 1$。唯一可能出现的答案为 $2^{31}$ 的情况已经被我们在「前言」部分进行了特殊处理，因此答案的最大值为 $2^{31} - 1$。如果二分查找失败，那么答案一定为 0。

在实现「快速乘」时，我们需要使用加法运算，然而较大的 Z 也会导致加法运算溢出。例如我们要判断 A + B 是否小于 C 时（其中 A,B,C 均为负数），A + B 可能会产生溢出，因此我们必须将判断改为 $A < C - B$ 是否成立。由于任意两个负数的差一定在 $[-2^{31} + 1, 2^{31} - 1]$ 范围内，这样就不会产生溢出。

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        # 快速乘
        def quickAdd(y: int, z: int, x: int) -> bool:
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    # 需要保证 result + add >= x
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True
        
        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans
```

复杂度分析
- 时间复杂度：$O(\log^2 C)$，其中 $C$ 表示 32 位整数的范围。二分查找的次数为 $O(\log C)$，其中的每一步我们都需要 $O(\log C)$ 使用「快速乘」算法判断 $Z \times Y \geq X$ 是否成立，因此总时间复杂度为 $O(\log^2 C)$。
- 空间复杂度：$O(1)$。



**2. 减法试除**
**思路一**
首先需要考虑正负号，处理为分子分母全是正数， 其次在返回的时候要注意是否溢出，如果溢出要判断。

核心是div函数怎么写？例如方法1中的div函数， 利用二进制搜索的思想就是， 每次利用加法，将当前的 divisor 乘以两倍，并同时用 multiple 记录下乘以了 2 的多少次方， multiple 的变化过程是1，2，4，8，16 。。。

因为任何一个数都可以用二进制的方法得到，所以我们可以利用二进制的思想来代表乘数 multiple， 最终能够得到一个 `divisor * multiple = dividend` 的multiple。

举例：算 $63 / 8$ 过程为：$63 / 8 = (63-32) / 8 + 4 = (63-32-16) / 8 + 2 + 4 = (63-32-16-8) / 8 + 1+ 2 + 4 = 7$ 其中 $(63-32-16-8) / 8 = 7 / 8 = 0$

```python
# 方法1：递归
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
        flag = 1                                    # 存储正负号，并将分子分母转化为正数
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor  = -flag, -divisor 
        
        def div(dividend, divisor):                 # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            if dividend < divisor:
                return 0
            cur = divisor
            multiple = 1
            while cur + cur < dividend:             # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur                          # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple
            return multiple + div(dividend - cur, divisor)
        res = div(dividend, divisor)

        res = res if flag > 0 else -res             # 恢复正负号
        
        if res < MIN_INT:                           # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT


# 方法2：迭代
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
        flag = 1                                    # 存储正负号，并将分子分母转化为正数
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor  = -flag, -divisor 
        
        res = 0
        while dividend >= divisor:                  # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            cur = divisor
            multiple = 1
            while cur + cur < dividend:             # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur                          # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple
            dividend -= cur                         # 辗转相减法
            res += multiple
        
        res = res if flag > 0 else -res             # 恢复正负号
        
        if res < MIN_INT:                           # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
```

**思路二**

用 $2^i$ 去作为乘法基数, $x * 2^i = x << i$。 从 $2^{31}$ 试到 $2^0$ 直到被除数被减到比除数小， 每个能满足除出来的最大的 2 的幂都加入答案, 也可以理解为每次计算出答案的 32 位中的某一位

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
```

_____

## 参考

- 两数相除——官方题解：[https://leetcode.cn/problems/divide-two-integers/solutions/1041939/liang-shu-xiang-chu-by-leetcode-solution-5hic/](https://leetcode.cn/problems/divide-two-integers/solutions/1041939/liang-shu-xiang-chu-by-leetcode-solution-5hic/)
- 减法试除：[https://leetcode.cn/problems/divide-two-integers/solutions/1042741/pythonjavajavascript-jian-fa-shi-chu-by-amrow/](https://leetcode.cn/problems/divide-two-integers/solutions/1042741/pythonjavajavascript-jian-fa-shi-chu-by-amrow/)
- 二进制搜索的思想：[https://leetcode.cn/problems/divide-two-integers/solutions/458026/29-python3-li-yong-er-jin-zhi-sou-suo-de-si-xiang-/](https://leetcode.cn/problems/divide-two-integers/solutions/458026/29-python3-li-yong-er-jin-zhi-sou-suo-de-si-xiang-/)