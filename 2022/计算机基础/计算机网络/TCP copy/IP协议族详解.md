&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCP/IP不是一个协议，而是一个协议族的统称。里面包括IP协议、IMCP协议、TCP协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCP/IP协议模型，包含了一系列构成互联网基础的网络协议，是Internet的核心协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;基于TCP/IP的参考模型将协议分成四个层次，它们分别是链路层、网络层、传输层和应用层。下图表示TCP/IP模型与OSI模型各层的对照关系。

<img src ="https://img-blog.csdnimg.cn/110fa8495eb14f44934e3e6e71b6912d.png#pic_center" width = 48%>

**1) 网络接口层**
        主要是指物理层次的一些接口，比如电缆等。

**2) 网络层**
        提供独立于硬件的逻辑寻址，实现物理地址与逻辑地址的转换。
        在 TCP / IP 协议族中，网络层协议包括 IP 协议（网际协议），ICMP 协议（ Internet 互联网控制报文协议），以及 IGMP 协议（ Internet 组管理协议）。

**3) 传输层**
        为网络提供了流量控制，错误控制和确认服务。
        在 TCP / IP 协议族中有两个互不相同的传输协议：TCP（传输控制协议）和 UDP（用户数据报协议）。

**4) 应用层**
        为网络排错，文件传输，远程控制和 Internet 操作提供具体的应用程序

<p><strong><font color=#9900CC>重要协议：<ul>
<li>http (文本传输协议  当我们访问网页时使用的是http协议)  https 动态网页数据传输</li>
<li>  ftp  (文件传输协议  专门用于文件传输) </li>
<li>dhcp (自动ip地址分配协议   网络中要有一个dhcp服务器(路由器)) </li>
<li>   dns  (实现了域名到ip地址的解析)    ip地址    域名(www.qq.com) </li>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;实际网络之间通信用的是ip地址<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns服务器记录了常用的ip地址和域名的对应关系<li>icmp (ping 命令通过icmp协议发送出去的、装载错误报文信息) </li></ul></font> </strong></p>

```html
容易碰到的笔试面试题
        1) tcp/ip有哪几层
                应用层、传输层、网络层、网络接口层
        2) 传输层有哪些协议
                tcp   udp    icmp
        3) 应用层有哪些协议
                http  ftp  dns  dhcp
        4) 请描述同一网段下主机A ping 主机B的全过程   (百度)
                同一网段下   没用到dns
                ping 192.168.1.100(不知道对方的网卡地址 MAC   MAC地址：每一个网卡有一个唯一地址(物理地址))    
                如何得到对方MAC地址(用arp协议)
                1) A发送一个ARP广播包，询问192.168.1.100的MAC地址是多少
                2) B回送ARP包，包中携带自己的MAC地址(00 50 A9 90 88 07)    
                3) A记录ip地址，ARP表中(以后不用发送广播包)（可以不写）
                4) A 发送一个icmp报文给B
                5) B收到回送一个icmp报文    
```
____

## 1 网络层
### 1.1 IP协议

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IP协议是TCP/IP协议的核心，所有的TCP，UDP，IMCP，IGMP的数据都以IP数据格式传输。要注意的是，IP不是可靠的协议，这是说，IP协议没有提供一种数据未传达以后的处理机制，这被认为是上层协议：TCP或UDP要做的事情。

#### 1.1.1 IP地址
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在数据链路层中我们一般通过MAC地址来识别不同的节点，而在IP层我们也要有一个类似的地址标识，这就是IP地址。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32位IP地址分为网络位和地址位，这样做可以减少路由器中路由表记录的数目，有了网络地址，就可以限定拥有相同网络地址的终端都在同一个范围内，那么路由表只需要维护一条这个网络地址的方向，就可以找到相应的这些终端了。

