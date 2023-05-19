DHCP（Dynamic Host configuration protocol）动态主机配置协议。 它可以为客户机自动分配 IP 地址、子网掩码以及缺省网关、DNS 服务器的 IP 地址等 TCP/IP 参数， 简单来说，就是在 DHCP 服务器上有一个数据库， 存放着 IP 地址、网关、DNS 等参数。 当客户端请求使用时，服务器则负责将相应的参数分配个客户端，避免客户端手动指定 IP 地址等。

工作流程：

<img src ="https://img-blog.csdnimg.cn/092f64088aa54a91ac1ca0381b720c56.png#pic_center" width = 48%>

DHCP 协议采用 UDP 作为传输协议，主机发送请求消息到 DHCP 服务器的 67 号端口，DHCP 服务器回应应答消息给主机的 68 号端口。其交互过程中对应着如下报文：
1. DHCP DISCOVER 报文: 寻找服务器，由 DHCP Client 以广播的方式发出，所有的 DHCP Server 都能够接收到 DHCP Client 发送的 DHCP Discover 报文；
2. DHCP OFFER 报文：所有的 DHCP Server 都会给出响应，向 DHCP Client 发送一个 DHCP Offer 报文。DHCP Offer 报文中Your(Client) IP Address字段就是 DHCP Server 能够提供给 DHCP Client 使用的 IP 地址，且 DHCP Server 会将自己的 IP 地址放在option字段中以便 DHCP Client 区分不同的 DHCP Server。DHCP Server 在发出此报文后会存储一个已分配 IP 地址的纪录。
3. DHCP REQUEST 报文：DHCP Client 只能处理其中的一个 DHCP Offer 报文，一般的原则是 DHCP Client 处理最先收到的 DHCP Offer 报文。DHCP Client 会发出一个广播的 DHCP Request 报文，在选项字段中会加入选中的 DHCP Server 的 IP 地址和需要的 IP 地址。
4. DHCP ACK 报文：DHCP Server 收到 DHCP Request 报文后，判断选项字段中的 IP 地址是否与自己的地址相同。如果不相同，DHCP Server 不做任何处理只清除相应 IP 地址分配记录；如果相同，DHCP Server 就会向 DHCP Client 响应一个 DHCP ACK 报文，并在选项字段中增加 IP 地址的使用租期信息。

另外，DHCP Client 在成功获取 IP 地址后，随时可以通过发送 DHCP Release 报文释放自己的 IP 地址，DHCP Server 收到 DHCP Release 报文后，会回收相应的 IP 地址并重新分配。

**三种地址分配方式**
- 自动分配（ Automatic Allocation ） 自动分配是当 DHCP 客户端第一次成功地从 DHCP 服务器端分配到一个 IP 地址之后，就永远使用这个地址。
- 动态分配（ Dynamic Allocation ） 动态分配是当 DHCP 客户端第一次从 DHCP 服务器分配到 IP 地址后，并非永久地使用该地址，每次使用完后，DHCP 客户端就得释放这个 IP 地址，以给其他客户端使用。
- 手动分配 手动分配是由 DHCP 服务器管理员专门为客户端指定 IP 地址。

**DHCP报文类型**

<img src ="https://img-blog.csdnimg.cn/45eb6e392bd546128fb22e829ca321d2.png#pic_center" width = 48%>

DHCP（ Dynamic Host Configuration Protocol, 动态主机配置协议）通常被用在大型的局域网络中，主要作用是集中管理和分配 IP 地址，使网络中主机动态获得 IP 地址，Gateway 地址，DNS 服务器地址等信息，并能够提升地址的使用率。

DHCP 适用于以下场景：
1. 网络规模大，手工配置需要很大的工作量，并难以对整个网络进行集中管理；
2. 网络中主机数目大于该网络支持的 IP 地址数量，无法给每个主机分配一个固定的 IP 地址；
3. 网络中只有少数主机需要固定的 IP 地址，大多数主机没有固定的 IP 地址需求。

## 1 DHCP协议
### 1.1 动态主机配置协议
DHCP 允许主机自动获取 IP 地址，由于其具有将主机连接到一个网络的网络相关方面的自动能力，因此又被称之为即插即用协议或零配置协议。网络管理员通过对 DHCP 服务器的配置，使得某给定主机每次与网络连接时能得到一个相同地址，或者是被分配一个临时 IP 地址。进行 IP 地址分配之后，DHCP 协议还能够提供子网掩码、默认网关和本地 DNS 服务器地址。

DHCP 协议被广泛应用于住宅因特网接入网、企业网和无线接入网中，这使得主机频繁加入、退出网络变得极其便利。若没有 DHCP 协议的应用，则任何需要临时接入的主机都需要由专人进行 IP 地址分配，而且需要 24 小时都有系统管理员可以提供这种服务，这无疑是开销很大的做法。

