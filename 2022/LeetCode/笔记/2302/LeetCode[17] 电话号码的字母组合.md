## 1 电话号码的字母组合
### 1.1 题目描述

<img src ="https://img-blog.csdnimg.cn/3fb5383f013d46ee991e26483bdb7566.png#pic_center" width = 80%>


题目链接：[https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)

### 1.2 回溯解法

这道题的解法是用回溯的方式，在循环里面套了递归调用。本来递归就不好理解了，再加上循环的递归，就更难理解了。 我们先不考虑递归，先看看下面这个问题怎么解决。 假设输入是2，只有一个字符，那么应该怎么解呢？ 按照题目要求2=“abc"，所以结果应该是`["a","b","c"]`先不用想着怎么去写递归，只思考下怎么打印出这个结果。 这个太简单了，一个循环就搞定了：

```python
result = []
for ch in "abc":
    result.append(ch)
return result
```

上面是伪代码，一个循环就搞定了。 如果输入的是23，应该怎么做呢？23的结果是`["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`，我们仍然不考虑怎么去写递归，只是考虑怎么把这个结果给弄出来。代码如下：
```python
result = []
for ch1 in "abc":
    for ch2 in "def":
        result.append(ch1+ch2)
return result
```

也就是说23这样的长度为2的字符串可以用两层循环搞定。 如果输入的是234呢，仍然不要考虑怎么去写递归，而是想怎么把结果打印出来。
```python
result = []
for ch1 in "abc":
    for ch2 in "def":
        for ch3 in "ghi":
            result.append(ch1+ch2+ch3)
return result
```


这次用了三层循环。 如果输入的是2345，那么代码可以这么写：
```python
result = []
for ch1 in "abc":
    for ch2 in "def":
        for ch3 in "ghi":
            for ch4 in "jkl":
                result.append(ch1+ch2+ch3+ch4)
return result
```

这次是用了四层循环。现在是不是能看出一些门道了？对的。循环的嵌套层数，就是输入的字符串长度。输入的字符串长度是1，循环只有1层。 输入的字符串长度是3，循环就是3层。如果输入的字符串长度是10，那么循环就是10层。 可是输入的字符串长度是不固定的，对应的循环的嵌套层数也是不固定的，那这种情况怎么解决呢？这时候递归就派上用场了。

<img src ="https://img-blog.csdnimg.cn/a1cc59d77c45433daf10890ccafe20f7.jpeg#pic_center" width = 48%>

对于打印"2345"这样的字符串： 第一次递归就是上图中最下面的方格，然后处理完第一个字符2之后，将输入的字符改变成"345"并调用第二个递归函数 第二次递归处理3，将字符串改变成"45"后再次递归 第三次递归处理4，将字符串改变成"5"后继续递归 第四次递归处理5，将字符串改变成""后继续递归 最后发现字符串为空了，将结果放到列表中并返回 上面是从函数调用的角度去看的，而每次调用下一层递归时，都需要将本层的一些处理结果放到一个临时变量中，再传递给下一层，从这个变量层层传递的变化看，就像一棵树一样，这个算法的时间复杂度很高，是 $O(3^n)$ 这个级别的，空间复杂度是 $O(n)$

<img src ="https://img-blog.csdnimg.cn/ebb00fc6c64f476c820d677320f7059d.jpeg#pic_center" width = 48%>


动图如下：
<img src ="https://img-blog.csdnimg.cn/231e6f91e8d14882ad4468243aa80fba.gif#pic_center" width = 48%>

```python
class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		# 注意边界条件
		if not digits:
			return []
		# 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
		# 这里也可以用map，用数组可以更节省点内存
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		# 最终输出结果的list
		res = []
		
		# 递归函数
		def backtrack(tmp, index):
			# 递归的终止条件，注意这里的终止条件看上去跟动态演示图有些不同，主要是做了点优化
			# 动态图中是每次截取字符串的一部分，"234"，变成"23"，再变成"3"，最后变成""，这样性能不佳
			# 而用index记录每次遍历到字符串的位置，这样性能更好
			if index==len(digits):
				res.append(tmp)
				return
			# 获取index位置的字符，假设输入的字符是"234"
			# 第一次递归时index为0所以c=2，第二次index为1所以c=3，第三次c=4
			# subString每次都会生成新的字符串，而index则是取当前的一个字符，所以效率更高一点
			c = digits[index]
			# map_string的下表是从0开始一直到9， ord(c)-48 是获取c的ASCII码然后-48, 48是0的ASCII
			# 比如c=2时候，2-'0'，获取下标为2, letter_map[2]就是"abc"
			letters = d[ord(c)-48]
			
			# 遍历字符串，比如第一次得到的是2，页就是遍历"abc"
			for i in letters:
				# 调用下一层递归，用文字很难描述，请配合动态图理解
				backtrack(tmp+i,index+1)
		backtrack("", 0)
		return res
```


### 1.3 队列

我们也可以使用队列，先将输入的 digits 中第一个数字对应的每一个字母入队，然后将出队的元素与第二个数字对应的每一个字母组合后入队...直到遍历到 digits 的结尾。最后队列中的元素就是所求结果。

<img src ="https://img-blog.csdnimg.cn/a3046909aa2643b2ad4bbd6819bc734e.gif#pic_center" width = 48%>

```python
class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""	
		if not digits:
			return []
		# 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
		# 这里也可以用map，用数组可以更节省点内存
		d = [" ","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
		# 先往队列中加入一个空字符
		res = [""]
		for i in digits:
			size = len(res)
			# 由当前遍历到的字符，取字典表中查找对应的字符串
			letters = d[ord(i)-48]
			# 计算出队列长度后，将队列中的每个元素挨个拿出来
			for _ in xrange(size):
				# 每次都从队列中拿出第一个元素
				tmp = res.pop(0)
				# 然后跟"def"这样的字符串拼接，并再次放到队列中
				for j in letters:
					res.append(tmp+j)
		return res
```


____

## 参考
- 通俗易懂+动画演示 17. 电话号码的字母组合：[https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solutions/44182/tong-su-yi-dong-dong-hua-yan-shi-17-dian-hua-hao-m/](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solutions/44182/tong-su-yi-dong-dong-hua-yan-shi-17-dian-hua-hao-m/)
- 回溯+队列 图解：[https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/)