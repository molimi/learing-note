# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230210
# @Version: 1.0
# @Description: 添加小球

import sys
import pygame

pygame.init()
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

pygame.quit()