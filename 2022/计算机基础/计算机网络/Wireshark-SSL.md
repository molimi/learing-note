本篇文章前半部分转载自阮一峰老师的[《SSL/TLS协议运行机制的概述》](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)，供学习使用。


<div class="asset-content entry-content" id="main-content">
<!-- div class="asset-body" -->
<p>互联网的通信安全，建立在SSL/TLS协议之上。</p>
<!-- /div -->
<!-- div id="more" class="asset-more" -->
<p>本文简要介绍SSL/TLS协议的运行机制。文章的重点是设计思想和运行过程，不涉及具体的实现细节。如果想了解这方面的内容，请参阅<a href="https://tools.ietf.org/html/rfc5246" target="_blank">RFC文档</a>。</p>

<p><img src="https://www.ruanyifeng.com/blogimg/asset/201402/bg2014020501.jpg" alt="" title=""></p>

<p><strong>一、作用</strong></p>

<p>不使用SSL/TLS的HTTP通信，就是不加密的通信。所有信息明文传播，带来了三大风险。</p>

<blockquote>
  <p>（1） <strong>窃听风险</strong>（eavesdropping）：第三方可以获知通信内容。</p>

<p>（2） <strong>篡改风险</strong>（tampering）：第三方可以修改通信内容。</p>

<p>（3） <strong>冒充风险</strong>（pretending）：第三方可以冒充他人身份参与通信。</p>
</blockquote>

<p>SSL/TLS协议是为了解决这三大风险而设计的，希望达到：</p>

<blockquote>
  <p>（1） 所有信息都是<strong>加密传播</strong>，第三方无法窃听。</p>

<p>（2） 具有<strong>校验机制</strong>，一旦被篡改，通信双方会立刻发现。</p>

<p>（3） 配备<strong>身份证书</strong>，防止身份被冒充。</p>
</blockquote>

<p>互联网是开放环境，通信双方都是未知身份，这为协议的设计带来了很大的难度。而且，协议还必须能够经受所有匪夷所思的攻击，这使得SSL/TLS协议变得异常复杂。</p>

<p><strong>二、历史</strong></p>

<p>互联网加密通信协议的历史，几乎与互联网一样长。</p>

<blockquote>
  <p>1994年，NetScape公司设计了SSL协议（Secure Sockets Layer）的1.0版，但是未发布。</p>

<p>1995年，NetScape公司发布SSL 2.0版，很快发现有严重漏洞。</p>

<p>1996年，SSL 3.0版问世，得到大规模应用。</p>

<p>1999年，互联网标准化组织ISOC接替NetScape公司，发布了SSL的升级版<a href="https://en.wikipedia.org/wiki/Secure_Sockets_Layer" target="_blank">TLS</a> 1.0版。</p>

<p>2006年和2008年，TLS进行了两次升级，分别为TLS 1.1版和TLS 1.2版。最新的变动是2011年TLS 1.2的<a href="https://tools.ietf.org/html/rfc6176" target="_blank">修订版</a>。</p>
</blockquote>

<p>目前，应用最广泛的是TLS 1.0，接下来是SSL 3.0。但是，主流浏览器都已经实现了TLS 1.2的支持。</p>

<p>TLS 1.0通常被标示为SSL 3.1，TLS 1.1为SSL 3.2，TLS 1.2为SSL 3.3。</p>

<p><strong>三、基本的运行过程</strong></p>

<p>SSL/TLS协议的基本思路是采用<a href="https://en.wikipedia.org/wiki/Public-key_cryptography" target="_blank">公钥加密法</a>，也就是说，客户端先向服务器端索要公钥，然后用公钥加密信息，服务器收到密文后，用自己的私钥解密。</p>

<p>但是，这里有两个问题。</p>

<p><strong>（1）如何保证公钥不被篡改？</strong></p>

<blockquote>
  <p>解决方法：将公钥放在<a href="https://en.wikipedia.org/wiki/Digital_certificate" target="_blank">数字证书</a>中。只要证书是可信的，公钥就是可信的。</p>
