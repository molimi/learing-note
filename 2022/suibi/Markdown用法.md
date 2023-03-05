## 1 基本用法
### 1.1 文本格式
**1. 设置分级标题**

```html
# 一级标题
## 二级标题
### 三级标题
```

# 一级标题
## 二级标题
### 三级标题

**2. 加粗文本**
```html
**印象笔记**
```
**印象笔记**


**3. 斜体**

```html
*印象笔记*
**天天向上**
*努力学习*
```

*印象笔记*
**天天向上**
*努力学习*
***

**4. 下划线**

```html
<u>how are you</u>
```
<u>how are you</u>


**5. 删除线**

```html
~~印象笔记不支持Markdown~~
```
~~印象笔记不支持Markdown~~

**6. 添加分割线**

```html
***
```

哈哈
***
那就这样吧
***

**7. 引用文本**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;文本前加`>`就可以了，如下所示：
> 鲁迅说：“横眉冷对千夫指，俯首甘为孺子牛”。


**8. 添加符号列表和数字列表**

```html
如何写代码
1. 下载编辑器
2. 找到代码框架
3. 根据语法编写
```

如何写代码
1. 下载编辑器
2. 找到代码框架
3. 根据语法编写

```html
- 编辑器正确
- 语法合法
```

- 编辑器正确
- 语法合法

***
**9. 添加待办事项**

```html
第十周工作安排
* [x] 周一上课
* [ ] 周二写作业
* [X] 周三锻炼
```

第十周工作安排
* [x] 周一上课
* [ ] 周二写作业
* [X] 周三锻炼



### 1.2 内容插入

**1. 插入链接**

```html
[百度百科](https://baike.baidu.com/)
```
[百度百科](https://baike.baidu.com/)

**2. 插入图片**

```html
![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011163847955-1939386973.png)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;效果如下图所示：

![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011163847955-1939386973.png)


**3. 插入表格**
```html
|账户类型|免费账户|标准账户|高级账户|
|---|---|---|---|
| 帐户流量 | 60M | 1GB | 10GB |
| 设备数目 | 2台 | 无限制 | 无限制 |
| 当前价格 | 免费 | ￥8.17/月 | ￥12.33/月|
```
***

|账户类型|免费账户|标准账户|高级账户|
|---|---|---|---|
| 帐户流量 | 60M | 1GB | 10GB |
| 设备数目 | 2台 | 无限制 | 无限制 |
| 当前价格 | 免费 | ￥8.17/月 | ￥12.33/月|


**4. 插入行内代码或代码块**

```html
```
#python
import turtle
turtle.pensize(50)
turtle.down
```
```
**5. 插入数学公式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;印象笔记 Markdown 支持绝大多数的 LaTeX 数学公式，行间公式使用`$$f(x)=sin(x)$$`，行内公式使用`$\pmb{A}\in{\mathcal{R}}$`
~~你太菜了~~

```math
e^{i/pi} +1 = 0
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详细了解，可以参考：[Cmd Markdown 公式指导手册](https://www.zybuluo.com/codeep/note/163962#3)



**6. 设置目录**

设置之后可以自动根据设置的分级标题来自动生成目录。
```html
@[TOC]
```

## 2 多学几招

Markdown也支持HTML格式，于是可以设置复杂的文本格式，比如页内跳转、图片大小，图片标题的设置等等

**1. 字体颜色设置**
```html
<font color=#9900CC ><strong> /etc/sudoers</strong></font>       
```
<font color=#9900CC ><strong> /etc/sudoers</strong></font>   

**2. 多个空格**
```html
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
```

**3. 换行**
```html
<br> </br>
```

**4. 复杂的表格设计**

```HTML
<table>
  <tr>
    <th> </th>
    <th colspan="3">可分享的(shareable)</th>
    <th colspan="3">不可分享的(unshareable) </th>
  </tr>
  <tr>
    <td rowspan="2"><center>不可变的(static) </center></td>
    <td colspan="3"><center>/usr(软件放置处)</center></td>
    <td colspan="3"><center>/etc(配置文件)</center></td>
  </tr>
  <tr>
    <td colspan="3"><center>/opt(第三方软件)</center></td>
    <td colspan="3"><center>/boot(开机及内核文件)</center></td>
  </tr>
  </tr>
  <tr>
    <td rowspan="2"><center>可变动的(variable) </center></td>
    <td colspan="3"><center>/var/mail(用户邮件信箱)</center></td>
    <td colspan="3">/var/run(程序相关)</center></td>
  </tr>
  <tr>
    <td colspan="3"><center>/var/news(新闻组)</center></td>
    <td colspan="3"><center>/var/lock(文件锁相关)</center></td>
  </tr>
  </table>
```
<table>
  <tr>
    <th> </th>
    <th colspan="3">可分享的(shareable)</th>
    <th colspan="3">不可分享的(unshareable) </th>
  </tr>
  <tr>
    <td rowspan="2"><center>不可变的(static) </center></td>
    <td colspan="3"><center>/usr(软件放置处)</center></td>
    <td colspan="3"><center>/etc(配置文件)</center></td>
  </tr>
  <tr>
    <td colspan="3"><center>/opt(第三方软件)</center></td>
    <td colspan="3"><center>/boot(开机及内核文件)</center></td>
  </tr>
  </tr>
  <tr>
    <td rowspan="2"><center>可变动的(variable) </center></td>
    <td colspan="3"><center>/var/mail(用户邮件信箱)</center></td>
    <td colspan="3">/var/run(程序相关)</center></td>
  </tr>
  <tr>
    <td colspan="3"><center>/var/news(新闻组)</center></td>
    <td colspan="3"><center>/var/lock(文件锁相关)</center></td>
  </tr>
  </table>

  
**5. 合并单元格**

```html
<table>
    <thead>
        <tr>
            <th>表头</th>
            <th>表头</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>单元格</td>
            <td>单元格</td>
        </tr>
        <tr>
            <td>单元格</td>
            <td>单元格</td>
        </tr>
    </tbody>
</table>
```

<table>
<thead>
<tr>
<th>表头</th>
<th>表头</th>
</tr>
</thead>
<tbody>
<tr>
<td>单元格</td>
<td>单元格</td>
</tr>
<tr>
<td>单元格</td>
<td>单元格</td>
</tr>
</tbody>
</table>


**6. 给图片添加题注**

```html
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="这里输入图片地址"> <br> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">这里输入题注</div> </center>
```


```html
<center class = "half"><img src ="https://img-blog.csdnimg.cn/0de4c927c29c43b6b1fa8490949eb032.png#pic_left" width = "40%"><img src = "https://img-blog.csdnimg.cn/7c5e9e98012f4108b874a5294d3e4566.png#pic_left"  width = "48%"></center></p>
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;修改width的值就可以修改图片大小。
<center class = "half"><img src ="https://img-blog.csdnimg.cn/0de4c927c29c43b6b1fa8490949eb032.png#pic_left" width = "40%"><img src = "https://img-blog.csdnimg.cn/7c5e9e98012f4108b874a5294d3e4566.png#pic_left"  width = "48%"></center></p>


**7. 页内跳转**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;定义一个锚(id)：
```html
使用markdown语法：[点击跳转](#jump)
<span id="jump">跳转到的地方</span>
```