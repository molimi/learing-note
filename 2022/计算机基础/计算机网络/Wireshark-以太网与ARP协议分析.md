## 1 以太网
### 1.1 介绍
以太网是现实世界中最普遍的一种计算机网络。以太网有两类：第一类是经典以太网，第二类是交换式以太网，使用了一种称为交换机的设备连接不同的计算机。
- 经典以太网：是以太网的原始形式，运行速度从 3~10 Mbps 不等；
- 交换式以太网：正是广泛应用的以太网，可运行在 100、1000 和 10000 Mbps 那样的高速率，分别以快速以太网、千兆以太网和万兆以太网的形式呈现。

**经典以太网**

<img src ="https://img-blog.csdnimg.cn/0e24b17634bb44a8843216bb759970eb.png#pic_center" width = 48%>

- 物理层：以太网的每个版本都有电缆的最大长度限制（即无须放大的长度），这个范围内的信号可以正常传播，超过这个范围信号将无法传播。为了允许建设更大的网络，可以用中继器把多条电缆连接起来。中继器是一个物理层设备，它能接收、放大并在两个方向上重发信号。

- MAC 子层：经典以太网使用1-坚持 CSMA/CD 算法，即当站有帧要发送时要侦听介质，一旦介质变为空闲便立即发送。在它们发送的同时监测信道上是否有冲突。如果有冲突，则立即终止传输，并发出一个短冲突加强信号，再等待一段随机时间后重发。

其实局域网技术还有令牌环、FDDI 和 ATM 等，但是以太网仍然具有很多独特的优势，使其保持着广泛的使用，原因有：
1. 以太网是第一个广泛部署的高速局域网，网络从业者对其更为熟悉；
2. 以太网相对令牌环、FDDI 和 ATM 等技术更为简洁、便宜；
3. 以太网也不断发展，诞生出更多数据效率高的新版本，使得其可以与新的局域网技术仍保持竞争力；
4. 以太网的网络硬件很便宜，因为以太网技术非常流行。

### 1.2 以太网硬件
初始的以太局域网使用同轴电缆总线互联结点，也就是总线型。使用总线拓扑的以太网是广播局域网，也就是所有传输的真传输到总线连接的所有适配器来处理。这就说明了所有结点会在同一冲突域中，因此彼此之间很容易发生冲突，需要用具有二进制指数回退的 CSMA/CD 多路访问协议。

<img src ="https://img-blog.csdnimg.cn/87a0c7732f444981866d75d2d09d8208.png#pic_center" width = 48%>

在发展之后就出现了基于集线器的星形拓扑以太网，集线器是物理层设备，操作的不是以太帧而是各个字节。集线器的工作原理是当在一个接口接收到一个比特，就将这个比特生成一个副本并向其他接口发送。随着不断的发展，后续交换机取代了集线器，仍然使用星形拓扑。星形拓扑的好特点是没一个节点的冲突域是单独的，结点间彼此不冲突。

<img src ="https://img-blog.csdnimg.cn/494b3fd185d2471ba43bb685647ee979.png#pic_center" width = 48%>

### 1.3 以太帧类型

以太帧有很多种类型。不同类型的帧具有不同的格式和 MTU 值。但在同种物理媒体上都可同时存在。
1. 以太网第二版或者称之为 Ethernet II 帧，DIX 帧，是最常见的帧类型。并通常直接被 IP 协议使用；
2. Novell 的非标准 IEEE 802.3 帧变种；
3. IEEE 802.2 逻辑链路控制(LLC) 帧；
4. 子网接入协议（SNAP）帧。

**1. Ethernet帧格式**
以太网中大多数的数据帧使用的是 Ethernet II 格式

<img src ="https://img-blog.csdnimg.cn/589e6c8ed4974ff5bc1681550772bb96.png#pic_center" width = 48%>

