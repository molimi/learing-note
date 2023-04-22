## 1 WEB服务器编程实现

## 1 Python3 网络编程
### 1.1 介绍

本文将首先利用 Python 实现面向TCP连接的套接字编程基础知识：如何创建套接字，将其绑定到特定的地址和端口，以及发送和接收数据包。其次还将学习 HTTP 协议格式的相关知识。在此基础上，本篇将用 Python 语言开发一个简单的 Web 服务器，它仅能处理一个HTTP连接请求。

Web 服务器的基本功能是接受并解析客户端的 HTTP 请求，然后从服务器的文件系统获取所请求的文件，生成一个由头部和响应文件内容所构成成的 HTTP 响应消息，并将该响应消息发送给客户端。如果请求的文件不存在于服务器中，则服务器应该向客户端发送“404 Not Found”差错报文。

具体的过程分为：
    - 当一个客户（浏览器）连接时，创建一个连接套接字；
    - 从这个连接套接字接收 HTTP 请求；
    - 解释该请求以确定所请求的特定文件；
    - 从服务器的文件系统获得请求的文件；
    - 创建一个由请求的文件组成的 HTTP 响应报文，报文前面有首部行；
    - 经 TCP 连接向请求浏览器发送响应。
    - 如果浏览器请求一个在该服务器中不存在的文件，服务器应当返回一个“404 Not Found”差错报文。

要实现 Web 服务器，需使用套接字 Socket 编程接口来使用操作系统提供的网络通信功能。
Socket 是应用层与 TCP/IP 协议族通信的中间软件抽象层，是一组编程接口。它把复杂的 TCP/IP 协议族隐藏在 Socket 接口后面，对用户来说，一组简单的接口就是全部，让 Socket 去组织数据，以符合指定的协议。使用 Socket 后，无需深入理解 TCP/UDP 协议细节（因为Socket 已经为我们封装好了），只需要遵循 Socket 的规定去编程，写出的程序自然就是遵循 TCP/UDP 标准的。Socket 的地位如下图所示：

<img src ="https://img-blog.csdnimg.cn/87bbbfc842844ab98cb3abbb77c4bd36.png#pic_center" width = 48%>

从某种意义上说，Socket 由地址IP和端口Port构成。IP 是用来标识互联网中的一台主机的位置，而 Port 是用来标识这台机器上的一个应用程序，IP 地址是配置到网卡上的，而 Port 是应用程序开启的，IP 与 Port 的绑定就标识了互联网中独一无二的一个应用程序。

套接字类型
- 流式套接字（SOCK_STREAM）：用于提供面向连接、可靠的数据传输服务。————TCP
- 数据报套接字（SOCK_DGRAM）：提供了一种无连接的服务。该服务并不能保证数据传输的可靠性，数据有可能在传输过程中丢失或出现数据重复，且无法保证顺序地接收到数据。————UDP
- 原始套接字（SOCK_RAW）：主要用于实现自定义协议或底层网络协议。

在本 WEB 服务器程序实验中，采用流式套接字进行通信。其基本模型如下图所示：

<img src ="https://img-blog.csdnimg.cn/909d13fc5554419f9e4c668df9a36418.png#pic_center" width = 48%>


其工作过程如下：服务器首先启动，通过调用 `socket()` 建立一个套接字，然后调用绑定方法 `bind()` 将该套接字和本地网络地址联系在一起，再调用 `listen()` 使套接字做好侦听连接的准备，并设定的连接队列的长度。客户端在建立套接字后，就可调用连接方法 `connect()` 向服务器端提出连接请求。服务器端在监听到连接请求后，建立和该客户端的连接，并放入连接队列中，并通过调用 `accept()` 来返回该连接，以便后面通信使用。客户端和服务器连接一旦建立，就可以通过调用接收方法 `recv()／recvfrom()` 和发送 方法 `send()／sendto()` 来发送和接收数据。最后，待数据传送结束后，双方调用 `close()` 关闭套接字。


