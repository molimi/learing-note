在因特网协议族（Internet Protocol Suite）中，TCP 层是位于 IP 层之上，应用层之下的中间层。不同主机的应用层之间经常需要可靠的、像管道一样的连接，但是 IP 层不提供这样的流机制，而是提供不可靠的包交换。TCP 和 UDP 处在同一层——传输层，但是它们有很多的不同。TCP 是 TCP/IP 系列协议中最复杂的部分，它具有以下特点：

- TCP 提供<font color=#9900CC><strong>可靠的</strong></font>数据传输服务，TCP 是<font color=#9900CC><strong>面向连接的</strong></font>。应用程序在使用 TCP 通信之前，先要建立连接，这是一个类似“打电话”的过程，通信结束后还要“挂电话”。
- TCP 连接是<font color=#9900CC><strong>点对点</strong></font>的，一条 TCP 连接只能连接两个端点。
- TCP 提供可靠传输，无差错、不丢失、不重复、按顺序。
- TCP 提供<font color=#9900CC><strong>全双工</strong></font>通信，允许通信双方任何时候都能发送数据，因为 TCP 连接的两端都设有发送缓存和接收缓存。
- TCP 面向<font color=#9900CC><strong>字节流</strong></font>。TCP 并不知道所传输的数据的含义，仅把数据看作一连串的字节序列，它也不保证接收方收到的数据块和发送方发出的数据块具有大小对应关系。

## 1 TCP 协议
### 1.1 TCP 报文段结构

TCP 是面向字节流的，而 TCP 传输数据的单元是 报文段 。一个 TCP 报文段可分为两部分：报头和数据部分。数据部分是上层应用交付的数据，而报头则是 TCP 功能的关键。

TCP 报文段的报头有前 20 字节的固定部分，后面 4n 字节是根据需要而添加的字段。如图则是 TCP 报文段结构：

<img src ="https://img-blog.csdnimg.cn/0cfa297c63924635b88b335c6b37a953.png#pic_center" width = 48%>

**字段解析**
- 源端口、目的端口：各占 2 字节，端口是运输层与应用层的服务接口，运输层的复用和分用功能都要通过端口才能实现。
- 序号：占 4 字节序，序号范围 $[0，2^32-1]$，序号增加到 $2^32-1$ 后，下个序号又回到 0。TCP 是面向字节流的，通过 TCP 传送的字节流中的每个字节都按顺序编号，而报头中的序号字段值则指的是本报文段数据的<font color=#9900CC><strong>第一个字节的序号</strong></font>。
- 确认号：占 4 字节，是期望收到对方的下一个报文段的数据的第一个字节的序号。
- 数据偏移：占 4 位，它指出 TCP 报文段的数据起始处距离 TCP 报文段的起始处有多远，的单位是 32 位字（以 4 字节为计算单位）。
- 保留：占 6 位，保留为今后使用，但目前应置为 0。
- 接收窗口：占 2 字节，用于流量控制，窗口值是指发送者自己的接收窗口大小，因为接收缓存的空间有限，单位为字节。
- 检验和：占 2 字节。检验和字段检验的范围包括首部和数据这两部分。在计算检验和时，要在 TCP 报文段的前面加上 12 字节的伪首部。
- 紧急指针：2 字节。当 URG=1 时才有效，指出本报文段紧急数据的字节数。
- 选项：长度可变。TCP 最初只规定了最大报文段长度 MSS，表示缓存所能接收的报文段的数据字段的最大长度是 MSS 个字节。

**标志字段**

- 紧急 URG：当 URG = 1 时，表明紧急指针字段有效。它告诉系统此报文段中有紧急数据，应尽快传送(相当于高优先级的数据)。
- 确认 ACK：只有当 ACK = 1 时确认号字段有效，当 ACK = 0 时确认号无效。
- 推送 PSH(PuSH)：接收 TCP 收到 PSH = 1 的报文段，就尽快地交付接收应用进程，不再等到整个缓存都填满了后再向上交付。
- 复位 RST(ReSeT)：当 RST = 1 时，表明 TCP 连接中出现严重差错（如由于主机崩溃或其他原因）必须释放连接，然后再重新建立运输连接。
- 同步 SYN：同步 SYN = 1 表示这是一个连接请求或连接接受报文。
- 终止 FIN(FINish)：用来释放一个连接。FIN = 1 表明此报文段的发送端的数据已发送完毕，并要求释放运输连接。


**捕获从计算机到远程服务器的批量 TCP 传输**

我们需要使用 Wireshark 来获取文件从计算机到远程服务器的 TCP 传输的数据包内容。首先访问一个网页，在网页上输入计算机上存储的文件名（包含 Alice in Wonderland 的 ASCII 文本），然后使用 HTTP POST 方法将文件传输到 Web 服务器（不使用 GET 方法的原因是我们希望大量数据从您的计算机传输到另一台计算机）。而在此同时，要运行 Wireshark 以获取从您的计算机发送和接收的 TCP 区段的内容。