</blockquote>

<p><strong>（2）公钥加密计算量太大，如何减少耗用的时间？</strong></p>

<blockquote>
  <p>解决方法：每一次对话（session），客户端和服务器端都生成一个"对话密钥"（session key），用它来加密信息。由于"对话密钥"是对称加密，所以运算速度非常快，而服务器公钥只用于加密"对话密钥"本身，这样就减少了加密运算的消耗时间。</p>
</blockquote>

<p>因此，SSL/TLS协议的基本过程是这样的：</p>

<blockquote>
  <p>（1） 客户端向服务器端索要并验证公钥。</p>

<p>（2） 双方协商生成"对话密钥"。</p>

<p>（3） 双方采用"对话密钥"进行加密通信。</p>
</blockquote>

<p>上面过程的前两步，又称为"握手阶段"（handshake）。</p>

<p><strong>四、握手阶段的详细过程</strong></p>

<p><img src="https://www.ruanyifeng.com/blogimg/asset/201402/bg2014020502.png" alt="" title=""></p>

<p>"握手阶段"涉及四次通信，我们一个个来看。需要注意的是，"握手阶段"的所有通信都是明文的。</p>

<p><strong>4.1 客户端发出请求（ClientHello）</strong></p>

<p>首先，客户端（通常是浏览器）先向服务器发出加密通信的请求，这被叫做ClientHello请求。</p>

<p>在这一步，客户端主要向服务器提供以下信息。</p>

<blockquote>
  <p>（1） 支持的协议版本，比如TLS 1.0版。</p>

<p>（2） 一个客户端生成的随机数，稍后用于生成"对话密钥"。</p>

<p>（3） 支持的加密方法，比如RSA公钥加密。</p>

<p>（4） 支持的压缩方法。</p>
</blockquote>

<p>这里需要注意的是，客户端发送的信息之中不包括服务器的域名。也就是说，理论上服务器只能包含一个网站，否则会分不清应该向客户端提供哪一个网站的数字证书。这就是为什么通常一台服务器只能有一张数字证书的原因。</p>

<p>对于虚拟主机的用户来说，这当然很不方便。2006年，TLS协议加入了一个<a href="https://tools.ietf.org/html/rfc4366" target="_blank">Server Name Indication扩展</a>，允许客户端向服务器提供它所请求的域名。</p>

<p><strong>4.2 服务器回应（SeverHello）</strong></p>

<p>服务器收到客户端请求后，向客户端发出回应，这叫做SeverHello。服务器的回应包含以下内容。</p>

<blockquote>
  <p>（1） 确认使用的加密通信协议版本，比如TLS 1.0版本。如果浏览器与服务器支持的版本不一致，服务器关闭加密通信。</p>

<p>（2） 一个服务器生成的随机数，稍后用于生成"对话密钥"。</p>

<p>（3） 确认使用的加密方法，比如RSA公钥加密。</p>

<p>（4） 服务器证书。</p>
</blockquote>

<p>除了上面这些信息，如果服务器需要确认客户端的身份，就会再包含一项请求，要求客户端提供"客户端证书"。比如，金融机构往往只允许认证客户连入自己的网络，就会向正式客户提供USB密钥，里面就包含了一张客户端证书。</p>

<p><strong>4.3 客户端回应</strong></p>

<p>客户端收到服务器回应以后，首先验证服务器证书。如果证书不是可信机构颁布、或者证书中的域名与实际域名不一致、或者证书已经过期，就会向访问者显示一个警告，由其选择是否还要继续通信。</p>

<p>如果证书没有问题，客户端就会从证书中取出服务器的公钥。然后，向服务器发送下面三项信息。</p>

<blockquote>
  <p>（1） 一个随机数。该随机数用服务器公钥加密，防止被窃听。</p>

<p>（2） 编码改变通知，表示随后的信息都将用双方商定的加密方法和密钥发送。</p>