> 套接字这个词对很多不了解网络编程的人来说显得非常晦涩和陌生，其实说得通俗点，套接字就是一套用C语言写成的应用程序开发库，主要用于实现进程间通信和网络编程，在网络应用开发中被广泛使用。在Python中也可以基于套接字来使用传输层提供的传输服务，并基于此开发自己的网络应用。实际开发中使用的套接字可以分为三类：流套接字（TCP套接字）、数据报套接字和原始套接字。

## 2 创建TCP套接字
### 2.1 套接字

套接字（Socket）是一个抽象层，应用程序可以通过它发送或接收数据，可对其进行像对文件一样的打开、读写和关闭等操作。套接字允许应用程序将 I/O 插入到网络中，并与网络中的其他应用程序进行通信。网络套接字是 IP 地址与端口 Port 的组合。

为了满足不同的通信程序对通信质量和性能的要求，网络系统提供了三种不同类型的套接字，以供用户在设计网络应用程序时根据不同的要求来选择。分别是：

- 流式套接字（SOCK-STREAM）。提供一种可靠的、面向连接的双向数据传输服务，实现了数据无差错、无重复的发送。流式套接字内设流量控制，被传输的数据看作是无记录边界的字节流。在 TCP/IP 协议簇中，使用 TCP 协议来实现字节流的传输，当用户想要发送大批量的数据或者对数据传输有较高的要求时，可以使用流式套接字。
- 数据报套接字（SOCK-DGRAM）。提供一种无连接、不可靠的双向数据传输服务。数据包以独立的形式被发送，并且保留了记录边界，不提供可靠性保证。数据在传输过程中可能会丢失或重复，并且不能保证在接收端按发送顺序接收数据。在 TCP/IP 协议簇中，使用 UDP 协议来实现数据报套接字。在出现差错的可能性较小或允许部分传输出错的应用场合，可以使用数据报套接字进行数据传输，这样通信的效率较高。
- 原始套接字（SOCK-RAW）。该套接字允许对较低层协议（如 IP 或 ICMP ）进行直接访问，常用于网络协议分析，检验新的网络协议实现，也可用于测试新配置或安装的网络设备。


所谓TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口。在Python中可以通过创建 `socket` 对象并指定type属性为SOCK_STREAM来 使用TCP套接字。由于一台主机可能拥有多个IP地址，而且很有可能会配置多个不同的服务，所以作为服务器端的程序，需要在创建套接字对象后将其绑定到指定的IP地址和端口上。这里的端口并不是物理设备而是对IP地址的扩展，用于区分不同的服务，例如我们通常将HTTP服务跟80端口绑定，而MySQL数据库服务默认绑定在3306端口，这样当服务器收到用户请求时就可以根据端口号来确定到底用户请求的是HTTP服务器还是数据库服务器提供的服务。端口的取值范围是0~65535，而1024以下的端口我们通常称之为“著名端口”（留给像FTP、HTTP、SMTP等“著名服务”使用的端口，有的地方也称之为“周知端口”），自定义的服务通常不使用这些端口，除非自定义的是HTTP或FTP这样的著名服务。

Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。


### 2.2 如何创建套接字

套接字 Socket 实质上提供了主机间进程通信的连接点。进程通信之前,双方首先必须各自创建一个连接点,否则是没有办法建立联系并相互通信的。Python 中，我们用 `socket()` 函数来创建套接字，语法格式如下：

