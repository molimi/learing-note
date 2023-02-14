## 1 Django概述

Web框架，就是用于开发Web服务器端应用的基础设施，说得通俗一点就是一系列封装好的模块和工具。事实上，即便没有Web框架，我们仍然可以通过socket或CGI来开发Web服务器端应用，但是这样做的成本和代价在商业项目中通常是不能接受的。通过Web框架，我们可以化繁为简，降低创建、更新、扩展应用程序的工作量。刚才我们说到Python有上百个Web框架，这些框架包括Django、Flask、Tornado、Sanic、Pyramid、Bottle、Web2py、web.py等。

在上述Python的Web框架中，Django无疑是最有代表性的重量级选手，开发者可以基于Django快速的开发可靠的Web应用程序，因为它减少了Web开发中不必要的开销，对常用的设计和开发模式进行了封装，并对MVC架构提供了支持（Django中称之为MTV架构）。MVC是软件系统开发领域中一种放之四海而皆准的架构，它将系统中的组件分为模型（Model）、视图（View）和控制器（Controller）三个部分并借此实现模型（数据）和视图（显示）的解耦合。由于模型和视图进行了分离，所以需要一个中间人将解耦合的模型和视图联系起来，扮演这个角色的就是控制器。稍具规模的软件系统都会使用MVC架构（或者是从MVC演进出的其他架构），Django项目中我们称之为MTV，MTV中的M跟MVC中的M没有区别，就是代表数据的模型，T代表了网页模板（显示数据的视图），而V代表了视图函数，在Django框架中，视图函数和Django框架本身一起扮演了MVC中C的角色。

<img src ="https://img-blog.csdnimg.cn/3aa307a09f5c466384d7ff1cc0a02f7e.png#pic_center" width = 48%>

## 2 基本使用
### 2.1 安装Django Web框架
方式一：使用 pip 安装Django(不推荐)
在命令行中执行`pip install django=-2.0`命令，即可安装指定的2.0版本的Django。

方式二：使用virtualenv安装Django
在多个项目的复杂工作中，常常会碰到使用不同版本的 Python 包，而虚拟环境则会处理各个包之间的隔离问题。virtualenv 是一种虚拟环境，该环境中可以安装 Django，步骤如下:
<img src ="https://img-blog.csdnimg.cn/58b9da2417e34f109f5febfdf7dad7b4.png#pic_center" width = 48%>

方式三：使用 Anaconda 安装 Django
Anaconda 也是一种虚拟环境，严格来讲也是一种包管理工具，安装王成输入一下命令创建虚拟环境：
```python
conda create -n venv1 python=3.6        # 常见名字为 venv1 环境
conda activate venv1                    # 激活环境
conda install django                    # 安装Django 
```
下表展示了Django版本和Python版本的对应关系，请大家自行对号入座。
| Django版本 | Python版本                                |
| ---------- | ----------------------------------------- |
| 1.8        | 2.7、3.2、3.3、3.4、3.5                   |
| 1.9、1.10  | 2.7、3.4、3.5                             |
| 1.11       | 2.7、3.4、3.5、3.6、3.7（Django 1.11.17） |
| 2.0        | 3.4、3.5、3.6、3.7                        |
| 2.1        | 3.5、3.6、3.7                             |
| 2.2        | 3.5、3.6、3.7、3.8（Django 2.2.8）        |
| 3.0        | 3.6、3.7、3.8                             |

### 2.2 创建一个 Django 项目
(1) 建立一个项目文件夹，并激活环境，使用`django-admin`命令创建一个项目，详细如下：
<img src ="https://img-blog.csdnimg.cn/161e9edab6974594b26e89c85dedfbfa.png#pic_center" width = 48%>
(2) 使用Pycharm/VSCode打开demo项目，查看目录结构，如下图所示：

<img src ="https://img-blog.csdnimg.cn/782562cbd67240e4854a0dbef840c58d.png#pic_center" width = 48%>

项目已创建完成，Django项目中的文件及说明如下图所示：
<img src ="https://img-blog.csdnimg.cn/a984898a2bdb443483770e37e764511b.png#pic_center" width = 48%>