-  A类IP地址: 0.0.0.0~127.255.255.255    IP 地址的前 8 位代表网络 ID ，后 24 位代表主机 ＩＤ。
- B类IP地址:128.0.0.0~191.255.255.255   IP 地址的前 16 位代表网络 ID ，后 16 位代表主机 ＩＤ。
- C类IP地址:192.0.0.0~239.255.255.255

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;全是 0 的主机 ID 代表网络本身，比如说 IP 地址为 130.100.0.0 指的是网络 ID 为130.100 的 B 类地址。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;全是 1 的主机 ID 代表广播，是用于向该网络中的全部主机方法消息的。 IP 地址为 130.100.255.255 就是网络 ID 为 130.100 网络的广播地址（二进制 IP 地址中全是 1 ，转换为十进制就是 255 ）

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;以十进制 127 开头的地址都是环回地址。目的地址是环回地址的消息，其实是由本地发送和接收的。主要是用于测试 TCP/IP 软件是否正常工作。我们用 ping 功能的时候，一般用的环回地址是 127.0.0.1

#### 1.1.2 IP协议头
<img src ="https://img-blog.csdnimg.cn/22bbd2e30bba4ebf956480e1959ddf72.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这里只介绍:八位的TTL字段。这个字段规定该数据包在穿过多少个路由之后才会被抛弃。某个IP数据包每穿过一个路由器，该数据包的TTL数值就会减少1，当该数据包的TTL成为零，它就会被自动抛弃。
这个字段的最大值也就是255，也就是说一个协议包也就在路由器里面穿行255次就会被抛弃了，根据系统的不同，这个数字也不一样，一般是32或者是64


### 1.2 ARP及RARP协议
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ARP 是根据IP地址获取MAC地址的一种协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ARP（地址解析）协议是一种解析协议，本来主机是完全不知道这个IP对应的是哪个主机的哪个接口，当主机要发送一个IP包的时候，会首先查一下自己的ARP高速缓存（就是一个IP-MAC地址对应表缓存）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果查询的IP－MAC值对不存在，那么主机就向网络发送一个ARP协议广播包，这个广播包里面就有待查询的IP地址，而直接收到这份广播的包的所有主机都会查询自己的IP地址，如果收到广播包的某一个主机发现自己符合条件，那么就准备好一个包含自己的MAC地址的ARP包传送给发送ARP广播的主机。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而广播主机拿到ARP包后会更新自己的ARP缓存（就是存放IP-MAC对应表的地方）。发送广播的主机就会用新的ARP缓存数据准备好数据链路层的的数据包发送工作。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RARP协议的工作与此相反，不做赘述。


### 1.3 ICMP协议
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IP协议并不是一个可靠的协议，它不保证数据被送达，那么，自然的，保证数据送达的工作应该由其他的模块来完成。其中一个重要的模块就是ICMP(网络控制报文)协议。ICMP不是高层协议，而是IP层的协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当传送IP数据包发生错误。比如主机不可达，路由不可达等等，ICMP协议将会把错误信息封包，然后传送回给主机。给主机一个处理错误的机会，这也就是为什么说建立在IP层以上的协议是可能做到安全的原因。

____

## 2 传输层
### 2.1 TCP和UDP协议
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCP/UDP都是是传输层协议，但是两者具有不同的特性，同时也具有不同的应用场景，下面以图表的形式对比分析。

<img src ="https://img-blog.csdnimg.cn/ca11eb0302d149bba620344d57925414.png#pic_center" width = 48%>


**面向报文(UDP)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;面向报文的传输方式是应用层交给UDP多长的报文，UDP就照样发送，即一次发送一个报文数据---大小有限制（64k）。因此，应用程序必须选择合适大小的报文。若报文太长，则IP层需要分片，降低效率。若太短，会是IP太小。

**面向字节流(TCP)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;面向字节流的话，虽然应用程序和TCP的交互是一次一个数据块（大小不等），但TCP把应用程序看成是一连串的无结构的字节流。TCP有一个缓冲，当应用程序传送的数据块太长，TCP就可以把它划分短一些再传送。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;关于拥塞控制，流量控制，是TCP的重点，后面讲解。

### 2.2 TCP和UDP协议的一些应用
<img src ="https://img-blog.csdnimg.cn/ed357e6d8e39413f84df339b028a0d11.png#pic_center" width = 48%>

**什么时候应该使用TCP？**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当对网络通讯质量有要求的时候，比如：整个数据要准确无误的传递给对方，这往往用于一些要求可靠的应用，比如HTTP、HTTPS、FTP等传输文件的协议，POP、SMTP等邮件传输的协议。

**什么时候应该使用UDP？**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当对网络通讯质量要求不高的时候，要求网络通讯速度能尽量的快，这时就可以使用UDP。

____