<img src ="https://img-blog.csdnimg.cn/d098c8ae7dea4b109e8336759759a8b4.png#pic_center" width = 48%>

### 1.2 DHCP 服务器

DHCP 协议是一个客户-服务器协议，DHCP 服务器用于提供 DHCP 协议的服务，客户是需要接入网络的主机，为了正常地访问互联网，它需要获取 IP 地址及相关网络配置信息。

在最简单的场合下，每个子网都需要部署一台 DHCP 服务器(通常是一台路由器)，若子网中没有 DHCP 服务器，则需要 DHCP 中继代理来提供 DHCP 服务，DHCP 中继代理的任务是存储用于该网络的 DHCP 服务器地址。当 DHCP 中继代理收到 DHCP 发现报文时，就会使用单播的方式向 DHCP 服务器转发该报文，并等待应答，中继代理也同样需要负责转发 DHCP 服务器的应答信息。

<img src ="https://img-blog.csdnimg.cn/2c6c95d409cd4091a20a671474573cb4.png#pic_center" width = 48%>

### 1.3 配置步骤

DHCP 协议的运行过程可以分为 4 个步骤，分别是 DHCP 服务器发现、DHCP 服务器提供、DHCP 请求和 DHCP ACK。

**1. DHCP 服务器发现**

对于需要接入网络的主机，首要任务是发现一个能够为其分配 IP 地址的 DHCP 服务器。要完成这个工作，主机会使用 UDP 协议使用端口 67发送 DHCP 发现报文。

DHCP 发现报文应该如何发送？注意在这个时候主机并不知道所在网络的网络前缀，自然也不知道该网络的 DHCP 服务器的 IP 地址了，因此 DHCP 发现报文将使用广播进行报文发送，仅有 DHCP 服务器可以对 DHCP 发现报文进行回应，此时的目的地址为广播地址 255.255.255.255，而源地址为 0.0.0.0。DHCP 服务器讲吧 IP 数据报传递给链路层，链路层将该帧广播到所有与子网连接的孩子结点。

**2. DHCP 服务器提供**

当 DHCP 服务器收到 DHCP 发现报文时，会现在服务器的数据库中查找计算机的配置信息，若找到则返回找到的信息。若找不到，则服务器将发送一个 DHCP 提供报文为用户做出回应，包括收到的发现报文的事务 ID，向客户推荐的 IP 地址，网络掩码和 IP 地址租用期。此时报文的发送的方式也是使用广播地址 255.255.255.255，使用 68 端口向子网中的所有孩子结点进行广播，为什么此处还是广播？这是因为在子网中，DHCP 服务器可能并不唯一，因此先收到 DHCP 发现报文的 DHCP 服务器可以通过广播的方式告知其它 DHCP 服务器，让它们收回 DHCP 服务。

这里我们稍微讨论下租用期，对于新接入的主机，分配的 IP 地址不能够永久地存在，因为只要该主机移动到另一个网络中，该 IP 地址的滞留将变为额外的开销。在实际情况下，主机在到达租用期的一半时间时，就会向 DHCP 服务器申请延长租用期，若主机因为某些原因没有进行延期申请(例如移动到另一子网)，DHCP 服务器将在租用期到期时收回分配的 IP 地址。注意此时 DHCP 服务器可以拒绝用户的延期，此时将发送 DHCP NACK 报文，此时主机需要重新使用 DHCP 协议申请新的 IP 地址。租用期的设置由 DHCP 服务器自己决定，例如学校的机房可以把租用期设置为一节课的时间。

**3. DHCP 请求**

新到的客户将选择一个 DHCP 服务器，而且此时主机已经知道了 DHCP 服务器的 IP 地址了，因此向选中的 DHCP 服务器发送 DHCP 请求报文进行回应。

**4. DHCP ACK**
服务器使用 DHCP ACK 报文对 DHCP 请求报文进行响应，正是所要求的的参数。当客户收到 DHCP ACK 保温之后，DHCP 协议交互就完成了，此时客户可以在租用期内使用 DHCP 分配的 IP 地址，这种状态被称之为已绑定状态。

<img src ="https://img-blog.csdnimg.cn/713d95ad97684b8594233752bb2b94a0.png#pic_center" width = 48%>

### 1.4 DHCP 协议缺陷

从移动性的角度来看，当结点连接到一个新子网时，要通过 DHCP 协议得到一个新的 IP 地址，而当一个移动节点在子网之间移动时，就不能维持与远程应用之间的 DHCP 连接。因此对于移动 IP，我们需要一种对 IP 基础设施的扩展，允许移动节点在网络之间移动时，也能使用其单一的永久的地址。


