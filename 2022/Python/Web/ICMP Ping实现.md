&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ping是一个网络应用程序，用于测试某个主机在IP网络中是否可访问。它也用于测试计算机的网卡或测试网络延迟。Ping的实现通常使用ICMP协议。ICMP协议在协议族中的地位如下图所示：

<img src ="https://img-blog.csdnimg.cn/2ca698b797864102a44c0532711be76a.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过本文，你将更好地理解因特网控制报文协议（`ICMP`），学习使用`ICMP`请求和响应消息实现`Ping`程序。通过向目标主机发送`ICMP`回显包并监听`ICMP`回显应答来工作。回显有时称为`pong`。`ping`程序测量往返时间，记录数据包丢失，并输出接收到的回显包的统计摘要（往返时间的最小值、最大值和平均值，以及在某些版本中的平均值的标准差）。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;主要任务：用`python`开发自己的简单`Ping`程序。程序将使用`ICMP`协议，但为了保持简单，将不完全遵循`RFC 1739`中的正式规范。在本实训中只需要编写程序的客户端，因为服务器端所需的功能几乎内置于所有操作系统中。Ping程序的基本功能如下： Ping 程序能将 ping 请求发送到指定的主机，间隔大约一秒钟。每个消息包含一个带有时间戳的数据包。 每个数据包发送完后，程序最多等待一秒，用于接收响应。如果一秒后服务器没有响应，那么客户端应假设 ping 数据包或 pong 数据包在网络中丢失（或者服务器已关闭）。 统计摘要信息（往返时间的最小值、最大值和平均值，以及在某些版本中的平均值的标准差） 本实训将使用原始套接字来使用ICMP协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面将为为Ping客户端创建一个原始类型的套接字。


## 1 Ping客户端创建原始套接字
### 1.1 原始套接字

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;原始套接字（SOCK-RAW）。该套接字允许对较低层协议（如IP或ICMP）进行直接访问，常用于网络协议分析，检验新的网络协议实现，也可用于测试新配置或安装的网络设备。使用原始套接字进行网络通信的基本步骤为：
- （1）创建原始套接字、设置套接字选项和创建并填充相应协议头；
- （2）用 `sendto()` 函数将组装好的数据发送出去；
- （3）使用 `recvfrom()` 函数接收数据并解析；
- （4）关闭套接字。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Python中使用套接字编程，需要先引入套接字（import socket）；使用 `socket()` 函数来创建套接字。其语法如下：

```python
socket(socket_family,socket_type,protocol=0)
socket_family可以是如下参数之一：
  　　AF_INET IPv4（默认）
　　  AF_INET6 IPv6
　　  AF_UNIX 只能够用于单一的Unix系统进程间通信
socket_type可以是如下参数之一:
　　  SOCK_STREAM　　流式socket , for TCP （默认）
　  　SOCK_DGRAM　　 数据报式socket , for UDP
　  　SOCK_RAW 		原始套接字
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;普通的套接字无法处理ICMP、IGMP等网络报文，而原始套接字 `SOCK_RAW` 可以；`SOCK_RAM` 用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。`SOCK_RAM` 通常仅限于高级用户或管理员运行的程序使用。

```python
protocol参数：
　　0　（默认）与特定的地址家族相关的协议。如果是 0 ，则系统就会根据地址格式和套接类别，自动选择一个合适的协议。也可以使用
  getprotobyname()指定要使用的协议名称如“ICMP”、“UDP”等。
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在本实验中，要创建一个使用IPV4地址族的的原始套接字，并指定使用ICMP协议，可以使用如下语句：

```python
icmp = getprotobyname("icmp")   /*指定ICMP协议
rawsocket=socket(AF_INET, SOCK_RAW, icmp)
```
## 2 封装并发送ICMP报文
### 2.1 ICMP协议
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP协议：`Internet Control Message Protocol`（Internet控制报文协议）；由于IP协议并不是一个可靠的协议，它不保证数据被成功送达。原因是，在通信途中的某处的一个路由器由于不能处理所有的数据包，就将数据包一个一个丢弃了。或者，虽然到达了对方，但是由于搞错了端口号，服务器软件可能不能接受它。这时，在错误发生的现场，为了联络而飞过来的信鸽就是ICMP 报文。在IP 网络上，由于数据包被丢弃等原因，为了控制将必要的信息传递给发信方。ICMP 协议是为了辅助IP 协议，交换各种各样的控制信息而被制造出来的，经常供IP层或更高层协议（TCP或UDP）使用。所以它经常被认为是IP层的一个组成部分。

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

