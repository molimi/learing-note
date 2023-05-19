ICMP（Internet Control Message Protocol）网络控制报文协议。它是 TCP/IP 协议簇的一个子协议，用于在 IP 主机、路由器之间传递控制消息。控制消息是指网络通不通、主机是否可达、路由是否可用等网络本身的消息。这些控制消息虽然并不传输用户数据，但是对于用户数据的传递起着重要的作用。每个 ICMP 消息都是直接封装在一个 IP 数据包中的，因此，和 UDP 一样，ICMP 是不可靠的。

ICMP（Internet Control Message Protocol）网络控制报文协议。它是 TCP/IP 协议簇的一个子协议，用于在 IP 主机、路由器之间传递控制消息。控制消息是指网络通不通、主机是否可达、路由是否可用等网络本身的消息。这些控制消息虽然并不传输用户数据，但是对于用户数据的传递起着重要的作用。每个 ICMP 消息都是直接封装在一个 IP 数据包中的，因此，和 UDP 一样，ICMP 是不可靠的。

<img src ="https://img-blog.csdnimg.cn/d9c4d2b510a74d25821c3015d02ac23d.png#pic_center" width = 64%>

几种常用的 ICMP 报文类型：

<img src ="https://img-blog.csdnimg.cn/3b4070a5b48242dfbe389a1fa08ee05b.png#pic_center" width = 64%>

Ping 是基于 ICMP 协议的，就是互联网控制报文协议，网络包在异常复杂的网络环境进行传输的时候，常常会遇到各种各样的问题，当遇到问题的时候，总要传出消息来，报告情况，这样才可以调整传输策略。

Ping 基本使用：在网络中 Ping 是一个十分强大的 TCP/IP 工具。
(1) 用来检测网络的连通情况和分析网络速度；
(2) 根据域名得到服务器 IP；
(3) 根据 Ping 返回的 TTL 值来判断对方所使用的操作系统及数据包经过路由器数量。


## 1 ICMP协议
### 1.1 协议解析
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP协议：`Internet Control Message Protocol`（Internet控制报文协议）；由于IP协议并不是一个可靠的协议，它不保证数据被成功送达。原因是，在通信途中的某处的一个路由器由于不能处理所有的数据包，就将数据包一个一个丢弃了。或者，虽然到达了对方，但是由于搞错了端口号，服务器软件可能不能接受它。这时，在错误发生的现场，为了联络而飞过来的信鸽就是ICMP 报文。在IP 网络上，由于数据包被丢弃等原因，为了控制将必要的信息传递给发信方。ICMP 协议是为了辅助IP 协议，交换各种各样的控制信息而被制造出来的，经常供IP层或更高层协议（TCP或UDP）使用。所以它经常被认为是IP层的一个组成部分。

<img src ="https://img-blog.csdnimg.cn/84a42d98815e4c1ea6bc25f595118686.png#pic_center" width = 48%>

制定万维网规格的IETF 在1981 年将RFC7922作为ICMP 的基本规格整理出来了。那个RFC792 的开头部分里写着<font color=#9900CC><strong>“ICMP 是IP 的不可缺少的部分，所有的IP 软件必须实现ICMP协议”</font></strong>。即，ICMP 是为了分担IP 一部分功能而被制定出来的。

<img src ="https://img-blog.csdnimg.cn/e437751af0d04ab6a61e2f94c8b5d5e2.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP协议是一种面向无连接的协议，用于传输出错报告控制信息。它属于网络层协议，主要用于在主机与路由器之间传递控制信息，包括报告错误、交换受限控制和状态信息等。当遇到IP数据无法访问目标、IP路由器无法按当前的传输速率转发数据包等情况时，会自动发送ICMP消息。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在RFC，将ICMP 大致分成两种功能：差错通知和信息查询。

<img src ="https://img-blog.csdnimg.cn/83b35284ce8b44a2a0b36f96f61fcde9.png#pic_center" width = 48%>