Ethernet II 类型以太网帧的最小长度为 64 字节($6＋6＋2＋46＋4$)，最大长度为 1518 字节($6＋6＋2＋1500＋4$)。其中：
(1) 前 12 字节分别标识出发送数据帧的源节点 MAC 地址和接收数据帧的目标节点 MAC 地址；
(2) 接下来的 2 个字节标识出以太网帧所携带的上层数据类型，如 16 进制数0x0800代表 IP 协议数据，16 进制数0x86dd代表 IPv6 协议数据，16 进制数0x809B代表 AppleTalk 协议数据，16 进制数0x8138代表 Novell 类型协议数据等；
(3) 在不定长的数据字段（Data）：其长度是 46 至 1500 字节；
(4) 4 个字节的帧校验序列（Frame. Check Sequence，FCS），采用 32 位 CRC 循环冗余校验对从“目标 MAC 地址”字段到“数据”字段的数据进行校验。

**2. IEEE 802.3 帧格式**

<img src ="https://img-blog.csdnimg.cn/19cdf7a3bdab4e7d99c43a34381db0cf.png#pic_center" width = 48%>

各字段说明如下：
(1) D-MAC && S-Mac：分别表示标识目标地址和源地址。它们均为 6 个字节长。如果传输出去的目标地址第一位是 0，则表示这是一个普通地址；如果是 1， 则表示这是一个组地址。
(2) Length / Type ：通常这个字段用于指定报文头后所接的数据类型。通常使用的值包括：IPv4（0x0800）, IPv6(0x86DD), ARP(0x0806)。 而值0x8100代表一个 Q-tagged 帧（802.1q）。通常一个基础的以太网帧长为 1518 字节，但是更多的新标准把这个值扩展为 2000 字节。
(3) MAC Client Data: 数据主体，由 LLC、SNAP 及 Data 构成。最小长度为 48 字节(加上帧头 12 字节，CRC4 字节刚好 64 字节), 当数据主体小于 48 字节时，会添加 pad 字段。选取最小长度是出于冲突检测的考虑(CSMA/CD)。而数据字段最大长度为 1502 字节。

IEEE 802.2 LLC的头构成：
(a) DSAP 目的服务访问字段，1 字节长，指明帧的目的上层协议类型；
(b) ASAP 源服务访问字段，1 字节长，指明帧的源上层协议类型；
(c) control 控制 1 字节或者 2 字节，长度要看被封装的 LLC 数据类型，是 LLC 数据报（类型1）1 字节，LLC 对话的一部分（类型2）2 字节。

类型1 表明是无连接的，不可靠的 LLC 数据报，控制字段用0x03指明；类型 2 表明是面向连接可靠的 LLC 会话。
(4) FCS（Frame Check Sequence）：也叫 CRC（Cyclic Redundancy Check），CRC 是差错检测码，用来确定接收到的帧比特是否正确。

**3. IEEE 802.3 SNAP**

虽然 IEEE 802.3 是标准，但没有被业界采用。以太网 II 已成事实标准。于是 IEEE 802.3 扩展产生 IEEE 802.3 SNAP 来兼容以太网网头部协议，在 IEEE 802.2 LLC 头部后插入了 SNAP 头部。
SNAP 头部字段构成：
(1) 组织代码 3 字节长，指明维护接下来 2 字节意义的组织，对 IP 和 ARP，该字段被设置为0x00-00-00。
(2) 以太网类型 如果组织代码为0x00-00-00，接下来 2 字节就是以太网类型 IP （0x0800）ARP（0x0806）。
因为增加了 LLC 头部的 3 字节和 SNAP 头部的 5 字节所以有效载荷比以太网 II 少 8 个字节。

**4. Ethernrt 包**

Ethernet II 类型以太网的帧结构：

<img src ="https://img-blog.csdnimg.cn/f94af165601f4ae5b0c048565f75b27c.png#pic_center" width = 48%>

- 报头: 8 个字节，前 7 个 0，1 交替的字节(10101010)用来同步接收站，一个1010101011字节指出帧的开始位置。报头提供接收器同步和帧定界服务。
- 目标地址: 6 个字节，单播、多播或者广播。单播地址也叫个人、物理、硬件或 MAC 地址。广播地址全为 1 , 0xFF FF FF FF。
- 源地址: 6 个字节。指出发送节点的单点广播地址。
- 以太类型: 2 个字节，用来指出以太网帧内所含的上层协议。即帧格式的协议标识符。对于 IP 报文来说，该字段值是0x0800。对于 ARP 信息来说，以太类型字段的值是0x0806。
- 有效负载：由一个上层协议的协议数据单元 PDU 构成。可以发送的最大有效负载是 1500 字节。由于以太网的冲突检测特性，有效负载至少是 46 个字节。如果上层协议数据单元长度少于 46 个字节，必须增补到 46 个字节。
- 帧检验序列：4 个字节。验证比特完整性。