### 2.2 ping程序原理分析
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ping程序是由Mike Muuss编写，目的是为了测试另一 台主机是否可达，现在已经成为一个常用的网络状态检查工具。该程序发送一份 ICMP回显请求报文给远程主机，并等待返回 ICMP回显应答。利用ping这种原理，已经出现了许多基于ping的网络扫描器，比如nmap、arping、fping、hping3等。所以随着Internet安全意识的增强，现在有些提供访问控制策略的路由器和防火墙已经可以设置过滤特定ICMP报文请求。因此并不能通过简单的ping命令判断远程主机是否在线。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ping 使用的是ICMP协议，它发送icmp回送请求消息给目的主机。ICMP协议规定：目的主机必须返回ICMP回送应答消息给源主机。如果源主机在一定时间内收到应答，则认为主机可达。大多数的 TCP/IP 实现都在内核中直接支持Ping服务器，ICMP回显请求和回显应答报文如下图所示。

<img src ="https://img-blog.csdnimg.cn/9118b8c8ef0f4d9dbe35508b91515133.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ping的原理是用类型码为0的ICMP发请 求，受到请求的主机则用类型码为8的ICMP回应。通过计算ICMP应答报文数量和与接受与发送报文之间的时间差，判断当前的网络状态。这个往返时间的计算方法是：ping命令在发送ICMP报文时将当前的时间值存储在ICMP报文中发出，当应答报文返回时，使用当前时间值减去存放在ICMP报文数据中存放发送请求的时间值来计算往返时间。ping返回接受到的数据报文字节大小、TTL值以及往返时间。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unix系统在实现ping程序时是把ICMP报文中的标识符字段置成发送进程的 ID号。这样 即使在同一台主机上同时运行了多个 ping程序实例，ping程序也可以识别出返回的信息。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ping` 操作中就包括了相应请求（类型字段值为8）和应答（类型字段值为0）ICMP报文。

<img src ="https://img-blog.csdnimg.cn/08018b8f3a4f4f599d6cee0e33b8f986.png#pic_center" width = 48%>

过程如下：
1. 向目标服务器发送回送请求。
首先，向目标服务器发出回送请求（类型是8，代码是0）报文（同2）。在这个回送请求报文里，除了类型和代码字段，还被追加了标识符和序号字段。标识符和序号字段分别是16 位的字段。ping 命令在发送回送请求报文时，在这两个字段里填入任意的值。对于标识符，应用程序执行期间送出的所有报文里填入相同的值。对于序号，每送出一个报文数值就增加1。而且，回送请求的选项数据部分用来装任意数据。这个任意数据用来调整ping 的交流数据包的大小。

2. 鹦鹉学舌一样返回回送回答。
计算机送出的回送请求到达目标服务器后，服务器回答这一请求，向送信方发送回送请求（类型是0，代码是0）（同3）。这个ICMP 回送回答报文在IP 层来看，与被送来的回送请求报文基本上一样。不同的只是，源和目标IP 地址字段被交换了，类型字段里填入了表示回送回答的0。也就是，从送信方来看，自己送出的ICMP 报文从目标服务器那里象鹦鹉学舌那样原样返回了。
送信方的计算机可以通过收到回送回答报文，来确认目标服务器在工作着。进一步，记住发送回送请求报文的时间，与接收到回送回答报文的时间一比较，就能计算出报文一去一回往复所需要的时间（同4）。但是，收到的回送回答报文里写的只是类型和代码的话，发送方计算机将无法判断它是否是自己发出去请求的回答。因此，前面说到的标识符和序号字段就有它的意义了。将这两个值与回送回答报文中的相同字段值一比较，送行方计算机就能够简单地检测回送回答是否正确了。执行ping 命令而调查的结果没什么问题的话，就将目标服务器的IP 地址，数据大小，往复花费的时间打印到屏幕上。

