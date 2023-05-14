IP 协议（Internet Protocol），又译为网际协议或互联网协议，是用在 TCP/IP 协议簇中的网络层协议。主要功能是无连接数据报传送、数据报路由选择和差错控制。IP 协议是 TCP/IP 协议族的核心协议，其主要包含两个方面：

1. IP 头部信息。IP 头部信息出现在每个 IP 数据报中，用于指定 IP 通信的源端 IP 地址、目的端 IP 地址，指导 IP 分片和重组，以及指定部分通信行为； IP 协议分为 IPv4 版本和 IPv6 版本。

2. IP数据报的路由和转发。IP数据报的路由和转发发生在除目标机器之外的所有主机和路由器上。它们决定数据报是否应该转发以及如何转发；


IP 的主要目的是通过一个互联的网络传输数据报，涉及两个最基本的功能：
- 寻址( Addressing )：IP 协议根据数据报首部中包括的目的地址将数据报传送到目的节点，这就要涉及传送路径的选择，即路由功能。IP 协议使用 IP 地址来实现路由；
- 分片( Fragmentation )：IP 协议还提供对数据大小的分片和重组，以适应不同网络对数据包大小的限制。如果网络只能传送小数据包，IP 协议将对数据报进行分段并重新组成小块再进行传送。


要注意的是：IP 协议提供尽最大努力投递( Best-effort Delivery )的传输服务，是不可靠无连接的数据报服务。源主机只是简单地将 IP 数据报发送出去，数据报传输路由可以完全不同，数据报抵达的先后顺序也不确定。不可靠性则是指数据报在传输过程中可能会出现丢失、重复、延迟时间大或者次序混乱等现象，但 IP 协议并不进行检查，不回送确认，也没有流量控制和差错控制功能。如果数据报在传输中发生某种错误，如某个路由器暂时用完了缓冲区，IP 有一个简单的错误处理算法：丢弃该数据报，然后发送 ICMP 消息报给信源端。因此，要实现数据报的可靠传输，就必须依靠高层的协议或应用程序，如传输层的 TCP 协议。


## 1 IP协议分析
### 1.1 IP数据包

IP 协议提供的数据传送服务是不可靠和无连接的，具体表现如下：
- 不可靠（unreliable）：IP 协议不能保证数据报能成功地到达目的地，它仅提供传输服务。当发生某种错误时，IP 协议会丢弃该数据报。传输的可靠性全由上层协议来提供。
- 无连接（connectionless）：IP 协议对每个数据报的处理是相互独立的。这也说明，IP 数据报可以不按发送顺序接收。如果发送方向接收方发送了两个连续的数据报（先是 A，然后是 B），每个数据报可以选择不同的路线，因此 B 可能在 A 到达之前先到达。



**IPV4数据包**

网际协议第 4 版（Internet Protocol version 4，IPv4）是 TCP/IP 协议使用的数据报传输机制。数据报是一个可变长分组，由两部分组成：头部和数据。头部长度可由 20~60 个字节组成，该部分包含有与路由选择和传输有关的重要信息。头部各字段意义按顺序如下：

<img src ="https://img-blog.csdnimg.cn/49bda0b166474a098cf179b92fc06bca.png#pic_center" width = 48%>