<p>（3） 客户端握手结束通知，表示客户端的握手阶段已经结束。这一项同时也是前面发送的所有内容的hash值，用来供服务器校验。</p>
</blockquote>

<p>上面第一项的随机数，是整个握手阶段出现的第三个随机数，又称"pre-master key"。有了它以后，客户端和服务器就同时有了三个随机数，接着双方就用事先商定的加密方法，各自生成本次会话所用的同一把"会话密钥"。</p>

<p>至于为什么一定要用三个随机数，来生成"会话密钥"，<a href="http://blog.csdn.net/dog250/article/details/5717162" target="_blank">dog250</a>解释得很好：</p>

<blockquote>
  <p>"不管是客户端还是服务器，都需要随机数，这样生成的密钥才不会每次都一样。由于SSL协议中证书是静态的，因此十分有必要引入一种随机因素来保证协商出来的密钥的随机性。</p>

<p>对于RSA密钥交换算法来说，pre-master-key本身就是一个随机数，再加上hello消息中的随机，三个随机数通过一个密钥导出器最终导出一个对称密钥。</p>

<p>pre master的存在在于SSL协议不信任每个主机都能产生完全随机的随机数，如果随机数不随机，那么pre master secret就有可能被猜出来，那么仅适用pre master secret作为密钥就不合适了，因此必须引入新的随机因素，那么客户端和服务器加上pre master secret三个随机数一同生成的密钥就不容易被猜出了，一个伪随机可能完全不随机，可是是三个伪随机就十分接近随机了，每增加一个自由度，随机性增加的可不是一。"</p>
</blockquote>

<p>此外，如果前一步，服务器要求客户端证书，客户端会在这一步发送证书及相关信息。</p>

<p><strong>4.4 服务器的最后回应</strong></p>

<p>服务器收到客户端的第三个随机数pre-master key之后，计算生成本次会话所用的"会话密钥"。然后，向客户端最后发送下面信息。</p>

<blockquote>
  <p>（1）编码改变通知，表示随后的信息都将用双方商定的加密方法和密钥发送。</p>

<p>（2）服务器握手结束通知，表示服务器的握手阶段已经结束。这一项同时也是前面发送的所有内容的hash值，用来供客户端校验。</p>
</blockquote>

<p>至此，整个握手阶段全部结束。接下来，客户端与服务器进入加密通信，就完全是使用普通的HTTP协议，只不过用"会话密钥"加密内容。</p>

<p><img src="https://www.ruanyifeng.com/blogimg/asset/201402/bg2014020503.gif" alt="" title=""></p>


<p><strong>五、实验分析</strong></p>

在本实验中，我们将研究安全套接层（SSL）协议，我们将会重点关注通过 TCP 连接发送的 SSL 记录。我们将会通过您的主机和电子商务服务器发送的 SSL 记录 的跟踪来实现。 我们将研究各种 SSL记录类型以及 SSL 消息中的字段。

实验过程：
**1. 在 SSL 会话中抓包**

第一步是在 SSL会话中捕获数据包。要做这一步，您应该去你最喜欢电子商务网站开始购买物品（但是请勿真的购买）。使用 Wireshark捕获数据包后，应设置过滤器，使其仅显示包含主机发送和接收的 SSL记录的以太网帧。 （SSL记录就是 SSL消息）您应该获得如下屏幕截图所示的内容。

我这里访问的是京东，其实只要访问ssl加密的网站都可以（也就是以https开头的网站）。

<img src ="https://img-blog.csdnimg.cn/4faf75c542744a0ba7e82d310ae021d7.png#pic_center" width = 48%>

**2. 分析抓包结果**

您使用的 Wireshark界面应该仅仅显示含有 SSL记录的以太网帧。建议您记住：每个以太网帧可能包含一个或多个的 SSL记录，这点很重要。（这与 HTTP消息不 同，每个以太网帧包含一个完整的 HTTP消息或者仅仅包含 HTTP消息的一部分） 因此，一个SSL记录可能会被多个以太网承载。