3. 用ping 命令不能确定与对方连通的原因大致有三个。
1）目标服务器不存在；2)花在数据包交流上的时间太长ping 命令认为超时；3）目标服务器不回答ping 命令。如果是原因2），通过ping 命令的选项来延长到超时的等待时间，就能正确显示结果了。如果原因是1）或3）的话，仅凭ping 命令的结果就不能判断是哪方了。正如这样，ping 命令不一定一定能判断对方是否存在。


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一台主机向一个节点发送一个类型字段值为8的ICMP报文，如果途中没有异常（如果没有被路由丢弃，目标不回应ICMP或者传输失败），则目标返回类型字段值为0的ICMP报文，说明这台主机存在。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;时间戳请求报文（类型值字段13）和时间戳应答报文（类型值字段14）用于测试两台主机之间数据报来回一次的传输时间。传输时，主机填充原始时间戳，接受方收到请求后填充接受时间戳后以类型值字段14的报文格式返回，发送方计算这个时间差。

### 2.3 协议数据包的封装
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python中处理二进制数据如存取文件、socket操作时，可以使用 Python 的 struct 模块来完成。使用该模块可以方便地来实现协议数据的封装与解封。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;struct模块中最重要的三个函数是：

```python
pack(fmt, v1, v2, ...)     # 按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)
unpack(fmt, string)        # 按照给定的格式(fmt)解析字节流string，返回解析出来的数组
calcsize(fmt)              # 计算给定的格式(fmt)占用多少字节的内存
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中fmt支持的格式如下表描述：

<img src ="https://img-blog.csdnimg.cn/7413f079a5a047cfbf1a1bd1e0b5b65c.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在完成封装后，将封装后的数据data，使用原始套接字的 `sendto()` 方法进行发送。`sendto()` 主要参数：
- packet：发送的数据
- Addr：形式为 `(ipaddr，port)` 的元组
## 3 解析IP包ICMP头信息
### 3.1 接收ICMP报文

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用原始套接字的 `recvfrom()` 函数接收报文，输入参数指定为报文最大长度，如1024；函数返回值为报文发送方的地址、报文内容。接收代码示例如下:

```python
recvfpacket, addr = mysocket.recvfrom(1024)
```

### 3.2 解析ICMP报文

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP报文内容是放在IP数据包的数据部分里来互相交流的。也就是，从ICMP的报文格式来说，ICMP是IP的上层协议。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个ICMP报文包括IP报头（至少20字节）、ICMP报头（至少八字节）和ICMP报文（属于ICMP报文的数据部分）。当IP报头中的协议类型字段值为1时，就说明这是一个ICMP报文。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ICMP报头如下图：

<img src ="https://img-blog.csdnimg.cn/75e65d846ffa4e69b5bbc26f64ff8cf7.png#pic_center" width = 48%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;解析ICMP报文可以使用Python中struct模块的 `upack()` 函数来实现。其参数：
- fmtstr: 格式化字符串
- packet: 需要解析的字符数组

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;函数的返回值可以是多个，根据格式串中指定的类型返回到相应变量中。例如：

```python
a,b,c,d=struct.unpack('5s6sif',bytes)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则从bytes这个数组中解析出a：5个字符的字符串（5s），b:6个字符的字符串(6s)，c为整型(i)，d为浮点型数据(f)。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于Ping命令的ICMP报文，我们需从IP包中取出ICMP报头，位于20到28字节；从中可以取出报文类型type,代码code，校验和checksum，报文ID及报文序号字段；
   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于类型为1的报文且其ID为需要接收的报文，从28字节后面开始解析发送的数据为发送时间，数据类型及长度根据发送的数据来确定。
