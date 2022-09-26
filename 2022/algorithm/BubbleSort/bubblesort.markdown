&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;冒泡排序（Bubble Sort）是一种简单的排序算法，它也是一种稳定排序算法。其实现原理是重复扫描待排序序列，并比较每一对相邻的元素，当该对元素顺序不正确时进行交换。一直重复这个过程，直到没有任何两个相邻元素可以交换，就表明完成了排序。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当一趟操作完成时，序列中最大的未排序元素就被放置到了所有未排序的元素中最后的位置上，它就像水中的石块一样沉到了水底。而其它较小的元素则被移动到了序列的前面，就像水中的气泡冒到了水面一样。这就是为什么该算法被叫做冒泡排序的原因。


<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/ed777a810bb74acab8cd23b172ad3970.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图1  冒泡排序的基本原理</div> </center>

____
## 1 基本概念
### 1.1 算法原理
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;图1展示了冒泡排序的基本原理。假设一个序列中共有 n 个元素，那么上面的比较和交换过程一共需要进行$n-1$趟：
- 第一趟需要比较序列中的所有元素，它的效果是将整个序列中最大的元素放置到了序列最后一个位置上。
- 第二趟只需要比较前面$n-1$个元素，因为前一趟中已经将最大的元素移到了它最终的位置上了。这一趟结束时，整个序列中第二大的元素就被放置到了倒数第二个位置上。
- 同样的，第三趟只需要比较前面$n-2$个元素。该趟结束时，序列中第三大的元素就被放到了倒数第三个位置上。
当进行第$i$趟的时候，需要比较的是前面$n-(i-1)$个元素，因为序列中最大的$i-1$个元素已经在前面的$i-1$趟排序中被排好了。注意，比较 $n-(i-1)$个元素需要进行$n-i$次比较。
- 当最终到达第$n-1$趟的时候，只需要比较序列中最前面的两个数而已。该趟结束时，序列中第二小的数就被放置到了顺数第二个位置上。同时，序列中最小的数也被放到了第一个位置上。整个排序过程完成。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从以上对算法原理的讲解中，我们首先可以知道冒泡排序是一种交换排序，它需要进行大量的交换操作。其次，因为当两个元素相等时它们不会被交换，所以相等元素的相对位置在排序前后不会改变，因此冒泡排序又是一种稳定的排序算法。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;假设待排序序列为[5,1,4,2,8]，如果采用冒泡排序对其进行升序（由小到大）排序，则整个排序过程如下所示：
1) 第一轮排序，此时整个序列中的元素都位于待排序序列，依次扫描每对相邻的元素，并对顺序不正确的元素对交换位置，整个过程如图2所示。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/572cd9cda2c849788a59a0e698558fca.gif#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图2  第一轮排序（白色字体表示参与比较的一对相邻元素）</div> </center>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从图 1 可以看到，经过第一轮冒泡排序，从待排序序列中找出了最大数 8，并将其放到了待排序序列的尾部，并入已排序序列中。

2) 第二轮排序，此时待排序序列只包含前 4 个元素，依次扫描每对相邻元素，对顺序不正确的元素对交换位置，整个过程如图3所示。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/13312fb6aebd48ed9f1618463962ac38.gif#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图3  第二轮排序</div> </center>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看到，经过第二轮冒泡排序，从待排序序列中找出了最大数 5，并将其放到了待排序序列的尾部，并入已排序序列中。

3) 第三轮排序，此时待排序序列包含前 3 个元素，依次扫描每对相邻元素，对顺序不正确的元素对交换位置，整个过程如图4所示。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/94b76f61376243c0819c5779c4dc4d3b.gif#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图4  第三轮排序</div> </center>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;经过本轮冒泡排序，从待排序序列中找出了最大数 4，并将其放到了待排序序列的尾部，并入已排序序列中。

4) 第四轮排序，此时待排序序列包含前 2 个元素，对其进行冒泡排序的整个过程如图5所示。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/ab525ee9e331468595a22a56c66e3d8a.gif#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图5  第四轮排序</div> </center>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;经过本轮冒泡排序，从待排序序列中找出了最大数 2，并将其放到了待排序序列的尾部，并入已排序序列中。

5) 当进行第五轮冒泡排序时，由于待排序序列中仅剩 1 个元素，无论再进行相邻元素的比较，因此直接将其并入已排序序列中，此时的序列就认定为已排序好的序列（如图6所示）。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/8f0c6a8263fb49e1b53ead7a4b8105f1.gif#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图6  冒泡排序好的序列</div> </center>