回答问题：
1. 对于前 8个以太网帧，请分别指出每一个帧的来源（客户端和服务器），确定每个帧包含的SSL记录的数量，并且列出包含SSL记录的类型。绘制客户端和服务器含有箭头指向的时序图。
答：帧的来源直接可以通过 Source 和 Destination 可以看出，每个帧包含的SSL记录的数量可以在每个帧的Transport Layer Security可以看到，SSL记录的类型可以从Info看出

<img src ="https://img-blog.csdnimg.cn/a23b3456ac9e426cbd6aa31ef7eed81f.png#pic_center" width = 48%>

时序图可以直接看WireShark自己绘制的，点击统计 -> 流量图 -> 限制显示过滤器：

<img src ="https://img-blog.csdnimg.cn/827d4f56147e4cff947517d97beb972a.png#pic_center" width = 48%>


**1) 客户端发出请求(ClientHello) 记录(ClientHello Record:)**
2. 每个 SSL记录都以相同的三个字段（可能具有不同的值）开头。 其中一个 字段是“内容类型”，长度为一个字节。 请列出所有三个字段及其长度。
答：Content Type字段为1字节，Version字段为2字节，Length字段为2字节。
<img src ="https://img-blog.csdnimg.cn/22d50f906e0743988bd279a9fe3700cb.png#pic_center" width = 48%>

3. 展开 ClientHello记录（如果您的跟踪包含多个 ClientHello记录，请展开包 含第一个记录的以太网帧），内容类型的值是多少？
答：如上图：Content Type: Handshake(22)

4. ClientHello记录是否包含随机数（也称为“挑战码”（ challenge））？ 如果是 这样，十六进制的挑战码值是多少？
答：包含，也就是下面的Random

<img src ="https://img-blog.csdnimg.cn/0121cb6ed6b9420181c5c5bdfdc6a9de.png#pic_center" width = 48%>

5. ClientHello记录是否通知了它所支持密码加密套件（suite）？如果是这样， 请在第一个密码套件， 分别指出非对称密钥加密算法，对称密钥加密算法，哈希算法分别都是什么？

<img src ="https://img-blog.csdnimg.cn/f6900d7f369b43cbaff6b8cf2fdcff9c.png#pic_center" width = 48%>

> 对称加密：加密和解密使用相同密钥。
> 举例：DES(不安全，被3DES 或AES)取代，AES，3DES
> 
> 非对称加密：使用两个不同的密钥，两个密钥无法不一样，无法相互推出，但是可以相互解密，公钥指的是可以任意发布的密钥，私钥是指只有自己持有，不给任何人使用（自己唯一所以才叫私钥），包括已经信任的另一方。特例，当公钥私钥相同变成非对称加密。
> 举例：DH，RSA，ECC
> 
> 消息摘要：把一段消息进行数学运算（哈希函数）生成一段固定长度摘要消息（指纹），用以证明消息的完整性不被篡改。
> 举例：MD5,SHA1,SHA2
> 
> 数字签名：为了证明和保证接收到消息就是所需要的消息，由发送方做消息摘要并且使用自己私钥签名。由于发送方已经公布公钥，所以直接接收方可以解密认为这是发送方，且因为公钥无法直接推出私钥，而私钥只有发送方所有，所以保证的发送方唯一性。为了防止数字签名被冒用，因此引入了数字证书的概念。
> 
> 数字证书：由权威机关CA 认证发送方准确性，并将它的公钥以及一些信做摘要运算，然后使用自己的私钥签名，证明发送方可靠。同样CA 机关会公布自己的公钥，而公钥无法直接推出私钥，而私钥只有CA 所有，我们信任CA机关因此认为它私钥签名的证书证明发送者准确唯一。CA 机关的密钥已经内置系统，CA 的私钥就像银行一样金库进行安全保管。当发送方丢失私钥自己签名，会要求CA 机关声明源数字证书作废，且重新签发保持安全。
> 
> 非对称加密虽然安全，但是需要长时间计算计算密文和解密；而对称加密虽然虽然解密速度快，但是一旦密钥丢失会造成同密钥的通信都不安全。所以我们在SSL（TLS）中我们把它们相结合来进行安全传输，首先进行服务器的数字签名和数字证书检验来证明服务器的准确唯一，然后通过非对称加密传输用于本次加密的对称密钥随机值，当双方获取本次用于加密的对称密钥后就改用对称密钥传输，因为本次对称密钥仅对本对话有效，保证了安全和效率。
> 
> 同时为了防止信息被篡改，每份信息都有使用哈希函数校验值来保证。

