## 1 逆波兰表达式求值
### 1.1 题目描述

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据逆波兰表示法，求表达式的值。有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意：两个整数之间的除法只保留整数部分。可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

> 示例 1：
> 输入：tokens = [“2”,“1”,“+”,“3”,“*”]
> 输出：9
> 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

> 示例 2：
> 输入：tokens = [“4”,“13”,“5”,“/”,“+”]
> 输出：6
> 解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

> 示例 3：
> 输入：tokens = [“10”,“6”,“9”,“3”,“+”,“-11”,““,”/“,””,“17”,“+”,“5”,“+”]
> 输出：22
> 解释：该算式转化为常见的中缀算术表达式为：
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;题目链接：[https://leetcode.cn/problems/evaluate-reverse-polish-notation/](https://leetcode.cn/problems/evaluate-reverse-polish-notation/)

### 1.2 思路分析
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如(3+4)*5-6的逆波兰表达式为`3 4 + 5 * 6 -`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. 将表达式`3 4 + 5 * 6 -`放到`List`中（方便遍历）
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. 将`List`传递给一个方法，用于计算
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. 拿到`List`后，从左至右开始遍历，遇到数字直接压入栈
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. 遇到运算符，弹出栈顶和次顶的元素，进行计算，将得到的结果再次放入栈中
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. 一直重复，直到`List`遍历完毕，可得到最终结果

**复杂度分析**
- 时间复杂度：$O(n)$，其中$n$是数组`tokens`的长度。需要遍历数组`tokens`一次，计算逆波兰表达式的值。
- 空间复杂度：$O(n)$，其中$n$是数组`tokens`的长度。使用栈存储计算过程中的数，栈内元素个数不会超过逆波兰表达式的长度。

### 1.3 代码实现

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python中的运算符函数：
**方法一：**
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y)
        }       # 定义运算符              
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                num = op_to_binary_fn[token](operand1, operand2)
            finally:
                operand_stack.append(num)
        
        return operand_stack.pop()
```

**方法二：**
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                num = self.doMatch(token, operand1, operand2)
            finally:
                operand_stack.append(num)
        
        return operand_stack.pop()

        
    def doMatch(self, op, op1, op2):        # 自定义运算规则
        if op == "*":
            return op1 * op2
        elif op == "/":
            return int(op1/op2)
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;看了其他人的解题思路，一般就是在运算符上操作不同，有的使用`eval()`函数。
**解题心得：**
**问题一：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 中没有一个函数可以判断一个字符串是否为合理的整数（包括正、负数）。`str.isdigit()`可以判断正数，但是无法判断负数。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用`int()`函数，并做`try-except`。
- 如果是整数，那么可以用`int()`转成数字；
- 如果是运算符，那么`int()`会报错，从而进入 `except`中。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;整数字符串的最后一位肯定是数字，也可以以此来区分数字和运算符。
```python
if token[-1].isdigit():
    stack.append(int(token))
else:
    pass    # 处理运算符
