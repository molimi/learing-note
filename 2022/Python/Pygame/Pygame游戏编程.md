## 1 初识Pygame

Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，其中包含对图像、声音、视频、事件、碰撞等的支持。Pygame建立在SDL的基础上，SDL是一套跨平台的多媒体开发库，用C语言实现，被广泛的应用于游戏、模拟器、播放器等的开发。而Pygame让游戏开发者不再被底层语言束缚，可以更多的关注游戏的功能和逻辑。



对于该模块的详细用法，可以参考：(Pygame详解)[https://blog.csdn.net/qq_41556318/category_9283450.html]

本节是在编写游戏的过程中学习Pygame。会先通过“跳跃的小球”的游戏学习 Pygame 基础知识，然后应用 Pygame 实现 Flappy Bird 游戏。

## 2 基本使用
### 2.1 Pygame常用模块

Pygame中集成了很多和底层开发相关的模块，如访问显示设备、管理事件、使用字体等。Pygame常用模块如下图所示。

<img src ="https://img-blog.csdnimg.cn/c8f4128a00994ce9a0729746cec8c9ab.png#pic_center" width = 64%>


下面，使用pygame的 display模块和 event 模块创建一个 Pygame 窗口，代码如下:


```python
import sys
import pygame

pygame.init()
size = width, height = 320, 240             # 设置窗口
screen = pygame.display.set_mode(size)      # 显示窗口

# 执行死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():        # 遍历所有事件
        if event.type == pygame.QUIT:       # 如果单击关闭窗口，则退出
            sys.exit()

pygame.quit()       # 退出pygame
```
## 3 游戏开发

然后在窗口内创建一个小球。以一定的速度移动小球，当小球碰到游戏窗口的边缘时，小球弹回，继续移动。按照如下步骤实现该功能：

(1) 创建一个游戏窗口，宽和高设置为 640*480，并在窗口中添加小球。我们先准备好一张 `ball.png` 图片，然后加载该图片，最后将图片显示在窗口中，具体代码如下:

```python
import sys
import pygame

pygame.init()                               # 初始化 pygame
size = width, height = 640, 480             # 设置窗口
screen = pygame.display.set_mode(size)      # 显示窗口
color = (0, 0, 0)

ball = pygame.image.load('ball.png')        # 加载图片
ballrect = ball.get_rect()                  # 获取矩形区域

# 执行死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 如果单击关闭窗口，则退出
            sys.exit()

    screen.fill(color)                      # 填充颜色
    screen.blit(ball, ballrect)             # 将图片画到窗口上
    pygame.display.flip()                   # 更新全部显示

pygame.quit()                               # 退出pygame
```
上述代码中，首先导入pygame模块，然后调用 `init()` 方法初始化 pygame 模块。接下来，设置窗口的宽和高，最后使用 display 模块显示窗体。display模块的常用方法如下表所示。

<img src ="https://img-blog.csdnimg.cn/8855a0ff749a4c04a9d02f61b3eaa546.png#pic_center" width = 64%>

上述代码中，为了让窗口一直显示，需要使用 `while True` 让程序一直执行。同时设置关闭按钮，添加了轮询事件检测。`pygame.event.get()` 能够获取事件队列，使用`for ... in`遍历事件，然后根据type属性判断事件类型。这里的 `event.type` 等于 `pygame.QUIT` 表示检测到关闭 pygame 窗口事件，`pygame.KEYDOWN` 表示键盘按下事件，`pgame.MOUSEBUTTONDOWN` 表示鼠标按下事件等。

上述代码中使用 image 模块的 `load()` 方法加载图片，返回值 ball 是一个 Surface 对象。Surface 是用来代表图片的 pygame 对象，可以对一个 Surface 对象进行涂画、变形、复制等各种操作。事实上，屏幕也只是一个 surface，`pygame.display.set_mode`就返回了一个屏幕 Surface 对象。如果将 ball 这个 Surface 对象画到 screen Surface 对象，需要使用 `blit()`方法，最后使用 display 模块的 `flip()` 方法更新整个待显示的 Surface 对象到屏幕上。Surface 对象的常用方法如下图所示。

<img src ="https://img-blog.csdnimg.cn/875c2f43e602467e8f293aee2099a1b2.png#pic_center" width = 64%>

效果如下图所示：
<img src ="https://img-blog.csdnimg.cn/5cbb3293887c4e77b622d71c095d8930.png#pic_center" width = 64%>

(2) 下面该让小球动起来了。`ball.get_rect()` 方法返回值balrect 是一个 Rect 对象，该对象有一个 `move()` 方法可以用于移动矩形。`move(x,y)` 函数有两个参数，第一个参数是 X 轴移动的距离，第二个参数是 Y 轴移动的距离。窗体左上角坐标为(0,0)，为实现小球不停地移动，将 `move()` 函数添加到 while循环内，具体代码如下:

```python
import sys
import pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (0, 0, 0)

ball = pygame.image.load('ball.png')
ballrect = ball.get_rect()

speed = [5, 5]              # 设置移动的X轴、Y轴距离
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)         # 移动小球
    screen.fill(color)
    screen.blit(ball, ballrect)
    pygame.display.flip()

pygame.quit()
```
(3) 运行上述代码，发现小球在屏幕中一闪而过，此时，小球并没有真正消失，而是移动到窗体之外，此时需要添加碰撞检测的功能。当小球与窗体任一边缘发生碰撞，则更改小球的移动方向。具体代码如下：

```python
import sys
import pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (0, 0, 0)

ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()

speed = [5, 5]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 如果单击关闭窗口，则退出
            sys.exit()
        
    ball_rect = ball_rect.move(speed)         # 移动小球
    # 碰到左右边缘
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)                  # 填充颜色
    screen.blit(ball, ball_rect)        # 将图片画到窗口上
    pygame.display.flip()               # 更新全部显示

pygame.quit()
```

上述代码中，添加了碰撞检测功能。如果碰到左右边缘，更改 X 轴数据为负数，如果碰到上下边缘，更改 Y 轴数据为负数。运行结果如下图所示。

<img src ="https://img-blog.csdnimg.cn/b6cb7c63484d46a8aa2cbe7bcf87a968.png#pic_center" width = 64%>

(4) 运行上述代码发现好像有多个小球在飞快移动，这是因为运行上述代码的时间非常短，导致肉眼观察出现错觉，因此需要添加一个“时钟”来控制程序运行的时间。这时就需要使用 Pygame 的time 模块。使用 Pygame 时钟之前，必须先创建 Clock 对象的一个实例，然后在 while循环中设置多长时间运行一次。具体代码如下:

```python
import sys
import pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (0, 0, 0)

ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()

speed = [5, 5]
clock = pygame.time.Clock()     # 设置时钟 

while True:
    clock.tick(60)              # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 如果单击关闭窗口，则退出
            sys.exit()
        
    ball_rect = ball_rect.move(speed)         # 移动小球
    # 碰到左右边缘
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)                  # 填充颜色
    screen.blit(ball, ball_rect)        # 将图片画到窗口上
    pygame.display.flip()               # 更新全部显示

pygame.quit()
```
至此，我们完成了小球的跳跃游戏。

## 4 开发 Flappy Bird 游戏

### 4.1 游戏简介

[Flappy Bird](https://flappy-bird.io/) 是一款鸟类飞行游戏，由越南河内独立游戏开发者阮哈东（Dong Nguyen）开发。在FlappyBird 这款游戏中，玩家只需要用一根手指来操控，单击触摸手机屏幕，小鸟就会往上飞。不断地单击屏幕，小鸟就会不断地往高处飞；放松手指，则会快速下降。玩家要控制小鸟一直向前飞行，并且注意躲避途中高低不平的管子。如果小鸟碰到了障碍物，游戏就会结束。每当小鸟飞过一组管道，玩家就会获得1分。

### 4.2 游戏分析

在 Flappy Bird 游戏中，主要有两个对象：小鸟和管道。可以创建 Bird 类和 Pincline 类来分别表示这两个对象。小鸟可以通过上下移动来躲避管道，所以在 Bird 类中创建一个 `bird_update()`方法，实现小鸟的上下移动。为了体现小鸟向前飞行的特征，可以让管道一直向左侧移动，这样在窗口中就好像小鸟在向前飞行。所以，在 Pineline 类中也创建一个`update_pipeline()` 方法，实现管道的向左移动。此外，还创建了3个函数: `create_map()`函数用于绘制地图; `check_dead()`函数用于判断小鸟的生命状；`get_result()` 函数用于获攻最终分数。最后在主逻辑中，实例化类并调用相关方法，实现相应功能。

### 4.3 搭建主框架

通过前面的分析，我们可以搭建起 Flappy Bird 游戏的主框架。Flappy Bird 游戏有两个对象：小鸟和管道。先来创建这两个类，类中具体的方法可以先使用pass语句代替。然后创建一个绘制地图的函数 `create_map()`。最后，在主逻辑中绘制背景图片。关键代码如下:

```python
import sys
import pygame
import random

class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义初始化方法"""
        pass

    def bird_update(self):
        pass


class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""
        pass


    def update_pipeline(self):
        """管道水平移动"""
        pass

def create_map():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))        # 填充颜色
    screen.blit(back_ground, (0, 0))    # 填入到背景
    pygame.display.update()             # 更新显示


if __name__ == '__main__':
    """主程序"""
    pygame.init()                           # 初始化pygame
    size = width, height = 288, 512
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()                   # 实例化管道类
    Bird = Bird()                           # 实例化鸟类
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        back_ground = pygame.image.load('assets/bg_day.png')    # 加载背景图片
        create_map()            # 绘制地图
    pygame.quit()               # 退出
```


### 4.4 创建小鸟类

下面来创建小鸟类。该类需要初始化很多参数，所以定义一个 `__init__()` 方法，用来初始化各种参数，包括鸟飞行的几种状态、飞行的速度、跳跃的高度等。然后定义 `bird_update()` 方法，该方法用于实现小鸟的跳跃和坠落。接下来，在主逻辑的轮询事件中添加键盘按下事件或鼠标单击事件，如按下鼠标，使小鸟上升等。最后，在 `create_map()` 方法中，显示小鸟的图像。关键代码如下:


```python
import sys
import pygame
import random

class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义初始化方法"""
        self.bird_rect = pygame.Rect(65, 50, 50, 50)        # 鸟的矩形
        # 定义鸟的3种状态列表
        self.bird_status = [pygame.image.load('assets/bird0_0.png'),
                            pygame.image.load('assets/bird0_1.png'),
                            pygame.image.load('assets/bird0_2.png')]
        self.status = 0         # 默认飞行状态
        self.bird_x = 150       # 鸟所在的X轴坐标
        self.bird_y = 350       # 鸟所在的Y轴坐标，即上下飞行高度
        self.jump = False       # 默认情况小鸟自动降落
        self.jump_speed = 10    # 跳跃高度
        self.gravity = 5        # 重力
        self.dead = False       # 默认小鸟生命状态为活着

    def bird_update(self):
        if self.jump:
            # 小鸟跳跃
            self.jump_speed -= 1                # 速度递减，上升越来越慢
            self.bird_y -= self.jump_speed      # 鸟的Y轴坐标减小，小鸟上升
        else:
            # 小鸟坠落
            self.gravity += 0.2                 # 重力递增，下降越来越快
            self.bird_y += self.gravity         # 鸟的Y轴坐标增加，小鸟下降
        self.bird_rect[1] = self.bird_y         # 更改Y轴坐标


class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""
        pass

    def update_pipeline(self):
        """管道水平移动"""
        pass


def create_map():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))        # 填充颜色
    screen.blit(back_ground, (0, 0))    # 填入到背景

    # 显示小鸟
    if Bird.dead:
        Bird.status = 2                 # 撞管道状态
    elif Bird.jump:
        Bird.status = 1                 # 起飞状态
    screen.blit(Bird.bird_status[Bird.status], (Bird.bird_x, Bird.bird_y))  # 设置小鸟坐标
    Bird.bird_update()                  # 鸟移动
    pygame.display.update()             # 更新显示


if __name__ == '__main__':
    """主程序"""
    pygame.init()                           # 初始化pygame
    size = width, height = 288, 512
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()                   # 实例化管道类
    Bird = Bird()                           # 实例化鸟类
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True        # 跳跃
                Bird.gravity = 2        # 重力
                Bird.jump_speed = 10    # 跳跃速度
            
        back_ground = pygame.image.load('assets/bg_day.png')    # 加载背景图片
        create_map()            # 绘制地图
    pygame.quit()               # 退出
```
上述代码在 Bird 类中设置了 `bird_status` 属性，该属性是一个鸟类图片的列表，列表中显示鸟类3种飞行状态，根据小鸟的不同状态加载相应的图片。在 `bird_update()` 方法中，为了达到较好的动画效果，使 `jump_speed` 和 `gravity` 两个属性逐渐变化。运行上述代码，在窗体内创建一只小鸟，默认情况小鸟会一直下降。当单击一下鼠标或按一下键盘，小鸟会跳跃一下，高度上升。


### 4.5 创建管道类

创建完鸟类后，接下来创建管道类。同样，在 `__init__` 方法中初始化各种参数，包括设置管道的坐标，加载上下管道图片等。然后在 `update_pipeline()` 方法中，定义管道向左移动的速度，并且当管道移出屏幕时，重新绘制下一组管道。最后，在 `create_map()` 函数中显示管道。关键代码如下:


```python
import sys
import pygame
import random

class Bird(object):
    """定义一个鸟类"""
    # 代码和前面一致，此处省略


class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""
        self.wall_x = 288               # 管道所在X轴坐标
        self.pipe_up = pygame.image.load('assets/pipe_up.png')          # 加载上管道图片
        self.pipe_down = pygame.image.load('assets/pipe_down.png')      # 加载下管道图片

    def update_pipeline(self):
        """管道水平移动"""
        self.wall_x -= 5        # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞跃管道，分数加1，并且重置管道
        if self.wall_x < -80:
            global score
            score += 1
            self.wall_x = 288

def create_map():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))        # 填充颜色
    screen.blit(back_ground, (0, 0))    # 填入到背景

    # 显示管道
    screen.blit(Pipeline.pipe_up, (Pipeline.wall_x, -200))      # 上管道坐标位置
    screen.blit(Pipeline.pipe_down, (Pipeline.wall_x, 400))     # 下管道坐标位置
    Pipeline.update_pipeline()          # 管道移动

    # 显示小鸟
    if Bird.dead:
        Bird.status = 2                 # 撞管道状态
    elif Bird.jump:
        Bird.status = 1                 # 起飞状态
    screen.blit(Bird.bird_status[Bird.status], (Bird.bird_x, Bird.bird_y))  # 设置小鸟坐标
    Bird.bird_update()                  # 鸟移动

    # 显示分数
    screen.blit(font.render('Score:'+str(score), -1, (255, 255, 255)), (100, 50))   # 设置颜色及坐标位置
    pygame.display.update()             # 更新显示


if __name__ == '__main__':
    """主程序"""
    # 代码和前面一致，此处省略
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True        # 跳跃
                Bird.gravity = 2        # 重力
                Bird.jump_speed = 10    # 跳跃速度
            
        back_ground = pygame.image.load('assets/bg_day.png')    # 加载背景图片
        create_map()            # 绘制地图
    pygame.quit()               # 退出
```

上述代码中，在 `create_map()` 函数内，设置先显示管道，再显示小鸟。这样傲的目的是为了当小鸟与管道图像重合时，小鸟的图像显示在上层，而管道的图像显示在底层。


### 4.6 计算得分
当小鸟飞过管道时，玩家得分加1。这里对于飞过管道的逻辑做了简化处理：当管道移动到窗体左侧一定距离后，默认为小鸟飞过管道，使分数加1，并显示在屏幕上。在 `update_pipeline()` 方法中已实现该功能，代码如下：

```python
import sys
import pygame
import random

class Bird(object):
    """定义一个鸟类"""
    # 代码和前面一致，此处省略


class Pipeline(object):
    """定义一个管道类"""
    # 代码和前面一致，此处省略


    def update_pipeline(self):
        """管道水平移动"""
        self.wall_x -= 5        # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞跃管道，分数加1，并且重置管道
        if self.wall_x < -80:
            global score
            score += 1
            self.wall_x = 288

def create_map():
    """定义创建地图的方法"""
    # 代码和前面一致，此处省略

    # 显示分数
    screen.blit(font.render('Score:'+str(score), -1, (255, 255, 255)), (100, 50))   # 设置颜色及坐标位置
    pygame.display.update()             # 更新显示


if __name__ == '__main__':
    """主程序"""
    pygame.init()                           # 初始化pygame
    pygame.font.init()                      # 初始化字体
    font = pygame.font.SysFont(None, 50)    # 设置默认字体和大小
    size = width, height = 288, 512
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()                   # 实例化管道类
    Bird = Bird()                           # 实例化鸟类
    score = 0
    while True:
        # 代码和前面一致，此处省略
```

### 4.7 碰撞检测
当小鸟与管道相撞时，小鸟颜色变为灰色，游戏结束，并且显示总分数。在 `check_dead()` 函数中通过 `pygame.Rect()` 可以分别获取小鸟的矩形区域对象和管道的矩形区域对象，该对象有一个 `collidcrect()` 方法可以判断两个矩形区域是否相撞。如果相撞，设置 `Bird.dead` 属性为 True。此外，当小鸟飞出窗体时，也设置 `Bird.dead` 属性为True。最后，用两行文字显示游戏得分。关键代码如下:


```python
import sys
import pygame
import random

class Bird(object):
    """定义一个鸟类"""
    # 代码和前面一致，此处省略

class Pipeline(object):
    """定义一个管道类"""
    # 代码和前面一致，此处省略

def create_map():
    """定义创建地图的方法"""
    # 代码和前面一致，此处省略

def check_dead():
    # 上方管子的矩形位置
    up_rect = pygame.Rect(Pipeline.wall_x, -200, 
                          Pipeline.pipe_up.get_width() - 10,
                          Pipeline.pipe_up.get_height())
    down_rect = pygame.Rect(Pipeline.wall_x, 400, 
                            Pipeline.pipe_down.get_width() - 10,
                            Pipeline.pipe_down.get_height())
    # 检测小鸟与上下方管道是否碰撞
    if up_rect.colliderect(Bird.bird_rect) or down_rect.colliderect(Bird.bird_rect):
        Bird.dead = True
    # 检测小鸟是否飞出上下边界
    if not 0 < Bird.bird_rect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def get_result1():
    final_text1 = "Game Over"
    final_text2 = "Your final score is: " + str(score)
    ft1_font = pygame.font.SysFont('Arial', 40)             # 设置第一行文字字体
    ft1_surf = ft1_font.render(final_text1, 1, (243, 3, 36))    # 设置第一行文字颜色
    ft2_font = pygame.font.SysFont('Arial', 30)
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))
    # 设置第一行文字显示位置
    screen.blit(ft1_surf, [screen.get_width()/2-ft1_surf.get_width()/2, 100])
    screen.blit(ft2_surf, [screen.get_width()/2-ft2_surf.get_width()/2, 200])
    pygame.display.flip()       # 更新整个待显示的Surface对象到屏幕上


if __name__ == '__main__':
    """主程序"""
    # 代码和前面一致，此处省略
    while True:
         # 代码和前面一致，此处省略
            
        back_ground = pygame.image.load('assets/bg_day.png')    # 加载背景图片
        if check_dead():            # 检测小鸟生命状态
            get_result1()           # 如果小鸟死亡，显示游戏总分数        
        else:
            create_map()            # 绘制地图
    pygame.quit()               # 退出
```
上述代码的 `check_dead()` 方法中，`up_rect.colliderect(Bird.bird_rect)` 用于检测小鸟的矩形区域是否与上面的管道的矩形区域相撞, `colliderect()`函数的参数是另一个矩形区域对象。运行结果如下图所示。

<img src ="https://img-blog.csdnimg.cn/4b841b17600646feaccd16cbb3efd552.png#pic_center" width = 64%>

这里只是实现了 Flappy Bird 的基本功能，还可以继续完善设置游戏的难度，包括设置管道的高度、小鸟的飞行速度等，感兴趣的朋友可以进一步尝试。


完整代码如下：

```python
# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230210
# @Version: 1.0
# @Description: 移动小球

import sys
import pygame
import random

class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义初始化方法"""
        self.bird_rect = pygame.Rect(65, 50, 50, 50)        # 鸟的矩形
        # 定义鸟的3种状态列表
        self.bird_status = [pygame.image.load('assets/bird0_0.png'),
                            pygame.image.load('assets/bird0_1.png'),
                            pygame.image.load('assets/bird0_2.png')]
        self.status = 0         # 默认飞行状态
        self.bird_x = 150       # 鸟所在的X轴坐标
        self.bird_y = 350       # 鸟所在的Y轴坐标，即上下飞行高度
        self.jump = False       # 默认情况小鸟自动降落
        self.jump_speed = 10    # 跳跃高度
        self.gravity = 5        # 重力
        self.dead = False       # 默认小鸟生命状态为活着


    def bird_update(self):
        if self.jump:
            # 小鸟跳跃
            self.jump_speed -= 1                # 速度递减，上升越来越慢
            self.bird_y -= self.jump_speed      # 鸟的Y轴坐标减小，小鸟上升
        else:
            # 小鸟坠落
            self.gravity += 0.2                 # 重力递增，下降越来越快
            self.bird_y += self.gravity         # 鸟的Y轴坐标增加，小鸟下降
        self.bird_rect[1] = self.bird_y         # 更改Y轴坐标



class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""
        self.wall_x = 288               # 管道所在X轴坐标
        self.pipe_up = pygame.image.load('assets/pipe_up.png')          # 加载上管道图片
        self.pipe_down = pygame.image.load('assets/pipe_down.png')      # 加载下管道图片


    def update_pipeline(self):
        """管道水平移动"""
        self.wall_x -= 5        # 管道X轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞跃管道，分数加1，并且重置管道
        if self.wall_x < -80:
            global score
            score += 1
            self.wall_x = 288

def create_map():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))        # 填充颜色
    screen.blit(back_ground, (0, 0))    # 填入到背景

    # 显示管道
    screen.blit(Pipeline.pipe_up, (Pipeline.wall_x, -200))      # 上管道坐标位置
    screen.blit(Pipeline.pipe_down, (Pipeline.wall_x, 400))     # 下管道坐标位置
    Pipeline.update_pipeline()          # 管道移动

    # 显示小鸟
    if Bird.dead:
        Bird.status = 2                 # 撞管道状态
    elif Bird.jump:
        Bird.status = 1                 # 起飞状态
    screen.blit(Bird.bird_status[Bird.status], (Bird.bird_x, Bird.bird_y))  # 设置小鸟坐标
    Bird.bird_update()                  # 鸟移动

    # 显示分数
    screen.blit(font.render('Score:'+str(score), -1, (255, 255, 255)), (100, 50))   # 设置颜色及坐标位置
    pygame.display.update()             # 更新显示

def check_dead():
    # 上方管子的矩形位置
    up_rect = pygame.Rect(Pipeline.wall_x, -200, 
                          Pipeline.pipe_up.get_width() - 10,
                          Pipeline.pipe_up.get_height())
    down_rect = pygame.Rect(Pipeline.wall_x, 400, 
                            Pipeline.pipe_down.get_width() - 10,
                            Pipeline.pipe_down.get_height())
    # 检测小鸟与上下方管道是否碰撞
    if up_rect.colliderect(Bird.bird_rect) or down_rect.colliderect(Bird.bird_rect):
        Bird.dead = True
    # 检测小鸟是否飞出上下边界
    if not 0 < Bird.bird_rect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def get_result1():
    final_text1 = "Game Over"
    final_text2 = "Your final score is: " + str(score)
    ft1_font = pygame.font.SysFont('Arial', 40)             # 设置第一行文字字体
    ft1_surf = ft1_font.render(final_text1, 1, (243, 3, 36))    # 设置第一行文字颜色
    ft2_font = pygame.font.SysFont('Arial', 30)
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))
    # 设置第一行文字显示位置
    screen.blit(ft1_surf, [screen.get_width()/2-ft1_surf.get_width()/2, 100])
    screen.blit(ft2_surf, [screen.get_width()/2-ft2_surf.get_width()/2, 200])
    pygame.display.flip()       # 更新整个待显示的Surface对象到屏幕上


if __name__ == '__main__':
    """主程序"""
    pygame.init()                           # 初始化pygame
    pygame.font.init()                      # 初始化字体
    font = pygame.font.SysFont(None, 50)    # 设置默认字体和大小
    size = width, height = 288, 512
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()                   # 实例化管道类
    Bird = Bird()                           # 实例化鸟类
    score = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True        # 跳跃
                Bird.gravity = 2        # 重力
                Bird.jump_speed = 10    # 跳跃速度
            
        back_ground = pygame.image.load('assets/bg_day.png')    # 加载背景图片
        if check_dead():            # 检测小鸟生命状态
            get_result1()           # 如果小鸟死亡，显示游戏总分数        
        else:
            create_map()            # 绘制地图
    pygame.quit()               # 退出
```

______

## 参考
- Pygame教程：[http://c.biancheng.net/pygame/](http://c.biancheng.net/pygame/)
- Pygame详解：[https://blog.csdn.net/qq_41556318/category_9283450.html](https://blog.csdn.net/qq_41556318/category_9283450.html)