## 3 TCP“三次握手”和“四次挥手”

### 3.1 三次握手
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCP是面向连接的，无论哪一方向另一方发送数据之前，都必须先在双方之间建立一条连接。在TCP/IP协议中，TCP协议提供可靠的连接服务，连接是通过三次握手进行初始化的。<font color=#9900CC><strong>三次握手的目的是同步连接双方的序列号和确认号并交换 TCP窗口大小信息。</font></strong>

<img src ="https://img-blog.csdnimg.cn/edff57c0019b421ca397a7be46c99850.png#pic_center" width = 48%>

 1. 第一次握手： 建立连接。客户端发送连接请求报文段，将SYN位置为1，Sequence Number为x；然后，客户端进入SYN_SEND状态，等待服务器的确认；
2. 第二次握手： 服务器收到SYN报文段。服务器收到客户端的SYN报文段，需要对这个SYN报文段进行确认，设置Acknowledgment Number为x+1(Sequence Number+1)；同时，自己自己还要发送SYN请求信息，将SYN位置为1，Sequence Number为y；服务器端将上述所有信息放到一个报文段（即SYN+ACK报文段）中，一并发送给客户端，此时服务器进入SYN_RECV状态；
3. 第三次握手： 客户端收到服务器的SYN+ACK报文段。然后将Acknowledgment Number设置为y+1，向服务器发送ACK报文段，这个报文段发送完毕以后，客户端和服务器端都进入ESTABLISHED状态，完成TCP三次握手。

**为什么要三次握手？**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了防止已失效的连接请求报文段突然又传送到了服务端，因而产生错误。

### 3.2 四次挥手
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当客户端和服务器通过三次握手建立了TCP连接以后，当数据传送完毕，肯定是要断开TCP连接的啊。那对于TCP的断开连接，这里就有了神秘的“四次分手”。

<img src ="https://img-blog.csdnimg.cn/52710df99497481ab0b4d61d85934f95.png#pic_center" width = 40%>

1. 第一次挥手： 主机A（可以使客户端，也可以是服务器端），设置Sequence Number，向主机B发送一个FIN报文段；此时，主机1进入FIN_WAIT_1状态；这表示主机A没有数据要发送给主机B了；
2. 第二次挥手： 主机B收到了主机A发送的FIN报文段，向主机A回一个ACK报文段，Acknowledgment Number为Sequence Number加1；主机A进入FIN_WAIT_2状态；主机B告诉主机A，我“同意”你的关闭请求；
3. 第三次挥手： 主机B向主机A发送FIN报文段，请求关闭连接，同时主机B进入LAST_ACK状态；
4. 第四次挥手： 主机A收到主机B发送的FIN报文段，向主机B发送ACK报文段，然后主机A进入TIME_WAIT状态；主机B收到主机A的ACK报文段以后，就关闭连接；此时，主机A等待2MSL后依然没有收到回复，则证明Server端已正常关闭，那好，主机A也可以关闭连接了。

**为什么要四次挥手？** 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCP协议是一种面向连接的、可靠的、基于字节流的运输层通信协议。TCP是全双工模式，这就意味着，当主机A发出FIN报文段时，只是表示主机A已经没有数据要发送了，主机A告诉主机B，它的数据已经全部发送完毕了；但是，这个时候主机A还是可以接受来自主机B的数据；当主机B返回ACK报文段时，表示它已经知道主机A没有数据发送了，但是主机B还是可以发送数据到主机A的；当主机B也发送了FIN报文段时，这个时候就表示主机B也没有数据要发送了，就会告诉主机A，我也没有数据要发送了，之后彼此就会愉快的中断这次TCP连接。

**为什么在第四次挥手后会有2个MSL的延时？**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MSL是Maximum Segment Lifetime，最大报文段生存时间，2个MSL是报文段发送和接收的最长时间。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;假定网络不可靠，那么第四次发送的ACK可能丢失，即B端无法收到这个ACK，如果B端收不到这个确认ACK，B端会定时向A端重复发送FIN，直到B端收到A的确认ACK。所以这个2MSL就是用来处理这个可能丢失的ACK的。而且能确保下一个新的连接中没有这个旧连接的报文。
_____
## 4 TCP流量控制

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果发送方把数据发送得过快，接收方可能会来不及接收，这就会造成数据的丢失。所谓流量控制就是让发送方的发送速率不要太快，要让接收方来得及接收。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;利用滑动窗口机制可以很方便地在TCP连接上实现对发送方的流量控制。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;设A向B发送数据。在连接建立时，B告诉了A：“我的接收窗口是 rwnd = 400 ”(这里的 rwnd 表示 receiver window) 。因此，发送方的发送窗口不能超过接收方给出的接收窗口的数值。请注意，TCP的窗口单位是字节，不是报文段。假设每一个报文段为100字节长，而数据报文段序号的初始值设为1。ACK表示首部中的确认位ACK，ack表示确认字段的值ack。

