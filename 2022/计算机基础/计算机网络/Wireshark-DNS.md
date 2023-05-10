DNS 系统是一种将域名和 IP 地址相互映射的以层次结构分布的数据库系统。DNS 系统采用递归查询请求的方式来响应用户的查询，为互联网的运行提供关键性的基础服务。

DNS 系统的解析过程描述如下：
1. 主机先向本地域名服务器进行递归查询；
2. 本地域名服务器采用迭代查询，向一个根域名服务器进行查询；
3. 根域名服务器告诉本地域名服务器，下一次应该查询的顶级域名服务器的 IP 地址；
4. 本地域名服务器向顶级域名服务器进行查询；
5. 顶级域名服务器告诉本地域名服务器，下一步查询权威服务器的 IP 地址；
6. 本地域名服务器向权威服务器进行查询；
7. 权威服务器告诉本地域名服务器所查询的主机的IP地址；
8. 本地域名服务器最后把查询结果告诉主机。

本实验的主要内容是基于 Wireshark 工具去分析 DNS 的解析过程及其协议字段。

## 1 DNS 协议分析
### 1.1 nslookup 域名解析
#### 1.1.1 域名结构

IP 地址是网络中面向应用的计算机主机的标志，而域名则是互联网中面向用户的主机的标志。为了保证域名的唯一性，域名系统采用层次结构。如下图所示：

<img src ="https://img-blog.csdnimg.cn/4759351873544d3394b7dfb412ce319a.png#pic_center" width = 48%>

- 每一个域名（只讨论英文域名）都是一个标号序列（labels），用字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成；
- 标号序列总长度不能超过 255 个字符，它由点号分割成一个个的标号（label）；
- 每个标号应该在 63 个字符之内，每个标号都可以看成一个层次的域名；
- 级别最低的域名写在左边，级别最高的域名写在右边，如www.baidu.com；
- com: 一级域名。表示这是一个企业域名。同级的还有 “net”(网络提供商)， “org”(非盈利组织) 等；
- baidu: 二级域名，指公司名；
- www: 表示该公司的 WEB 服务器对应的主机。

#### 1.1.2 域名服务器

域名需要由遍及全世界的域名服务器去解析，域名服务器实际上就是装有域名及其 IP 地址数据库的主机。

域名服务器由高向低进行层次划分，可分为以下几大类：

- 根域名服务器：最高层次的域名服务器，本地域名服务器解析不了的域名就会向其求助；
- 顶级域名服务器：负责管理在该顶级域名服务器下注册的二级域名；
- 权限域名服务器：负责一个区的域名解析工作；
- 本地域名服务器：当一个主机发出 DNS 查询请求时，这个查询请求首先发给本地域名服务器。

注：一个域名服务器所负责的范围，或者说有管理权限的范围，就称为区。

我们需要注意的是：
- 每个层的域名上都有自己的域名服务器，最顶层的是根域名服务器；
- 每一级域名服务器都知道下级域名服务器的 IP 地址；
- 为了容灾，每一级至少设置两个或以上的域名服务器。

#### 1.1.3 域名解析

域名解析主要是将主机名（例如www.example.com）转换为计算机友好的 IP 地址（例如192.168.1.1）
域名解析的基本过程：
(1) 输入域名后，先查找自己主机对应的域名服务器，域名服务器先查找自己的数据库中的数据；
(2) 如果没有， 就向上级域名服务器进行查找， 依次类推；
(3) 最多回溯到根域名服务器，肯定能找到这个域名的 IP 地址；
(4) 域名服务器自身也会进行一些缓存， 把曾经访问过的域名和对应的 IP 地址缓存起来，可以加速查找过程。

简单的域名对应的 IP 地址查询，也可以使用 ping 命令来完成。

<img src ="https://img-blog.csdnimg.cn/d790b058cbca42b49d5d33eea9dfa71c.png#pic_center" width = 48%>

#### 1.1.4 域名解析与 nslookup