### 1.4 以太网服务

以太网向网络层提供 2 种服务。首先是无连接服务，也就是适配器之间发送接收真，发送网卡和接收网卡间不需要“握手”，类似于 IP 协议和 UDP 协议。第二是不可靠服务，虽然接收适配器执行 CRC 校验，但是这个校验并不发送类似 ACK 的确认帧。虽然将到时传递到网络层的数据流出现间隙，这种传输方式可以使得以太网可以简洁且便宜。对于这种间隙，接收方遇到查错帧就直接丢弃，若要修复丢弃帧的数据，需要依靠类似 TCP 这样的高层协议。

## 2 ARP协议
### 2.1 原理分析
由于 IP 地址是网络层地址，MAC 地址是链路层地址，因此当我需要传输数据时就需要对地址进行转换。在同一个 LAN 里如何在已知目的 IP 地址的前提下确定 MAC 地址？这就需要 ARP 协议。这个好像和 DNS 有些相似之处，DNS 是在因特网中进行主机的主机名解析，ARP 是在一个子网上的主机和路由器接口解析 IP 地址。

每台主机和路由器在内存中有 ARP 缓存表，表中有 3 个内容，前两个是 IP 地址和 MAC 地址，这表示了 IP 地址和对应的 MAC 地址的映射关系，还有一个是 TTL，这是每个映射关系保存的时间，这是因为我们其实不必要去为每一台主机和路由器都存储映射关系，毕竟有的主机我可能从来不访问。

ARP 缓存表使用过程：
- 当主机要发送一个 IP 数据报的时候，会首先查询一下自己的 ARP 缓存表；
- 如果在 ARP 缓存表中找到对应的 MAC 地址，则将 IP 数据报封装为数据帧，把 MAC 地址放在帧首部，发送数据帧；
- 如果查询的 IP－MAC 值对不存在，那么主机就向网络中广播发送一个 ARP 请求数据帧，ARP 请求中包含待查询 IP 地址；
- 网络内所有收到 ARP 请求的主机查询自己的 IP 地址，如果发现自己符合条件，就回复一个 ARP 应答数据帧，其中包含自己的 MAC 地址；
- 收到 ARP 应答后，主机将其 IP - MAC 对应信息存入自己的 ARP 缓存，然后再据此封装 IP 数据报，再发送数据帧。


拥有 ARP 表之后是怎么实现功能呢？首先发送方构造一个 ARP 查询分组，这个分组用于询问子网上的所有主机和路由器，使用 MAC 广播地址(FF-FF-FF-FF-FF-FF)发送分组，LAN 中的所有结点都会受到这个 ARP 查询分组，此时只有接收方会接收这个分组匹配，这个匹配是通过ARP 模块实现的，模块的作用是将适配器将 ARP 分组传入时，检查 IP 地址是否与 ARP 的目的 IP 地址匹配。匹配成功之后就可以用单播(不是广播)发送 ARP 响应分组，其他的就忽略这个分组。发送方接收到这个响应分组之后，就在 ARP 表中缓存该 IP-MAC 映射关系，然后超时后刷新。
这里有 2 个细节需要注意。首先是 ARP 查询分组是广播，而响应分组是单播。第二是 ARP 是即插即用的，也就是 ARP 表不需要手动配置，只需要让协议自动建立就行。

<img src ="https://img-blog.csdnimg.cn/0cf8f75ab6734ffbb4e29c18d1bd6741.png#pic_center" width = 48%>

ARP（Address Resolution Protocol），地址解析协议，是根据 IP 地址获取物理地址的一个 TCP/IP 协议。主机发送信息时将包含目标 IP 地址的 ARP 请求广播到局域网络上的所有主机，并接收返回消息，以此确定目标的物理地址；收到返回消息后将该 IP 地址和物理地址存入本机 ARP 缓存中并保留一定时间，下次请求时直接查询 ARP 缓存以节约资源
ARP 协议是通过报文工作的，报文格式如下：

