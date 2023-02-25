## 1 计数质数
### 1.1 题目描述
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。


> 示例 1：
> 输入：n = 10
> 输出：4
> 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

> 示例 2：
> 输入：n = 0
> 输出：0

> 示例 3：
> 输入：n = 1
> 输出：0

题目链接：[https://leetcode.cn/problems/count-primes](https://leetcode.cn/problems/count-primes/)


### 1.2 思路分析
**方法一：枚举法（计算超时）**

很直观的思路是我们枚举每个数判断其是不是质数。

考虑质数的定义：在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数的自然数。因此对于每个数 $x$，我们可以从小到大枚举 $[2, −1]$ 中的每个数 $y$，判断 $y$ 是否为 $x$ 的因数。但这样判断一个数是否为质数的时间复杂度最差情况下会到 $O(n)$，无法通过所有测试数据。

考虑到如果 $y$ 是 $x$ 的因数，那么 $\frac{x}{y}$ 也必然是 $x$ 的因数，因此我们只要校验 $y$ 或者 $\frac{x}{y}$ 即可。而如果我们每次选择校验两者中的较小数，则不难发现较小数一定落在 $[2, \sqrt(x)]$ 的区间中，因此我们只需要枚举  $[2, \sqrt(x)]$  中的所有数即可，这样单次检查的时间复杂度从 $O(n)$ 降低至了 $O(\sqrt(n))$。

示例代码：
```python
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(n):
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        count = 0 if n < 2 else 1
        for i in range(2, n):
            if is_prime(i):
                count += 1
        return count
```
复杂度分析：
- 时间复杂度：$O(n\sqrt(n))$。单个数检查的时间复杂度为$O(\sqrt(n))$，一共要检查 $O(n)$ 个数，因此总时间复杂度为：$O(n\sqrt(n))$。
- 空间复杂度：$O(1)$。

做进一步的优化，首先素数的判断，没必要去除以 $[2, \sqrt(x)]$ 之间的所有数，寻找质数时，质数里除了2以外都是奇数，只需要遍历小于 $n$ 的奇数即可，但依然超时，毕竟复杂度的数量级没降下来。

```python
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(number):
            """优化对素数的判断"""
            if number == 2 or number == 3:
                return True
            if number % 2 == 0 or number % 3 == 0:
                return False
            for i in range(6, int(sqrt(number))+2, 6):  
                if number % (i-1) == 0 or number % (i+1) == 0:
                    return False
            return True

        count = 0 if n < 2 else 1
        for i in range(3, n, 2):    # 偶数除了2肯定不能是质数，只判断奇数
            if is_prime(i):
                count += 1
        return count
```

**方法二：厄拉多塞筛算法**

厄拉多塞筛算法（Eratosthenes Sieve）是一种求素数的方法，由古希腊数学家厄拉多塞提出，简称埃氏筛，也称素数筛。这是一种简单且历史悠久的筛法，用来找出一定范围内所有的素数。它的原理是，给定一个数 n，从 2 开始依次将 $\sqrt(n)$以内的素数的倍数标记为 **合数**，标记完成后，剩余未被标记的数为素数（从 2 开始）。如此可省去检查每个数的步骤，使筛选素数的过程更加简单。厄拉多塞筛算法具体步骤如下：
1. 读取输入的数 n，将 2 到 n 的所有整数记录在表中
2. 从 $i=2$ 开始，划去表中所有 2 的倍数
3. 由小到大寻找表中下一个未被划去的整数，再划去表中所有该整数的倍数
4. 重复第（3）步，直到找到的 $i$ 大于$\sqrt(n)$为止
5. 表中所有未被划去的整数均为素数

<img src ="https://img-blog.csdnimg.cn/8116abbbf7cd46e99ebf631fdc2fc30c.jpeg#pic_center" width = 48%>


算法流程图：

<img src ="https://img-blog.csdnimg.cn/9d2aacd8ffa04414818faf86dea5ea90.jpeg#pic_center" width = 48%>

> 一个素数的各个倍数，是一个差为此素数本身的等差数列。此为这个筛法和试除法不同的关键之处，后者是以素数来测试每个待测数能否被整除。

下面以所有不超过100的素数为例，因为小于等于10的所有素数为2、3、5、7，所以依次删除2、3、5、7的倍数。

<img src ="https://img-blog.csdnimg.cn/8ce0247b32994186897b4afde1aa098c.gif#pic_center" width = 36%>

代码实现：
```python
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0                  # 不存在小于 2 的素数
        flag_list = [1 for _ in range(n)]
        flag_list[:2] = [0, 0]
        for i in range(2, int(n**0.5)+1):   #  遍历 i=2 到 根号 n
            if flag_list[i]:                 # 筛去 i 的倍数
                for j in range(i*i, n, i):
                    flag_list[j] = 0
        return sum(flag_list)
```
这里在筛去 $i$ 的倍数的时候，第一个数是 $i\times i$ 而不是 $i$，这是因为对于所有 $k\times i$，$k<i$，都在前面被筛过，故可以跳过这些数



**温馨提示：** 使用 python 时间和空间效率都较低，对于标记素数，可以采用 c++ 的 bitset，bitset 是以比特为单位标记的，会极大降低存储消耗。可以参考：[运用比特表（Bitmap）算法对筛法进行内存优化](https://leetcode.cn/problems/count-primes/solution/ji-shu-zhi-shu-bao-li-fa-ji-you-hua-shai-fa-ji-you/)