```

补充知识点：
operator 模块


<table class="reference">

  <thead>
  <tr><th><p>运算</p></th>
  <th><p>语法</p></th>
  <th><p>函数</p></th>
  </tr>
  </thead>
  <tbody>
  <tr><td><p>加法</p></td>
  <td><p><code>a + b</code></p></td>
  <td><p><code>add(a, b)</code></p></td>
  </tr>
  <tr><td><p>字符串拼接</p></td>
  <td><p><code>seq1 + seq2</code></p></td>
  <td><p><code>concat(seq1, seq2)</code></p></td>
  </tr>
  <tr><td><p>包含测试</p></td>
  <td><p><code>obj in seq</code></p></td>
  <td><p><code>contains(seq, obj)</code></p></td>
  </tr>
  <tr><td><p>除法</p></td>
  <td><p><code>a / b</code></p></td>
  <td><p><code>truediv(a, b)</code></p></td>
  </tr>
  <tr><td><p>除法</p></td>
  <td><p><code>a // b</code></p></td>
  <td><p><code>floordiv(a, b)</code></p></td>
  </tr>
  <tr><td><p>按位与</p></td>
  <td><p><code>a &amp; b</code></p></td>
  <td><p><code>and_(a, b)</code></p></td>
  </tr>
  <tr><td><p>按位异或</p></td>
  <td><p><code>a ^ b</code></p></td>
  <td><p><code>xor(a, b)</code></p></td>
  </tr>
  <tr><td><p>按位取反</p></td>
  <td><p><code>~ a</code></p></td>
  <td><p><code>invert(a)</code></p></td>
  </tr>
  <tr><td><p>按位或</p></td>
  <td><p><code>a | b</code></p></td>
  <td><p><code>or_(a, b)</code></p></td>
  </tr>
  <tr><td><p>取幂</p></td>
  <td><p><code>a ** b</code></p></td>
  <td><p><code>pow(a, b)</code></p></td>
  </tr>
  <tr><td><p>标识</p></td>
  <td><p><code>a is b</code></p></td>
  <td><p><code>is_(a, b)</code></p></td>
  </tr>
  <tr><td><p>标识</p></td>
  <td><p><code>a is not b</code></p></td>
  <td><p><code>is_not(a, b)</code></p></td>
  </tr>
  <tr><td><p>索引赋值</p></td>
  <td><p><code>obj[k] = v</code></p></td>
  <td><p><code>setitem(obj, k, v)</code></p></td>
  </tr>
  <tr><td><p>索引删除</p></td>
  <td><p><code>del obj[k]</code></p></td>
  <td><p><code>delitem(obj, k)</code></p></td>
  </tr>
  <tr><td><p>索引取值</p></td>
  <td><p><code>obj[k]</code></p></td>
  <td><p><code>getitem(obj, k)</code></p></td>
  </tr>
  <tr><td><p>左移</p></td>
  <td><p><code>a &lt;&lt; b</code></p></td>
  <td><p><code>lshift(a, b)</code></p></td>
  </tr>
  <tr><td><p>取模</p></td>
  <td><p><code>a % b</code></p></td>
  <td><p><code>mod(a, b)</code></p></td>
  </tr>
  <tr><td><p>乘法</p></td>
  <td><p><code>a * b</code></p></td>
  <td><p><code>mul(a, b)</code></p></td>
  </tr>
  <tr><td><p>矩阵乘法</p></td>
  <td><p><code>a @ b</code></p></td>
  <td><p><code>matmul(a, b)</code></p></td>
  </tr>
  <tr><td><p>取反（算术）</p></td>
  <td><p><code>- a</code></p></td>
  <td><p><code>neg(a)</code></p></td>
  </tr>
  <tr><td><p>取反（逻辑）</p></td>
  <td><p><code>not a</code></p></td>
  <td><p><code>not_(a)</code></p></td>
  </tr>
  <tr><td><p>正数</p></td>
  <td><p><code>+ a</code></p></td>
  <td><p><code>pos(a)</code></p></td>
  </tr>
  <tr><td><p>右移</p></td>
  <td><p><code>a &gt;&gt; b</code></p></td>
  <td><p><code>rshift(a, b)</code></p></td>
  </tr>
  <tr><td><p>切片赋值</p></td>
  <td><p><code>seq[i:j] = values</code></p></td>
  <td><p><code>setitem(seq, slice(i, j), values)</code></p></td>
  </tr>
  <tr><td><p>切片删除</p></td>
  <td><p><code>del seq[i:j]</code></p></td>
  <td><p><code>delitem(seq, slice(i, j))</code></p></td>
  </tr>
  <tr><td><p>切片取值</p></td>
  <td><p><code>seq[i:j]</code></p></td>
  <td><p><code>getitem(seq, slice(i, j))</code></p></td>
  </tr>
  <tr><td><p>字符串格式化</p></td>
  <td><p><code>s % obj</code></p></td>
  <td><p><code>mod(s, obj)</code></p></td>
  </tr>
  <tr><td><p>减法</p></td>
  <td><p><code>a - b</code></p></td>
  <td><p><code>sub(a, b)</code></p></td>
  </tr>
  <tr><td><p>真值测试</p></td>
  <td><p><code>obj</code></p></td>
  <td><p><code>truth(obj)</code></p></td>
  </tr>
  <tr><td><p>比较</p></td>
  <td><p><code>a &lt; b</code></p></td>
  <td><p><code>lt(a, b)</code></p></td>
  </tr>
  <tr><td><p>比较</p></td>
  <td><p><code>a &lt;= b</code></p></td>
  <td><p><code>le(a, b)</code></p></td>
  </tr>
  <tr><td><p>相等</p></td>
  <td><p><code>a == b</code></p></td>
  <td><p><code>eq(a, b)</code></p></td>
  </tr>
  <tr><td><p>不等</p></td>
  <td><p><code>a != b</code></p></td>
  <td><p><code>ne(a, b)</code></p></td>
  </tr>
  <tr><td><p>比较</p></td>
  <td><p><code>a &gt;= b</code></p></td>
  <td><p><code>ge(a, b)</code></p></td>
  </tr>
  <tr><td><p>比较</p></td>
  <td><p><code>a &gt; b</code></p></td>
  <td><p><code>gt(a, b)</code></p></td>
  </tr>
  </tbody>
  </table>