nslookup 是一种网络管理命令行工具，可用于查询 DNS 域名和 IP 地址。无论是 linux 或者是 window 下都有这个工具，用好它对平常的域名解析情况，或者对域名服务器的维护都有帮助。
语法：

```bash
    nslookup [ -Option ... ] [ Host ] [ -NameServer ]
``` 

nslookup 命令以两种方式查询域名服务器：
- 交互模式：当没有给出操作参数时进入，操作对象和操作方式可以通过相应交互命令来告诉。
- 命令模式：在一个命令行中将操作对象和操作方式告知命令，nslookup 将执行结果返回。实际使用中，采用这种方式比较多。

下面列举几种主要用法：

1. 直接查询 查询一个域名的 A 记录，使用默认的 DNS 服务器，语法为：`nslookup domain`  例如： `nslookup baidu.com`

<img src ="https://img-blog.csdnimg.cn/ed87d1aa2f074071be38d81d9294865b.png#pic_center" width = 48%>

从中可以看出:
(1) `baidu.com` 的域名解析所使用的 DNS 服务器地址 `172.21.0.10`；
(2) `baidu.com` 域名对应的主机有几个IP地址。


2. 指定域名服务器查询

```bash
nslookup domain  dns-server
```

将查询请求发送到 DNS 服务器 `bitsy.mit.edu`，而不是默认的 DNS 服务器。
如：
```bash
nslookup baidu.com 172.21.0.10
```

3. 查询其他记录，语法格式如下：

```bash
nslookup -type=type domain 
```

通过指定 -type 参数的具体类型，执行其他类型的查询。常用类型说明：
- MX：邮件服务器记录；
- NS：名字服务器记录；
- PTR：反向记录。

如查询baidu.com对应的名字服务器记录：

```bash
nslookup -type=NS baidu.com
```

结果如图：

<img src ="https://img-blog.csdnimg.cn/30e835916e654b269de9380915a1f835.png#pic_center" width = 48%>


查询 IP 地址172.11.4.107对应的域名（反向查询）:

```bash
nslookup -type=PTR 172.11.4.107
```
结果如图：

<img src ="https://img-blog.csdnimg.cn/8ab188b1d3d2478792889f4f0127e590.png#pic_center" width = 48%>


### 1.2 查看与设置 DNS 服务器操作

#### 1.2.1 如何查看网卡默认的 DNS 服务器
在我们使用的 Linux 操作系统里面，DNS 服务器的配置信息在 `/etc/resolv.conf` 文件里面。查看该文件的命令如下：

```bash
cat /etc/resolv.conf
```
该文件内容如下图所示：

<img src ="https://img-blog.csdnimg.cn/479b0bf705594cfca93cbd8833ccc8c9.png#pic_center" width = 48%>

可以看出，默认的 DNS 服务器 IP 是：172.21.0.10

#### 1.2.2 如何修改网卡默认的 DNS 服务器

可以直接修改 `resolv.` conf文件，方法如下：
```bash
vim /etc/resolv.conf        //打开resolv.conf 文件
```

改为如下内容：

```bash
nameserver 114.114.114.114 #修改成你的主DNS
nameserver 8.8.8.8    #修改成你的备用DNS
```

配置完成后，需重启网络服务才生效，重启网络服务的语句为：

```bash
service networking restart
```

<img src ="https://img-blog.csdnimg.cn/c9e1c210bf9548d4beebd86481519ec2.png#pic_center" width = 48%>


### 1.3 DNS 报文分析
#### 1.3.1 DNS 域名解析过程

DNS 协议属于应用层，使用客户端-服务器模式运行在通信的端系统之间。在通信的端系统之间通过端到端传输输协议（ UDP 协议，通常使用 53 号端口）来传送 DNS 报文。

DNS 系统解析过程如下图所示：

<img src ="https://img-blog.csdnimg.cn/91c3e70b0672411eb5fa9515b976007c.png#pic_center" width = 48%>