- 响应时间：计算收到报文的时间与发送报文（ICMP报文的数据部分）的时间差；
- TTL：TTL指Time To Live生成周期，指定IP包被路由器丢弃之前允许通过的最大网段数量。在IPv4包头中TTL是一个8 bit字段，它位于IPv4包的第9个字节。因此只需从接收报文中解析出第9字节即可。

```python
import socket
import os
import struct
import time
import select

ICMP_ECHO_REQUEST = 8


def chesksum(data):
    """
    校验
    """
    n = len(data)
    m = n % 2
    sum = 0 
    for i in range(0, n - m ,2):
        sum += (data[i]) + ((data[i+1]) << 8)   # 传入data以每两个字节（十六进制）通过ord转十进制，第一字节在低位，第二个字节在高位
    if m:
        sum += (data[-1])
    # 将高于16位与低16位相加
    sum = (sum >> 16) + (sum & 0xffff)
    sum += (sum >> 16)      # 如果还有高于16位，将继续与低16位相加
    answer = ~sum & 0xffff
    # 主机字节序转网络字节序列（参考小端序转大端序）
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer 



# 接收一次Ping的返回消息
def receiveOnePing(mySocket, ID, sequence, destAddr, timeout):
    timeLeft = timeout

    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return None

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        
        header = recPacket[20:28]
        type, code, checksum, packetID, sequence = struct.unpack("!bbHHh", header)
        if type == 0 and packetID == ID:  # type should be 0
            byte_in_double =  struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28+byte_in_double])[0]
            delay = timeReceived - startedSelect
            ttl = struct.unpack("!b", recPacket[8:9])[0]
            return (delay, ttl, byte_in_double)
        
        
        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return None

# 发送一次Ping数据包
def sendOnePing(mySocket, ID, sequence, destAddr):
    # 头部构成： type (8), code (8), checksum (16), id (16), sequence (16)

    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, sequence)
    data = struct.pack("!d", time.time())
    # 计算头部和数据的校验和
    myChecksum = checksum(header + data)

    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, sequence)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object

# 向指定地址发送Ping消息
def doOnePing(destAddr, ID, sequence, timeout):
    icmp = socket.getprotobyname("icmp")

    # 创建原始套接字
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
 
    sendOnePing(mySocket, ID, sequence, destAddr)
    delay = receiveOnePing(mySocket, ID, sequence, destAddr, timeout)

    mySocket.close()
    return delay

# 主函数Ping
def ping(host, timeout=1):
    
    # timeout=1指: 如果1秒内没从服务器返回，客户端认为Ping或Pong丢失。
    dest = socket.gethostbyname(host)
    print("Pinging " + dest + " using Python:")
    print("")
    
    # 每秒向服务器发送一次Ping请求
    myID = os.getpid() & 0xFFFF  # 返回进程ID
    loss = 0
    for i in range(4):
        result = doOnePing(dest, myID, i, timeout)
        if not result:
            print("Request timed out.")
            loss += 1
        else:
            delay = int(result[0]*1000)
            ttl = result[1]
            bytes = result[2]
            print("Received from " + dest + ": byte(s)=" + str(bytes) + " delay=" + str(delay) + "ms TTL=" + str(ttl))
        time.sleep(1)  # one second
    print("Packet: sent = " + str(4) + " received = " + str(4-loss) + " lost = " + str(loss))

    return

ping("127.0.0.1")
```


<img src ="https://img-blog.csdnimg.cn/0269599ff3614cee986b28b04892455a.png#pic_center" width = 36%>

