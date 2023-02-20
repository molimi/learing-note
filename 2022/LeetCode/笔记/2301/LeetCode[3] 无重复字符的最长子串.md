## 1 无重复字符的最长子串
### 1.1 题目描述
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

> 示例 1:
> 输入: s = "abcabcbb"
> 输出: 3 
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

> 示例 2:
> 输入: s = "bbbbb"
> 输出: 1
> 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

> 示例 3:
> 输入: s = "pwwkew"
> 输出: 3
> 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     > 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

题目链接：[https://leetcode.cn/problems/longest-substring-without-repeating-characters/](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

### 1.2 思路分析
滑动窗口法：其实用一句话描述就是使用两个指针，指针头和指针尾依次遍历，当指针尾遍历到的字母包含在指针头和指针尾的字符串里，就把指针头移动到当前字母出现的位置，重新构成一个子串，并判断当前子串的长度与原来记录的最大长度作比较，并更新最大长度。示意图如下面：

![img](https://img2022.cnblogs.com/blog/2692004/202209/2692004-20220928223526110-1543219085.png)


### 1.3 代码实现

**思路一：滑动窗口法**
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 思路一：滑动窗口法
        temp_str = ''
        max_len, current_len = 0, 0
        for i in range(len(s)):
            if s[i] not in temp_str:
                temp_str += s[i]
                current_len += 1
            else:
                index = temp_str.index(s[i])
                temp_str = temp_str[index+1:]
                temp_str += s[i]
                current_len = len(temp_str)
            if max_len < current_len:
                max_len = current_len
        
        return max_len
```