DNS 客户需要访问 WEB 服务器 `www.abc.xyz.com`，则客户机可以访问本地的 hosts 文件，看能否知道主机名称对应的 IP 地址，如果 hosts 文件不能解析该主机名称，则只能通过向客户机所设定的 DNS 服务器进行查询。查询过程如下：
(1) DNS 客户机向本地域名服务器发送查询请求，查找域名 `www.abx.xyz.com` 的 IP 地址。本地域名服务器查询本地的缓存，如果有这个地址，则将地址返回给 DNS 客户机；
(2) 如果本地域名服务器缓存没有这个地址，则发送查询请求到根域名服务器，询问 `www.abx.xyz.com` 的地址，根域名服务器会将子域 `com` 的域名服务器的地址返回给本地域名服务器；
(3) 本地域名服务器再向 `com` 域发送查询请求，`com` 域服务器无法提供地址，但会把下一级的域名服务器 `xyz.com` 的地址发送给本地域名服务器；
(4) 重复（2）、（3）的过程，最后 `xyz.com` 域名服务器把 `abc.xyz.com` 域名服务器地址发送给本地域名服务器；
(5) 本地域名服务器再向 `abc.xyz.com` 域名服务器发送地址查询请求 `abc.xyz.com`，找到了 `www.abc.xyz.com` 的地址，就将这个地址发送给本地域名服务器；
(6) 本地域名服务器把地址保存到缓存，同时返回给 DNS 客户机。

有两种查询方式，分别是:
1. 递归查询：主机向本地域名服务器的查询一般都是采用递归查询；
2. 迭代查询：本地域名服务器向根域名服务器的查询通常采用迭代查询。只是通常，也有的采用递归查询。

#### 1.3.2 域名解析协议
域名解析的实现是依靠 DNS 协议来完成。有两种 DNS 报文——查询报文和响应报文，分别来实现 DNS 的查询请求和响应请求。

DNS 协议报文格式如下：

<img src ="https://img-blog.csdnimg.cn/61b128f00726498296411808df2d1556.png#pic_center" width = 48%>


**1. 头部**
(1) 会话标识（2 字节） DNS 报文的 ID 标识，对于请求报文和其对应的应答报文，这个字段是相同的，通过它可以区分 DNS 应答报文是哪个请求的响应。
(2) 标志（2 字节） 各字段定义如下：

<img src ="https://img-blog.csdnimg.cn/9cc4a8c4759846e88c13be9975df4ae8.png#pic_center" width = 48%>


- QR（1 bit） 查询/响应标志，0 为查询，1 为响应
- opcode（4 bit） 0 表示标准查询，1 表示反向查询，2 表示服务器状态请求
- AA（1 bit） 表示授权回答
- TC（1 bit） 表示可截断的
- RD（1 bit） 表示期望递归
- RA（1 bit） 表示可用递归
- rcode（4 bit） 表示返回码，0 表示没有差错，3 表示名字差错，2 表示服务器错误（Server Failure）

(3) 数量字段（总共 8 字节）： 各自表示后面的四个区域的数目。
- Questions 表示查询问题区域节的数量
- Answers 表示回答区域的数量
- Authoritative nameservers 表示授权区域的数量
- Additional recoreds 表示附加区域的数量



**2. 正文 **

正文部分由查询区域和资源记录区域组成。
**(1) 查询区域**

<img src ="https://img-blog.csdnimg.cn/984f7a5f7bf3478cafbdc176fd74611d.png#pic_center" width = 48%>


查询名：长度不固定，且不使用填充字节，一般该字段表示的就是需要查询的域名（如果是反向查询，则为 IP ，反向查询即由 IP 地址反查域名）。其构成如下：

<img src ="https://img-blog.csdnimg.cn/880b8cc208fa4949b6617b7d9bbedb5a.png#pic_center" width = 48%>

查询类型：规定如下

<img src ="https://img-blog.csdnimg.cn/c4041825086d49a5a658343e304f2481.png#pic_center" width = 48%>