<img src ="https://img-blog.csdnimg.cn/e0b4ab1454c44f1d97ee8410c62840bf.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从图中可以看出，B进行了三次流量控制。第一次把窗口减少到 rwnd = 300 ，第二次又减到了 rwnd = 100 ，最后减到 rwnd = 0 ，即不允许发送方再发送数据了。这种使发送方暂停发送的状态将持续到主机B重新发出一个新的窗口值为止。B向A发送的三个报文段都设置了 ACK = 1 ，只有在ACK=1时确认号字段才有意义。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCP为每一个连接设有一个持续计时器(persistence timer)。只要TCP连接的一方收到对方的零窗口通知，就启动持续计时器。若持续计时器设置的时间到期，就发送一个零窗口控测报文段（携1字节的数据），那么收到这个报文段的一方就重新设置持续计时器。

____

## 5 TCP拥塞控制
### 5.1 慢开始和拥塞避免
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;发送方维持一个拥塞窗口 cwnd ( congestion window )的状态变量。拥塞窗口的大小取决于网络的拥塞程度，并且动态地在变化。发送方让自己的发送窗口等于拥塞窗口。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;发送方控制拥塞窗口的原则是：只要网络没有出现拥塞，拥塞窗口就再增大一些，以便把更多的分组发送出去。但只要网络出现拥塞，拥塞窗口就减小一些，以减少注入到网络中的分组数。

**慢开始算法**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当主机开始发送数据时，如果立即所大量数据字节注入到网络，那么就有可能引起网络拥塞，因为现在并不清楚网络的负荷情况。
因此，较好的方法是 先探测一下，即由小到大逐渐增大发送窗口，也就是说，由小到大逐渐增大拥塞窗口数值。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通常在刚刚开始发送报文段时，先把拥塞窗口 cwnd 设置为一个最大报文段MSS的数值。而在每收到一个对新的报文段的确认后，把拥塞窗口增加至多一个MSS的数值。用这样的方法逐步增大发送方的拥塞窗口 cwnd ，可以使分组注入到网络的速率更加合理。

<img src ="https://img-blog.csdnimg.cn/4368793c864043afb4e13eb4ee14a0e0.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;每经过一个传输轮次，拥塞窗口 cwnd 就加倍。一个传输轮次所经历的时间其实就是往返时间RTT。不过“传输轮次”更加强调：把拥塞窗口cwnd所允许发送的报文段都连续发送出去，并收到了对已发送的最后一个字节的确认。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;另外，慢开始的“慢”并不是指cwnd的增长速率慢，而是指在TCP开始发送报文段时先设置cwnd=1，使得发送方在开始时只发送一个报文段（目的是试探一下网络的拥塞情况），然后再逐渐增大cwnd。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了防止拥塞窗口cwnd增长过大引起网络拥塞，还需要设置一个慢开始门限ssthresh状态变量。慢开始门限ssthresh的用法如下：
- 当 cwnd < ssthresh 时，使用上述的慢开始算法。
- 当 cwnd > ssthresh 时，停止使用慢开始算法而改用拥塞避免算法。
- 当 cwnd = ssthresh 时，既可使用慢开始算法，也可使用拥塞控制避免算法。

**拥塞避免**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;让拥塞窗口cwnd缓慢地增大，即每经过一个往返时间RTT就把发送方的拥塞窗口cwnd加1，而不是加倍。这样拥塞窗口cwnd按线性规律缓慢增长，比慢开始算法的拥塞窗口增长速率缓慢得多。

