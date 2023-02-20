## 1 整数转罗马数字
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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;给你一个整数，将其转为罗马数字。

> 示例 1:
> 输入: num = 3
> 输出: "III"

> 示例 2:
> 输入: num = 4
> 输出: "IV"


> 示例 3:
> 输入: num = 9
> 输出: "IX"

> 示例 4:
> 输入: num = 58
> 输出: "LVIII"
> 解释: L = 50, V = 5, III = 3.

> 示例 5:
> 输入: num = 1994
> 输出: "MCMXCIV"
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;提示：1 <= num <= 3999

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;题目链接：[https://leetcode.cn/problems/integer-to-roman/](https://leetcode.cn/problems/integer-to-roman/)


### 1.2 思路分析
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据题目分析，我们知道罗马数字由 7 个不同的单字母符号组成，每个符号对应一个具体的数值。此外，减法规则（如问题描述中所述）给出了额外的 6 个复合符号。这给了我们总共 13 个独特的符号（每个符号由 1 个或 2 个字母组成），如下图所示
![img](https://img2022.cnblogs.com/blog/2692004/202209/2692004-20220928105934767-150779760.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;考虑 140140 的罗马数字表示，我们用来确定罗马数字的规则是：对于罗马数字从左到右的每一位，选择尽可能大的符号值。对于 140，最大可以选择的符号值为 C=100。接下来，对于剩余的数字 40，最大可以选择的符号值为 XL=40。因此，140 的对应的罗马数字为 `C+XL=CXL`。这说明罗马数字是唯一表示的。(这不就是贪心策略，和找零钱的问题有点类似)


### 1.3 代码实现

**1. 思路一: 模拟**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据罗马数字的唯一表示法，为了表示一个给定的整数 num，我们寻找不超过 num 的最大符号值，将 num 整除该符号值，并将整除的值乘以该符号，然后继续寻找不超过 num 的最大符号值，将该符号拼接在上一个找到的符号之后，循环直至 num 为 0。最后得到的字符串即为 num 的罗马数字表示。设计算法的思想如下：每一步都使用当前对应阿拉伯数字较大的罗马数字作为加法因子，最后得到罗马数字表示就是长度最少的。(贪心算法)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;编程时，可以建立一个数值-符号对的列表 value_symbol，按数值从大到小排列。遍历 value_symbol 中的每个数值-符号对，若当前数值 value 不超过 num，则从 num 中不断减去 value，直至 num 小于 value，然后遍历下一个数值-符号对。若遍历中 num 为 0 则跳出循环。

**示例代码：**
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbol = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        for value, symbol in value_symbol:
            if num >= value:
                result += symbol * (num // value)
                num = num % value
            if num == 0:
                break

        return result
```

**复杂度分析**
- 时间复杂度：$O(1)$。由于 value_symbol 长度是固定的，且这 13 字符中的每个字符的出现次数均不会超过 3(超过3就要进位了)，因此循环次数有一个确定的上限。
- 空间复杂度：$O(1)$。

**2. 思路二：硬编码数字**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们可以计算出每个数字在每个位上的表示形式，整理成一张硬编码表。如下图所示，其中 0 对应的是空字符串。

![img](https://img2022.cnblogs.com/blog/2692004/202209/2692004-20220928110001715-821758298.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;利用模运算和除法运算，我们可以得到 num 每个位上的数字：
```python
thousands_digit = num // 1000
hundreds_digit = (num % 1000) // 100
tens_digit = (num % 100) // 10
ones_digit = num % 10
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;最后，根据 num 每个位上的数字，在硬编码表中查找对应的罗马字符，并将结果拼接在一起，即为 num 对应的罗马数字。

```python
class Solution:
    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    def intToRoman(self, num: int) -> str:
        return Solution.thousands[num//1000] + Solution.hundreds[num%1000//100] + Solution.tens[num%100//10] + Solution.ones[num%10]
```
**复杂度分析**
- 时间复杂度：$O(1)$。计算量与输入数字的大小无关。
- 空间复杂度：$O(1)$。