注：查询类通常为 1 ，表明是 Internet 数据。

(2) 资源记录 (RR) 区域（包括回答区域、授权区域和附加区域）

<img src ="https://img-blog.csdnimg.cn/8e1344162dae40568808d148efc2e190.png#pic_center" width = 48%>

这三个区域分别是：回答区域，授权区域和附加区域，其格式都是一样的。

域名（ 2 字节或不定长）：格式和 Queries 区域的查询名字字段是一样的；
查询类型：表明资源纪录的类型，与查询类型表格相同；
查询类：对于 Internet 信息，总是 IN ；
生存时间（TTL）：以秒为单位，表示的是资源记录的生命周期；
资源数据：可变长字段，表示按照查询段的要求返回的相关资源记录的数据。


### 1.4 NS 类型的 DNS 解析报文分析

#### 1.4.1 如何捕获 NS 类型的 DNS 报文

DNS 中 NS 记录 NS（Name Server）记录是域名服务器记录，用来指定该域名由哪个 DNS 服务器来进行解析。 在注册域名时，总有默认的 DNS 服务器，每个注册的域名都是由一个 DNS 域名服务器来进行解析的，DNS 服务器 NS 记录地址一般以以下的形式出现：`ns1.domain.com`、`ns2.domain.com` 等。 简单的说，NS 记录是指定由哪个 DNS 服务器解析你的域名。

在执行 nslookup 时，可以通过指定参数 -type=NS 来查询指定域名对应的域名服务器。如下图所示。

<img src ="https://img-blog.csdnimg.cn/392ce4baac554eb1ae814e5fc1f6e52e.png#pic_center" width = 48%>

#### 1.4.2 解析 DNS 请求报文

通过 Wireshark 可以抓取执行上述操作报文列表。筛选 DNS 协议的报文，找到查询请求报文，展开如下图所示。

<img src ="https://img-blog.csdnimg.cn/11c6ed15911340188c3d610607a3c281.png#pic_center" width = 48%>

可以看出，请求查询报文的的 Type 字段为 NS ，即 Authorizative Name Server 。即希望得到权威的名字服务。该请求报文是通过 UDP 协议进行传输的，端口号为 53 。



传输层协议使用 TCP 还是 UDP ？
DNS 可以使用 UDP/53 ，也可以使用 TCP/53 。当响应报文的长度小于 512B 时，就使用 UDP (因为 UDP 的最大报文长度为 512B )；若响应报文的长度超过 512B ，则选用 TCP 。DNS 协议关于 UDP 和 TCP 的选择通常为以下两种情况：
(1) 若 DNS 客户程序事先知道响应报文的长度超过 512B ，则应当使用 TCP 连接；

注意：主域名服务器与辅助域名服务器在进行区域传送时，通常数据量都比较大，所以 DNS 规定，区域传送使用 TCP 协议。

(2) 若解析程序不知道响应报文的长度，它一般使用 UDP 协议发送 DNS 查询报文，若 DNS 响应报文的长度大于 512B ，服务器就截断响应报文，并把 TC(truncated) 置为 1 。在这种情况下，DNS 客户程序通常使用 TCP 重发原来的查询请求，从而它将来能够从 DNS 服务器中收到完整的响应。


#### 1.4.3 解析 DNS 应答报文
查看随后的响应报文，可以看到有多个响应报文。这些报文就是在进行解析baidu.com域名对应的权威服务器过程中响应的报文。展开这些报文，可以看到第一个响应报文如下图所示。

<img src ="https://img-blog.csdnimg.cn/fe6ca0053f414f14999b391d1e6e1d46.png#pic_center" width = 48%>


该报文应答部分有多个服务器地址，其第一个地址类型为 SOA（start of a zone of an authority），即权威区域的开始。其后的服务器地址类型为 SRV（Server selection），即服务器选择。
随后的多个报文都是对查询报文的响应。