```python
my_socket = socket(socket_family, socket_type, protocol=0)
'''
socket_family可以是如下参数之一：
  　　AF_INET IPv4（默认）
　　  AF_INET6 IPv6
　　  AF_UNIX 只能够用于单一的Unix系统进程间通信
socket_type可以是如下参数之一:
　　  SOCK_STREAM　　流式socket , for TCP （默认）
　  　SOCK_DGRAM　　 数据报式socket , for UDP
　  　SOCK_RAW 原始套接字
'''

**Socket 对象(内建)方法**

<table> <thead> <tr> <th align="left">函数</th> <th align="left">描述</th> </tr> </thead> <tbody><tr> <td align="left">服务器端套接字</td>  </tr> <tr> <td align="left">s.bind()</td> <td align="left">绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。</td> </tr> <tr> <td align="left">s.listen()</td> <td align="left">开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。</td> </tr> <tr> <td align="left">s.accept()</td> <td align="left">被动接受TCP客户端连接,(阻塞式)等待连接的到来</td> </tr> <tr> <td align="left">客户端套接字</td>  </tr> <tr> <td align="left">s.connect()</td> <td align="left">主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。</td> </tr> <tr> <td align="left">s.connect_ex()</td> <td align="left">connect()函数的扩展版本,出错时返回出错码,而不是抛出异常</td> </tr> <tr> <td align="left">公共用途的套接字函数</td>  </tr> <tr> <td align="left">s.recv()</td> <td align="left">接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。</td> </tr> <tr> <td align="left">s.send()</td> <td align="left">发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。</td> </tr> <tr> <td align="left">s.sendall()</td> <td align="left">完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。</td> </tr> <tr> <td align="left">s.recvfrom()</td> <td align="left">接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。</td> </tr> <tr> <td align="left">s.sendto()</td> <td align="left">发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。</td> </tr> <tr> <td align="left">s.close()</td> <td align="left">关闭套接字</td> </tr> <tr> <td align="left">s.getpeername()</td> <td align="left">返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。</td> </tr> <tr> <td align="left">s.getsockname()</td> <td align="left">返回套接字自己的地址。通常是一个元组(ipaddr,port)</td> </tr> <tr> <td align="left">s.setsockopt(level,optname,value)</td> <td align="left">设置给定套接字选项的值。</td> </tr> <tr> <td align="left">s.getsockopt(level,optname[.buflen])</td> <td align="left">返回套接字选项的值。</td> </tr> <tr> <td align="left">s.settimeout(timeout)</td> <td align="left">设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）</td> </tr> <tr> <td align="left">s.gettimeout()</td> <td align="left">返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。</td> </tr> <tr> <td align="left">s.fileno()</td> <td align="left">返回套接字的文件描述符。</td> </tr> <tr> <td align="left">s.setblocking(flag)</td> <td align="left">如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。</td> </tr> <tr> <td align="left">s.makefile()</td> <td align="left">创建一个与该套接字相关连的文件</td> </tr> </tbody></table>



### 2.3 如何为套接字绑定主机及端口

一个完整的 Socket 可以用一个通信双方的相关描述：
         {协议,本地地址,本地端口,远程地址,远程端口}

实际应用中，在创建一个 Socket 时先用一个半相关描述（服务器这一半可以确定，而另一半尚不确定）:
         {协议,本地地址,本地端口}
每一个 Socket 有一个本地的唯一端口号，由操作系统分配。

绑定指为套接字绑定地址包含主机及其端口。 在 AF_INET 下，以元组（host,port）的形式表示地址。
- host：用字符串表示主机的 IP 地址。表示本机‘’，也可用‘127.0.0.1’表示回环地址，或者主机的一般 IP 地址。
- port：端口号，数字表示。1024 以下为系统约定，自定义的用 1024 以上。

绑定通过套接字的绑定方法 `bind()` 来完成，输入参数为元组 `(host,port)`。
绑定示例：

```python
my_socket.bind(('127.0.0.1', 1234))         # 绑定本地回环地址
my_socket.bind(('', 1234))                  # 自动获取IP地址
```

### 2.4 如何设置套接字监听

服务器程序在调用创建套接字 `socket()` 和绑定 `bind()` 之后需要处于监听状态，因为不知客户端什么时候开始进行请求连接。为此，需调用套接字的监听方法 `listen()`。

一个服务端可能同时面对多个客户端的连接请求，为此服务器程序需创建一个连接队列来保存的连接请求，并依次为连接请求建立相应连接。为此需设置队列的大小作为监听方法的参数。
监听示例：

```python
my_socket.listen(10)    # 设置连接队列大小为10，并使套接字处于监听状态。
```

### 2.5 服务端获取连接请求
#### 2.5.1 如何获取客户端的连接请求

当服务器中的套接字监听到了连接请求之后，内核和客户建立连接，并将连接放入连接队列中。典型的服务器程序是可以同时服务多个客户端的，当有客户端发起连接时，服务器就调用 `accept()` 返回并接收这个连接，如果有大量客户端发起请求，服务器来不及处理，还没有 accept 的客户端就处于连接等待状态。如果服务器调用 `accept()` 时还没有客户端的连接请求，就阻塞等待直到有客户端连接上来。

示例：

```python
connection_socket，addr = my_socket.accept()
'''
返回值： 
connectionSocket 客户端连接套接字
addr 连接的客户端地址
'''
```

这里的 connectionSocket 称为客户端连接套接字，是 `accept()` 接收到一个客户端连接请求后返回的一个新的套接字，它代表了服务端和客户端的连接。后面可以用于读取数据以及关闭连接。

#### 2.5.2 如何获取客户端发送的报文内容

服务器与客户端的连接建立好之后，就可以接收或发送消息操作。相应有下面几组方法：

```python
recv()/send()
recvmsg()/sendmsg()
recvfrom()/sendto()
```
接收报文方法 `recv()` 用法如下：

```python
data = socket.recv(buffersize)
'''
　　　　　功能 ： 接收对应客户端消息
　　　　　参数 ： 一次最多接收多少字节
　　　　　返回值 ： 接收到的内容
　　　    *  如果没有消息则会阻塞等待
'''
```

### 2.6 服务端读取请求文件内容

#### 2.6.1 如何获取客户端请求的网页文件名

HTTP 请求是客户端通过发送信息向服务器请求对资源的访问。HTTP 请求由三部分组成：请求行、请求头和请求正文。

```python
POST /index.html HTTP/1.1   # 请求方法 url 协议及版本号
Host: localhost             # 主机地址
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:10.0.2) Gecko/20100101 Firefox/10.0.2
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: <a target=_blank href="http://localhost/" style="color: rgb(51, 102, 153); text-decoration: none;">http://localhost/</a>
Content-Length：25
Content-Type：application/x-www-form-urlencoded
`     `
username=aa&password=1234             # 请求体
```

从上方代码可以看出，请求网页文件名位于请求行（第一行）中用空格分隔的第二个部分。

在获得请求文件名后，读取文件内容使用文件操作来实现。Python 提供了必要的函数和方法进行默认情况下的文件基本操

### 2.7 服务端响应请求头部信息
#### 2.7.1 WEB服务器响应消息头部定义

WEB 服务器在接收到客户端的连接请求后，接下来就会响应该请求。HTTP 响应报文由三部分组成：响应行、响应头、响应体。如下图所示。

<img src ="https://img-blog.csdnimg.cn/56b40737ea794b419a6078d46adc13bb.png#pic_center" width = 48%>

- 响应行：一般由协议版本、状态码及其描述组成，比如 `HTTP/1.1 200 OK` 其中协议版本 `HTTP/1.1` 或者 `HTTP/1.0`，`200` 就是它的状态码，`OK` 则为它的描述。
- 响应头：用于描述服务器的基本信息，以及数据的描述，服务器通过这些数据的描述信息，可以通知客户端如何处理它回送的数据。

常见的响应头字段含义：
    - Allow：服务器支持哪些请求方法(如GET、POST等)。
    - Content-Encoding：文档的编码(Encode)方法。
    - Content-Length：表示内容长度。
    - Content-Type：表示后面的文档属于什么MIME类型。
    - Date：当前的GMT时间
    - Expires：告诉浏览器把回送的资源缓存多长时间，-1或0则是不缓存。
    - Last-Modified：文档的最后改动时间。
    - Location：用于重定向接收者到一个新URI地址。
    - Refresh：告诉浏览器隔多久刷新一次，以秒计。
    - Server：服务器通过这个头告诉浏览器服务器的类型。

在这个 WEB 服务器返回的头部信息示例如下：

```python
HTTP/1.1 200 OK
Connection: close
Content-Type: text/html
Content-Length: 24
```

#### 2.7.2 发送响应消息头部内容

在定义好响应消息的头部信息后，使用套接字的 send 方法发送即可。
在发送前需要使用编码 `encode()` 方法，将字符串转换为字节数组后发送。
例如：
```python
socket.send(header.encode())
```

#### 2.7.3 如何捕获请求文件读取错误的异常

在本服务器程序中，采用 `try...except` 结构来捕获异常。当请求的文件不存在（可能是文件名错误或路径错误）及其他可能导致文件访问错误（如没有相应权限）时，就会产生 IOError 异常。从而进入异常处理部分代码。

**发送自定义的异常信息给客户端**

在异常处理代码中，定义响应客户端请求文件不存在的响应消息头代码 404 及消息内容not Found。

将此响应消息头发给客户端，可以使用 socket 的发送方法 `send()` 完成，发送前需要使用编码方法 `encode()` 对响应消息进行编码。


**完整代码如下：**

```python
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) 
# Prepare a sever socket 
serverSocket.bind(("127.0.0.1",6789))
serverSocket.listen(1)

