
使用 PicX 创建免费的图床神器

写博客文章时，图片的上传和存放是一个问题，我们也许会在不同的平台发布同一篇文章，这样一来每个平台都要上传图片。

为了解决这些问题，做法是把图片统一上传到一个在线的第三方静态资源库中，我们把这个资源库称为图床。其返回一个图片的URL，使用 `markdown+图片url` 的方式写作文章，然后就可以直接使用链接引入图片。然后整篇文章复制即可，再也不用担心图片的问题了。


## 介绍

PicX，基于 GitHub API 开发的图床管理神器，图片外链使用 jsDelivr 进行全球 CDN 加速。免费、稳定、高效。免下载、免安装，只需一个 **GitHub 账号**，打开网站即可进行配置使用，轻松解决图床难题。

一共3个步骤就完成设置了
1. 创建 GitHub 仓库
2. 获取 GitHub Token
3. 配置图床

<p>网站：<a href="https://link.juejin.cn?target=https%3A%2F%2Fpicx.xpoet.cn%2F" target="_blank" title="https://picx.xpoet.cn/" ref="nofollow noopener noreferrer">picx.xpoet.cn/</a></p>
<p>仓库：<a href="https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2FXPoet%2Fpicx" target="_blank" title="https://github.com/XPoet/picx" ref="nofollow noopener noreferrer">github.com/XPoet/picx</a></p>
<p>文档：<a href="https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2FXPoet%2Fpicx%2Fblob%2Fmaster%2FREADME.md" target="_blank" title="https://github.com/XPoet/picx/blob/master/README.md" ref="nofollow noopener noreferrer">github.com/XPoet/picx/…</a></p>

**1. 创建 GitHub 仓库**

创建 一个用来存储图片的 GitHub 仓库，仓库属性必须选 Public 。

点击链接 [https://github.com/](https://github.com/) 快速新建仓库

<img src ="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/123.5icizwyveeg0.webp#pic_center" width = 48%/>


**2. 创建 GitHub Token**

PicX 的图床服务依赖于 `GitHub Token`，在开始使用之前，你必须先 创建 一个带有 repo 权限的 `GitHub Token`。

点击 [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new) 快速新建 GitHub Token

<img src ="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/124.25nlu5i5j1ds.webp#pic_center" width = 48%/>

这里我们填完名称和勾选上repo选项之后呢，然后直接点击 Generate token 按钮，即可生成一个token，如下图：

<img src ="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/001.6lklllgnfxc0.webp#pic_center" width = 48%/>

注意：这里英文的意思是：确保立即复制您的个人访问令牌。你将无法再看到它！那万一没了重新生成一个就行。


**3. 配置图床**

**1) 一键自动配置**

填写 GitHub Token，点击 “一键自动配置” 按钮会自动创建 GitHub 仓库，并完成仓库、分支和目录之间的绑定。
- 一键自动配置 > 创建的仓库：picx-images-hosting
- 一键自动配置 > 创建的分支：master
- 一键自动配置 > 创建的目录：yyyyMMdd (当天日期，例如：20230403)

如果你刚开始使用 PicX，那么推荐使用一键自动配置，非常方便。当然你也可以随时切换成手动配置。

**2) 手动配置**

填入刚刚在Github生成的Token，点击确认Token。会自动获取该用户下的仓库

如果你绑定的仓库有多个分支，那么会出现选择分支的下拉列表，否则直接进入选择目录。

多个分支情况，选择其中一个即可。PicX 暂时不支持新建分支，需要你手动去创建。只有一个分支情况，无分支下拉列表。

<img src ="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/128.62w39qmdbb00.webp#pic_center" width = 48% />

- 新建目录：需手动输入一个新目录。
- 根目录：图片将直接存储在仓库根目录下。
- 自动目录：自动生成日期格式 YYYYMMDD 的目录。例如：20230526
- 选择仓库目录：自动获取仓库下所有目录，选择一个即可。

至此，完成图床配置，点击 “确认” 按钮即可跳转到图片上传界面。

> 如果想对图片进行一个分类怎么办呢？
> 这个也很简单，新建一个文件夹然后再上传，等到下次还要上传到这个文件夹，我们在目录方式中勾选选择仓库目录，就会展示你创建的所有文件夹。然后进行选择。


**4. 上传图片**

在上传图片界面，你可以使用 拖拽文件、复制粘贴、选择文件 这三种方式选择你的图片到上传区域。
- 你可以拖拽 一张 或 多张 图片到上传区域。
- 你可以先将一张图片复制（快捷键 Ctrl+C / Command+C）到系统剪贴板，然后在 PicX 上传界面通过按下快捷键 Ctrl+V / Command+V 将图片粘贴到上传区域。
- 你可以选择 一张 或 多张 图片到上传区域。

选择图片完成后，在上传之前，可以自由修改图片名。

<img src="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/131.1zt39d3iin5s.webp#pic_center" alt="131" width=48% />


勾选中哈希化，会在图片名称加上一串哈希值，确保图片名的唯一性，强烈建议开启。

图片上传成功之后，会自动复制图片链接到系统剪贴板，也可以点击 “复制链接” 按钮进行复制。

**5. 图床管理**

点击左侧菜单栏的图床管理，我们可以看到当前目录是我们选择的 2230526

<img src="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/132.3r5biof03tg0.webp#pic_center" alt="132" width=48% />

双击目录图标，可进入下一级目录，点击图片，可放大预览。

<img src="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/133.94otifievhs.webp#pic_center" alt="133" width=48% />

支持的操作：
- 在属性面板，可以查看到图片名称和图片大小。
- 在重命名输入框键入新名称后，按回车键确认。
- 删除单张图片/批量删除多张图床
- 复制/批量复制链接


**6. 我的设置**

在我的设置界面，你可以体验到 PicX 图床丰富多彩的功能，根据自己需求调整最佳配置。

<img src="https://cdn.staticaly.com/gh/molimi/image-hosting@main/230526/130.6ywi4j6ahwc.webp#pic_center" alt="130" width=48% />



## 参考

- 使用 PicX 创建免费的图床神器：[https://juejin.cn/post/6991273636493524999](https://juejin.cn/post/6991273636493524999)
- 图床配置：[https://picx-docs.xpoet.cn/usage-guide/config.html](https://picx-docs.xpoet.cn/usage-guide/config.html)