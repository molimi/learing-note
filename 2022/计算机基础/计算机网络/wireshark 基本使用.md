要深入理解网络协议，需要仔细观察协议实体之间交换的报文序列。为探究协议操作细节，可使协议实体执行某些动作，观察这些动作及其影响。这些任务可以在仿真环境下或在如因特网这样的真实网络环境中完成。观察在正在运行协议实体间交换报文的基本工具被称为分组嗅探器(`packet sniffer`)。顾名思义，一个分组嗅探器捕获（嗅探）计算机发送和接收的报文。一般情况下，分组嗅探器将存储和显示出被捕获报文的各协议头部字段内容。

<img src ="https://img-blog.csdnimg.cn/b0f29d3943f24016b9840dc185696a73.png#pic_center" width = 48%>

上图右边是计算机上正常运行的协议（在这里是因特网协议）和应用程序（如：`Web` 浏览器和 `ftp` 客户端）。分组嗅探器（虚线框中的部分）是附加在计算机普通软件上的，主要由两部分组成。分组捕获库接收计算机发送和接收的每一个链路层帧的拷贝。高层协议（如：`HTTP`、 `FTP`、 `TCP`、 `UDP`、 `DNS`、 `IP` 等）交换的报文都被封装在链路层帧(Frame)中，并沿着物理介质（如以太网的电缆）传输。上图假设所使用的物理媒体是以太网，上层协议的报文最终封装在以太网帧中。

分组嗅探器的第二个组成部分是分析器。分析器用来显示协议报文所有字段的内容。为此，分析器必须能够理解协议所交换的所有报文的结构。例如：我们要显示上图中 HTTP 协议所交换的报文的各个字段。分组分析器理解以太网帧格式，能够识别包含在帧中的 IP 数据报。分组分析器也要理解 IP 数据报的格式，并能从 IP 数据报中提取出 TCP 报文段。然后，它需要理解 TCP 报文段，并能够从中提取出 HTTP 消息。最后，它需要理解 HTTP 消息。