<img src ="https://img-blog.csdnimg.cn/69c2a72bb2c249a0b8d9355f4d1415db.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;无论在慢开始阶段还是在拥塞避免阶段，只要发送方判断网络出现拥塞（其根据就是没有收到确认），就要把慢开始门限ssthresh设置为出现拥塞时的发送 方窗口值的一半（但不能小于2）。然后把拥塞窗口cwnd重新设置为1，执行慢开始算法。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这样做的目的就是要迅速减少主机发送到网络中的分组数，使得发生 拥塞的路由器有足够时间把队列中积压的分组处理完毕。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如下图，用具体数值说明了上述拥塞控制的过程。现在发送窗口的大小和拥塞窗口一样大。

<img src ="https://img-blog.csdnimg.cn/915597e6591742339e931278156c5739.png#pic_center" width = 48%>

### 5.2 快重传和快恢复
**快重传**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;快重传算法首先要求接收方每收到一个失序的报文段后就立即发出重复确认（为的是使发送方及早知道有报文段没有到达对方）而不要等到自己发送数据时才进行捎带确认。
       
<img src ="https://img-blog.csdnimg.cn/0468e65e928f463395d8a88ed64c92d1.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;接收方收到了M1和M2后都分别发出了确认。现在假定接收方没有收到M3但接着收到了M4。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;显然，接收方不能确认M4，因为M4是收到的失序报文段。根据 可靠传输原理，接收方可以什么都不做，也可以在适当时机发送一次对M2的确认。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;但按照快重传算法的规定，接收方应及时发送对M2的重复确认，这样做可以让 发送方及早知道报文段M3没有到达接收方。发送方接着发送了M5和M6。接收方收到这两个报文后，也还要再次发出对M2的重复确认。这样，发送方共收到了 接收方的四个对M2的确认，其中后三个都是重复确认。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;快重传算法还规定，发送方只要一连收到三个重复确认就应当立即重传对方尚未收到的报文段M3，而不必 继续等待M3设置的重传计时器到期。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于发送方尽早重传未被确认的报文段，因此采用快重传后可以使整个网络吞吐量提高约20%。

**快恢复**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;与快重传配合使用的还有快恢复算法，其过程有以下两个要点：
- 当发送方连续收到三个重复确认，就执行“乘法减小”算法，把慢开始门限ssthresh减半。
- 与慢开始不同之处是现在不执行慢开始算法（即拥塞窗口cwnd现在不设置为1），而是把cwnd值设置为 慢开始门限ssthresh减半后的数值，然后开始执行拥塞避免算法（“加法增大”），使拥塞窗口缓慢地线性增大。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;应用层做为 TCP/IP 协议的最高层级，对于我们移动开发来说，是接触最多的。

**运行在TCP协议上的协议：**

 - HTTP（Hypertext Transfer Protocol，超文本传输协议），主要用于普通浏览。 
 - HTTPS（Hypertext Transfer Protocol over Secure Socket Layer, or HTTP over SSL，安全超文本传输协议）,HTTP协议的安全版本
 - FTP（File Transfer Protocol，文件传输协议），由名知义，用于文件传输。 
 - POP3（Post Office Protocol, version 3，邮局协议），收邮件用。 
 - SMTP（Simple Mail Transfer Protocol，简单邮件传输协议），用来发送电子邮件。
 - TELNET（Teletype over the Network，网络电传），通过一个终端（terminal）登陆到网络。
 - SSH（Secure Shell，用于替代安全性差的TELNET），用于加密安全登陆用。

**运行在UDP协议上的协议：**

 - BOOTP（Boot Protocol，启动协议），应用于无盘设备。 
 - NTP（Network Time Protocol，网络时间协议），用于网络同步。 
 - DHCP（Dynamic Host Configuration Protocol，动态主机配置协议），动态配置IP地址。

**其他：**

 - DNS（Domain Name Service，域名服务），用于完成地址查找，邮件转发等工作（运行在TCP和UDP协议上）。
 - ECHO（Echo Protocol，回绕协议），用于查错及测量应答时间（运行在TCP和UDP协议上）。 
 - SNMP（Simple Network Management Protocol，简单网络管理协议），用于网络信息的收集和网络管理。 
 - ARP（Address Resolution Protocol，地址解析协议），用于动态解析以太网硬件的地址。

____

面试问题整理
[面试问题整理之TCP/IP和网络编程](https://blog.csdn.net/u013354486/article/details/80588916)