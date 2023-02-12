# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230210
# @Version: 1.0
# @Description: 初识Pygame

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