while True:
    print('开始WEB服务...')
    try:
            connectionSocket, addr = serverSocket.accept()
            message = connectionSocket.recv(1024) # 获取客户发送的报文
            
            # 读取文件内容
            filename = message.split()[1]       
            f = open(filename[1:])
            outputdata = f.read()
            
            # 向套接字发送头部信息
            header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
            connectionSocket.send(header.encode())

            # 发送请求文件的内容
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            
            # 关闭连接
            connectionSocket.close()
    except IOError:             # 异常处理
            # 发送文件未找到的消息
            header = ' HTTP/1.1 404 not Found'
            #########Begin#########
            connectionSocket.send(header.encode())
            #########End#########
            # 关闭连接
            connectionSocket.close()
    # 关闭套接字
    serverSocket.close()
```

### 2.8 示例分析

**1. 服务端**

下面的代码实现了一个提供时间日期的服务器。

```python
# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230420
# @Version: 1.0
# @Description: 一个提供时间日期的服务器
# @Filename: server.py

from socket import socket, SOCK_STREAM, AF_INET, gethostname
from datetime import datetime

def main():
    # 1. 创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP地址和端口（端口用于区分不同的服务）
    # 同一个时间在同一个端口只能绑定一个服务否则报错
    # server.bind(('192.168.1.2', 1030))
    host = gethostname()            # 获取本地主机名
    port = 9999                     # 绑定端口号
    server.bind((host, port))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小，超过后排队
    server.listen(512)
    print("服务器启动开始监听……")
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + "连接到了服务器.")
        # 5. 发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. 断开连接
        client.close()