**代码一：**
```python
def bubble_sort(items):
    """简单冒泡排序"""
    items = items[:]        # 复制原序列
    length = len(items)     # 序列中元素的数量
    # 外层循环控制第1至第(n-1)趟排序
    for i in range(1, length):
        # 内层循环用于第i趟时，对前面n-(i-1)个元素进行比较和交换
        for j in range(length - i):
            # 如果前一个元素大于后一个元素，则交换他们
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
```
### 1.2 性能分析
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由上面的排序步骤可知：$N$个数字要排序完成，总共进行$N-1$趟排序，每$i$趟的排序次数为$(N-i)$次，所以可以用双重循环语句，外层控制循环多少趟，内层控制每一趟的循环次数

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;冒泡排序的优点：每进行一趟排序，就会少比较一次，因为每进行一趟排序都会找出一个较大值。如上例：第一趟比较之后，排在最后的一个数一定是最大的一个数，第二趟排序的时候，只需要比较除了最后一个数以外的其他的数，同样也能找出一个最大的数排在参与第二趟比较的数后面，第三趟比较的时候，只需要比较除了最后两个数以外的其他的数，以此类推……也就是说，每进行一趟比较，每一趟少比较一次，一定程度上减少了算法的量。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;时间复杂度：1）如果我们的数据正序，只需要走一趟即可完成排序。所需的比较次数$C$和记录移动次数$M$均达到最小值，即：$C_{min}=n-1; M_{min}=0$；所以，冒泡排序最好的时间复杂度为$O(n)$；2）如果很不幸我们的数据是反序的，则需要进行$n-1$趟排序。每趟排序要进行$n-i$次比较($1≤i≤n-1$)，且每次比较都必须移动记录三次来达到交换记录位置。在这种情况下，比较和移动次数均达到最大值：
$$C_{max}=\frac{n(n-1)}{2}=O(n^2)\\
M_{max}=\frac{3n(n-1)}{2}=O(n^2)$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上所述：冒泡排序总的平均时间复杂度为：$O(n^2)$时间复杂度和数据状况无关。
____
## 2 算法优化
### 2.1 第一次优化
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因为冒泡排序必须要在最终位置找到之前不断交换数据项，所以它经常被认为是最低效的排序方法。这些“浪费式”的交换操作消耗了许多时间。比如序列中的元素有可能出现这样的情况，即经过前面几趟的排序后整个序列就已经排好序了，那么后面的那几趟排序就不需要再执行了。但是我们上面的第一版的冒泡排序即便是在这种情况下，仍然会执行所有的$n-1$趟的排序。即使后面几趟排序只进行比较而不需交换元素，但是当数据量很大的时候，这依旧会造成整体性能的明显下降。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此，我们首先想到的优化方案就是当某一趟排序之后，如果整个序列已排好序了，那么就立即退出函数。这要怎么实现呢？其实很简单，只要在某一趟的排序中没有进行任何一次的元素交换，那么此时整个序列就排好序了。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此，在每一趟排序的开始将一个标记`swapped`设置为`False`。在这一趟排序过程中，如果发生了数据交换，那么就将`swapped`设置为`True`。当这一趟排序结束，我们通过检查该`swapped`的值就可以知道整个序列是否已经排好序了。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;假设我们有一个序列，它的元素分别为整数9、4、6、15、13。那么图7至图8则展示了经本次优化后的冒泡排序的完整执行过程。注意，虽然第一趟排序后整个序列就排好序了，但在第一趟排序中进行了元素交换（`swapped`被设置为`True`），算法此时并不知道整个序列已经排好了，所以还要进行第二趟排序。在第二趟排序中，不会进行任何元素交换（`swapped`最终为`False`），此时算法才知道整个序列已经是排好序了的。
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/048c96d75a0c4133929757ca1ec39acf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=45%>  <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图7  [9,4,6,15,13] 第1趟排序</div> </center>

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/a46b30dc6bb64340950be256d596dceb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图8  [9,4,6,15,13] 第2趟排序</div> </center>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上，如果一个列表只需要几次遍历就可排好，冒泡排序就占有优势：它可以在发现列表已排好时立刻结束。代码二就是改良版冒泡排序。它通常被称作“短路冒泡排序”。
**代码二：**
```python
def short_bubble_sort(items):
    """第一次优化"""
    items = items[:]  		# 复制原序列
    length = len(items)  	# 序列中元素的数量
    # 外层循环控制第1至第(n-1)趟排序
    for i in range(1, length):
        swapped = False  # 每一趟开始时，将swapped设为False，False表示为交换，True表示交换
        # 内层循环用于第i趟时，对前面n-(i-1)个元素进行比较和交换
        for j in range(length - i):
            # 如果前一个元素大于后一个元素，则交换他们
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True  # 标记发生了元素交换
        # 每一趟结束后，检查是否发生了交换，如果没有发生交换，则提前退出整个算法
        if not swapped:
            break
    return items
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在最好的情况下，第二版冒泡排序只需进行$n-1$次比较和0次元素移动；在最坏的情况下，还是进行$n(n-1)/2$次比较和$3n(n-1)/2$次元素移动。虽然这一版的冒泡排序的时间复杂度依旧是$O(n^2)$，但是和第一版相比肯定性能上更好。

### 2.2 第二次优化
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在我们之前的想法中，当进行第$i$趟排序时，序列中只有最大的$i-1$个元素已经排好序了。因为那时我们认为每一趟仅排好一个元素，即它比较的所有元素中最大的那一个。因此第$i$趟排序的时候，需要对前面$n-(i-1)$个元素进行比较和交换。但其实此时这前$n-(i-1)$个元素中可能最大的那几个元素已经在它们最终的位置上了，这时第$i$趟实际需要比较的元素个数就可以小于$n-(i-1)$。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;比如有一个序列24、30、12、40、50，那么第1趟排序之后的结果为24、12、30、40、50。在原来的想法中，第2趟需要比较前面4个数。但此时前4个数中最大的两个30和40已经在它们最终的位置上了，不需要再对它们进行位置上的调整。因此，第2趟可以只比较前两个数。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;注意这个例子中，虽然在序列的初始状态中40和50就已经在它们最终的位置上了，但第1趟排序还是需要比较全部的5个数。因为此时没有任何信息可以将序列的这种特殊状态告知算法，某一趟是否可以执行比它原本理论上更少的比较次数，需要前一趟排序对序列状态的了解。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在每一趟排序中，我们都用一个变量`last_index`记录下本趟排序最后一次元素交换中前一个元素的下标。在该下标之后没有发生交换，说明该下标之后的所有元素都已经排好序了。那么下一趟排序就只需要对该下标及其之前的元素进行比较而已。这样下一趟排序需要比较的次数可能比原本需要的次数更少，也就在一定程度上提升了算法的效率。
**代码三：**
```python
def short_bubble_sort(items):
    items = items[:]  		# 复制原序列
    length = len(items)  	# 序列中元素的数量
    last_index = length - 1	# 记录每一趟中最后一次交换中前一个元素的下标，他的初值为n-1
    # 外层循环控制第1至第(n-1)趟排序
    for i in range(1, length):
        swapped = False  # 每一趟开始时，将swapped设为False，False表示为交换，True表示交换
        # 内层循环用于第i趟时，对前面last_index+1个元素进行比较和交换
        for j in range(last_index):
            if items[j] > items[j + 1]:
                # 如果前一个元素大于后一个元素，则交换他们
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True  # 标记发生了元素交换
                last_index = j  # 记录本次交换中前一个元素的下标
        # 每一趟结束后，检查是否发生了交换，如果没有发生交换，则提前退出整个算法
        if not swapped:
            break
    return items
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;图9至图11详细展示了经过第二次优化后的冒泡排序对[24, 30, 12, 40, 50]这个序列的执行情况。该例子中另一个值得注意的问题是，虽然在第2趟排序后整个序列就已经排好序了，但是第2趟中进行了一次元素交换而导致`swapped`等于`True`。因此第2趟后并不会立即退出函数，还要进行第3趟排序。在第3趟中内层循环不会执行而立即退出，因为此时`last_index`等于0，`j`（此时也等于0）小于`last_index`的条件不满足。在第3趟最后`swapped`为`False`，此时才退出算法。

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/f54bb078e2e5400aacfcba86316cf221.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图9  [24, 30, 12, 40, 50] 第1趟排序</div> </center>

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/d9c5bb8e9bb34f1abc70d148b4abc321.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图10  [24, 30, 12, 40, 50] 第2趟排序</div> </center>

