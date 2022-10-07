## 1 罗马数转整数
### 1.1 题目描述
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;罗马数字包含以下七种字符： `I`， `V`， `X`， ``L`，`C`，`D` 和 `M`。

| 字符 | 数值 |
|--|--|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;例如， 罗马数字 2 写做 `II` ，即为两个并列的 1。12 写做 `XII` ，即为 `X + II` 。 27 写做  `XXVII`, 即为 `XX + V + II` 。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

> 示例 1:
> 输入: s = "III"
> 输出: 3

> 示例 2:
> 输入: s = "IV"
> 输出: 4

> 示例 3:
> 输入: s = "IX"
> 输出: 9

> 示例 4:
> 输入: s = "LVIII"
> 输出: 58
> 解释: L = 50, V= 5, III = 3.

> 示例 5:
> 输入: s = "MCMXCIV"
> 输出: 1994
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

题目链接：[https://leetcode.cn/problems/roman-to-integer/](https://leetcode.cn/problems/roman-to-integer/)


### 1.2 代码实现

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;思路一：观察下图，我们可以发现罗马数字最多为两位，所以可以利用这个来判断和下一个字母组合是否是构成一个整数，示例代码如下：

![img](https://img2022.cnblogs.com/blog/2692004/202209/2692004-20220928105934767-150779760.png)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'M': 1000, 'CM': 900, 'D':500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        result = 0
        index = 0
        while index < len(s):
            if s[index:index+2] in symbol_value.keys():
                result += symbol_value[s[index:index+2]]
                index += 2
            else:
                result += symbol_value[s[index]]
                index += 1
        return result
```


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;思路二：我们由上面的定义可以知道，对于罗马数字`AB`，A代表的整数小于B是，要用B代表的整数减去A代表的整数，否则两个代表的整数相加。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'M': 1000, 'D':500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        for i in range(len(s)-1):
            if symbol_value[s[i]] < symbol_value[s[i+1]]:
                result -= symbol_value[s[i]]
            else:
                result += symbol_value[s[i]]
        return result + symbol_value[s[-1]]
```