(1) 版本（ 4 位）：该字段定义 IP 协议版本，负责向处理机所运行的 IP 软件指明此 IP 数据报是哪个版本，所有字段都要按照此版本的协议来解释。如果计算机使用其他版本，则丢弃数据报；
(2) 头部长度（ 4 位）：该字段定义数据报协议头长度，表示协议头部具有 32 位字长的数量。协议头最小值为 5 ，最大值为 15；
(3) 服务（ 8 位）：该字段定义上层协议对处理当前数据报所期望的服务质量，并对数据报按照重要性级别进行分配。前 3 位成为优先位，后面 4 位成为服务类型，最后 1 位没有定义。这些 8 位字段用于分配优先级、延迟、吞吐量以及可靠性；
(4) 总长度（ 16 位）：该字段定义整个 IP 数据报的字节长度，包括协议头部和数据。其最大值为 65535 字节。以太网协议对能够封装在一个帧中的数据有最小值和最大值的限制（ 46~1500 个字节）；
(5) 标识（ 16 位）：该字段包含一个整数，用于识别当前数据报。当数据报分段时，标识字段的值被复制到所有的分段之中。该字段由发送端分配，帮助接收端集中数据报分段；
(6) 标记（ 3 位）：该字段由 3 位字段构成，其中最低位（ MF ）控制分段，存在下一个分段置为 1 ，否则置 0 代表该分段是最后一个分段。中间位（ DF ）指出数据报是否可进行分段，如果为 1 则机器不能将该数据报进行分段。第三位即最高位保留不使用，值为 0；
(7) 分段偏移（ 13 位）：该字段指出分段数据在源数据报中的相对位置，支持目标 IP 适当重建源数据；
(8) 生存时间（ 8 位）：该字段是一种计数器，在丢弃数据报的每个点值依次减 1 直至减少为 0 。这样确保数据报拥有有限的环路过程（即 TTL ），限制了数据报的寿命；
(9) 协议（ 8 位）：该字段指出在 IP 处理过程完成之后，有哪种上层协议接收导入数据报。这个字段的值对接收方的网络层了解数据属于哪个协议很有帮助；

常见的协议值有：
<table>
<thead>
<tr>
<th>协议字段值</th>
<th>协议名</th>
<th>缩写</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>互联网消息控制协议</td>
<td>ICMP</td>
</tr>
<tr>
<td>2</td>
<td>互联网组管理协议</td>
<td>IGMP</td>
</tr>
<tr>
<td>6</td>
<td>传输控制协议</td>
<td>TCP</td>
</tr>
<tr>
<td>17</td>
<td>用户数据报协议</td>
<td>UDP</td>
</tr>
<tr>
<td>41</td>
<td>IPv6 封装</td>
<td>ENCAP</td>
</tr>
<tr>
<td>89</td>
<td>开放式最短路径优先</td>
<td>OSPF</td>
</tr>
<tr>
<td>132</td>
<td>流控制传输协议</td>
<td>SCTP</td>
</tr>
</tbody>
</table>

(10) 头部校验和（ 16 位）：该字段帮助确保 IP 协议头的完整性。由于某些协议头字段的改变，这就需要对每个点重新计算和检验。计算过程是先将校验和字段置为 0 ，然后将整个头部每 16 位划分为一部分，将个部分相加，再将计算结果取反码，插入到校验和字段中；校验和的运算方式是采用反码算术运算求和，和的反码作为该字段的值，可以参考下面的例子：

<img src ="https://img-blog.csdnimg.cn/ce4e8ba8095b4572818f9c89dd7bb3e0.png#pic_center" width = 48%>

(11) 源地址（ 32 位）：源主机 IP 地址，该字段在 IPv4 数据报从源主机到目的主机传输期间必须保持不变；
(12) 目的地址（ 32 位）：目标主机 IP 地址，该字段在 IPv4 数据报从源主机到目的主机传输期间同样必须保持不变。


**IPv6数据包**

在 2011 年 2 月，IANA 向一个区域注册机构分配完了未分配的 IPv4 地址的最后剩余地址池。这些注册机构可用的 IPv4 地址一旦用完，IPv4 地址就会耗尽，因此IPv6 技术就被开始进行研发部署。(原计划让 ST-2 作为 IPv5，但是 ST-2 后来就被舍弃了。)下面就让我们看看 IPv6 数据报有什么内容：

<img src ="https://img-blog.csdnimg.cn/e83f97ba2651448d97827835972c0910.png#pic_center" width = 48%>