### 1.5 报文分析

DHCP 报文一共有 8 种，各种类型报文的基本功能如下：

- Discover（0x01）：DHCP 客户端在请求 IP 地址时，并不知道 DHCP 服务器的位置，因此 DHCP 客户端会在本地网络内以广播方式发送 Discover 请求报文，以发现网络中的 DHCP 服务器。所有收到 Discover 报文的 DHCP 服务器都会发送应答报文，DHCP 客户端据此可以知道网络中存在的 DHCP 服务器的位置。
- Offer（0x02）：DHCP 服务器收到 Discover 报文后，就会在所配置的地址池中，查找一个合适的 IP 地址，加上相应的租约期限和其他配置信息（如网关、DNS 服务器等），构造一个 Offer 报文，发送给 DHCP 客户端，告知用户本服务器可以为其提供 IP 地址。但这个报文只是告诉 DHCP 客户端可以提供 IP 地址，最终还需要客户端通过 ARP 来检测该 IP 地址是否重复。
- Request（0x03）：DHCP 客户端可能会收到很多 Offer 请求报文，所以必须在这些应答中选择一个。通常是选择第一个 Offer 应答报文的服务器作为自己的目标服务器，并向该服务器发送一个广播的 Request 请求报文，通告选择的服务器，希望获得所分配的 IP 地址。另外，DHCP 客户端在成功获取 IP 地址后，在地址使用租期达到 50% 时，会向 DHCP 服务器发送单播 Request 请求报文请求续延租约，如果没有收到 ACK 报文，在租期达到 87.5% 时，会再次发送广播的 Request 请求报文以请求续延租约。
- ACK（0x05）：DHCP 服务器收到 Request 请求报文后，根据 Request 报文中携带的用户 MAC 来查找有没有相应的租约记录，如果有则发送 ACK 应答报文，通知用户可以使用分配的 IP 地址。
- NAK（0x06）：如果 DHCP 服务器收到 Request 请求报文后，没有发现有相应的租约记录或者由于某些原因无法正常分配 IP 地址，则向 DHCP 客户端发送 NAK 应答报文，通知用户无法分配合适的 IP 地址。
- Release（0x07）：当 DHCP 客户端不再需要使用分配 IP 地址时（一般出现在客户端关机、下线等状况）就会主动向 DHCP 服务器发送 RELEASE 请求报文，告知服务器用户不再需要分配 IP 地址，请求 DHCP 服务器释放对应的 IP 地址。
- Decline（0x04）：DHCP 客户端收到 DHCP 服务器 ACK 应答报文后，通过地址冲突检测发现服务器分配的地址冲突或者由于其他原因导致不能使用，则会向 DHCP 服务器发送 Decline 请求报文，通知服务器所分配的 IP 地址不可用，以期获得新的 IP 地址。
- Inform（0x08）：DHCP 客户端如果需要从 DHCP 服务器端获取更为详细的配置信息，则向 DHCP 服务器发送 Inform 请求报文；DHCP 服务器在收到该报文后，将根据租约进行查找到相应的配置信息后，向 DHCP 客户端发送 ACK 应答报文。目前基本上不用了。

DHCP报文格式如下：

<img src ="https://img-blog.csdnimg.cn/067b9d9d20a44e47ae2dd7bc86edde28.png#pic_center" width = 48%>

各字段说明如下：
- OP：报文的操作类型。分为请求报文和响应报文。1：请求报文，2：应答报文。即 client 送给 server 的封包，设为 1，反之为 2。
- 请求报文：DHCP Discover、DHCP Request、DHCP Release、DHCP Inform 和 DHCP Decline。
- 应答报文：DHCP Offer、DHCP ACK 和 DHCP NAK。
- Htype：DHCP 客户端的 MAC 地址类型。MAC 地址类型其实是指明网络类型。Htype 值为 1 时表示为最常见的以太网 MAC 地址类型。
- Hlen：DHCP 客户端的 MAC 地址长度。以太网 MAC 地址长度为 6 个字节，即以太网时 Hlen 值为 6。
- Hops：DHCP 报文经过的 DHCP 中继的数目，默认为 0。DHCP 请求报文每经过一个 DHCP 中继，该字段就会增加 1。没有经过 DHCP 中继时值为 0(若数据包需经过 router 传送，每站加 1，若在同一网内，为 0)。
- Xid：客户端通过 DHCP Discover 报文发起一次 IP 地址请求时选择的随机数，相当于请求标识。用来标识一次 IP 地址请求过程。在一次请求中所有报文的 Xid 都是一样的。
- Secs：DHCP 客户端从获取到 IP 地址或者续约过程开始到现在所消耗的时间，以秒为单位。在没有获得 IP 地址前该字段始终为 0(DHCP 客户端开始 DHCP 请求后所经过的时间。目前尚未使用，固定为 0)。
- Flags：标志位，只使用第 0 比特位，是广播应答标识位，用来标识 DHCP 服务器应答报文是采用单播还是广播发送，0 表示采用单播发送方式，1 表示采用广播发送方式。其余位尚未使用(即从 0-15 bits，最左 1 bit 为 1 时表示 server 将以广播方式传送封包给 client)。