<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/c079a7a9dc4e45b8ba2a8c01728fa585.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6ZW_6Lev5ryr5ryrMjAyMQ==,size_17,color_FFFFFF,t_70,g_se,x_16#pic_center" width=45%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图11  [24, 30, 12, 40, 50] 第3趟排序</div> </center>

### 2.3 鸡尾酒排序
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[鸡尾酒排序](https://baike.baidu.com/item/%E9%B8%A1%E5%B0%BE%E9%85%92%E6%8E%92%E5%BA%8F/7515196#:~:text=%E9%B8%A1%E5%B0%BE%E9%85%92%20%E6%8E%92%E5%BA%8F%E5%8F%88%E7%A7%B0%E5%8F%8C%E5%90%91%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F%E3%80%81%E9%B8%A1%E5%B0%BE%E9%85%92%E6%90%85%E6%8B%8C%E6%8E%92%E5%BA%8F%E3%80%81%E6%90%85%E6%8B%8C%E6%8E%92%E5%BA%8F%E3%80%81%E6%B6%9F%E6%BC%AA%E6%8E%92%E5%BA%8F%E3%80%81%E6%9D%A5%E5%9B%9E%E6%8E%92%E5%BA%8F%E6%88%96%E5%BF%AB%E4%B9%90%E5%B0%8F%E6%97%B6%E6%8E%92%E5%BA%8F,,%E6%98%AF%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F%E7%9A%84%E4%B8%80%E7%A7%8D%E5%8F%98%E5%BD%A2%E3%80%82%20%E8%AF%A5%E7%AE%97%E6%B3%95%E4%B8%8E%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F%E7%9A%84%E4%B8%8D%E5%90%8C%E5%A4%84%E5%9C%A8%E4%BA%8E%E6%8E%92%E5%BA%8F%E6%97%B6%E6%98%AF%E4%BB%A5%E5%8F%8C%E5%90%91%E5%9C%A8%E5%BA%8F%E5%88%97%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%8E%92%E5%BA%8F%E3%80%82%20%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%95%B0%E5%AD%97%E6%9C%AC%E6%98%AF%E6%97%A0%E8%A7%84%E5%BE%8B%E7%9A%84%E6%8E%92%E6%94%BE%EF%BC%8C%E5%85%88%E6%89%BE%E5%88%B0%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0%E5%AD%97%EF%BC%8C%E6%8A%8A%E4%BB%96%E6%94%BE%E5%88%B0%E7%AC%AC%E4%B8%80%E4%BD%8D%EF%BC%8C%E7%84%B6%E5%90%8E%E6%89%BE%E5%88%B0%E6%9C%80%E5%A4%A7%E7%9A%84%E6%95%B0%E5%AD%97%E6%94%BE%E5%88%B0%E6%9C%80%E5%90%8E%E4%B8%80%E4%BD%8D%E3%80%82)又称双向冒泡排序、鸡尾酒搅拌排序、搅拌排序、涟漪排序、来回排序或快乐小时排序, 是冒泡排序的一种变形。该算法与冒泡排序的不同处在于排序时是以双向在序列中进行排序。因此，根据名字可以看到搅拌排序的原理，每次都是从左往右，交换相邻的元素，从而达到循环一边可以把最大的元素放在右边。而双向冒泡排序，在完成一次从左往右的冒泡排序后，再从右往左进行冒泡，从而把小的元素放在左边。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面这张图可以很好地表达：
<center> <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://img-blog.csdnimg.cn/1be9f6c85b5c4d748d94efe6d015ad2d.gif#pic_center" width=36%> <div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">图12 双向排序动图演示</div> </center>

**代码四：**

```python
def cocktail_sort(items):
    """搅拌排序"""
    items = items[:]  # 复制原序列
    length = len(items)  # 序列中元素的数量
    # 外层循环控制第1至第(n-1)趟排序
    for i in range(1, int(length/2)):
        swapped = False  # 每一趟开始时，将swapped设为False
        # 正向：把当前循环最大的放到最右边
        for j in range(length - i):
            # 如果前一个元素大于后一个元素，则交换他们
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True  # 标记发生了元素交换
        if swapped:
            swapped = False
            # 反向：把当前循环最小的放到最右边
            for k in range(length-i-1, i-1, -1):
                if items[k-1] > items[k]:
                    items[k], items[k-1] = items[k-1], items[k]
                    swapped = True
        # 每一趟结束后，检查是否发生了交换，如果没有发生交换，则提前退出整个算法
        if not swapped:
            break
    return items
```


____

### 3 参考
- 图文详解冒泡排序：[https://baijiahao.baidu.com/s?id=1662238914941980592&wfr=spider&for=pc](https://baijiahao.baidu.com/s?id=1662238914941980592&wfr=spider&for=pc)
- Python 冒泡排序：[https://www.runoob.com/python3/python-bubble-sort.html](https://www.runoob.com/python3/python-bubble-sort.html)
- 冒泡排序算法：[http://c.biancheng.net/view/6506.html](http://c.biancheng.net/view/6506.html)