对于IPv6的详细介绍，请阅读：[网络层——IPv6概述](https://www.cnblogs.com/linfangnan/p/13026397.html)

### 1.2 数据包分片

对于链路层协议，不同的链路层协议能承载的网络层分组长度并不同，一个链路层协议能承载的最大数据量称之为最大传输单元 (MTU)。若传输时经过很多路由器，而之间的每条链路的 MTU 不同怎么办？解决方法就是将 IP 数据报中的数据分片为多个 IP 数据报，然后用单独的链路层帧封装数据报并发送。大 IP 数据分组向较小 MTU 链路转发时，在允许的情况下可以进行分片。
分片时每个分片的标识复制原 IP 分组标识，通常除了最后一个分组，其他分片均分为 MTU 允许的最大分片。一个最大分片可封装的数据，应该为 8 的倍数。既然有分片，那就需要重组为完整的数据报，IP 分片的重组工作由目的端系统负责。

<img src ="https://img-blog.csdnimg.cn/726847cff3774282a9556ac6c2ed8185.png#pic_center" width = 48%>

**相关字段**
**标识符(Identification)**
占 16 位，这个字段主要被用来唯一地标识一个报文的所有分片，因为分片不一定按序到达，所以在重组时需要知道分片所属的报文。

**标志符(Flags)**
占 3 位，这个字段有 DF 和 MF 2 个标志。DF 标志为 1 时禁止分片，为 0 时允许分片。MF 标志为 1 时表示当前分片并非最后一片，为 0 时表示当前分片为最后一片。

**分片偏移(Fragment Offset)**
占 13 位，该字段指明了每个分片相对于原始报文开头的偏移量，以 8 字节作单位。

**分片实例**
现有一个数据报的总长度为 3820 字节，链路的 MTU 为 1400。由于首部占有 20 字节，因此该数据报将被分为 3 个数据报片，其数据部分的长度分别为 1400、1400 和 1000 字节。值的一提的是，分片后的每一个小数据报也需要 20 字节的首部。

<img src ="https://img-blog.csdnimg.cn/9df068d47a8b4967ab12ac5be28097e8.png#pic_center" width = 48%>

对于这 3 个数据报，它们的各个参数为：

<table>
<thead>
<tr>
<th>数据报</th>
<th>总长度</th>
<th>标识</th>
<th>MF</th>
<th>DF</th>
<th>片位移</th>
</tr>
</thead>
<tbody>
<tr>
<td>数据报</td>
<td>3820</td>
<td>相同</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>数据分片 1</td>
<td>1420</td>
<td>相同</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>数据分片 2</td>
<td>1420</td>
<td>相同</td>
<td>1</td>
<td>0</td>
<td>175</td>
</tr>
<tr>
<td>数据分片 3</td>
<td>1020</td>
<td>相同</td>
<td>0</td>
<td>0</td>
<td>350</td>
</tr>
</tbody>
</table>


### 1.3 IPv4 编址
**1. IP 地址的表示**

主机与物理链路、路由器与其任意一条链路之间的边界，都被称之为接口。由于每个主机和路由器都可以发送和接受 IP 数据报，因此所有接口都得拥有自己的 IP 地址。问题是如果 IP 地址乱分配，会使得转发表变得异常复杂，应该怎么样为接口分配 IP 地址？


IP 地址由 2 个字段组成，分别是网络前缀和主机号。网络前缀用于指明主机或路由器所连接到的网络，网络前缀在互联网中必须是唯一的。主机号用于标志主机或路由器，主机号在其所在的网络中是唯一的。就像电话号码划分区号一样，只有通过网络号和主机号的标识，路由器才能知道如何转发，而一个 IP 地址在互联网中是唯一的。




**2. CIDR 策略**
现在在全球因特网中，地址分配策略采用的是无类别域间路由选择 (CIDR)策略。CIDR 消除了传统 A、B、C 类地址和子网划分的概念，将子网寻址的概念一般化了。网络前缀可以是任意长度，融合子网地址和子网掩码可以更为方便地进行子网划分。当子网寻址时，32 bit 的 IP 地址的形式是 a.b.c.d/x，其中 x 指示了地址第一部分的比特数，构成了网络前缀。
CIDR 策略使得路由器转发分组时，可以往网络前缀相同的 IP 地址的区域发送，也就是缩小了发送链路的选择范围。因此采用 CIDR 策略提高了 IPv4 地址空间的分配效率，同时也提高了路有效率。

**3. 特殊的 IP 地址**

<table>
<thead>
<tr>
<th>网络号</th>
<th>主机号</th>
<th>作为 IP 分组源地址</th>
<th>作为 IP 分组目的地址</th>
<th>用途</th>
</tr>
</thead>
<tbody>
<tr>
<td>全 0</td>
<td>全 0</td>
<td>√</td>
<td>×</td>
<td>本网络内表示本主机，路由表内表示默认路由</td>
</tr>
<tr>
<td>全 0</td>
<td>host-id</td>
<td>×</td>
<td>√</td>
<td>本网络范围内表示某个特定主机</td>
</tr>
<tr>
<td>全 1</td>
<td>全 1</td>
<td>×</td>
<td>√</td>
<td>本网络范围内表示广播地址</td>
</tr>
<tr>
<td>net-id</td>
<td>全 0</td>
<td>×</td>
<td>×</td>
<td>网络地址，表示一个网络</td>
</tr>
<tr>
<td>net-id</td>
<td>全 1</td>
<td>×</td>
<td>√</td>
<td>直接广播地址，对特定网络的主机进行广播</td>
</tr>
<tr>
<td>127</td>
<td>非全 0/1</td>
<td>√</td>
<td>√</td>
<td>用于本地软件的环回测试</td>
</tr>
</tbody>
</table>

**4. 私有地址**

私有 IP 地址是一段保留的 IP 地址，只使用在局域网中，无法在 Internet 上使用。一共需要记住 3 组：

<table>
<thead>
<tr>
<th>地址类型</th>
<th>保留的地址空间</th>
</tr>
</thead>
<tbody>
<tr>
<td>A 类</td>
<td>10.0.0.0 ~ 10.255.255.255</td>
</tr>
<tr>
<td>B 类</td>
<td>172.16.0.0 ~ 172.31.255.255</td>
</tr>
<tr>
<td>C 类</td>
<td>192.168.0.0 ~ 192.168.255.255</td>
</tr>
</tbody>
</table>



#### 1.4 划分子网

**1. 子网**
IP 地址如果只使用 ABCDE 类来划分，会造成大量的浪费：一个有 500 台主机的网络，无法使用 C 类地址。但如果使用一个 B 类地址，6 万多个主机地址只有 500 个被使用，造成 IP 地址的大量浪费。

因此，可以在 ABC 类网络的基础上，进一步划分子网：占用主机号的前几个位，用于表示子网号。

这样 IP 地址就可看作 IP = 网络号 + 子网号 + 主机号。

所谓子网就是不跨越路由器(第三次及以上的网络设备)，可以彼此物理连通的接口。如图 3 个主机接口和 1 个路由器接口的网络，就形成了一个子网。


<img src ="https://img-blog.csdnimg.cn/c43f3a6105ad4eb681a87c7fe8edd159.png#pic_center" width = 48%>



接下来考虑“系统内的子网”例如一个公司中的某个部门拥有一个 C 类地址，但是连接的主机仅有个位数，而另一个部门希望拥有自己的局域网，就不能使用剩余的 IP 地址，这就造成了 IP 地址空间的利用率很低。IP 地址空间的利用率低也会导致所需的 IP 地址增加，导致了路由器转发表需要更多的空间来存储。
因此将物理网络再分为若干子网是局域网的内部行为，对外表现出来的还是一个网络。对于这种子网，分开主机和路由器的每个接口，这就产生了几个隔离的网络，每一个隔离的网络都是一个子网。

<img src ="https://img-blog.csdnimg.cn/94701f49742c4e7e964915b43885b433.png#pic_center" width = 48%>

**2. 子网掩码**

从 IP 数据报首部无法看出源主机或目的主机的网络是否划分了子网，如何确定？这是就采用了子网掩码，其特性为子网掩码和主机 IP 地址做“与 (AND)”运算后，得到的结果的主机号部分全部为 0。已知 IP 地址是 141.14.72.24，子网掩码是 255.255.192.0，就可以通过这个性质得到其网络前缀。

<img src ="https://img-blog.csdnimg.cn/ec5301f92ae04e96ade9f9e17cb6fd96.png#pic_center" width = 48%>


子网划分的手法是什么？若分为 $2^n$ 个子网，则子网掩码往后移动 n 位。

### 1.5 IP 路由选择
如果发送方与接收方直接相连（点对点）或都在一个共享网络上（以太网），那么 IP 数据报就能直接送达。

而大多数情况则是发送方与接收方通过若干个路由器(router)连接，那么数据报就需要经过若干个路由器的转发才能送达，它是怎么选择一个合适的路径来"送货"的呢？

IP 层在内存中有一个路由表（输入命令 route -n 可以查看路由表），当收到一份数据报并进行发送时，都要对该表进行搜索：
- 搜索路由表，如果能找到和目的 IP 地址完全一致的主机，则将 IP 数据报发向该主机；
- 搜索路由表，如果匹配主机失败，则匹配同子网的路由器(这需要子网掩码的协助)。如果找到路由器，则将该 IP 数据报发向该路由器；
- 搜索路由表，如果匹配同子网路由器失败，则匹配同网络号路由器，如果找到路由器，则将该 IP 数据报发向该路由器；
- 如果以上都失败了，就搜索默认路由，如果默认路由存在，则发报；
- 如果都失败了，就丢掉这个包；
- 接收到数据报的路由器再按照它自己的路由表继续转发，直到数据报被转发到目的主机；
- 如果在转发过程中，IP 数据报的 TTL（生命周期）已经被减为 0，则该 IP 数据报就被抛弃。


### 1.6 由聚合

**1. 组合大子网**

使用单个网络前缀通告多个网络的能力称之为路由聚合，这也可以理解为将多个子网合成一个较大的子网。这是很重要的，因为 ISP 往往需要把它所有的多个组织连接到因特网，而这些组织也都有子网。

<img src ="https://img-blog.csdnimg.cn/3a074bebd26b414b828134f60eecf20e.jpeg#pic_center" width = 48%>

路由聚合的过程可以看做子网划分的逆过程，即子网划分的手法是子网掩码往后移动，路由聚合则是向前移动。

**2. 基于最长前缀**

思考一个问题，若组织的 IP 不连续怎么办？此时将使用最长前缀匹配，也就是路由表寻找最长匹配项，并向其相关联的链路接口转发分组。

<img src ="https://img-blog.csdnimg.cn/985564939005444eba971aaed38228cd.png#pic_center" width = 48%>

从这个也可以看出，子网掩码向前移动时，只有相邻的子网可以聚合，如果不相邻那就只好聚合成更大的子网。

<img src ="https://img-blog.csdnimg.cn/bb6d36298cf6406eb0d7fef5a2d9515b.png#pic_center" width = 48%>

下面看一个路由聚合的实例，如图 ISP 共有 64 个 C 类网络。如果不采用 CIDR 技术，则在与该 ISP 的路由器交换路由信息的每一个路由器的路由表中需要有 64 个项目。但采用地址聚合后，只需用路由聚合后的 1 个项目 206.0.64.0/18 就能找到该 ISP。

<img src ="https://img-blog.csdnimg.cn/0f613b7fb67d4ba7b871217d59115ff5.png#pic_center" width = 48%>


### 1.7 IP分组转发

**1. 转发原理**

IP 分组的转发指的是从一个路由器转发到下一个路由器，每一跳路由器都要给出目标的网络前缀和下一跳地址，即沿途的路由器必须知道目标网络的下一路要给哪个接口。同时根据这一点我们也可以得到网络畅通的条件，也就是满足数据报能去能回。

<img src ="https://img-blog.csdnimg.cn/c24aa8bd88904e3d8750c25da1f494d0.png#pic_center" width = 48%>

**2. 默认路由**

默认路由是对IP数据包中的目的地址找不到存在的其他路由时，路由器所选择的路由。目的地不在路由器的路由表里的所有数据包都会使用默认路由，这条路由一般会连去另一个路由器。对于 Windows 系统而言，网关就是默认路由。

**3. 结合子网掩码**

由于子网的存在性问题不能不能忽视，因此需要集合子网掩码进行转发。先用各网络的子网掩码和目的 IP 地址逐位做“与”预算，看是否和相应的网络地址匹配。若匹配，则将分组直接交付，否则就送往下一跳路由器。

## 2 实验分析

捕获执行 traceroute 的数据包
为了生成本实验的一系列 IP 数据报，我们将使用 traceroute 程序向不同的目的地 X 发送不同大小的数据报。回想一下，traceroute 通过
- 首先发送一个或多个带有生存时间(TTL: Time-to-Live)字段设置为 1 的数据报；
- 然后发送一个或多个带有生存时间(TTL: Time-to-Live)字段设置为 2 的数据报到同一个目的地；
- 接着发送一个或多个带有生存时间(TTL: Time-to-Live)字段设置为 3 的数据报到同一个目的地，
以此类推，直到目的地真正收到此数据报为止。
回想一下，路由器必须将每个接收到的数据报中的 TTL 减 1。如果 TTL 达到 0，路由器会向来源主机发送 ICMP 消息。由于这种行为，
- TTL 为 1 的数据报（由执行 traceroute 的主机发送）将导致距发送方一次跳跃的路由器，将 ICMP TTL 超出的消息发送回发送方主机；
- 以TTL 为 2 发送的数据报将导致距离为两次跳跃的路由器，将 ICMP 消息发送回发送方主机；
- 以 TTL 为 3 发送的数据报将导致距离为两次跳跃的路由器，将 ICMP 消息发送回发送方主机，等等。
以这种方式，执行 traceroute 的主机可通过查看包含ICMP TTL 超出消息的数据报中的来源 IP 地址来获知其自身与目的地 X 之间的路由器的身份。


<img src ="https://img-blog.csdnimg.cn/a72c2b1c588841ff9dc84f373c579ab7.png#pic_center" width = 48%>

不过 Windows 的 tracert 程序不允许更改 tracert 程序发送的 ICMP echo 请求（ping）消息的大小。因此要使用 [pingplotter](http://www.pingplotter.com) 等其他程序来实验。

具体的步骤：

(1) 启动 Wireshark 并开始数据包捕获（Capture-> Start），然后在 Wireshark 数据包捕获选项屏幕上按 OK（我们不需要在此处选择任何选项）。

(2) 在 pingplotter 设置 `Edit->Options->Default` 和 `Settings->Engine` 包大小设置为56Byte

<img src ="https://img-blog.csdnimg.cn/73428265dfaa41cda786b403cb49cc69.png#pic_center" width = 48%>

(3) 然后打开gaia.cs.umass.edu 的跟踪，大约跟踪3 次（由于无法控制，可以稍微超一些），然后暂停。
(4) 重复2-3 步，只不过将大小设置2000Byte 以及3500Byte，然后也大约跟踪3 次。

这期间保持 wireshark 一直打开，总共设置3次，每次差不多也跟踪3次。由于暂停pingplotter再恢复是接着上次的跟踪统计继续，因此序号会一直增加。当然也可以选择重新开一个跟踪。

<img src ="https://img-blog.csdnimg.cn/1c4e7e22d3d4422ea940d058c0e247c7.png#pic_center" width = 48%>

(5) 关闭 wireshark 的捕获，并且分析实验结果。


回答问题：

1. 选择计算机发送的第一个 ICMP Echo Request 消息，然后在 packet details window 中展开数据包的 Internet 协议部分。您的计算机的 IP 地址是多少？
答：IP地址：10.69.164.78

<img src ="https://img-blog.csdnimg.cn/94ad26d33e484627ba15f4c2ede72069.png#pic_center" width = 48%>

2. 在 IP header 中，上层协议字段的值是多少？
答：上层协议就是ICMP，值为1。见上图

查询常见协议值：

<img src ="https://img-blog.csdnimg.cn/39acf2469cf9486585d1eb3b4d7bbf91.png#pic_center" width = 48%>

3. IP header 有多少 bytes？ IP datagram 的有效负载中有多少 bytes？ 说明如何确定 payload bytes 的数。

答：Header Length：20 bytes IP数据报总长度 = IP头长度 + IP数据长度(就是有效负载)
IP datagram payload bytes：56bytes

方法1：
IP datagram payload bytes = Total Length - Header Length = 56 - 20 = 36

<img src ="https://img-blog.csdnimg.cn/f4d63d44f3e24e8f948a9645c1600ede.png#pic_center" width = 48%>



方法2：

IP数据报的有效负载，这里装的就是ICMP数据报，所以看ICMP占多少字节即可。

<img src ="https://img-blog.csdnimg.cn/76da69363f83423f8c8bd56d9f4e0339.png#pic_center" width = 48%>



4. 此 IP 数据报是否已被分段(fragmented)？解释您如何确定数据报是否已被分段(fragmented)。

答：这里的IP数据报没有被分段， 因为 `Fragment offset = 0`，分段的偏移量为0，所以没有分段，而且 `More fragments` 也是为 `Not set`，表示没有设置分段。

<img src ="https://img-blog.csdnimg.cn/31b0c90e72c440f595ce07d467f08931.png#pic_center" width = 48%>


5. 在您的计算器发送的这一系列 ICMP 消息中，IP 数据报中的哪些字段 一直在改变？
答：发送的ICMP Echo(ping)request：标识号Identification、校验和Header checksum、存活时间TTL 一直在变。

<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/78fa37abf2ef49c9b891471cbb805845.png#pic_left" width = "46%"><img src = "https://img-blog.csdnimg.cn/dae2bf85bc804acfaa81430a6b9c61d2.png#pic_left"  width = "47%"></center></p>

也就是下图这些部分：

<img src ="https://img-blog.csdnimg.cn/3f72476e4dfa4ee6b4a0e8687f4246af.png#pic_center" width = 48%>

6. 哪些字段保持不变？哪个字段必须保持不变？哪些字段必须更改？
必须保持不变：
1. 版本（Version）：占 4 bit，通信双方使用的版本必须一致，对于 IPv4 字段的值是4；
2. 首部长度（Internet Header Length， IHL）：占 4 bit，首部长度说明首部有多少 32 位字（4字节）。由于IPv4首部可能包含数目不定的选项，这个字段也用来确定数据的偏移量；
3. 区分服务（Differentiated Services，DS）：占 6 bit，只有在使用区分服务时，这个字段才起作用，在一般的情况下都不使用这个字段；

保持不变：
- 显式拥塞通告（ Explicit Congestion Notification，ECN）：允许在不丢弃报文的同时通知对方网络拥塞的发生。
- 全长（Total Length）：占 16 位字段，定义了报文总长，包含首部和数据，单位为字节。这个字段的最小值是 20（0 字节数据），最大值是65535。
- 标识符（Identification）：占16位，这个字段主要被用来唯一地标识一个报文的所有分片，因为分片不一定按序到达，所以在重组时需要知道分片所属的报文。
- 分片偏移 （Fragment Offset）：这个13位字段指明了每个分片相对于原始报文开头的偏移量，以8字节作单位。
- 源地址：报文的发送端；
- 目的地址：报文的接收端；
- 选项：附加的首部字段可能跟在目的地址之后；

必须更改：
- 标识符（Identification）：占 16 位，主要被用来唯一地标识一个报文的所有分片；
- 存活时间（Time To Live，TTL）：占 8 位，避免报文在互联网中永远存在。实现为跳数计数器，报文经过的每个路由器都将此字段减1，当此字段等于0时，报文不再向下一跳传送并被丢弃，最大值是255。这是traceroute的核心原理；
- 首部检验和 （Header Checksum）：占 16 位，检验和字段只对首部查错，在每一跳，路由器都要重新计算出的首部检验和并与此字段进行比对，如果不一致，此报文将会被丢弃；
- 数据

所谓的保持不变指的是这次 traceroute 不会改变的，但是下一次 traceroute 可能就会改了。

如图蓝色框是保持不变（下次可能改变），绿色框是一定不会改变的（仅指路
由跟踪），红色框是必须改变的。

<img src ="https://img-blog.csdnimg.cn/b92b61b4239b40cca5d14f8726044fa9.png#pic_center" width = 48%>


7. 描述您在 IP datagram 的 Identification field 中的值中所看到的？
答：主要被用来唯一地标识一个报文的所有分片，因此对于不同的报文就需要改变这个值，使得报文可以唯一确定。
下一步查找第一跳路由器发送到您的计算器的一系列 ICMP TTL 超出的回复讯息。

8. ID 字段和 TTL 字段的值是多少？
答：ID 字段 10501，TTL 字段 253。
<img src ="https://img-blog.csdnimg.cn/a7fa08b7262a494a94f5ffd63cdce2ab.png#pic_center" width = 48%>

9. 对于第一跳路由器发送到您的计算器的所有 ICMP TTL 超时的回复，这些值是否保持不变？为什么？
答：ID 字段改变，TTL 字段改变。（我这里查看所有的超时回复都改变，不知道是为啥）

<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/db81b4d0eab34955beb82767586caff2.png#pic_left" width = "46%"><img src = "https://img-blog.csdnimg.cn/004942d891a145d99c4c8469001b43a8.png#pic_left"  width = "47%"></center></p>

10. 在将 pingplotter 中的数据包大小更改为 2000 后，查找计算机发送的第一个 ICMP Echo Request 消息。该消息是否已碎片化为多个 IP 数据报？
答：可以看出该消息被碎片化为 2 个 IP 数据报。

<img src ="https://img-blog.csdnimg.cn/24824706ddb54bb38ac6a57130b5b045.png#pic_center" width = 48%>


11. IP 数据报的第一个片段。 IP 头中的哪些信息表明数据报已碎片化？ IP 头中的哪些信息表明这是第一个片段还是后一个片段？ 这个 IP 数据报有多长？
答：More fragments字段为 1 表示 Set，即该数据包被分片。通过 ID 字段判断这是第一个片段，分片长度为 1456 bytes。

<img src ="https://img-blog.csdnimg.cn/66581b9c19214848a913803d633f1b3d.png#pic_center" width = 48%>

12. 找到碎片 IP 数据报的第二个片段。 IP 标头中的哪些信息表明这不是第一个数据报片段？ 是否还有更多的片段？你是如何知道的？
答：Fragment Offset 字段表示偏移量，1456 bytes 的偏移量表示是上一个片段的后续。没有更多片段了，因为 More fragments 字段为 Not set，表示后面没有分片了。
<img src ="https://img-blog.csdnimg.cn/21455ace8ae648cf8020be139f25d4e4.png#pic_center" width = 48%>

13. 在第一个和第二个片段中，IP 标头中哪些字段发生了变化？
答：全长（Total Length）、标志 （Flags）和分片偏移 （Fragment Offset）。

<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/c331d1b2a9bf4ae7aec5ad44220ae922.png#pic_left" width = "46%"><img src = "https://img-blog.csdnimg.cn/e41ecb5971d44a40a23d71608bcf88d3.png#pic_left"  width = "47%"></center></p>


接下来在将 pingplotter 中的数据包大小更改为 3500 后，找到计算机发送的第一个 ICMP Echo Request 消息。


14. 从原始数据报创建了多少个片段？
答：创建了三个片段。

<img src ="https://img-blog.csdnimg.cn/c357643290b04bd0b354cb81b2357578.png#pic_center" width = 48%>




_____

## 参考
- Wireshark实验——IP协议：[https://www.cnblogs.com/linfangnan/p/12835848.html](https://www.cnblogs.com/linfangnan/p/12835848.html)
- IP网际协议：[https://www.lanqiao.cn/courses/98/learning/?id=474&compatibility=false](https://www.lanqiao.cn/courses/98/learning/?id=474&compatibility=false)