注意：在客户端正式分配了 IP 地址之前的第一次 IP 地址请求过程中，所有 DHCP 报文都是以广播方式发送的，包括客户端发送的 DHCP Discover 和 DHCP Request 报文，以及 DHCP 服务器发送的 DHCP Offer、DHCP ACK 和 DHCP NAK 报文。当然，如果是由 DHCP 中继器转的报文，则都是以单播方式发送的。另外，IP 地址续约、IP 地址释放的相关报文都是采用单播方式进行发送的。
- Ciaddr：DHCP 客户端的 IP 地址。仅在 DHCP 服务器发送的 ACK 报文中显示，因为在得到 DHCP 服务器确认前，DHCP 客户端是还没有分配到 IP 地址的。在其他报文中均显示，只有客户端是 Bound、Renew、Rebinding 状态，并且能响应 ARP 请求时，才能被填充。
- Yiaddr：DHCP 服务器分配给客户端的 IP 地址。仅在 DHCP 服务器发送的 Offer 和 ACK 报文中显示，其他报文中显示为 0。
- Siaddr：下一个为 DHCP 客户端分配 IP 地址等信息的 DHCP 服务器 IP 地址。仅在 DHCP Offer、DHCP ACK 报文中显示，其他报文中显示为 0。(用于 bootstrap 过程中的 IP 地址)

一般来说是服务器的 IP 地址。但是注意！根据 openwrt 源码给出的注释，当报文的源地址、Siaddr、option­>server_id 字段不一致（有经过跨子网转发）时，通常认为 option­>srever_id 字段为真正的服务器 IP，Siaddr 有可能是多次路由跳转中的某一个路由的 IP。
- Giaddr：DHCP 客户端发出请求报文后经过的第一个 DHCP 中继的 IP 地址。如果没有经过 DHCP 中继，则显示为 0。(转发代理（网关）IP地址)
- Chaddr：DHCP 客户端的 MAC 地址。在每个报文中都会显示对应 DHCP 客户端的 MAC 地址
- Sname：为 DHCP 客户端分配 IP 地址的 DHCP 服务器名称（DNS 域名格式）。在 Offer 和 ACK 报文中显示发送报文的 DHCP 服务器名称，其他报文显示为 0。
- File：DHCP 服务器为 DHCP 客户端指定的启动配置文件名称及路径信息。仅在 DHCP Offer 报文中显示，其他报文中显示为空。
- Options：可选项字段，长度可变，格式为代码 + 长度 + 数据。

<table>
<thead>
<tr>
<th>代码</th>
<th>长度/字节</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>4</td>
<td>子网掩码</td>
</tr>
<tr>
<td>3</td>
<td>长度可变，必须是 4 字节的倍数</td>
<td>默认网关（可以是一个路由器 IP 地址列表）</td>
</tr>
<tr>
<td>6</td>
<td>长度可变，必须是 4 字节的倍数</td>
<td>DNS 服务器（可以是一个 DNS 服务器 IP 地址列表）</td>
</tr>
<tr>
<td>15</td>
<td>长度可变</td>
<td>域名称（主 DNS 服务器名称）</td>
</tr>
<tr>
<td>42</td>
<td>长度可变，必须是 4 字节的倍数</td>
<td>NTP 服务器（可以是一个 NTP 服务器 IP 地址列表）</td>
</tr>
<tr>
<td>44</td>
<td>长度可变，必须是 4 字节的倍数</td>
<td>WINS 服务器（可以是一个 WINS 服务器 IP 地址列表）</td>
</tr>
<tr>
<td>51</td>
<td>4</td>
<td>有效租约期（以秒为单位）</td>
</tr>
<tr>
<td>53</td>
<td>1</td>
<td>报文类型（1 ~ 8）分别表示：Discover，Offer，Request，Decline，ACK，NAK，Release，Inform</td>
</tr>
<tr>
<td>58</td>
<td>4</td>
<td>续约时间</td>
</tr>
<tr>
<td>60</td>
<td>长度可变</td>
<td>Authentication for DHCP Message，用来完成基于标准DHCP协议，以在客户端输入用户名和密码的方式进行地址鉴权主要用在按用户认证收费场合，与之对应的是pppoe认证计费</td>
</tr>
<tr>
<td>255</td>
<td>0</td>
<td>标记 Options 结束</td>
</tr>
</tbody></table>