(3) 在虚拟环境命令行中执行以下命令运行项目：
```python
python manage.py runserver
```
此时可以看到Web服务器已经开始监听8000端口的请求了。在浏览器中输入:“http./127.0.0.1:8000"，即可看到创建的Django项目页面，如下图所示。
<img src ="https://img-blog.csdnimg.cn/1577d9f8d00e4183a7062d175b60ba38.png#pic_center" width = 48%>

> 说明：
> 这里启动的Django自带的服务器只能用于开发和测试环境，因为这个服务器是纯Python编写的轻量级Web服务器，不适合在生产环境中使用。
> 如果修改了代码，不需要为了让修改的代码生效而重新启动Django自带的服务器。但是，在添加新的项目文件时，该服务器不会自动重新加载，这个时候就得手动重启服务器。
> 可以在终端中通过python manage.py help命令查看Django管理脚本程序可用的命令参数。
> 使用python manage.py runserver启动服务器时，可以在后面添加参数来指定IP地址和端口号，默认情况下启动的服务器将运行在本机的8000端口。
> 在终端中运行的服务器，可以通过Ctrl+C来停止它 。通过PyCharm的“运行配置”运行的服务器直接点击窗口上的关闭按钮就可以终止服务器的运行。
> 不能在同一个端口上启动多个服务器，因为会导致地址的冲突（端口是对IP地址的扩展，也是计算机网络地址的一部分）。

补充：
修改项目的配置文件settings.py。
Django是一个支持国际化和本地化的框架，因此刚才我们看到的Django项目的默认首页也是支持国际化的，我们可以通过修改配置文件将默认语言修改为中文，时区设置为东八区。
修改前为：
```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
```
修改后为：
```python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Beijing'
```
<img src ="https://img-blog.csdnimg.cn/71cebc8fa02e42ab89570269a902ac43.png#pic_center" width = 48%>

(4) 创建完 Django 项目后，在 Pycharm 的命令行执行以下命令，可以为 Django 项目生成数据表，并创建一个账户名和密码。
```python
python manage.py migrate            # 执行数据库迁移生成数据表
python manage.py createsuperuser    # 按照提示输入账户和密码，密码强度符合一定的规则要求
```

<img src ="https://img-blog.csdnimg.cn/8cf81df758d142d7a388c13f07ca65a4.png#pic_center" width = 48%>

(5) 重启服务器，在浏览器中访问“http://127.0.0.1:8000/admin”，使用刚刚创建的账户登录，即可看到后台管理界面。

<img src ="https://img-blog.csdnimg.cn/8b793523f6ce42219b1e6b1bb53440af.png#pic_center" width = 48%>


### 2.3 创建 APP
如果要开发自己的Web应用，需要先在Django项目中创建“应用”，一个Django项目可以包含一个或多个应用，推荐使用 App 来完成不同模块的任务。

(1) 通过执行如下命令创建名为 app1 的应用。
```python
python manage.py startapp app1 
```

此时，在项目的根目录下可以看到一个名称为 app1 的目录。

<img src ="https://img-blog.csdnimg.cn/9e3e6c60560141e59e660a777d2e9924.png#pic_center" width = 48%>

其目录结构如下所示：
- `__init__.py`：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
- `admin.py`：可以用来注册模型，用于在Django框架自带的管理后台中管理模型。
-  `apps.py`：当前应用的配置文件。
- `migrations`：存放与模型有关的数据库迁移信息。
- `__init__.py`：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
- `models.py`：存放应用的数据模型（MTV中的M）。
- `tests.py`：包含测试应用各项功能的测试类和测试函数。
- `views.py`：处理用户HTTP请求并返回HTTP响应的函数或类（MTV中的V）。

(2) 下面将已经创建的 app 添加到settings.py 配置文件中，然后将其激活，否则 app 内的文件都不会生效，效果如下图所示。

<img src ="https://img-blog.csdnimg.cn/9a24a35d8a294c8f925c6d13c01f3be5.png#pic_center" width = 48%>


(3) 修改应用目录下的视图文件 views.py。
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_index(request):
    return HttpResponse('<h1>Hello, Dingo!</h1>')
