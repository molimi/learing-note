
#### 关于使用Git出现“git Failed to connect to 127.0.0.1 port xxxx: Connection refused”的问题解决方案**

**1. 问题描述**

在使用 git 拉取、提交代码的时候，会出现 git Failed to connect to 127.0.0.1 port xxxx: Connection refused 的问题。

原因：无法连接到127.0.0.1: xxx端口: 连接被拒绝。

**2. 解决方案**
方案一：
思路：查询当前是否有代理，如果有就取消。
```bash
// 首先，查一下当前全局的 http 代理：
git config --global http.proxy
// 如果有代理，就取消
git config --global --unset http.proxy


// 再查 https 的代理：
git config --global https.proxy
// 同样的，有就取消
git config --global --unset https.proxy
```
方案二：
上面的方案如果不行的话，再参考这个方案
```bash
// 首先，查一下代理：
env|grep -i proxy
// 有就取消
unset http_proxy
unset https_proxy

// 再查
env|grep -i proxy
// 正常情况下是没有代理了
// 再次查询一下，如果还有的再取消
```

方案三
修改环境变量
在系统变量中找到了变量`http_proxy`和`https_proxy`，用户变量也可以看看有没有，删除他就可以了。

重启计算机。

再用 git，正常了，再查`env|grep -i proxy`，代理没有了。

**3. 小结**

代理没有了，就可以正常拉取、提交代码了。

> 本部分参考自：[关于使用Git出现“git Failed to connect to 127.0.0.1 port xxxx: Connection refused”的问题解决方案](https://blog.csdn.net/XH_jing/article/details/115095225)