if __name__ == "__main__":
    main()
```


> 查找自己电脑IP和端口的方法：
>   **第一步： Win+R**
>   **第二步： 输入：cmd  然后点击确定（Enter）进入**
>   **第三步： 输入：ipconfig  然后Enter**
>   **第四步： 输入：netstat 然后Enter**  一般用第一个就行

<img src ="https://img-blog.csdnimg.cn/ac240a014d184b73a7a51927c288b7f7.png#pic_center" width = 48%>

运行服务器程序后我们可以通过Windows系统的telnet来访问该服务器，结果如下图所示。

<center class = "half"><img src ="https://img-blog.csdnimg.cn/fb0fb5b6873e49ff821880f77261afcd.png#pic_left" width = "30%"><img src = "https://img-blog.csdnimg.cn/71394f87909c418ea6c19b8f60b964af.png#pic_left"  width = "48%"></center></p>

Windows开启telnet服务，见下图所示：

<img src ="https://img-blog.csdnimg.cn/d2de3e8cfba444fb80940100e54eeb21.gif#pic_center" width = 48%>


当然我们也可以通过Python的程序来实现TCP客户端的功能，相较于实现服务器程序，实现客户端程序就简单多了，代码如下所示。


**2. 客户端**

```python
# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230420
# @Version: 1.0
# @Description: 一个接受时间日期的客户端
# @Filename: client.py