<img src ="https://img-blog.csdnimg.cn/09d9155e20d848578a2f10d0ca2b33fd.png#pic_center" width = 48%>

### 2.2 子网外的地址解析

在相同子网内的 ARP 很好理解，那么当子网中的主机要向子网外发送网络层数据报时，ARP 又是怎么工作的呢？对于主机，每台主机只有一个 IP 地址和一个适配器，对于一台路由器来说，每个接口都有一个 IP 地址，也都有一个 ARP 模块和一个适配器。

<img src ="https://img-blog.csdnimg.cn/0e307d09008545a6a182b0339d214bec.png#pic_center" width = 48%>

当一个子网向另一个子网发送 IP 数据报时，发送主机向适配器传递，此时应该传递什么 MAC 地址呢？明显不是目的主机的 MAC 地址，因为在所在子网中该地址与所有的适配器之间都不匹配，那就只好丢弃了。所以适当的 MAC 地址应该是路由器接口的适配器地址，但是路由器接口的 MAC 地址怎么获取？ARP 嘛！
接下来路由器就需要将数据报发到正确的目的地去，也就是要发到哪个接口去呢？可以查询路由器的转发表，根据转发表送到对应的接口去。接口收到数据包之后，适配器把数据报封装到新的帧中，发送到下一个子网去，下一个子网的 MAC 地址怎么确定？再搞个 ARP 就行了！

### 2.3 ARP 代理

如果 ARP 请求是从一个网络上的主机发往另一个网络上的主机，那么连接这两个网络的路由器就可以回答该 ARP 请求，这个过程称作代理 ARP（Proxy ARP）。

当连接这两个网络的路由器收到该 ARP 请求时，它会发现自己有通向目的主机的路径，随后它会将自己（路由器）的 MAC 地址回复给源主机。源主机会认为路由器的 MAC 地址就是目的主机的 MAC 地址，而对于随后发来的数据帧，路由器会转发到它后面真实 MAC 地址的目的主机。

两个物理网络之间的路由器可以使这两个网络彼此透明化，在这种情况下，只要路由器设置成一个 ARP 代理，以响应一个网络到另一个网络主机的 ARP 请求，两个物理网络就可以使用相同的网络号。

### 2.4 ARP 欺骗

从 ARP 代理的原理可以看出来：IP - MAC 的对应信息很容易被伪造！黑客可以伪造 ARP 应答数据帧而欺骗 ARP 请求者，从而达到截获数据的目的。

> RARP 与 ARP 是相反的关系，用于将 MAC 地址转换为 IP 地址。对应于 ARP，RARP 请求以广播方式传送，而 RARP 应答一般是单播传送的。
> 某些设备，比如无盘机在启动时可能不知道自己的 IP 地址，它们可以将自己的 MAC 地址使用 RARP 请求广播出去，RARP 服务器就会响应并回复无盘机的 IP 地址。

## 2 实验分析
### 2.1 以太网帧分析
**实验步骤**

1. 首先，确保浏览器的缓存为空(清除浏览器缓存)，启动 Wireshark 数据包嗅探器。
<img src ="https://img-blog.csdnimg.cn/830e79e422c447a4b7e096a2492b6c8c.png#pic_center" width = 48%>

2. 打开以下 URL “http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html” 您的浏览器应显示一段长文档。

<img src ="https://img-blog.csdnimg.cn/369facea4ec3452e984c530edd31c4c1.png#pic_center" width = 48%>


3. 停止 Wireshark 数据包捕获，找到您向 gaia.cs.umass.edu 的 HTTP GET 消息的数据包编号以及 gaia.cs.umass.edu 相应您的 HTTP 回应。

<img src ="https://img-blog.csdnimg.cn/9d7d5ed1f8044b98badea7fb6aa4f89c.png#pic_center" width = 48%>

干扰巨大，还是看看现成的包吧。

4. 打开实验并且选中分析-启用的协议-把 IPV4 的勾去掉，仅显示有关 IP 以下协议的信息。

<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/c48a3f78319542c19e5b5e1750d61965.png#pic_left" width = "42%"><img src = "https://img-blog.csdnimg.cn/ce26ce0a3cbf4f56859d7efa200152b8.png#pic_left"  width = "50%"></center></p>

