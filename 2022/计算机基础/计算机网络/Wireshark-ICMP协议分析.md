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






## 2 实验分析