```


(4) 修改Django项目目录下的 urls.py 文件，将视图函数和用户在浏览器中请求的路径对应
```python
from django.contrib import admin
from django.urls import path, include

from app1.views import show_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', show_index),
]
```


(5) 重新运行项目，并打开浏览器中访问 `http://127.0.0.1:8000/hello/`

<img src ="https://img-blog.csdnimg.cn/0a5eff19400d4b00a17fabe45f888854.png#pic_center" width = 48%>

(6) 上面我们通过代码为浏览器生成了内容，但仍然是静态内容，如果要生成动态内容，可以修改views.py文件并添加如下所示的代码。
```python
from django.shortcuts import render
from django.http import HttpResponse

from random import sample

# Create your views here.
def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry', 
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    content = '<h3>今天推荐的水果是：</h3>'
    content += '<hr>'
    content += '<ul>'
    for fruit in selected_fruits:
        content += f'<li>{fruit}</li>'
    content += '</ul>'
    return HttpResponse(content)
```

(7) 刷新页面查看程序的运行结果，看看每次刷新的网页的时候，是不是可以看到不一样的内容

<img src ="https://img-blog.csdnimg.cn/8134060aee22448ba280f365f8fb5ef6.png#pic_center" width = 48%>

### 2.4 使用模板

上面通过拼接HTML代码的方式为浏览器生成动态内容的做法在实际开发中是无能接受的，因为实际项目中的前端页面可能非常复杂，无法用这种拼接动态内容的方式来完成，这一点大家一定能够想到。为了解决这个问题，我们可以提前准备一个模板页（MTV中的T），所谓模板页就是一个带占位符和模板指令的HTML页面。


Django框架中有一个名为render的便捷函数可以来完成渲染模板的操作。所谓的渲染就是用数据替换掉模板页中的模板指令和占位符，当然这里的渲染称为后端渲染，即在服务器端完成页面的渲染再输出到浏览器中。后端渲染的做法在Web应用的访问量较大时，会让服务器承受较大的负担，所以越来越多的Web应用会选择前端渲染的方式，即服务器只提供页面所需的数据（通常是JSON格式），在浏览器中通过JavaScript代码获取这些数据并渲染页面上。

使用模板页的步骤如下所示。

(1) 在项目目录下创建名为templates文件夹。

(2) 添加模板页index.html

说明：实际项目开发中，静态页由前端开发者提供，后端开发者需要将静态页修改为模板页，以便通过Python程序对其进行渲染，这种做法就是上面提到的后端渲染。
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>首页</title>
        <style>
            #fruits {
                font-size: 1.25em;
            }
        </style>
    </head>
    <body>
        <h1>今天推荐的水果是：</h1>
        <hr>
        <ul id="fruits">
            {% for fruit in fruits %}
            <li>{{ fruit }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```
在上面的模板页中我们使用了{{ fruit }}这样的模板占位符语法，也使用了{% for %}这样的模板指令，这些都是Django模板语言（DTL）的一部分。关于模板语法和指令，大家可以看看[Django 模板语言 DTL](https://www.imooc.com/wiki/djangolesson/djangodtl.html)。

(3) 修改views.py文件，调用render函数渲染模板页。
```python
from django.shortcuts import render
from django.http import HttpResponse

from random import sample

# Create your views here.
def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry', 
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})
```
render函数的第一个参数是请求对象 request，第二个参数是我们要渲染的模板页的名字，第三个参数是要渲染到页面上的数据，我们通过一个字典将数据交给模板页，字典中的键就是模板页中使用的模板指令或占位符中的变量名。


(4) 到此为止，视图函数中的render还无法找到模板文件index.html，需要修改settings.py文件，配置模板文件所在的路径。修改settings.py文件，找到TEMPLATES配置，修改其中的DIRS配置。
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

(5) 重新运行项目或直接刷新页面查看结果。

<img src ="https://img-blog.csdnimg.cn/f63f039b2a9a4d5cb14d53ec1015d1b1.png#pic_center" width = 48%>

至此，通过这个项目对Django框架有一个感性的认识。