1. 打开浏览器，在 `http://gaia.cs.umass.edu/wireshark-labs/alice.txt` 查看 Alice in Wonderland 的 ASCII 档案文件，将其保存；
2. 浏览 `http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html`，能得到以下内容；

<img src ="https://img-blog.csdnimg.cn/09efab86c34f49b1ae82db802a3f26db.png#pic_center" width = 48%>

3. 在此表单的"Browse..."按钮在计算机上输入包含 Alice in Wonderland 的文件名（完整路径名）。这时不用按下"Upload alice.txt file"按钮；
4. 启动 Wireshark ，开始捕获，在 Wireshark 数据包捕获选项视窗上按 OK；
5. 返回浏览器，按"Upload alice.txt file"将按钮文件上传到 gaia.cs.umass.edu 服务器。文件上传后，浏览器窗口显示一条简短的祝贺消息；
6. 停止 Wireshark 数据包捕获，Wireshark 显示内容。

<img src ="https://img-blog.csdnimg.cn/82698d503ede4d56a9ddb986ef2d6030.png#pic_center" width = 48%>

抓包软件中的 TCP 分析

<img src ="https://img-blog.csdnimg.cn/c4878f2e0c894f2eb353de22393e5e8e.png#pic_center" width = 48%>

展开 Flags 的头，得到的信息如下：

<img src ="https://img-blog.csdnimg.cn/3f59348c1bfc427d8cfc218e6ebc4d11.png#pic_center" width = 48%>


由此我们可以得到具体的 TCP 报文信息。

### 1.3 连接的建立与释放
#### 1.3.1 建立连接

TCP 是面向连接的，在传输 TCP 报文段之前先要创建连接，发起连接的一方被称为客户端，而响应连接请求的一方被称为服务端，而这个创建连接的过程被称为三次握手：

<img src ="https://img-blog.csdnimg.cn/4e06edf7e68747e48845f15c9532583d.png#pic_center" width = 48%>

- 第一次握手：客户端将标志位 SYN 置为 1 ，随机产生一个值SEQ = X，并将该数据包发送给服务器，客户机进入 SYN_SENT(同步已发送) 状态，等待服务器确认；
- 第二次握手：服务端收到请求报文段后，向客户端发送确认报文段。确认报文段的首部中 `SYN=1，ACK=1`，确认号是 `ack=x+1`，同时为自己选择一个初始序号 seq=y。服务端进入 SYN-RCVD（同步收到）状态。
- 第三次握手：客户端收到服务端的确认报文段后，还要给服务端发送一个确认报文段。这个报文段中 ACK=1，确认号 `ack=y+1`，而自己的序号 `seq=x+1`。这个报文段已经可以携带数据，如果不携带数据则不消耗序号，则下一个报文段序号仍为 `seq=x+1`。如果正确则连接建立成功，客户端和服务器进入 ESTABLISHED 状态。

握手过程中传送的包里不包含数据，三次握手完毕后，客户端与服务器才正式开始传送数据。理想状态下，TCP 连接一旦建立，在通信双方中的任何一方主动关闭连接之前，TCP 连接都将被一直保持下去。

#### 1.3.2 释放连接

当传输数据结束后，通信双方都可以释放连接，这个释放连接过程被称为释放连接:

<img src ="https://img-blog.csdnimg.cn/49c3cd7d82224a0b9bb99bfc943b730f.png#pic_center" width = 48%>

- 第一次挥手：此时 TCP 连接两端都还处于 ESTABLISHED 状态，客户端停止发送数据，并发出一个 FIN 报文段。首部 `FIN=1`，序号 `seq=u`（u 等于客户端传输数据最后一字节的序号加 1）。客户端进入 FIN-WAIT-1（终止等待 1）状态。
- 第二次挥手：服务端回复确认报文段，确认号 `ack=u+1`，序号 `seq=v`（v 等于服务端传输数据最后一字节的序号加 1），服务端进入 CLOSE-WAIT（关闭等待）状态。现在 TCP 连接处于半开半闭状态，服务端如果继续发送数据，客户端依然接收。
- 第三次挥手：客户端收到确认报文，进入 FIN-WAIT-2 状态，服务端发送完数据后，发出 FIN 报文段，`FIN=1`，确认号 `ack=u+1`，然后进入 LAST-ACK(最后确认)状态。
- 第四次挥手：客户端回复确认报文段，`ACK=1`，确认号 `ack=w+1`（w 为半开半闭状态时，收到的最后一个字节数据的编号） ，序号 `seq=u+1`，然后进入 TIME-WAIT（时间等待）状态。

注意此时连接还没有释放，需要时间等待状态结束后（4 分钟）连接两端才会 CLOSED。设置时间等待是因为，有可能最后一个确认报文丢失而需要重传。

#### 1.3.3 TCP 的三次握手在 Wireshark 中分析