5. 选择包含 HTTP GET 消息的以太网帧，在数据包详细信息窗口中展开以太网信息，以太网帧的内容（标题以及有效负载）显示在数据包内容窗口中。

**问题解答**

根据包含 HTTP GET 消息的以太网帧进行分析：

<img src ="https://img-blog.csdnimg.cn/8d1f55e2398a4fc5ac88fb431f9a2abc.png#pic_center" width = 48%>


1. 你的电脑 48 位的地址是多少
答：源地址：AmbitMic_a9:3d:68 (00:d0:59:a9:3d:68)

<img src ="https://img-blog.csdnimg.cn/5cb72e66772d4c13a40895fbf5718a68.png#pic_center" width = 48%>

2. 以太网帧中的 48 位目标地址是什么？这是 gaia.cs.umass.edu 的以太网地址吗？
答：目的地址: LinksysG_da:af:73 (00:06:25:da:af:73)。这个不是 gaia.cs.umass.edu 的以太网地址，这个应该是出子网的路由器的地址。

<img src ="https://img-blog.csdnimg.cn/d75bd3180bfe4e6a8c69ab180a33b526.png#pic_center" width = 48%>


3. 以太网帧上层协议 16 进制值是什么?这对应的上层协议是什么？
答：0x0800，表示上层协议是 IPv4。

<img src ="https://img-blog.csdnimg.cn/f7271397f0c8475482a825ec484bf8d4.png#pic_center" width = 48%>

<img src ="https://img-blog.csdnimg.cn/af0791baf9b3490991ff0e785c39c409.png#pic_center" width = 48%>

4. 从以太帧的开始，一直到“GET”中的 ASCII“G”出现在以太网帧中為止，有多少字节？
答：有 16 × 3 + 6 = 54 Byte

<img src ="https://img-blog.csdnimg.cn/ac538fc5037d4e8ab76415481640d1e2.png#pic_center" width = 48%>

5. 这个帧中，以太网源地址的值是多少？这是你的计算机的地址，还是 gaia.cs.umass.edu 的地址？拥有这个以太网地址的设备是什么？
答：源地址：LinksysG_da:af:73 (00:06:25:da:af:73)，这个应该是出子网的路由器的地址。

<img src ="https://img-blog.csdnimg.cn/b344f173c48f4264b38c590689d6d42b.png#pic_center" width = 48%>


6. 以太网帧中的目的地址是什么？这是您的计算机的以太网地址吗？
答：目的地址：Destination: AmbitMic_a9:3d:68 (00:d0:59:a9:3d:68)，这个是我的计算机的以太网地址。

<img src ="https://img-blog.csdnimg.cn/052875a372764cc38adbdc0d47503ba0.png#pic_center" width = 48%>


7. 以太网帧上层协议 16 进制值是什么?这对应的上层协议是什么？
答：0x0800，表示上层协议是 IPv4。

<img src ="https://img-blog.csdnimg.cn/ced4a733744f41d59d6674349e88fbf3.png#pic_center" width = 48%>

8. 从以太帧的开始，一直到 “OK” 中的 ASCII“O” 出现在以太网帧中为止，有多少字节？
答：有 16 × 4 + 4 = 68 Byte
<img src ="https://img-blog.csdnimg.cn/04ec7a50259540ce97693f52890f45f5.png#pic_center" width = 48%>

### 2.2 地址解析协议

ARP 协议通常在您的计算机上维护 IP 到以太网地址转换对的缓存 .arp 命令（在 MSDOS 和 Linux / Unix 中）用于查看和操作此缓存的内容。 arp 命令用于查看和操作 ARP 缓存内容，而 ARP 协议定义了发送和接收的消息的格式和含义，并定义了对消息传输和接收所采取的操作。
现在查看计算机上 ARP 缓存的内容，没有参数的 Windows arp 命令将显示计算机上 ARP 缓存的内容，运行 ARP 命令。

1. 打开命令提示符显示arp 缓存，`arp -a`

<img src ="https://img-blog.csdnimg.cn/ecf20d8196204c30a2dfdc255611aee1.png#pic_center" width = 48%>

2. 管理员打开命令提示符，清除arp 缓存，`arp -d *`