- [1]给送信者的错误通知；[2]送信者的信息查询。
- [1]是到IP 数据包被对方的计算机处理的过程中，发生了什么错误时被使用。不仅传送发生了错误这个事实，也传送错误原因等消息。
- [2]的信息询问是在送信方的计算机向对方计算机询问信息时被使用。被询问内容的种类非常丰富，他们有目标IP 地址的机器是否存在这种基本确认，调查自己网络的子网掩码，取得对方机器的时间信息等。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP是TCP/IP模型中网络层的重要成员，与IP协议、ARP协议、RARP 协议及 IGMP协议共同构成 TCP/IP模型中的网络层。`ping` 和 `tracert` 是两个常用网络管理命令，`ping` 用来测试网络可达性，`tracert` 用来显示到达目的主机的路径。`ping` 和 `tracert` 都利用ICMP 协议来实现网络功能，它们是把网络协议应用到日常网络管理的典型实例。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP报文内容是放在IP数据包的数据部分里来互相交流的。也就是，从ICMP的报文格式来说，ICMP是IP的上层协议。但RFC认为ICMP是分担了IP的一部分功能。所以，ICMP也被认为是与IP同层的协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个ICMP报文包括IP报头（至少20字节）、ICMP报头（至少八字节）和ICMP报文（属于ICMP报文的数据部分）。看一下RFC 规定的数据包格式和报文内容吧。

<img src ="https://img-blog.csdnimg.cn/b4383e86b10f480493bbd0848b333f6a.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当IP报头中的协议字段值为1时，就说明这是一个ICMP报文。ICMP的数据报文格式如下所示。所有报文的前4个字节都是一样的，其他的因报文类型不同而不一样。类型字段可以有15个不同的值，用以描述不同的ICMP报文。校验和字段覆盖整个ICMP报文，使用了和IP首部检验和一样的算法，详细请搜索TCP/IP检验和算法。

<img src ="https://img-blog.csdnimg.cn/2d04b69bb93f4db7b4b5d786680597f4.png#pic_center" width = 48%>


