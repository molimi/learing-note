## 1 单调栈

栈（stack）是很简单的一种数据结构，先进后出的逻辑顺序，符合某些问题的特点，比如说函数调用栈。

单调栈实际上就是栈，只是利用了一些巧妙的逻辑，使得每次新元素入栈后，栈内的元素都保持有序（单调递增或单调递减）。

用简洁的话来说就是：单调栈就是<font color=#9900CC><strong>栈内元素单调递增或者单调递减</strong></font>的栈，单调栈只能在栈顶操作。

听起来有点像堆（heap）？不是的，单调栈用途不太广泛，只处理一种典型的问题，叫做 Next Greater Element。本文用讲解单调队列的算法模版解决这类问题，并且探讨处理「循环数组」的策略。



## 2 真题演练
### 2.1 题库列表

<table><thead><tr><th>题号</th><th>链接</th></tr></thead><tbody><tr><td>496</td><td><a href="https://leetcode.cn/problems/next-greater-element-i/" target="_blank">下一个更大元素 I</a>（简单）</td></tr><tr><td>503</td><td><a href="https://leetcode.cn/problems/next-greater-element-ii/" target="_blank">下一个更大元素 II</a>（中等）</td></tr><tr><td>739</td><td><a href="https://leetcode.cn/problems/daily-temperatures/" target="_blank">每日温度</a>（中等）</td></tr><tr><td>42</td><td><a href="https://leetcode.cn/problems/trapping-rain-water/" target="_blank">接雨水</a>（困难）</td></tr><tr><td>84</td><td><a href="https://leetcode.cn/problems/largest-rectangle-in-histogram/" target="_blank">柱状图中最大的矩形</a>（困难）</td></tr><tr><td>402</td><td><a href="https://leetcode.cn/problems/remove-k-digits/" target="_blank">移掉 K 位数字</a>（中等）</td></tr><tr><td>316</td><td><a href="https://leetcode.cn/problems/remove-duplicate-letters/" target="_blank">去除重复字母</a>（中等）</td></tr><tr><td>321</td><td><a href="https://leetcode.cn/problems/create-maximum-number/" target="_blank">拼接最大数</a>（困难）</td></tr></tbody></table>



**496. 下一个更大元素 I**

<img src ="https://img-blog.csdnimg.cn/46b0683955fc491994e872ca053927bd.png#pic_center" width = 64%>



**503. 下一个更大元素 II**

<img src ="https://img-blog.csdnimg.cn/984a323bc3644f658e86ca0d573d91c6.png#pic_center" width = 64%>





**739. 每日温度**

<img src ="https://img-blog.csdnimg.cn/c9567749c1a743e2b94324331b26ec9e.png#pic_center" width = 64%>



**42. 接雨水**

<img src ="https://img-blog.csdnimg.cn/16fbf37c4c0a4ffda718be399aab036f.png#pic_center" width = 64%>


**84. 柱状图中最大的矩形**

<img src ="https://img-blog.csdnimg.cn/01960973ec774e63905883fc1aca1806.png#pic_center" width = 64%>


**402. 移掉 K 位数字**

<img src ="https://img-blog.csdnimg.cn/e2e4d9bc498f40b9a27ed56011275722.png#pic_center" width = 64%>







**316. 去除重复字母**

<img src ="https://img-blog.csdnimg.cn/7fbf7fc1d70e49bf9d931a3e2f1f4d27.png#pic_center" width = 64%>



**321. 拼接最大数**


<img src ="https://img-blog.csdnimg.cn/d0ae08993e7244af8e8b58fb61f3336c.png#pic_center" width = 64%>