Wireshark是一种免费的网络协议分析器，可在Windows，Mac和Linux/Unix计算机上运行，是进行网络实验的理想分组分析器。该软件具有庞大的用户基础，文档支持包括用户指南、手册和常见问题(详见[http://www.wireshark.org/docs](http://www.wireshark.org/docs))，丰富的功能包括分析数百种协议，以及精心设计的用户界面。可以运行在使用以太网、串行(PPP和SLIP)、802.11无线局域网和许多其他链路层技术的计算机上。

<img src ="https://img-blog.csdnimg.cn/a4c4e36f841b48d5bf9f465dcee0b384.png#pic_center" width = 48%>


wireshark是非常流行的网络封包分析软件，功能十分强大。可以截取各种网络封包，显示网络封包的详细信息。使用wireshark的人必须了解网络协议，否则就看不懂wireshark了。
为了安全考虑，wireshark只能查看封包，而不能修改封包的内容，或者发送封包。

wireshark能获取HTTP，也能获取HTTPS，但是不能解密HTTPS，所以wireshark看不懂HTTPS中的内容，总结，如果是处理HTTP,HTTPS 还是用Fiddler, 其他协议比如TCP,UDP 就用wireshark。

## 1 下载并安装Wireshark软件

WireShark 是一种可以运行在 Windows，UNIX，Linux 等操作系统上的分组分析器。运行Wireshark，需要有一台支持Wireshark和libpcap或WinPCap分组捕获库的计算机。安装Wireshark时，如果操作系统中未安装libpcap软件，它将会自动安装。支持的操作系统和下载站点的列表，请访问[http://www.wireshark.org/download.html](http://www.wireshark.org/download.html。按照系统版本选择下载，下载完成后，按照软件提示一路Next安装。

**温馨提示：** 当您在安装或运行Wireshark时遇到问题时，可以查看Wireshark FAQ，它包含一些有用的提示和信息。如果你是Win10系统，安装完成后，选择抓包但是不显示网卡，下载win10pcap兼容性安装包。下载路径：[下载路径：win10pcap兼容性安装包](http://www.win10pcap.org/download/)


## 2 Wireshark 开始抓包示例

1、双击桌面上的图标，可启动Wireshark。启动后的用户界面如下图所示，中间列表部分列出了所有网络接口。

<img src ="https://img-blog.csdnimg.cn/e79b2d981cc94fd5b52002bc30935bc1.png#pic_center" width = 48%>

2、选择菜单栏上捕获 -> 选项，勾选WLAN网卡（这里需要根据各自电脑网卡使用情况选择，简单的办法可以看使用的IP对应的网卡）。点击Start。启动抓包。

<img src ="https://img-blog.csdnimg.cn/cc57c547d9c24ba2b9e88544ed79f192.png#pic_center" width = 48%>

3、wireshark启动后，wireshark处于抓包状态中。

<img src ="https://img-blog.csdnimg.cn/d331cdba36ed4d61a302b1284d91ac57.png#pic_center" width = 48%>


4、执行需要抓包的操作，如在cmd窗口下执行`ping www.baidu.com`。


5、抓取分组操作

<p>A.单击中间网络接口列表中，某一网络接口如<code>eth0</code>，选中网络接口，通过菜单“捕获”-“开始”或工具栏中的<img src="https://data.educoder.net/api/attachments/448948" width=4% alt=""> 按钮，开始捕获选定接口中的网络分组；
B．也可以双击中间网络接口列表中，某一网络接口如<code>eth0</code>，可以开始抓取分组；
C．通过菜单“捕获”-“停止”或工具栏中的按钮<img src="https://data.educoder.net/api/attachments/448957" width=4% alt=""> 停止抓取分组。
D．通过菜单“捕获”-“重新开始”或工具栏中的按钮<img src="https://data.educoder.net/api/attachments/448959" width=4% alt=""> 重新开始抓取。</p>


6、Wireshark窗口功能

**A．命令菜单和工具栏**

命令菜单位于窗口的最顶部，是标准的下拉式菜单。最常用菜单命令有两个： 文件、 捕获。 文件 菜单允许你保存捕获的分组数据，或打开一个已被保存的捕获分组数据文件，或退出 WireShark 程序。 捕获 菜单允许你开始捕获分组。
工具栏位于命令菜单的下方，提供常用功能的快捷方式。如<img src="https://data.educoder.net/api/attachments/448948" width=4% alt="">：开始捕获、<img src="https://data.educoder.net/api/attachments/448957" width=4% alt="">：停止捕获、<img src="https://data.educoder.net/api/attachments/448959" width=4% alt="">：重新抓取分组。

**B．显示过滤规则**

在该字段中，可以填写协议的名称或其他信息，根据此内容可以对分组列表窗口中的分组进行过滤。

**C．捕获分组列表**

按行显示已被捕获的分组内容，其中包括： WireShark 赋予的分组序号、捕获时间、分组的源地址和目的地址、协议类型、分组中所包含的协议说明信息。单击某一列的列名，可以使分组按指定列进行排序。 在该列表中，所显示的协议类型是发送或接收分组的最高层协议的类型。

**D．分组头部明细**

显示捕获分组列表窗口中被选中分组的头部详细信息。包括：与以太网帧有关的信息，与包含在该分组中的 IP 数据报有关的信息。
单击以太网帧或 IP 数据报所在行左边的向右或向下的箭头可以展开或最小化相关信息。如果利用 TCP 或 UDP 承载分组， WireShark 也会显示 TCP 或 UDP 协议头部信息。分组最高层协议的头部字段也会显示在此窗口中。

**E．分组内容窗口**

以 ASCII 码和十六进制两种格式显示被捕获帧的完整内容。



7、通常，分组列表窗口中会显示许多类型的分组。即使仅仅是下载了一个网页，但是还有许多其他协议在您的计算机上运行，只是用户所看不见。可以在中间过滤窗口中输入过滤的分组协议如http， 选择应用按钮，就可以只让HTTP分组消息显示在分组列表窗口。

<img src ="https://img-blog.csdnimg.cn/7674ad7b8e37462e8eea4f067dbcc967.png#pic_center" width = 36%>

8、操作完成后相关数据包就抓取到了。为避免其他无用的数据包影响分析，可以通过在过滤栏设置过滤条件进行数据包列表过滤，获取结果如下。说明：`ip.addr == 119.75.217.26 and icmp` 表示只显示ICPM协议且源主机IP或者目的主机IP为`119.75.217.26`的数据包。说明：协议名称icmp要小写。

<img src ="https://img-blog.csdnimg.cn/58094292b1334792882516ef75701ef0.png#pic_center" width = 36%>


## 3 Wireshakr抓包界面介绍

<img src ="https://img-blog.csdnimg.cn/9cc295b4770346238e6cefa899e930e9.png#pic_center" width = 36%>

说明：数据包列表区中不同的协议使用了不同的颜色区分。协议颜色标识定位在菜单栏 视图(View) --> 着色规则(Coloring Rules)。如下所示

<img src ="https://img-blog.csdnimg.cn/db580cb181a048088b067119bc061c6a.png#pic_center" width = 36%>

1. 显示过滤器(Display Filter)，用于设置过滤条件进行数据包列表过滤。菜单路径：分析(Analyze) --> 显示过滤器(Display Filters)。

<img src ="https://img-blog.csdnimg.cn/428c5a6e8a0945308232ca5773128910.png#pic_center" width = 36%>

2. 数据包列表(Packet List Pane)， 显示捕获到的数据包，每个数据包包含编号，时间戳，源地址，目标地址，协议，长度，以及数据包信息。 不同协议的数据包使用了不同的颜色区分显示。

Time:时间；Source:发送主机IP地址；Destination: 接收主机IP地址；Protocol：分组协议；Length：分组长度；Info：分组内容

<img src ="https://img-blog.csdnimg.cn/7241b8ab380e44678c48363ee49e3227.png#pic_center" width = 36%>

3. 数据包详细信息(Packet Details Pane), 在数据包列表中选择指定数据包，在数据包详细信息中会显示数据包的所有详细信息内容。数据包详细信息面板是最重要的，用来查看协议中的每一个字段。各行信息分别为
（1）Frame:   物理层的数据帧概况
（2）Ethernet II: 数据链路层以太网帧头部信息
（3）Internet Protocol Version 4: 互联网层IP包头部信息
（4）Transmission Control Protocol:  传输层T的数据段头部信息，此处是TCP
（5）Hypertext Transfer Protocol:  应用层的信息，此处是HTTP协议

<img src ="https://img-blog.csdnimg.cn/04b7ed919b0f43a58f392c12990834d6.png#pic_center" width = 36%>

TCP包的具体内容

从下图可以看到wireshark捕获到的TCP包中的每个字段。

<img src ="https://img-blog.csdnimg.cn/a0ded99728a44306b9aa0bb130d20612.png#pic_center" width = 36%>

4. 数据包字节区(Dissector Pane)。

在分组内容窗口中，可以显示出该分组内容的16进制和ASCII两种格式的内容。鼠标指向内容窗口，可以将分组中某一字段的内容突出显示。在分组头部信息窗口中，展开选择某一头部信息时，分组内容中相应内容同步突出显示。


## 4 Wireshark过滤器设置

初学者使用wireshark时，将会得到大量的冗余数据包列表，以至于很难找到自己需要抓取的数据包部分。wireshark工具中自带了两种类型的过滤器，学会使用这两种过滤器会帮助我们在大量的数据中迅速找到我们需要的信息。

1) 抓包过滤器

捕获过滤器的菜单栏路径为Capture --> Capture Filters。用于在抓取数据包前设置。

<img src ="https://img-blog.csdnimg.cn/16d179cc091c47dc828038d7565c30b3.png#pic_center" width = 36%>

如何使用？可以在抓取数据包前设置如下。

<img src ="https://img-blog.csdnimg.cn/a07fe953c0794667b68b66a408e6bc49.png#pic_center" width = 36%>s

`ip host 60.207.246.216 and icmp` 表示只捕获主机IP为60.207.246.216的ICMP数据包。获取结果如下：

<img src ="https://img-blog.csdnimg.cn/56188bf328b34333815cac05276c7db6.png#pic_center" width = 36%>


（2）显示过滤器

显示过滤器是用于在抓取数据包后设置过滤条件进行过滤数据包。通常是在抓取数据包时设置条件相对宽泛或者没有设置导致抓取的数据包内容较多时使用显示过滤器设置条件过滤以方便分析。同样上述场景，在捕获时未设置抓包过滤规则直接通过网卡进行抓取所有数据包，如下

<img src ="https://img-blog.csdnimg.cn/b5d1753518914accba158fcb35153815.png#pic_center" width = 36%>


执行 `ping www.baidu.com` 获取的数据包列表如下

<img src ="https://img-blog.csdnimg.cn/4e9a75303cb04c49a93a6a7d4af99b39.png#pic_center" width = 36%>

观察上述获取的数据包列表，含有大量的无效数据。这时可以通过设置显示器过滤条件进行提取分析信息。`ip.addr == 14.119.104.254 and icmp`。并进行过滤。

<img src ="https://img-blog.csdnimg.cn/f2ac8c31558642dbb5b45ea019b42b67.png#pic_center" width = 36%>


上述介绍了抓包过滤器和显示过滤器的基本使用方法。在组网不复杂或者流量不大情况下，使用显示器过滤器进行抓包后处理就可以满足我们使用。下面介绍一下两者间的语法以及它们的区别。

wireshark过滤器表达式的规则

1、抓包过滤器语法和实例

抓包过滤器类型Type（host、net、port）、方向Dir（src、dst）、协议Proto（ether、ip、tcp、udp、http、icmp、ftp等）、逻辑运算符（&& 与、|| 或、！非）

(1) 协议过滤

比较简单，直接在抓包过滤框中直接输入协议名即可。

- tcp，只显示TCP协议的数据包列表
- http，只查看HTTP协议的数据包列表
- icmp，只显示ICMP协议的数据包列表

(2) IP过滤
- host 192.168.1.104
- src host 192.168.1.104
- dst host 192.168.1.104

(3) 端口过滤

- port 80
- src port 80
- dst port 80

(4) 逻辑运算符 && 与、|| 或、！非
`src host 192.168.1.104 && dst port 80` 抓取主机地址为192.168.1.80、目的端口为80的数据包
`host 192.168.1.104 || host 192.168.1.102` 抓取主机为192.168.1.104或者192.168.1.102的数据包
`!broadcast` 不抓取广播数据包

2、显示过滤器语法和实例
(1) 比较操作符
比较操作符有== 等于、！= 不等于、> 大于、< 小于、>= 大于等于、<=小于等于。

(2) 协议过滤

比较简单，直接在Filter框中直接输入协议名即可。注意：协议名称需要输入小写。
- tcp，只显示TCP协议的数据包列表
- http，只查看HTTP协议的数据包列表
- icmp，只显示ICMP协议的数据包列表

<img src ="https://img-blog.csdnimg.cn/ef029d3774e54520923c09d4ae072ef0.png#pic_center" width = 36%>

(3) ip过滤
- `ip.src ==192.168.1.104`，显示源地址为192.168.1.104的数据包列表
- `ip.dst==192.168.1.104`，显示目标地址为192.168.1.104的数据包列表
- `ip.addr == 192.168.1.104`，显示源IP地址或目标IP地址为192.168.1.104的数据包列表

<img src ="https://img-blog.csdnimg.cn/a85ae0d21a934de09dfbe73bed6d8f4f.png#pic_center" width = 36%>

(4) 端口过滤
- tcp.port ==80,  显示源主机或者目的主机端口为80的数据包列表。
- tcp.srcport == 80,  只显示TCP协议的源主机端口为80的数据包列表。
- tcp.dstport == 80，只显示TCP协议的目的主机端口为80的数据包列表。

<img src ="https://img-blog.csdnimg.cn/5c162e438b5b49549d0b84244bdbb5b3.png#pic_center" width = 36%>

(5) Http模式过滤

`http.request.method=="GET"`, 只显示HTTP GET方法的。

(6) 逻辑运算符为 and/or/not

过滤多个条件组合时，使用and/or。比如获取IP地址为192.168.1.104的ICMP数据包表达式为 `ip.addr == 14.119.104.254 and icmp`

<img src ="https://img-blog.csdnimg.cn/00ebb1437048498ea6595cc73f352417.png#pic_center" width = 36%>

(7) 按照数据包内容过滤。假设我要以IMCP层中的内容进行过滤，可以单击选中界面中的码流，在下方进行选中数据。如下

<img src ="https://img-blog.csdnimg.cn/522cfc5d168f41afb2397e5fd43d78aa.png#pic_center" width = 36%>

右键单击选中后出现如下界面

<img src ="https://img-blog.csdnimg.cn/b0577ad336514a968c603cdb2d72084c.png#pic_center" width = 36%>


选中Select后在过滤器中显示如下，后面条件表达式就需要自己填写。如下我想过滤出data数据包中包含"abcd"内容的数据流。包含的关键词是contains 后面跟上内容。

<img src ="https://img-blog.csdnimg.cn/04fc32bbc68f462489a8ada178cfae40.png#pic_center" width = 36%>


调整数据包列表中时间戳显示格式。调整方法为View -->Time Display Format --> Date and Time of Day。调整后格式如下：

<img src ="https://img-blog.csdnimg.cn/a6d8368445cd4cc0a3a97d15b98979b3.png#pic_center" width = 36%>


____

## 参考
- wireshark 基本使用：[https://www.educoder.net/shixuns/5kuyi2hn/challenges](https://www.educoder.net/shixuns/5kuyi2hn/challenges)
- wireshark抓包新手使用教程：[https://www.cnblogs.com/linyfeng/p/9496126.html](https://www.cnblogs.com/linyfeng/p/9496126.html)
- 《计算机网络－自顶向下方法》笔记：[https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)