由于前述响应报文长度大于 512B ，随后再次出现了一个查询请求报文，查看其传输层协议，可以看到换用了 TCP 协议。
同样有多个应答报文进行响应。查看这些报文的应答类型，有些是 SRV ，有些是 A（Address，内容是具体的 IP 地址）。
查看最后一个应答报文，如下图所示。

<img src ="https://img-blog.csdnimg.cn/4f9ae992196f411b959f8b5a2968385e.png#pic_center" width = 48%>

可以看出，其权威 DNS 服务器的名称为：`ns.dns.cluster.local`。

### 1.5 反向 DNS 解析
#### 1.5.1 反向解析

在 nslookup 中，类型参数设为 PTR 表示反向解析。反向解析是用于将一个 IP 地址映射到对应的域名，也可以看成是 A 记录的反向，IP 地址的反向解析。下图演示了反向解析 IP 地址39.156.69.79的操作。

注意：反向解析时IP地址的顺序也是反的

<img src ="https://img-blog.csdnimg.cn/53395b09e09f4efe8def9b5bfe94820b.png#pic_center" width = 48%>

反向解析查询报文
下图是 Wireshark 抓获的查询报文。

<img src ="https://img-blog.csdnimg.cn/ba24d874cdec45e9bd048ac9c0837a44.png#pic_center" width = 48%>

展开 Query 段，可以看到，此报文的 Type 为 PTR ，即反向解析。反向解析的 name 是 IP 地址再加了in-addr.arpa这部分。

反向解析响应报文
下图是 Wireshark 抓获的反向解析应答报文。

<img src ="https://img-blog.csdnimg.cn/9e9df9643b3e4a9390ccbab69609e747.png#pic_center" width = 48%>

展开该报文的 Answers 部分，可以看到该段的 Type 是 PTR ，查询的 name 是 IP 地址加`in-addr.arpa` 部分，而响应的 Domain Name 的值为：`79-69-156-39.dynamic.dsl.as9105.com`。

### 1.6 指定服务器的DNS报文分析

打开 Wireshark ，并在过滤器中输入 DNS 。筛选出 DNS 协议报文，并开始捕获报文。然后打开终端，输入命令并执行 `nslookup baidu.com 114.114.114.114`，在 Wireshark 中停止捕获报文；

<img src ="https://img-blog.csdnimg.cn/a485f23ef6f3452eb0133d16f25c2045.png#pic_center" width = 48%>

从报文列表可以看出，经历了多次查询与应答，在最后一轮才得到了baidu.com的 A 地址。查询的百度域名依次为：

```html
baidu.com.default.svc.cluster.local
baidu.com.svc.cluster.local
baidu.com.cluster.local
baidu.com
```

依次查看其应答报文，可以看出，前几次的应答都是 Authoritative Nameserver ，类型为 SOA ，即域名分区，没有得到真正的 IP 地址；只有最后一次才得到 Answers ，其类型 Type 为 A ，其 IP 地址为 `220.181.38.148，39.156.69.79`。


补充：ipconfig

*ipconfig*（对于Windows）和*ifconfig*（对于Linux / Unix）是主机中最实用的程序，尤其是用于调试网络问题时。这里我们只讨论*ipconfig*，尽管Linux / Unix的*ifconfig*与其非常相似。 *ipconfig*可用于显示您当前的TCP/IP信息，包括您的地址，DNS服务器地址，适配器类型等。例如，您只需进入命令提示符，输入

```bash
ipconfig /all
```

所有关于您的主机信息都类似如下面的屏幕截图所显示。

<img src ="https://img-blog.csdnimg.cn/2bd29bf160f44063b7b4d330ab62669c.png#pic_center" width = 48%>


*ipconfig*对于管理主机中存储的DNS信息也非常有用。在第2.5节中，我们了解到主机可以缓存最近获得的DNS记录。要查看这些缓存记录，在 C:\\> 提示符后输入以下命令：

`ipconfig /displaydns`

每个条目显示剩余的生存时间（TTL）（秒）。要清除缓存，请输入