## 4 ICMP 的应用--Traceroute
### 4.1 原理介绍
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Traceroute 是用来侦测主机到目的主机之间所经路由情况的重要工具，也是最便利的工具。前面说到，尽管 ping 工具也可以进行侦测，但是，因为 ip 头的限制，ping 不能完全的记录下所经过的路由器。所以 Traceroute 正好就填补了这个缺憾。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Traceroute 的原理是非常非常的有意思，它受到目的主机的 IP 后，首先给目的主机发送一个 TTL=1(还记得 TTL 是什么吗?)的  UDP(后面就 知道 UDP 是什么了)数据包，而经过的第一个路由器收到这个数据包以后，就自动把 TTL 减1，而 TTL 变为0以后，路由器就把这个包给抛弃了，并同时产生 一个主机不可达的 ICMP 数据报给主机。主机收到这个数据报以后再发一个 TTL=2的 UDP 数据报给目的主机，然后刺激第二个路由器给主机发 ICMP 数据 报。如此往复直到到达目的主机。这样，traceroute 就拿到了所有的路由器 ip。从而避开了 ip 头只能记录有限路由 IP 的问题。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有人要问，我怎么知道 UDP 到没到达目的主机呢？这就涉及一个技巧的问题，TCP 和 UDP 协议有一个端口号定义，而普通的网络程序只监控少数的几个号码较小的端口，比如说80，比如说23，等等。而 traceroute 发送的是端口号>30000(真变态)的  UDP 报，所以到 达目的主机的时候，目的主机只能发送一个端口不可达的 ICMP 数据报给主机。主机接到这个报告以后就知道，主机到了，所以，说  Traceroute 是一个骗子一点也不为过。

<img src ="https://img-blog.csdnimg.cn/b6995c2213e641e5a7714de536cfa198.png#pic_center" width = 48%>

**过程如下：**
1. 执行tracert命令。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在Windows 上执行tracert 命令后，首先计算机向目的服务器发送IP 数据包。Windows 上使用的是与ping 同样的ICMP 回送请求报文。但是，有一点和通常的回送请求不一样。那是，最初将IP 首部的TTL(生存时间)字段设为1 这一点。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;路由器每转送一次数据包就将TTL 的值减1。当TTL 变为0 的时候，按规定将丢弃这个数据包。正如这样，与其说TTL 是时间，还不如说TTL 是经过路由器的个数。对于计算机发送出去的数据包，只要它与目标服务器不在同一局域网内，一定会被哪儿的路由器中继。这时如果TTL 的值是1，由于路由器的处理会变为0，则该数据包将会被丢弃（同2）。

2. 用超时报文来通知送信方。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;路由器丢弃数据包的同时，用ICMP 报文来通知错误。这时使用的ICMP 报文是，类型为11，代码为0 的ICMP 超时报文。而且在选项数据字段里，将填入原先数据包的IP 首部和ICMP 的开始8 字节。正如ping 命令的时候看到的，ICMP 回送请求的先头8 字节里包含了标识符和序号字段。因此，送信方的计算机看了超时报文后，就知道是针对自己发出的回送请求的错误通知。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;计算机接到针对第一个数据包的ICMP 超时报文后，接下来将TTL 加1（TTL=2）并同样地送出（同3）。这次通过第一个路由器，TTL 变为1，到达第二个路由器。但是第二个路由器象前面一样，由于TTL变为0，将不能转发该包。因此，同第一个路由器一样，将该包丢弃，并返回ICMP 超时报文。以后，收到错误的发送方计算机将TTL 加1，重复同样的工作（同4）。

3. 只有目标服务器的反应不同。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如此一个一个增加TTL，某个时候ICMP 回送请求报文将到达最终的目标服务器。这时，只有目标服务器与途中的路由器不同，不返回ICMP 超时报文。为什么呢？因为即使目标服务器收到TTL 为1 的数据包也不会发生错误。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;作为代替处理，服务器针对送信方计算机发出的ICMP 回送请求报文，返回ICMP 回送回答报文。也就是，送信方计算机与服务器之间，与ping 命令的执行一样了（同5）。得到了ICMP 回送回答报文的送信方知道了路经调查已经到了目标服务器，就结束了tracert 命令的执行（同6）。像这样，通过列出中途路由器返回的错误，就能知道构成到目标服务器路径的所有路由器的信息了。

4. 操作系统不同则实现方法略微不同。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;到这里，以Windows 上的tracert 命令为例看了原理，有些别的操作系统的traceroute 命令的原理略微不同。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;具体来说，也有用向目标发送UDP 数据包代替ICMP 回送请求报文来实现的。虽说是用UDP，但途中的路由器的处理与図 8完全相同。只是UDP 数据包到达目标后的处理不同。目标计算机突然收到与通信无关的数据包，就返回ICMP 错误，因此根据返回数据包的内容来判断命令的中止。

