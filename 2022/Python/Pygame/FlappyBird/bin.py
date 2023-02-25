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