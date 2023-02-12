# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230210
# @Version: 1.0
# @Description: 移动小球

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