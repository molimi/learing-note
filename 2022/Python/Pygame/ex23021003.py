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