打开 Wireshark 抓包软件，开始抓包，打开浏览器输入 `www.baidu.com`，进入网页。停止抓包，在过滤窗口输入TCP。

由下图可知，先进行了 TCP 三次传输，然后才开始 HTTP 传输。

<img src ="https://img-blog.csdnimg.cn/5533ec4a5cd14e73ab993807fac7ac17.png#pic_center" width = 48%>


第一次握手：客户端发送 SYN 报文到服务器；

<img src ="https://img-blog.csdnimg.cn/525bb7e6681c4cd2a4e2a91aa2ffc87a.png#pic_center" width = 48%>

第二次握手：服务器接收到客户端的 SYN 报文，回复 SYN + ACK 报文；

<img src ="https://img-blog.csdnimg.cn/91dcda541ed8441bb5c77efdce099843.png#pic_center" width = 48%>


第三次握手：客户端接收到服务端的 SYN + ACK 报文后，回复 ACK 报文。

<img src ="https://img-blog.csdnimg.cn/ca1db4bb01034b3a80421bd26608c381.png#pic_center" width = 48%>


### 1.4 TCP 可靠传输的实现

- TCP 报文段的长度可变，根据收发双方的缓存状态、网络状态而调整。
- 当 TCP 收到发自 TCP 连接另一端的数据，它将发送一个确认。
- 当 TCP 发出一个报文段后，它启动一个定时器，等待目的端确认收到这个报文段，如果不能及时收到一个确认，将重发这个报文段。这就是稍后介绍的超时重传。
- TCP 将保持它首部和数据的检验和。如果通过检验和发现报文段有差错，这个报文段将被丢弃，等待超时重传。
- TCP 将数据按字节排序，报文段中有序号，以确保顺序的正确性。
- TCP 还能提供流量控制。TCP 连接的每一方都有收发缓存。TCP 的接收端只允许另一端发送接收端缓冲区所能接纳的数据。这将防止较快主机致使较慢主机的缓冲区溢出。

可见超时重发机制是 TCP 可靠性的关键，只要没有得到确认报文段，就重新发送数据报，直到收到对方的确认为止。

### 1.5 超时重传

TCP 规定，接收者收到数据报文段后，需回复一个确认报文段，以告知发送者数据已经收到。而发送者如果一段时间内（超时计时器）没有收到确认报文段，便重复发送。

为了实现超时间重传，需要注意：
- 发送者发送一个报文段后，暂时保存该报文段的副本，为发生超时重传时使用，收到确认报文后删除该报文段。
- 确认报文段也需要序号，才能明确是发出去的哪个数据报得到了确认。
- 超时计时器比传输往返时间略长，但具体值是不确定的，根据网络情况而变

### 1.6 连续 ARQ 协议

在实际应用中的确不是这样的，真实情况是，采用了流水线传输：发送方可以连续发送多个报文段(连续发送的数据长度叫做窗口)，而不必每发完一段就停下来等待确认。

实际应用中，接收方也不必对收到的每个报文都做回复，而是采用累积确认方式：接收者收到多个连续的报文段后，只回复确认最后一个报文段，表示在这之前的数据都已收到。

这样，传输效率得到了很大的提升

<img src ="https://img-blog.csdnimg.cn/3f5ebedf5ad7461f8c880258ce7fa946.png#pic_center" width = 48%>

### 1.7 流量控制和拥塞控制

由于接收方缓存的限制，发送窗口不能大于接收方接收窗口。在报文段首部有一个字段就叫做**窗口(rwnd)**，这便是用于告诉对方自己的接收窗口，可见窗口的大小是可以变化的。

那么窗口的大小是如何变化的呢？TCP 对于拥塞的控制总结为“慢启动、加性增、乘性减”，如图所示：

<img src ="https://img-blog.csdnimg.cn/4adcdc4f10404fd9a5850654501796f2.png#pic_center" width = 48%>

- 慢启动 ：初始的窗口值很小，但是按指数规律渐渐增长，直到达到**慢开始门限(ssthresh)**。
- 加性增 ：窗口值达到慢开始门限后，每发送一个报文段，窗口值增加一个单位量。
- 乘性减 ：无论什么阶段，只要出现超时，则把窗口值减小一半。


## 2 实验分析
本篇使用下载好的包进行分析，在过滤器指定窗口中输入 “tcp” 过滤 Wireshark 视窗中显示的数据包：




_____

## 参考
- 传输层：TCP协议：[https://www.lanqiao.cn/courses/98/learning/?id=556&compatibility=false](https://www.lanqiao.cn/courses/98/learning/?id=556&compatibility=false)
- TCP协议与Wireshark实验：[https://www.cnblogs.com/linfangnan/p/12809541.html](https://www.cnblogs.com/linfangnan/p/12809541.html)
- TCP 协议分析：[https://www.educoder.net/shixuns/5o8ne4m6/challenges](https://www.educoder.net/shixuns/5o8ne4m6/challenges)