### 4.2 Python 实现
```python
# -*- coding=utf-8 -*-
# @Author: CarpeDiem
# @Date: 230423
# @Version: 1.0
# @Description: 基于ICMP协议Traceroute实现

from kamene.all import *
import time
import re

def Tracert_one(dst,dport,ttl_no):
    '''发一个Traceroute包，参数需要目的地址，目的端口，TTL'''
    send_time = time.time()         # 记录发送时间
    Tracert_one_reply = sr1(IP(dst=dst, ttl=ttl_no)/UDP(sport=6600, dport=dport)/b'my traceroute!!!', timeout = 1, verbose=False)
    # Scapy中UDP默认源目端口53，需要将源端口也改掉，否则中间设备将不回应
    try:
        if Tracert_one_reply.getlayer(ICMP).type == 11 and Tracert_one_reply.getlayer(ICMP).code == 0:
            # 如果收到TTL超时
            hop_ip = Tracert_one_reply.getlayer(IP).src
            received_time = time.time()
            time_to_passed = (received_time - send_time) * 1000
            return 1, hop_ip, time_to_passed        # 返回1表示并未抵达目的地
        elif Tracert_one_reply.getlayer(ICMP).type == 3 and Tracert_one_reply.getlayer(ICMP).code == 3:
            # 如果收到端口不可达
            hop_ip = Tracert_one_reply.getlayer(IP).src
            received_time = time.time()
            time_to_passed = (received_time - send_time) * 1000
            return 2, hop_ip, time_to_passed    # 返回2表示抵达目的地
    except Exception as e:
        if re.match('.*NoneType.*',str(e)):
            return None     # 测试失败返回None,没有回包

def MY_Tracert(dst,hops):
    dport = 33434           # Traceroute的目的端口从33434开始计算
    hop = 0
    while hop < hops:
        dport = dport + hop
        hop += 1
        Result = Tracert_one(dst,dport,hop)
        if Result == None:      # 如果测试失败就打印‘*’
            print(str(hop) + ' *',flush=True)
        elif Result[0] == 1:    # 如果未抵达目的，就打印这一跳和消耗的时间
            time_to_pass_result = '%4.2f' % Result[2]
            print(str(hop) + ' ' + str(Result[1]) + ' ' + time_to_pass_result + 'ms')
        elif Result[0] == 2:    # 如果抵达目的，就打印这一跳和消耗的时间，并且跳出循环！
            time_to_pass_result = '%4.2f' % Result[2]
            print(str(hop) + ' ' + str(Result[1]) + ' ' + time_to_pass_result + 'ms')
            break
        time.sleep(1)

if __name__ == '__main__':
    conf.route.add(net='172.16.10.0/24',gw='192.168.10.115')    # 为Scapy添加路由
    destIP=input("目标IP>>>")
    hops=input("最大跳数>>>")
    MY_Tracert(destIP, int(hops))
```

<img src ="https://img-blog.csdnimg.cn/c7a088bcbda2486c87c93a582134df1b.webp#pic_center" width = 64%>



> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;了解更多，请阅读：[ICMP实现之端口扫描、ICMP实现之改变路由、ICMP实现之源点抑制、ICMP实现之MTU探索](https://www.cnblogs.com/iiiiher/p/8513748.html)
____


## 参考
- python实现ping工具：[https://blog.csdn.net/jia666666/article/details/85254450](https://blog.csdn.net/jia666666/article/details/85254450)
- ICMP协议与ping原理以及用Python实现ping：[https://cloud.tencent.com/developer/article/1156671](https://cloud.tencent.com/developer/article/1156671)
- 《计算机网络－自顶向下方法》笔记：[https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)
- 完全理解icmp协议：[https://www.cnblogs.com/iiiiher/p/8513748.html](https://www.cnblogs.com/iiiiher/p/8513748.html)
- Python网络编程2--实现Ping程序与Traceroute程序：[https://www.jianshu.com/p/0c52955515c7](https://www.jianshu.com/p/0c52955515c7)