**1. DHCP Discover数据包**

<img src ="https://img-blog.csdnimg.cn/5842758fb0424367867f67d3fa9cf2fb.png#pic_center" width = 48%>

**2. DHCP Offer数据包**
当 DHCP 服务器收到一条 DHCP Discover 数据包时，用一个 DHCP Offerr 包给予客户端响应：

<img src ="https://img-blog.csdnimg.cn/16a115c453d9450a8f5d3663b4c514b2.png#pic_center" width = 48%>

发送 DHCP Offer 消息的 DHCP 服务器 IP 是172.31.159.254，如下截图：

<img src ="https://img-blog.csdnimg.cn/bd5004c51a68475c8bcf929413dd5594.png#pic_center" width = 48%>

**3. DHCP Request包**

当 Client 收到了 DHCP Offer 包以后，确认有可以和它交互的 DHCP 服务器存在，于是 Client 发送 Request 数据包，请求分配 IP。此时的源 IP 和目的 IP 依然是0.0.0.0和255.255.255.255。



**4. DHCP ACK包**

服务器用 DHCP ACK 包对 DHCP 请求进行响应：

<img src ="https://img-blog.csdnimg.cn/a406c8e206864fd5a6bd7ffe0c74882b.png#pic_center" width = 48%>

其中服务器发送给客户端的关于此地址的配置信息：

<img src ="https://img-blog.csdnimg.cn/b97eee9dfc5d4d13ae77410aa796b526.png#pic_center" width = 48%>


## 2 DHCP 服务器配置

