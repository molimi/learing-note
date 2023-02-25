本篇文章转载自阮一峰老师的[《HTTP协议入门》](http://www.ruanyifeng.com/blog/2016/08/http.html)，供学习使用。

<div class="asset-content entry-content" id="main-content">
<!-- div class="asset-body" -->
<p>HTTP 协议是互联网的基础协议，也是网页开发的必备知识，最新版本 HTTP/2 更是让它成为技术热点。</p>
<!-- /div -->

<!-- div id="more" class="asset-more" -->

<p>本文介绍 HTTP 协议的历史演变和设计思路。</p>

<p><img src="https://www.ruanyifeng.com/blogimg/asset/2016/bg2016081901.jpg" alt="" title=""></p>

<h2>一、HTTP/0.9</h2>



`<p>`HTTP 是基于 TCP/IP 协议的 `<a href="https://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html" target="_blank"><strong>`应用层协议 `</strong></a>`。它不涉及数据包（packet）传输，主要规定了客户端和服务器之间的通信格式，默认使用80端口。`</p>`

<p>最早版本是1991年发布的0.9版。该版本极其简单，只有一个命令<code>GET</code>。</p>

<blockquote><pre class=" language-http"><code class=" language-http">
GET /index.html
</code></pre></blockquote>

<p>上面命令表示，TCP 连接（connection）建立后，客户端向服务器请求（request）网页<code>index.html</code>。</p>

<p>协议规定，服务器只能回应HTML格式的字符串，不能回应别的格式。</p>

<blockquote><pre><code class="language-html">
<html>
  <body>Hello World</body>
</html>
</code></pre></blockquote>

<p>服务器发送完毕，就关闭TCP连接。</p>

<h2>二、HTTP/1.0</h2>

<h3>2.1 简介</h3>

<p>1996年5月，HTTP/1.0 版本发布，内容大大增加。</p>

<p>首先，任何格式的内容都可以发送。这使得互联网不仅可以传输文字，还能传输图像、视频、二进制文件。这为互联网的大发展奠定了基础。</p>

<p>其次，除了<code>GET</code>命令，还引入了<code>POST</code>命令和<code>HEAD</code>命令，丰富了浏览器与服务器的互动手段。</p>

<p>再次，HTTP请求和回应的格式也变了。除了数据部分，每次通信都必须包括头信息（HTTP header），用来描述一些元数据。</p>

<p>其他的新增功能还包括状态码（status code）、多字符集支持、多部分发送（multi-part type）、权限（authorization）、缓存（cache）、内容编码（content encoding）等。</p>

<h3>2.2 请求格式</h3>

<p>下面是一个1.0版的HTTP请求的例子。</p>

<blockquote><pre class=" language-http"><code class=" language-http">
GET / HTTP/1.0
<span class="token keyword">User-Agent:</span> Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)
<span class="token keyword">Accept:</span> */*
</code></pre></blockquote>

<p>可以看到，这个格式与0.9版有很大变化。</p>

<p>第一行是请求命令，必须在尾部添加协议版本（<code>HTTP/1.0</code>）。后面就是多行头信息，描述客户端的情况。</p>

<h3>2.3 回应格式</h3>

<p>服务器的回应如下。</p>

<blockquote><pre class=" language-http"><code class=" language-http">
HTTP/1.0 200 OK 
<span class="token keyword">Content-Type:</span> text/plain
<span class="token keyword">Content-Length:</span> 137582
<span class="token keyword">Expires:</span> Thu, 05 Dec 1997 16:00:00 GMT
<span class="token keyword">Last-Modified:</span> Wed, 5 August 1996 15:55:28 GMT
<span class="token keyword">Server:</span> Apache 0.84

`span`

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

`code`

`code`

`code`

`code`

`code`

`code`

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code

code
