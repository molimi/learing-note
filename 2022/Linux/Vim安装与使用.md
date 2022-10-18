&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Linux操作系统安装完成之后，我们在写代码时经常会面对尴尬的现象，使用vi非常的不方便，下面我们就来安装比较人性化的vim。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;直接使用vi，可以发现不能很自由的使用backspace，向上的那个键，光标的移动极其不自由，关键字也没有明确标识。

## 1 安装

1. 打开一个终端，在终端输入如下命令，然后有让输入y或者n的时候输入y。
```bash
pat@dell-Precision-7820-Tower:~$ sudo apt-get install vim
```
2. 安装完成以上操作之后，在控制台输入vi 按tab键，看看有没有vim，如果出现如下界面，即安装成功
![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011161435307-1240080549.png)

3. 修改 vim的配置文件，在终端输入如下命令：
```bash
root@dell-Precision-7820-Tower:~$ sudo vim /etc/vim/vimrc
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在这个文件中，会有这么一句：syntax on    意思是语法高亮，如果您的被注释掉了，请“让它出来”。如下图所示即可：
![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011161536876-2036035889.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;然后在最后一行添加以下6行命令：
```bash
set nu                         
set tabstop            
set nobackup           
set cursorline          
set ruler          
set autoindent
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分别是如下意思：
> set nu             // 设置左侧行号
> set tabstop        //tab 长度设置为 4
> set nobackup       //覆盖文件时不备份
> set cursorline     //突出显示当前行
> set ruler          //在右下角显示光标位置的状态行
> set autoindent     //自动缩进

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;操作界面如下所示，在输入6行之后，输入“：wq”存盘退出即可：
![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011161605332-265594375.png)

4. 测试是否会高亮显示 
```bash
pat@dell-Precision-7820-Tower:~$ vim helloworld.py
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;回车后出现如下界面即安装成功，里边出现了相应的配置结果，使用起来更加方便

![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011162049171-1280421003.png)

5. 问题分析：
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;安装vim可能出现以下报错，如下图所示：
![img](https://img2022.cnblogs.com/blog/2692004/202210/2692004-20221011113516210-1798971402.png)
解决方式：
```bash
root@dell-Precision-7820-Tower:~$ apt-get purge vim-common
root@dell-Precision-7820-Tower:~$ apt install vim
```


## 2 快速入门

这里只介绍Vim的6种基本模式：
- 普通模式(Normal mode)
在普通模式中，用的编辑器命令，比如移动光标，删除文本等等。这也是 Vim 启动后的默认模式。这正好和许多新用户期待的操作方式相反（大多数编辑器默认模式为插入模式）。

Vim 强大的编辑功能来自于其普通模式命令。普通模式命令往往需要一个操作符结尾。例如普通模式命令`dd`删除当前行，但是第一个"d"的后面可以跟另外的移动命令来代替第二个`d`，比如用移动到下一行的"j"键就可以删除当前行和下一行。另外还可以指定命令重复次数，`2dd`（重复`dd`两次），和`dj`的效果是一样的。用户学习了各种各样的文本间移动／跳转的命令和其他的普通模式的编辑命令，并且能够灵活组合使用的话，能够比那些没有模式的编辑器更加高效地进行文本编辑。

在普通模式中，有很多方法可以进入插入模式。比较普通的方式是按 `a`（append／追加）键或者 `i`（insert／插入）键。

- 插入模式(Insert mode)


在这个模式中，大多数按键都会向文本缓冲中插入文本。大多数新用户希望文本编辑器编辑过程中一直保持这个模式。

在插入模式中，可以按`ESC`键回到普通模式。

- 可视模式(Visual mode)



- 选择模式(Select mode)


- 命令行模式(Command line mode)


- Ex 模式(Ex mode)