`ipconfig /flushdns`

清除了所有条目并从hosts文件重新加载条目。


## 2 实验分析

现在，我们熟悉`nslookup`和`ipconfig`，我们准备好了一些正经的事情。首先让我们捕获一些由常规上网活动生成的DNS数据包。

* 使用*ipconfig*清空主机中的DNS缓存。
* 打开浏览器并清空浏览器缓存。 （若使用Internet Explorer，转到**工具**菜单并选择**Internet选项**；然后在**常规**选项卡中选择删除文件。）
* 打开Wireshark，然后在过滤器中输入“ip.addr==your_IP_address”，您可以先使用*ipconfig*获取你的IP地址。此过滤器将删除既从你主机不发出也不发往你主机的所有数据包。
* 在Wireshark中启动数据包捕获。
* 使用浏览器访问网页： https://www.nuaa.edu.cn/
* 停止数据包捕获。

<img src ="https://img-blog.csdnimg.cn/3da7cdc0e56242b6b488c7976457705b.png#pic_center" width = 48%>

1. 运行nslookup 以获取一个亚洲的Web 服务器的IP 地址。该服务器的IP 地址
是什么？

答：这里使用的阿里的公众 `DNS 223.5.5.5` 替代我的 ISP 服务商的 DNS 进行查
询，这里我查询的是南航(https://www.nuaa.edu.cn/)的IP 地址。可以在图中看到我请求阿里公共DNS 来获取南航的IP 地址，为：218.94.136.180。


由于干扰很大，这里使用现成的包来分析。

1. 找到DNS查询和响应消息。它们是否通过UDP或TCP发送？
答：是 UDP。
<img src ="https://img-blog.csdnimg.cn/fd9e241c1df64ddeb25b1957f41afe70.png#pic_center" width = 48%>


5. DNS是查询消息的目标端口是什么？ DNS响应消息的源端口是什么？
答：都是 53 端口。
<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/7935b2345026451c89fa6a7a67eeb951.png#pic_left" width = "48%"><img src = "https://img-blog.csdnimg.cn/a9c21669caab4473b37c667879a419e3.png#pic_left"  width = "48%"></center></p>


6. DNS 查询消息发送到哪个 IP 地址？使用 ipconfig 来确定本地 DNS 服务器的 IP 地址。这两个 IP 地址是否相同？

<img src ="https://img-blog.csdnimg.cn/ab6c72428d1d4da7979864318ab18cba.png#pic_center" width = 48%>

7. 检查 DNS 查询消息。DNS 查询是什么 "Type" 的？查询消息是否包含任何 "answers"？
答：Type 为 “A”，表示查询 IP 地址，没有任何 "answers"。
<img src ="https://img-blog.csdnimg.cn/f8ab6044cfff4f23afaa2936ec0a3651.png#pic_center" width = 48%>



8. 检查DNS响应消息。提供了多少个"answers"？这些答案具体包含什么？
答：提供了 2 个 "answers"，是该域名的 2 个 IPV4 地址。
<img src ="https://img-blog.csdnimg.cn/b4afaf11a0764f7caef34f1be48d17de.png#pic_center" width = 48%>



9. 考虑从您主机发送的后续 TCP SYN 数据包。 SYN 数据包的目的 IP 地址是否与 DNS 响应消息中提供的任何 IP 地址相对应？
答：是相对应的。
<img src ="https://img-blog.csdnimg.cn/be372be948c440488a8658ad46c351f4.png#pic_center" width = 48%>



10. 这个网页包含一些图片。在获取每个图片前，您的主机是否都发出了新的 DNS 查询？
答：没有，因为本机 DNS 已经被缓存了，因此不需要发起新的 DNS 查询。


11. DNS查询消息的目标端口是什么？ DNS响应消息的源端口是什么？
答：目标端口和源端口都是 53。
<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/5eb99cb0a716410ca00064911b9a85c3.png#pic_left" width = "48%"><img src = "https://img-blog.csdnimg.cn/7c5281239db64a69a57cc955e5a8959b.png#pic_left"  width = "48%"></center></p>

2. DNS 查询消息的目标 IP 地址是什么？这是你的默认本地 DNS 服务器的 IP 地址吗？
答：225.3.3.3，是我修改的默认本地 DNS 服务器的 IP 地址。
<p><center class = "half"><img src ="https://img-blog.csdnimg.cn/d9d59d122cf94912b28176a093ebd835.png#pic_left" width = "48%"><img src = "https://img-blog.csdnimg.cn/b6f29284d0394c22a31878673cf1c17d.png#pic_left"  width = "48%"></center></p>

13. 检查 DNS 查询消息。DNS 查询是什么 "Type" 的？查询消息是否包含任何 "answers"？
答：Type 为 “A”，表示查询 IP 地址，没有任何 "answers"。

<img src ="https://img-blog.csdnimg.cn/71a1c877e289498e99912b21cd259c0b.png#pic_center" width = 48%>

14. 检查 DNS 响应消息。提供了多少个 "answers"？这些答案包含什么？
答：提供了 1 个 "answers"，是该域名的 IPV4 地址。

<img src ="https://img-blog.csdnimg.cn/75cd727c70754e5fb35b74c1068f175d.png#pic_center" width = 48%>


现在重复上一个实验，但换成以下命令：

```bash
nslookup www.aiit.or.kr bitsy.mit.edu
```

<img src ="https://img-blog.csdnimg.cn/740002f9e33a4da9a741161a05b75eed.png#pic_center" width = 48%>


15. DNS 查询消息发送到的 IP 地址是什么？这是您的默认本地 DNS 服务器的 IP 地址吗？

答：`18.0.72.3`，不是我的默认本地 DNS 服务器的 IP 地址。

<img src ="https://img-blog.csdnimg.cn/e510a941e7114b4195c801e4b3f61d8b.png#pic_center" width = 48%>



2. 检查DNS查询消息。DNS 查询是什么 "Type" 的？查询消息是否包含任何 "answers"？
答：Type 为 “A”，表示查询 IP 地址，没有任何 "answers"。

<img src ="https://img-blog.csdnimg.cn/8fb4860e0ffe4950a5b446ba013abc56.png#pic_center" width = 48%>


3. 检查 DNS 响应消息。提供了多少个 "answers"？这些答案包含什么？
答：提供了 1 个 "answers"，是该域名的 IPV4 地址。

<img src ="https://img-blog.csdnimg.cn/4b15bc3e2e864d29930baef5812b92c5.png#pic_center" width = 48%>

____

补充：dig命令

命令行工具 dig 可以跟 DNS 服务器互动，它的查询语法如下（美元符号$是命令行提示符）
```bash
$ dig @[DNS 服务器] [域名]
```


网上有很多公用的 DNS 服务器，这篇文章选择 Cloudflare 公司提供的 1.1.1.1 进行演示,向 1.1.1.1 查询域名，就执行下面的命令。

<img src ="https://img-blog.csdnimg.cn/46a41471b8f247519e1e2f40075813db.png#pic_center" width = 48%>




______

## 参考
- DNS 原理入门：[http://www.ruanyifeng.com/blog/2016/06/dns.html](http://www.ruanyifeng.com/blog/2016/06/dns.html)
- DNS 查询原理详解：[http://www.ruanyifeng.com/blog/2022/08/dns-query.html](http://www.ruanyifeng.com/blog/2022/08/dns-query.html)
- DNS协议分析：[https://www.educoder.net/shixuns/4yze3kp5/challenges](https://www.educoder.net/shixuns/4yze3kp5/challenges)
- 《计算机网络－自顶向下方法》笔记：[https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)
- Wireshark实验——DNS域名系统：[https://www.cnblogs.com/linfangnan/p/12771157.html](https://www.cnblogs.com/linfangnan/p/12771157.html)