**字段说明：**
- 类型：标识ICMP报文的类型，从类型值来看ICMP报文可以分为两大类。第一类是取值为1~127的差错报文，第2类是取值128以上的信息报文。    
- 代码：标识对应ICMP报文的代码。它与类型字段一起共同标识了ICMP报文的详细类型。    
- 校验和：对包括ICMP报文数据部分在内的整个ICMP`数据报的校验和，以检验报文在传输过程中是否出现了差错。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=#9900CC><strong>不同类型的报文是由类型字段和代码字段来共同决定。</font></strong>下表是各种类型的ICMP报文。

<img src ="https://img-blog.csdnimg.cn/e79bd384284f464bb32f632188202117.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据上表可知，ICMP协议大致分为两类，一种是查询报文，一种是差错报文。查询报文是用一对请求和应答定义的，它通常有以下几种用途:
1. ping查询
2. 子网掩码查询（用于无盘工作站在初始化自身的时候初始化子网掩码）
3. 时间戳查询（可以用来同步时间）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而差错报文通常包含了引起错误的IP数据报的第一个分片的IP首部（和选项），加上该分片数据部分的前8个字节。RFC 792规范中定义的这8个字节中包含了该分组运输层首部的所有分用信息，这样运输层协议就可以向正确的进程提交ICMP差错报文。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当传送IP数据包发生错误时，比如主机不可达，端口不可达等，ICMP协议就会把错误信息封包，然后传送回给主机。给主机一个处理错误的机会，这也就是为什么说建立在IP层以上的协议是可能做到安全的原因。由上面可知，ICMP数据包由8bit的错误类型和8bit的代码和16bit的校验和组成，而前 16bit就组成了ICMP所要传递的信息。由数据链路层所能发送的最大数据帧，即MTU（Maximum Transmission Unit）为1500，计算易知ICMP协议在实际传输中数据包为：20字节IP首部 + 8字节ICMP首部+ 1472字节（数据大小）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;尽管在大多数情况下，错误的包传送应该给出ICMP报文，但是在特殊情况下，是不产生ICMP错误报文的。如下
1. ICMP差错报文不会产生ICMP差错报文（出IMCP查询报文）（防止IMCP的无限产生和传送）
2. 目的地址是广播地址或多播地址的IP数据报。
3. 作为链路层广播的数据报。
4. 不是IP分片的第一片。
5. 源地址不是单个主机的数据报。这就是说，源地址不能为零地址、环回地址、广播地 址或多播地址。

### 1.2 ICMP 报文格式

ICMP 报文包括 IP 头部、ICMP 头部和 ICMP 报文 3 个部分，ICMP 报文是作为 IP 有效载荷承载的。

<img src ="https://img-blog.csdnimg.cn/7334559d24864706b107d8c69a3926c7.png#pic_center" width = 48%>

<table>
<thead>
<tr>
<th>字段</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>Type</td>
<td>ICMP 的类型,标识生成的错误报文；</td>
</tr>
<tr>
<td>Code</td>
<td>进一步划分 ICMP 的类型,该字段用来查找产生错误的原因；</td>
</tr>
<tr>
<td>Checksum</td>
<td>校验码，字段包含有从 ICMP 报头和数据部分计算得来的，用于检查错误的数据；</td>
</tr>
<tr>
<td>ID</td>
<td>ID 值，在 Echo Reply 类型的消息中要返回这个字段；</td>
</tr>
<tr>
<td>Sequence</td>
<td>这个字段包含一个序号，在 Echo Reply 类型的消息中要返回这个字段。</td>
</tr>
</tbody>
</table>


### 1.3 ICMP 报文类型

ICMP 有 2 类报文，第一类是差错报告报文，分别是以下 5 种：

<table>
<thead>
<tr>
<th>差错报告报文</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>目的不可达</td>
<td>路由器或主机不能交付数据报</td>
</tr>
<tr>
<td>超时或超期</td>
<td>路由器收到生存时间为 0 的数据报</td>
</tr>
<tr>
<td>参数有问题</td>
<td>路由器或主机收到数据报中，首部有字段的值不正确</td>
</tr>
<tr>
<td>重定向</td>
<td>改变主机下一次发生数据报所选的路由</td>
</tr>
<tr>
<td>源抑制</td>
<td>发送给源主机，令其降低发送数据的速率(现在不用了)</td>
</tr>
</tbody>
</table>

第二类是网络探询报文，有以下 2 组：

<table>
<thead>
<tr>
<th>网络探询报文</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>回声请求与应答</td>
<td>主机或路由器向特定主机发送询问</td>
</tr>
<tr>
<td>时间戳请求与应答</td>
<td>请求某台主机或路由器应答当前日期和时间</td>
</tr>
</tbody>
</table>

除此之外还有 3 个不再使用的报文，分别是：信息请求与应答、子网掩码请求与应答、路由器询问和通报。常用报文类型如下：

<img src ="https://img-blog.csdnimg.cn/6e46f191c8ce47efa74f39ba1ba609a8.png#pic_center" width = 48%>

我们留意 3 个报文。首先是回显应答 (Echo Reply) 报文，我们知道 Ping 程序是会发送一个回显请求(类型 8 编码 0)报文给目的主机，目的主机收到之后就发送回显应答(类型 0 编码 0)报文进行回显。一般来说，第一个回显请求之前要先发送一个 ARP 请求并接收应答，会消耗一定的时间。

接着是TTL 报文(类型 11 编码 0)，这个是在 Traceroute 程序中，路由器检查到 Traceroute 发出的 IP 数据报中 TTL 正好过期，因此路由器就需要丢包并且发送该警告报文返回源主机。源主机就可以得到路由器的 IP 地址，以此达到路由追踪的目的。
还有一个是源抑制报文，这个报文是为了执行拥塞控制，令拥塞的路由器可以通过发送该报文令主机发送速率降低，不过 TCP 在运输层有自己的拥塞控制手法，因此源抑制报文在实践中很少使用。

## 2 实验分析
### 2.1 Ping 程序

Ping 程序允许我们验证某主机是否存在，通过将数据包发送到目标 IP 地址， 如果目标主机在线则目标主机中的 Ping 程序将会发送响应数据包进行响应，这两个 Ping 数据包都是 ICMP 数据包。

**1. 实验步骤**
1) 打开 Wireshark 启动捕获
2) 打开命令提示符使用 ping 命令，ping 其他大陆的服务器10 次，这里以 `gaia.cs.umass.edu` 为例，命令语法：`CMD > ping -n 10 gaia.cs.umass.edu`

<img src ="https://img-blog.csdnimg.cn/082e579ab55a4134996111241c3cdef6.png#pic_center" width = 48%>




**2. 实验结果**

1. 源主机的 IP 地址是多少？目标主机的 IP 地址是多少？
答：源主机的 IP 地址是：10.69.164.78；目标主机的 IP 地址是：128.119.245.12
<img src ="https://img-blog.csdnimg.cn/ae98f174602548698140119c42dc098e.png#pic_center" width = 48%>

2. 为什么 ICMP 数据包没有源端口号和目的端口号？
答：因为 ICMP 协议是网络层的协议，它不需要传输层TCP 和UDP 承载，直接使用IP 报承载，因此不需要源端口号目的端口号，只需要目的地址即可。

3. 查看任意的请求 ICMP 数据包， ICMP 类型和代码是什么？ 该 ICMP 数据包还有哪些其他字段？ 校验和，序列号和标识符字段有多少字节
答: ICMP 类型是 8（代表ICMP 请求），代码是 0，ICMP 数据包还包括校验码，ID 值，以及序号。校验和，序列号，标识符都是 16 个字符，4 个字节。

<img src ="https://img-blog.csdnimg.cn/6c59554ac8144f4488e2d74f4f350efc.png#pic_center" width = 48%>

<img src ="https://img-blog.csdnimg.cn/d6d5e66d35ad4b699d795eed97408c26.jpeg#pic_center" width = 48%>

4. 查看任意的响应 ICMP 数据包， ICMP 类型和代码是什么？ 该 ICMP 数据包还有哪些其他字段？ 校验和，序列号和标识符字段有多少字节？
答: ICMP 类型是0（代表ICMP 响应），代码是0，ICMP 数据包还包括校验码，ID 值，以及序号。校验和，序列号，标识符都是16 个字符，4 个字节。

<img src ="https://img-blog.csdnimg.cn/8dbf7150abe34e6cbc9566364872bd10.png#pic_center" width = 48%>


### 2.2 Traceroute 命令

**1. Traceroute 简介**

Traceroute 程序可用于确定数据包从源到目的地的路径，原理是发送 TTL 增加的数据包，当 TTL = 1 的包达到路由器，该路由器会将该包丢弃，并且发送 ICMP 错误给请求的机器。

traceroute 通过首先发送一个或多个带有生存时间 (TTL) 字段设置为 1 的数据报；然后发送一个或多个带有 TTL 字段设置为 2 的数据报到同一个目的地；然后发送一个或多个带有 TTL 字段设置为 3 的数据报到同一个目的地，以此类推，直到目的地真正收到此数据报为止。路由器必须将每个接收到的数据报中的 TTL 减 1，如果 TTL 达到 0，路由器会向来源主机发送 ICMP 消息。由于这种行为，TTL 为 1 的数据报将导致距发送方一次跳跃的路由器，将 ICMP TTL 超出的消息发送回发送方主机；以TTL 为 2 发送的数据报将导致距离为两次跳跃的路由器，将 ICMP 消息发送回发送方主机等等。以这种方式，执行 traceroute 的主机可以通过查看包含ICMP TTL 超出消息的数据报中的来源 IP 地址来获知其自身与目的地之间的路由器的身份。

<img src ="https://img-blog.csdnimg.cn/b4ae201266ea43eb99c0062c0f4db005.png#pic_center" width = 48%>

**2. 实验步骤**

1) 打开命令提示符进行路由跟踪，跟踪 `gaia.cs.umass.edu`，命令语法：`CMD > tracert gaia.cs.umass.edu`


**3. 问题解答**

5. 您的主机的 IP 地址是多少？目标目标主机的 IP 地址是多少？
答：源主机：10.69.164.78；目标主机：128.119.245.12

<img src ="https://img-blog.csdnimg.cn/9fc9e9470803450aa56f4e52ebe9a840.png#pic_center" width = 48%>


6. 如果 ICMP 发送了 UDP 数据包（如在 Unix / Linux 中），那么探测数据包的 IP 协议号仍然是 01 吗？ 如果没有，它会是什么？
答：发送请求路由跟踪的数据包是 UDP 数据包，因此 IP 承载上层协议号时 17。

7. 检查屏幕截图中的 ICMP 响应数据包。这与本实验的前半部分中的 ICMP ping 查询数据包不同吗？如果不同，请解释为什么？
答：不同，这里的 ICMP 报文时 **TTL 报文(类型 11 编码 0)，这个是在 Traceroute 程序中，路由器检查到 Traceroute 发出的 IP 数据报中 TTL 正好过期，因此路由器就需要丢包并且发送该警告报文返回源主机。这个与 Ping 程序中所要达成的目的不同，Ping 程序是为了请求响应。

<img src ="https://img-blog.csdnimg.cn/18d61e06d8934a858a9307f4b2f3f00a.png#pic_center" width = 48%>

8. 检查屏幕截图中的 ICMP 错误数据包。它具有比 ICMP 响应数据包更多的字段。这个数据包含哪些内容？
答：比响应数据包多了 ICMP 请求数据包的内容

<img src ="https://img-blog.csdnimg.cn/29e420aee503437685645159a3c23799.png#pic_center" width = 48%>


9. 检查源主机收到的最后三个 ICMP 数据包。这些数据包与 ICMP 错误数据包有何不同？他们为什么不同？
答：这个是目的主机返回的回显应答报文，因为 tracert 程序的原理是发送 TTL 增加的数据包，当 TTL = 1 的包达到路由器，该路由器会将该包丢弃，并且发送 ICMP 错误给请求的机器。而最后一组 3 个数据报时可以到达目的主机的，这时由于是被目的主机接收，目的主机不会丢包，而是确确实实收到的这个探测的数据报并进行了响应。

<img src ="https://img-blog.csdnimg.cn/2a2c9c510d974ff2a98699920118c5ae.png#pic_center" width = 48%>

1.  在 tracert 跟踪测量中，是否有一个连接的延迟比其他连接长得多？是否有连接的延迟明显长于其他连接？根据路由器名称，您能猜出这个连接末端的两个路由器的位置吗？
答：在第 8 个节点和第 9 个节点之间时延突增，之后的节点时延都达到了 250+ ms。之后的路由器名都是英文名，且目的地是法国，那应该是连接到了亚洲转欧洲的分界路由器了。

<img src ="https://img-blog.csdnimg.cn/fa729d0cdb594c32bc393a50065647a4.png#pic_center" width = 48%>

用 Best trace 做一次路由追踪，看来确实在这两个节点出现了从上海到伦敦的大跳跃！

<img src ="https://img-blog.csdnimg.cn/860083d8ce35435d9fea9cb4fe745dc6.png#pic_center" width = 48%>

______


**补充**
1) 在 Linux 虚拟机中进行路由跟踪，地址仍然是 `gaia.cs.umass.edu`，命令语法：`traceroute gaia.cs.umass.edu`

<img src ="https://img-blog.csdnimg.cn/ea094e68566041628573df2384ccdaaa.png#pic_center" width = 48%>

2) 同样，Linux 还可以指定路由跟踪使用ICMP 数据报。命令语法：`# traceroute gaia.cs.umass.edu -I`




## 参考