from socket import socket, SOCK_STREAM, AF_INET, gethostname

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    # client = socket()
    client = socket(family=AF_INET, type=SOCK_STREAM)

    # 2.连接到服务器（需要指定IP地址和端口）
    # client.connect(('10.69.164.78', 1030))
    host = gethostname()            # 获取本地主机名
    port = 9999                     # 绑定端口号
    client.connect((host, port))

    # 3.从服务器接受数据, 接收小于 1024 字节的数据
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()
```

现在我们打开两个终端，第一个终端执行 `server.py` 文件：
```bash
python3 server.py
```
第二个终端执行 `client.py` 文件：
```bash
python3 client.py
2023-04-19 17:04:30.293444
```

这时我们再打开第一个终端，就会看到有以下信息输出：
```bash
('192.168.1.2', 11046)连接到了服务器.
```

需要注意的是，上面的服务器并没有使用多线程或者异步I/O的处理方式，这也就意味着当服务器与一个客户端处于通信状态时，其他的客户端只能排队等待。很显然，这样的服务器并不能满足我们的需求，我们需要的服务器是能够同时接纳和处理多个用户请求的。下面我们来设计一个使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片。


服务器端代码：

```python
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    
    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('192.168.1.2', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('guido.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
```

客户端代码：

```python
from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('192.168.1.2', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')


if __name__ == '__main__':
    main()
```

在这个案例中，我们使用了JSON作为数据传输的格式（通过JSON格式对传输的数据进行了序列化和反序列化的操作），但是JSON并不能携带二进制数据，因此对图片的二进制数据进行了Base64编码的处理。Base64是一种用64个字符表示所有二进制数据的编码方式，通过将二进制数据每6位一组的方式重新组织，刚好可以使用0~9的数字、大小写字母以及“+”和“/”总共64个字符表示从000000到111111的64种状态。[维基百科](https://zh.wikipedia.org/wiki/Base64)上有关于Base64编码的详细讲解，不熟悉Base64的读者可以自行阅读。

## 3 创建数据包套接字

传输层除了有可靠的传输协议TCP之外，还有一种非常轻便的传输协议叫做用户数据报协议，简称UDP。TCP和UDP都是提供端到端传输服务的协议，二者的差别就如同打电话和发短信的区别，后者不对传输的可靠性和可达性做出任何承诺从而避免了TCP中握手和重传的开销，所以在强调性能和而不是数据完整性的场景中（例如传输网络音视频数据），UDP可能是更好的选择。可能大家会注意到一个现象，就是在观看网络视频时，有时会出现卡顿，有时会出现花屏，这无非就是部分数据传丢或传错造成的。

数据包格式套接字（Datagram Sockets）也叫“无连接的套接字”，在代码中使用 SOCK_DGRAM 表示。可以将 SOCK_DGRAM 比喻成高速移动的摩托车快递，它有以下特征：

    - 强调快速传输而非传输顺序；
    - 传输的数据可能丢失也可能损毁；
    - 限制每次传输的数据大小；
    - 数据的发送和接收是同步的。

数据包套接字也使用 IP 协议作路由，但是它不使用 TCP 协议，而是使用 UDP 协议（User Datagram Protocol，用户数据报协议）。

实际应用中，QQ 视频聊天和语音聊天主要使用 SOCK_DGRAM 来传输数据，因为首先要保证通信的效率，尽量减小延迟，而数据的正确性是次要的，即使丢失很小的一部分数据，视频和音频也可以正常解析，最多出现噪点或杂音，不会对通信质量有实质的影响。当然，SOCK_DGRAM 没有想象中的糟糕，不会频繁的丢失数据，数据错误只是小概率事件。

创建UDP套接字，绑定地址包含主机及其端口：

```python
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('0.0.0.0', 12000))
```


### 3.1 UDP Ping服务程序框架

在这个简单的 UDP Ping 服务器程序中，完成套接字创建及绑定后，当接收到消息后进行简单处理（这里是转化为大写），再将消息回传给相应的客户端。

#### 3.1.1 Ping服务端创建UDP套接字



#### 3.1.2 UDP通信中发送与接收数据

在 UDP 通信中，使用 `sendto()` 函数发送 UDP 数据，将数据发送到套接字，输入参数 address 是形式为 `(host, port)` 的元组，指定远程地址，其中host表示服务器地址，port表示服务器端口号。返回值是发送的字节数。

接收数据使用 `recvfrom()` 函数实现。输入参数为接收缓冲区大小。该函数接收 UDP 数据，与 `recv()` 类似，但返回值是 `(data, address)`。其中 `data` 是包含接收数据的字符串，`address` 是发送数据的套接字地址。


示例如下：
- 接收数据
```python
msg,addr=udp_server.recvfrom(BUFSIZE)   # 使用套接字对象udp_server的recvfrom()方法接收数据
```

- 发送数据

```python
udp_server.sendto(msg,addr)     # 使用套接字对象udp_server的sendto()方法发送数据
```

完整的服务器程序一般都处于后台服务状态，通过不断循环等待客户端发送 Ping 消息，经过简单处理后，将消息发给相应的客户端。
在本实验中，为了避免大量资源的消耗，设置了一个接收消息计数器，当接收到消息超过设定值后，服务程序就退出（break）循环。

#### 3.1.3 设置套接字超时时间

在进行客户端向服务器发送 Ping 消息的过程中，有时候可能会因为网络原因造成一直连不上服务器（如服务器程序没有开启），这时如不手动停止，Socket 可能会一直尝试重连，造成资源的浪费。这就需要设置 `timeout` 来限制重连时间，当 Socket 尝试重连到指定的时间时，就会停止一切操作，并提示达到 `timeout` 设定阈值。
设置超时时间一般在创建套接字后，在网络通信之前进行。示例如下：

```python
mysocket.settimeout(10)
```

代码作用为设定套接字的超时时间为 10 秒

### 3.2 客户端创建UDP套接字


客户端程序在创建完套接字后，通过循环向服务器发送消息，然后接收服务器回传的消息，通过计算收到消息及发送消息的时间差，来反映网络的状况。如果超时时间过后还没收到消息，则报出超时异常。

消息编解码
在网络通信中，网络线路中传输的是字节（二进制格式）流bytes。但在我们发送的消息习惯用字符串string来表示，这时就需要用编码encode()和解码decode()函数来转换。

encode()函数：字符串类型（str）提供的方法，用于将字符串类型转换成 bytes 类型，这个过程也称为“编码”。其语法如下：

```python
str.encode([encoding="utf-8"][,errors="strict"])
```

注意，格式中用 [] 括起来的参数为可选参数，也就是说，在使用此方法时，可以使用 [] 中的参数，也可以不使用。



### 3.3 客户端向服务器发送消息并接收消息



____

## 参考

- 网络编程入门：[https://gitee.com/zengyujin/Python-100-Days/blob/master/Day01-15/14.网络编程入门和网络应用开发.md](https://gitee.com/zengyujin/Python-100-Days/blob/master/Day01-15/14.%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8%E5%92%8C%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91.md)
- Python3 网络编程：[https://www.nowcoder.com/tutorial/10005/99e037cb31a1486a8cf8ea61eb58dc8c](https://www.nowcoder.com/tutorial/10005/99e037cb31a1486a8cf8ea61eb58dc8c)
- WEB服务器编程实现：[https://www.educoder.net/shixuns/synqujxr/challenges](https://www.educoder.net/shixuns/synqujxr/challenges)