这里以[《VLAN 单臂路由》](https://www.educoder.net/shixuns/l6caes5u/challenges)实训为基础，使用 [GNS3](https://blog.csdn.net/zhangpeterx/article/details/86407065) 模拟组建由两台 PC 、一台交换机以及一台路由器构成的简单网络，并通过相关配置实现 DHCP 功能。通过本实训，你将掌握：

（1）DHCP 分发 IP 的优缺点；
（2）如何配置 DHCP 服务；
（3）如何通过 DHCP 分发给 PC 机 IP 地址。

### 2.1 搭建网络拓扑图

**1. 创建工程文件**
创建名为 `fifth` 的工程，选择保存路径，点击 OK 

<img src ="https://img-blog.csdnimg.cn/dd04164a069a49a49ba1f24610c5f91a.png#pic_center" width = 48%>

**2. 添加设备并连接**

添加一台交换机，一台路由器，两台 PC 机：
路由器使用 C3600 ，交换机使用 C3600 模拟，PC 机使用 VPCS 。
（1）模拟交换机：
首先添加一台 C3600 路由器

<img src ="https://img-blog.csdnimg.cn/a15a821942df4e0f9d04e8d191dd887c.png#pic_center" width = 48%>

右键选择 configure ，点击，界面如下：

<img src ="https://img-blog.csdnimg.cn/329db60132534038ac6218aeb2b04794.png#pic_center" width = 48%>

选择 slots ，选择 slot1 下拉菜单添加 NM-16ESW ，点击 apply 后再点击 OK 。
再次点击路由器右键选择 change symbol ：

<img src ="https://img-blog.csdnimg.cn/3ddb1709a82f4a86b726342f64559219.png#pic_center" width = 48%>

选择 classic ，选择 ethernet_switch ，点击 apply 后再点击 OK :

<img src ="https://img-blog.csdnimg.cn/6d06a84b18124c85a55244607e51d9f1.png#pic_center" width = 48%>

此时 R2 路由器的图标变成了交换机的图标：

<img src ="https://img-blog.csdnimg.cn/2cc9bbb9d395452987dcb079dcc69c06.png#pic_center" width = 48%>

右键选择 change hostname ，修改为 SW1 ：

<img src ="https://img-blog.csdnimg.cn/0aadebe7729f4c7f8913c3a92b0fd01e.png#pic_center" width = 48%>

（2）完整创建拓扑，并开启设备：

<img src ="https://img-blog.csdnimg.cn/ce0d172096ed4e9e8015fa604882fce5.png#pic_center" width = 48%>

### 2.2 access口配置

**1. 创建 vlan**
打开交换机 SW1 的控制台，在特权模式下先使用 vlan database ，然后创建 vlan 10 和 vlan 20 ：

<img src ="https://img-blog.csdnimg.cn/0fcb8dee8a4342288468ae7f4c91b474.png#pic_center" width = 48%>

GNS3 创建 vlan 和平时大家在其他模拟平台上创建 vlan 方式不一样，这一点注意，GNS3 上无法在全局模式下创建 vlan 。并且在 GNS3 查看 vlan 信息也是不一样的，平常都是 show vlan 或者 show vlan brief 就可以查看 vlan 信息了，但是在 GNS3 要使用 show vlan-switch 来查看 vlan 信息。

<img src ="https://img-blog.csdnimg.cn/95aa90b9b2c844a09cb1f7729fff99b3.png#pic_center" width = 48%>

**2. vlan划分**
vlan 的划分有很多种方式：
1. 基于端口划分 vlan
2. 基于MAC地址划分 vlan
3. 基于子网划分 vlan
4. 基于协议划分 vlan
5. 基于策略划分 vlan

这里我们使用第一种方式划分 vlan ，这也是最简单，也是最常用的一种 vlan 划分方式。
SW1 交换机连接到电脑的接口配置为 access 口，并且允许需要通过的 VLAN ID 号。

```python
SW1(config)#interface fastEthernet 1/1　　# 进入到接口 1/1
SW1(config-if)#switchport mode access　　# 配置接口为 access 口
SW1(config-if)#switchport access vlan 10　　# 配置接口允许的 vlan10
SW1(config-if)#exit　　# 退出接口 1/1
SW1(config)#interface fastEthernet 1/2　　# 进入到接口 2/1
SW1(config-if)#switchport mode access　　# 配置接口为 access 口
SW1(config-if)#switchport access vlan 20　　# 配置接口允许的 vlan20
SW1(config-if)#exit　　# 退出接口 1/2
```

<img src ="https://img-blog.csdnimg.cn/e1e67edef9e743d79b8c6d735c186c74.png#pic_center" width = 48%>


### 2.3 trunk口配置

在全局模式下：

<img src ="https://img-blog.csdnimg.cn/df11207a0f41442fa419c61381224535.png#pic_center" width = 48%>

### 2.4 配置路由器子接口

R1 的接口 F0/0 上创建两个子接口，分别是 F0/0.10 对应的 vlan10、F0/0.20 对应的 vlan20 ，每个子接口必须封装 dot1Q 协议，并且标记相应的 vlan id 号，dot1Q 协议主要是标记 vlan 的 id 号，每个子接口必须配置 ip 地址，而且该接口的 ip 地址必须和相应的 vlan 的在同一个网段。

在配置子接口之前要记得打开物理接口，也就是这里与交换机相连的 f0/0 接口。
具体子接口配置如下：

```python
R1(config)#interface fastEthernet 0/0.10　　# 进入到 F0/0.10 接口
R1(config)#no shut
R1(config-subif)#encapsulation dot1Q 10 　　# 将 vlan10 封装在 F0/0.10 接口
R1(config-subif)#ip address 10.0.0.254 255.255.255.0　　# 配置接口的 ip 地址，该 ip 地址作为 vlan10 内的电脑的网关
R1(config-subif)#exit　　# 退出 F0/0.10 接口
R1(config)#interface fastEthernet 0/0.20　　# 进入到 F0/0.20 接口
R1(config)#no shut
R1(config-subif)#encapsulation dot1Q 20　　# 将 vlan20 封装在 F0/0.20 接口
R1(config-subif)#ip address 20.0.0.254 255.255.255.0　　# 配置 ip 地址，该 ip 地址作为 vlan20 内的电脑的网关
```
<img src ="https://img-blog.csdnimg.cn/ff589d4d509949c8a93181b36ba33140.png#pic_center" width = 48%>

### 2.5 配置DHCP服务

```python
R1(config)#service dhcp  //打开 DHCP 服务
R1(config)#ip dhcp pool vlan10 //创建一个 VLAN 10 的地址池
R1(dhcp-config)#default-router 10.0.0.254 //设置分配给子网的网关
R1(dhcp-config)#network 10.0.0.0 255.255.255.0 //设置可分配的子网地址段
R1(dhcp-config)#exit    //返回上一级
R1(config)#ip dhcp pool vlan20
R1(dhcp-config)#default-router 20.0.0.254
R1(dhcp-config)#network 20.0.0.0 255.255.255.0
R1(dhcp-config)#exit
R1(config)#ip dhcp excluded-address 20.0.0.254 //该地址不分配出去，因为子网的网关我们设置了这个地址
R1(config)#ip dhcp excluded-address 10.0.0.254
```

<img src ="https://img-blog.csdnimg.cn/372414764be94828a7a65ad31a0ee149.png#pic_center" width = 48%>


### 2.6 PC机获取IP

获取IP地址
PC1:
<img src ="https://img-blog.csdnimg.cn/822758998f564ac290522588b7927754.png#pic_center" width = 48%>

PC2:
<img src ="https://img-blog.csdnimg.cn/951d380aad864528ac58d0630c62fa53.png#pic_center" width = 48%>

### 2.7 小结

**DHCP 优点：**
1. 提供安全而可靠的配置。DHCP 避免了由于需要手动在每个计算机上配置而引起的配置错误。DHCP 还有助于防止由于在网络上配置新的计算机时重用以前指派的 IP 地址而引起的地址冲突；
2. 可以减少配置管理。使用 DHCP 服务器可以大大降低用于配置和重新配置网上计算机的时间。可以配置服务器以便在指派地址租约时提供其他配置值的全部范围。这些值是使用 DHCP 选项指派的；
3. DHCP 租约续订过程还有助于确保客户端计算机配置需要经常更新的情况(如使用移动或便携式计算机频繁更改位置的用户)，通过客户端计算机直接与 DHCP 服务器通讯可以高效、自动地进行这些更改；
4. IP 地址采用租用方式,需要时向 DHCP 服务器申请 IP ，用完后释放,使 IP 地址可以再利用；
5. DHCP 服务器数据库是一个动态数据库,向客户端提供租约或释放租约时会自动更新,降低了管理 IP 地址的难度，所有 DHCP 客户的设置和变更都由客户端和服务器自动完成，不需人工干涉。

**DHCP 缺点：**
1. DHCP 不能发现网络上非 DHCP 客户端已经在使用的 IP 地址；
2. DHCP 服务器对于用户的接入没有限制，任何一台电脑只要连接到网络上,就能够通过 DHCP 服务器获得正确的网络配置，从而访问网络。这样使得非法的用户很容易进入内部网络，带来安全隐患；
3. 当网络上存在多个 DHCP 服务器时，尤其是存在私设的冒充 DHCP 服务器时，一个 DHCP 服务器不能查出已被其它服务器租出去的 IP 地址，这样将会给网络造成混乱；
4. 如果用户在不同网段的 WLAN 之间不间断使用网络时，IP 地址的改变会造成应用中断。

## 3 实验分析
### 3.1 实验步骤
1. 打开命令提示符，输入 `ipconfig /release` 释放当前的IP

<img src ="https://img-blog.csdnimg.cn/f9a6e19ddae7484eb4c5501b21ba1684.png#pic_center" width = 48%>

2. 打开 wireshark 进行抓包
   
<img src ="https://img-blog.csdnimg.cn/dcac20dadb194a3eafdb4df2a46b574c.png#pic_center" width = 48%>

3. 命令提示符输入 `ipconfig /renew` 重新获取一个IP
4. 命令提示符再次输入 `ipconfig /renew`
5. 再次输入 `ipconfig /release` 释放当前的IP
6. 最后输入 `ipconfig /renew` 重新获取一个IP
7. 停止抓包并且分析实验结果


### 3.2 实验结果

1. DHCP 消息是通过UDP 还是TCP 发送的？
答：所有的DHCP 消息都是UDP 发送的

<img src ="https://img-blog.csdnimg.cn/c2656e69bbd542048c4a2a9bd46f33e3.png#pic_center" width = 48%>

2. 绘制时间流图形。说明客户端和服务器之间第一次四个DHCP 发现，DHCP 提供，DHCP请求以及DHCP 响应的顺序，说明您的结果中对于每个数据包，指示源和目标端口号是否与本实验分配中给出的示例相同？
答：第一次 DHCP 四次信息中，我电脑广播DHCP 发现请求（发现请求中允许服务器
单播回复，其中还包括我网卡 MAC 地址）；服务器广播 DHCP 提供从 IP 池给我分配
一个空闲的 IP 地址给我（但仍未确认使用）；然后我电脑又广播请求使用这个 IP 地址
（同样请求中允许服务器单播回复，其中仍然包括我的网卡 MAC 地址），服务又以广
播发送 DHCP 响应给我确认，这才完成IP 的自动分配。从图中可以看出我电脑DHCP
发现和 DHCP 请求都是68 端口发出，而服务器DHCP 提供和 DHCP 响应都是 67 端口
发出。

<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/f066f773240e4fbfabe8f6e3bbbdb14c.png#pic_left" width = "42%"><img src = "https://img-blog.csdnimg.cn/a3c85c5b086647cbab5ff9e98f315dd0.png#pic_left"  width = "50%"></center></p>

3. 主机的链路层（例如以太网）地址是什么？
答：00:08:74:4f:36:23，截图在上面。

4. DHCP 发现消息中的哪些值将此消息与 DHCP 请求消息区不同？
答：有三处不同。首先是 DHCP 选项 53 不同，一个是DHCP 发现，一个是DHCP 请求。然后DHCP 请求还比 DHCP 发现多了两个选项：54 DHCP 服务器标识-DHCP服务器的信息。

<img src ="https://img-blog.csdnimg.cn/a02a79c6c6664101945cfbc054ea0501.png#pic_center" width = 48%>

5. 第一次四个DHCP 发现，DHCP 提供，DHCP 请求以及DHCP 响应的Transaction-ID 值是多少？Transaction-ID 字段目的是什么。
答: 都是0x3e5e0ce3，这是个随机生成的值，当客户端请求和服务器一样使才会认为有效，这是一个安全性保证的措施。

<img src ="https://img-blog.csdnimg.cn/bf2e3cbde3404f2f85554bb795a055d2.png#pic_center" width = 48%>

6. 主机使用DHCP 获取IP 地址。主机在DHCP 的4 次问询和回答之后获取了地址。请问如果在这4 次DHCP 问询和回答中，如果主机没有IP 地址，那么IP 数据报的值是什么？请分别指出这4 个DHCP 的消息IP 数据报源头和目标IP。
答: 主机如果没有IP 地址， IP 数据报的值是0.0.0.0 ， 目的地址广播地址255.255.255.255。

<img src ="https://img-blog.csdnimg.cn/cc59bd1e6b4f4a97baf761644d0bd148.png#pic_center" width = 48%>


7. 您的DHCP 服务器的IP 地址是多少？
答：192.1681.1，截图如上

8. 发送DHCP Offer 消息的DHCP 服务器IP 是什么，指示哪条DHCP 消息包含提供的DHCP
地址。
答：就是我的 DHCP 的 IP 192.168.1.1，这条消息中也包含给我分配的IP。

<img src ="https://img-blog.csdnimg.cn/ad7463202a65409a84b5855eb0edc773.png#pic_center" width = 48%>


9. 在作者的例子中，主机和 DHCP 服务器之间没有中继代理。跟踪中的哪些值表明没有中
继代理？您的实验中是否有中继代理？如果是这样，代理的 IP 地址是什么？
答：查询下英文版维基百科，发现中继代理也是通过 DHCP 选项实现的。

<img src ="https://img-blog.csdnimg.cn/cfb163ffe4564a20a6733cfc36a5a936.png#pic_center" width = 48%>

DHCP 中续代理意义是，我们可以不在每个子网域配置多个 DHCP 服务器进行 DHCP 服务提供，而仅仅设置一台 DHCP 服务器，这样每个子网域路由当接受到客户端的 DHCP 请求时会自动转发请求给 DHCP 服务器完成服务。

10. 解释 DHCP offer 消息中路由器和子网掩码字段的用途。
答: 由上问可知路由器就起到了中续代理作用，而子网掩码就是区分该网段，可以得知相同网段的电脑 IP 范围，默认网关（路由地址）。

11. 在作者提供的抓包结果中，DHCP 服务器会向作者提供特定的 IP 地址。请问客户端接受使用是否对第一个提供 DHCP offer 消息的DHCP 地址？客户端的响应（DHCP 请求中）哪里是它所要求的地址。
答：DHCP 服务器会向作者提供地址供选择，而作者的电脑则使用了这个IP。

<img src ="https://img-blog.csdnimg.cn/263fd675820142a0b95e179bae36cf46.png#pic_center" width = 48%>

12. 解释租约时间的目的。 您的实验中的租约时间有多长？
答: 如图所示 86400s （1 天）

<img src ="https://img-blog.csdnimg.cn/ce2d36e2ae8e4a7bb89d124a9e730a63.png#pic_center" width = 48%>


13. DHCP 释放消息的目的是什么？DHCP 服务器是否发出收到客户端 DHCP 释放请求的确认。如果客户端的 DHCP 释放消息丢了会发生什么。
答：客户端用来发出释放该IP 不再租用的信息。如图服务器并没有发出DHCP 释放请求的确认，而是直接收回了IP；如果客户端的DHCP 释放消息丢了，猜测就会继续使用这个IP 判断是否到达租用时间，以及是否续订。

<img src ="https://img-blog.csdnimg.cn/5094c3ce8e4c44e698b683801efc8b43.png#pic_center" width = 48%>

14. 从 Wireshark 窗口中清除 bootp 过滤器。 在 DHCP 数据包交换期间是否发送或接
收了任何 ARP 数据包？ 如果接收到了，请说明这些 ARP 数据包的用途。
答: 在 DHCP 获取 IP 后同样发送了 ARP 广播消息用来获取路由的 MAC 地址并且到本机的 ARP 缓存表，用以网络传输。

<img src ="https://img-blog.csdnimg.cn/371335b167f54105967fe74013b2b1f7.png#pic_center" width = 48%>


________

## 参考
- 网络层——DHCP协议：[https://www.cnblogs.com/linfangnan/p/13234489.html](https://www.cnblogs.com/linfangnan/p/13234489.html)
- 《计算机网络－自顶向下方法》笔记：[https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)
