题目：PAT1015 德才论
## 1 题目描述
**1. 背景**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;宋代史学家司马光在《资治通鉴》中有一段著名的“德才论”：“是故才德全尽谓之圣人，才德兼亡谓之愚人，德胜才谓之君子，才胜德谓之小人。凡取人之术，苟不得圣人，君子而与之，与其得小人，不若得愚人。”

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;现给出一批考生的德才分数，请根据司马光的理论给出录取排名。

**2. 输入格式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输入第一行给出3个正整数，分别为：N（≤），即考生总数；L（≥），为录取最低分数线，即德分和才分均不低于L的考生才有资格被考虑录取；H（<），为优先录取线——德分和才分均不低于此线的被定义为“才德全尽”，此类考生按德才总分从高到低排序；才分不到但德分到线的一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后；德才分均低于 H，但是德分不低于才分的考生属于“才德兼亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；其他达到最低线 L 的考生也按总分排序，但排在第三类考生之后。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;随后N行，每行给出一位考生的信息，包括：准考证号 德分 才分，其中准考证号为8位整数，德才分为区间 [0, 100] 内的整数。数字间以空格分隔。

**3. 输出格式**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;输出第一行首先给出达到最低分数线的考生人数 M，随后 M 行，每行按照输入格式输出一位考生的信息，考生按输入中说明的规则从高到低排序。当某类考生中有多人总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出。

## 2 思路分析

- 德分和才分均不低于线H的被定义为“才德全尽”，此类考生按德才总分从高到低排序；
- 才分不到但德分到线H的一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后； 
- 德才分均低于H，但是德分不低于才分的考生属于“才德兼亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；
- 其他达到最低线L的考生也按总分排序，但排在第三类考生之后。
- 当某类考生中有多人总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出。



## 3 优化改进

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用一般思路，开四个列表分别存储各满足要求的数会发现有3个测试点超时，并且需要编写自定义排序函数。详细代码可以参考代码一。

**1. 更改存储信息**
   
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通常我们的存储方式是[准考证号，德分，才分]，这时候要根据题目要求去自定义排序规则，不过我们只需要改变一下存储的值和顺序，便可以解决这种问题。
   现在我们的存储方式是[德分+才分（总分），德分，准考证号]，这时候虽然我们少存了一种信息（才分），但是我们可以通过总分 - 德分去动态计算出才分。这时候我们就不需要编写自定义函数去更改排序规则了，因为sort函数对于列表中有多个值是从前往后依次比较排序，这种存储方式刚好满足题目要求。不过还有一点小问题就是前面两个值都是从大到小排序，而准考证号所示从小到大排序，不过我们只需要将准考证号变为负数即可解决问题，排序完成后输出时只需要再添负号变为正数。如a = 100001, a = -a, print(-a)

**2. 更改输入输出流**

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于Python中`input()`函数有可交互性（括号内可以输出你想在控制台输出的话），它会去掉末尾的换行等，会导致比`sys`库中的`stdin.readline()`在百万字符串数据量下慢约10倍。

**3. 程序整体优化**

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于全局变量的开销时间是高于局域变量的，故我们将程序整体放入函数中，这样就可以把全局变量转变为局部变量。

**4. 更改存储结构（重点）**

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;经过上面三步优化后，我们发现只有2个测试数据点依旧超时。这时候我们或许可以从时间复杂度去优化，通过观察我们发现程序最花费时间的地方就是排序，时间复杂度为$O(NlogN)$，那么能不能给他进一步优化呢？答案是可以的，通过观察我们发现数值比较小，故可以开辟足够大的空间通过下标来存储信息，这样我们得到的信息默认就是从小到大排好序的。
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如:“3, 9, 1”，那么我们可以f=[0]*10,f[3]=1,f[9]=1,f[1]=1,之后从小到大遍历，如果值为1那么输出，到这我们就完成了$O(N)$时间复杂度级别的排序。同理，对于这道题我们发现德分和才分比较小，可以进行这样的优化避免了对前面两个值的排序，由于准考证号数值过大，存储空间不够，我们只需要对这一维数据进行排序即可，实测是可以过的。

## 4 代码实现
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;常规思路，有两个测试点运行超时，代码如下：
**代码一：**
```python
[n, low, high] = list(map(int, input().split()))
student_list = []
one_list = []
second_list = []
third_list = []
fourth_list = []
for i in range(n):
    items = list(map(int, input().split()))
    if items[1] < low or items[2] < low:
        continue
    elif items[1] >= high and items[2] >= high:
        one_list.append(items)
    elif items[1] >= high and items[2] < high:
        second_list.append(items)
    elif items[1] >= items[2]:
        third_list.append(items)
    else:
        fourth_list.append(items)
key = lambda item: (item[1] + item[2], item[1], -item[0])
one_list.sort(key=key, reverse=True)
second_list.sort(key=key, reverse=True)
third_list.sort(key=key, reverse=True)
fourth_list.sort(key=key, reverse=True)
result_list = one_list + second_list + third_list + fourth_list

print(len(result_list))
for k in range(len(result_list) - 1):
    print('{} {} {}'.format(result_list[k][0], result_list[k][1], result_list[k][2]))
print('{} {} {}'.format(result_list[-1][0], result_list[-1][1], result_list[-1][2]), end='')
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;改进后的代码：
**代码二：**
```python
import sys

def printf(lst):
    # 根据题目要求从大到小输出实际存在的分数
    for i in range(200, 0, -1):
        for j in range(100, 0, -1):
            # 如果当前有值，则通过sorted排序返回一个列表，用for遍历这个排序好的列表依次输出即可
            # 这里存储的是准考证号，要求从小到大
            if lst[i][j]:
                for id in sorted(lst[i][j]):
                    sys.stdout.write('%s %s %s\n' % (id, j, i - j))


def main():
    # 通过列表推导式创建三维列表，为info[][][], 从前往后分别表示总分，德分，准考证号
    first_list = [[[] for j in range(101)] for i in range(201)]
    second_list = [[[] for j in range(101)] for i in range(201)]
    third_list = [[[] for j in range(101)] for i in range(201)]
    fourth_list = [[[] for j in range(101)] for i in range(201)]
    [n, low, high] = list(map(int, input().split()))
    student_list = [list(map(int, sys.stdin.readline().split())) for k in range(n)]
    count = n
    for item in student_list:
        # 不满足题目要求的学生不予存入
        if item[1] < low or item[2] < low:
            count -= 1
            continue
        # 由于准考证号值过大，无法通过索引形式，只能append添加至末尾
        elif item[1] >= high and item[2] >= high:
            first_list[item[1] + item[2]][item[1]].append(item[0])
        elif item[1] >= high and item[2] < high:
            second_list[item[1] + item[2]][item[1]].append(item[0])
        elif item[1] >= item[2]:
            third_list[item[1] + item[2]][item[1]].append(item[0])
        else:
            fourth_list[item[1] + item[2]][item[1]].append(item[0])
    print(count)
    printf(first_list)
    printf(second_list)
    printf(third_list)
    printf(fourth_list)

if __name__ == '__main__':
    main()
```

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;留个小疑问，不知道为啥测试的时候，会报错多一个空行，提交后却没有这种问题，麻烦知道的小伙伴们评论一下哦！


## 参考
- 1015 德才论 (Python 无超时 详解）：[https://blog.csdn.net/qq_55322766/article/details/122195466](https://blog.csdn.net/qq_55322766/article/details/122195466)
- 1015 德才论 (25 分)(问题分析、及易错点归纳)：[https://www.bilibili.com/read/cv11440616](https://www.bilibili.com/read/cv11440616)