## 1 Python3 网络编程

## 1 基于传输层协议的套接字编程

套接字这个词对很多不了解网络编程的人来说显得非常晦涩和陌生，其实说得通俗点，套接字就是一套用C语言写成的应用程序开发库，主要用于实现进程间通信和网络编程，在网络应用开发中被广泛使用。在Python中也可以基于套接字来使用传输层提供的传输服务，并基于此开发自己的网络应用。实际开发中使用的套接字可以分为三类：流套接字（TCP套接字）、数据报套接字和原始套接字。

### 1.1 TCP套接字

所谓TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口。在Python中可以通过创建 `socket` 对象并指定type属性为SOCK_STREAM来 使用TCP套接字。由于一台主机可能拥有多个IP地址，而且很有可能会配置多个不同的服务，所以作为服务器端的程序，需要在创建套接字对象后将其绑定到指定的IP地址和端口上。这里的端口并不是物理设备而是对IP地址的扩展，用于区分不同的服务，例如我们通常将HTTP服务跟80端口绑定，而MySQL数据库服务默认绑定在3306端口，这样当服务器收到用户请求时就可以根据端口号来确定到底用户请求的是HTTP服务器还是数据库服务器提供的服务。端口的取值范围是0~65535，而1024以下的端口我们通常称之为“著名端口”（留给像FTP、HTTP、SMTP等“著名服务”使用的端口，有的地方也称之为“周知端口”），自定义的服务通常不使用这些端口，除非自定义的是HTTP或FTP这样的著名服务。

Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。

Python 中，我们用 `socket()` 函数来创建套接字，语法格式如下：

```python
socket.socket([family[, type[, proto]]])
```
参数
- family: 套接字家族可以使AF_UNIX或者AF_INET
- type: 套接字类型可以根据是面向连接的还是非连接分SOCK_STREAM或SOCK_DGRAM
- protocol: 一般不填默认为0.


<table> <thead> <tr> <th align="left">函数</th> <th align="left">描述</th> </tr> </thead> <tbody><tr> <td align="left">服务器端套接字</td>  </tr> <tr> <td align="left">s.bind()</td> <td align="left">绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。</td> </tr> <tr> <td align="left">s.listen()</td> <td align="left">开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。</td> </tr> <tr> <td align="left">s.accept()</td> <td align="left">被动接受TCP客户端连接,(阻塞式)等待连接的到来</td> </tr> <tr> <td align="left">客户端套接字</td>  </tr> <tr> <td align="left">s.connect()</td> <td align="left">主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。</td> </tr> <tr> <td align="left">s.connect_ex()</td> <td align="left">connect()函数的扩展版本,出错时返回出错码,而不是抛出异常</td> </tr> <tr> <td align="left">公共用途的套接字函数</td>  </tr> <tr> <td align="left">s.recv()</td> <td align="left">接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。</td> </tr> <tr> <td align="left">s.send()</td> <td align="left">发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。</td> </tr> <tr> <td align="left">s.sendall()</td> <td align="left">完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。</td> </tr> <tr> <td align="left">s.recvfrom()</td> <td align="left">接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。</td> </tr> <tr> <td align="left">s.sendto()</td> <td align="left">发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。</td> </tr> <tr> <td align="left">s.close()</td> <td align="left">关闭套接字</td> </tr> <tr> <td align="left">s.getpeername()</td> <td align="left">返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。</td> </tr> <tr> <td align="left">s.getsockname()</td> <td align="left">返回套接字自己的地址。通常是一个元组(ipaddr,port)</td> </tr> <tr> <td align="left">s.setsockopt(level,optname,value)</td> <td align="left">设置给定套接字选项的值。</td> </tr> <tr> <td align="left">s.getsockopt(level,optname[.buflen])</td> <td align="left">返回套接字选项的值。</td> </tr> <tr> <td align="left">s.settimeout(timeout)</td> <td align="left">设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）</td> </tr> <tr> <td align="left">s.gettimeout()</td> <td align="left">返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。</td> </tr> <tr> <td align="left">s.fileno()</td> <td align="left">返回套接字的文件描述符。</td> </tr> <tr> <td align="left">s.setblocking(flag)</td> <td align="left">如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。</td> </tr> <tr> <td align="left">s.makefile()</td> <td align="left">创建一个与该套接字相关连的文件</td> </tr> </tbody></table>


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


### 1.2 UDP套接字

传输层除了有可靠的传输协议TCP之外，还有一种非常轻便的传输协议叫做用户数据报协议，简称UDP。TCP和UDP都是提供端到端传输服务的协议，二者的差别就如同打电话和发短信的区别，后者不对传输的可靠性和可达性做出任何承诺从而避免了TCP中握手和重传的开销，所以在强调性能和而不是数据完整性的场景中（例如传输网络音视频数据），UDP可能是更好的选择。可能大家会注意到一个现象，就是在观看网络视频时，有时会出现卡顿，有时会出现花屏，这无非就是部分数据传丢或传错造成的。