<img src ="https://img-blog.csdnimg.cn/fb28a58494cc466b98484d4214695d82.png#pic_center" width = 48%>

3. 确保浏览器的缓存是空的，启动 Wireshark 捕捉封包。

4. 打开以下 URL “http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html”，你的浏览器应该再次显示长文档。

5. 同样设置不显示 IP 和更高层协议

**问题解答**

9. 每个列值的含义是什么？
答：按照颜色分别是：网卡、路由 IP 和 MAC 地址、广播地址、组播地址。

<img src ="https://img-blog.csdnimg.cn/d30c909bf4504383be801f88c744e14a.png#pic_center" width = 48%>

10.  包含 ARP 请求消息的以太网帧中源和目标地址的十六进制值是什么？
答：目的地址: Broadcast (ff:ff:ff:ff:ff:ff)；源地址: AmbitMic_a9:3d:68 (00:d0:59:a9:3d:68)

<img src ="https://img-blog.csdnimg.cn/800c8ee51de242fa88a3290a4c5ddbbe.png#pic_center" width = 48%>

11. 以太网帧上层协议 16 进制值是什么?
答：0x0806，表示上层协议是 ARP。
<img src ="https://img-blog.csdnimg.cn/81d9a25e992c4a60ba685b9921c80a27.png#pic_center" width = 48%>


12. 分析 ARP 请求

<img src ="https://img-blog.csdnimg.cn/ca803198273e4a129ad8ab7b396af32f.png#pic_center" width = 48%>

<img src ="https://img-blog.csdnimg.cn/ce86e4228fc94c5ba9671f1ec3a9fc64.png#pic_center" width = 48%>


a) ARP 操作码字段开始从以太网帧的最开始有多少字节？
答：16 + 5 = 21 Byte

<img src ="https://img-blog.csdnimg.cn/405e5f39c5ee4e2aa15d3bc2a90d2cf0.png#pic_center" width = 48%>

b) 在进行 ARP 请求的以太网帧的 ARP 负载部分中，操作码字段的值是多少？
答：操作码的值为 1。见上图

c) ARP 消息是否包含发送方的 IP 地址？
答：ARP 消息包含发送方的 IP 地址。

<img src ="https://img-blog.csdnimg.cn/3505d672d3d645adaaf9a8b41f037372.png#pic_center" width = 48%>

d) 在 ARP 请求中从哪里看出我们要查询相应 IP 的以太网地址?

<img src ="https://img-blog.csdnimg.cn/e547ea3b5fa24dd78d5394c7fb890b1e.png#pic_center" width = 48%>


13. 找到相应 ARP 请求的而发送 ARP 回复。

a) ARP 操作码字段开始从以太网帧的最开始有多少字节？
16 + 5 = 21 Byte
b) 在进行 ARP 响应的以太网帧的 ARP 负载部分中，操作码字段的值是多少？
操作码的值为 2。

<img src ="https://img-blog.csdnimg.cn/5a4bea3328ee46efbc368fc5db6fd833.png#pic_center" width = 48%>

14. 包含 ARP 回复消息的以太网帧中的源地址和目标地址的十六进制值是多少？
答：目的地址: AmbitMic_a9:3d:68 (00:d0:59:a9:3d:68)；源地址: LinksysG_da:af:73 (00:06:25:da:af:73)

<img src ="https://img-blog.csdnimg.cn/208dd0a8f79341af868b01d387b0683f.png#pic_center" width = 48%>


15. 在作者抓包结果中，他有两台电脑，一台运行 wireshark 进行抓包，一台没有，那么为什么运行 wireshark 那台电脑发送 ARP 请求得到了应答，另外一台电脑的 ARP 请求没有得到应答?
答：因为 ARP 查询分组是广播，而响应分组是单播。


____

## 参考
- Ethernet and ARP及Wireshark实验：[https://www.cnblogs.com/linfangnan/p/12867566.html](https://www.cnblogs.com/linfangnan/p/12867566.html)
- ARP(Address Resolution Protocol)地址解析协议：[https://www.lanqiao.cn/courses/98/learning/?id=496&compatibility=false](https://www.lanqiao.cn/courses/98/learning/?id=496&compatibility=false)
- 《计算机网络－自顶向下方法》笔记：[https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)