**2) 服务器回应(ServerHello) 记录(ServerHello Record)**
6. 找到 ServerHello SSL记录。 此记录是否指定了之前的密码套件之一？ 选择的密码套件中有哪些算法？
答：指定了哈希加密算法（SHA哈希函数）。

<img src ="https://img-blog.csdnimg.cn/cb66ecb1971d4eeab75cf50b18ec6084.png#pic_center" width = 48%>

7. 此记录是否包含随机数？如果有，它有多长？SSL中客户端和服务器段随机数用来干什么？
答：包含，有32字节，也就是用64个16进制数来表示。多次随机数生成为未来生成对话密钥提高安全性能。
<img src ="https://img-blog.csdnimg.cn/c00afbf34b734ee0a02ac0d7b18e7e4b.png#pic_center" width = 48%>

8. 此记录是否包含会话 ID？ 会话 ID的目的是什么？
答：包含（有的可能不会包含，也就是可以有也可以没有）目的：用一定时间内端口连接快速恢复连接过程。

<img src ="https://img-blog.csdnimg.cn/fd88ae67171b4340b95d0807764a0b22.png#pic_center" width = 48%>

9. 此记录是否包含证书，或者证书是否包含在单独的记录中。 证书是否适合一个单独的以太网帧传输？
答：此记录包含证书，适合在一个单独的以太网帧传输。
<img src ="https://img-blog.csdnimg.cn/e782e363e0654177b363c3c14fc00d14.png#pic_center" width = 48%>

**3) 客户端密钥交换记录(Client Key Exchange Record)**

10. 找到客户端密钥交换记录。 此记录是否包含前主密钥(pre-master secret)？ 这个前主密钥用于什么？ 前主密钥加密了吗？ 如果是这样，为什么？ 加密的前主密钥有多长？
答：包含；使用EC Diffie-Hellman（ECDH加密算法）进行加密传输，使用的是服务器公钥加密，用以给服务器让服务器用私钥解密并且使用前面两个hello过程的随机数生成本次的会话加密密钥；32个字节

<img src ="https://img-blog.csdnimg.cn/d750d1ab205a48d5970f6f4eecc9a18f.png#pic_center" width = 48%>


**4) 由客户端发送编码改变记录和加密握手记录**
11. 编码改变记录目的是什么？在您的跟踪中本记录有多少字节。
答：告诉服务器已经计算好加密密钥，以后将会用商定的加密方式和密钥加密传输了，在我的跟踪中该记录有6个字节







<p><strong>六、参考链接</strong></p>

<ul>
<li>MicroSoft TechNet, <a href="https://technet.microsoft.com/en-us/library/cc785811(v=ws.10).aspx" target="_blank">SSL/TLS in Detail</a></li>
<li>Jeff Moser, <a href="http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html" target="_blank">The First Few Milliseconds of an HTTPS Connection</a></li>
<li>Wikipedia, <a href="https://en.wikipedia.org/wiki/Transport_Layer_Security" target="_blank">Transport Layer Security</a></li>
<li>StackExchange, <a href="https://security.stackexchange.com/questions/20803/how-does-ssl-work" target="_blank">How does SSL work?</a></li>
</ul>

<!-- /div --></div>