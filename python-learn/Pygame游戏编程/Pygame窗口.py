import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 320, 240  # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口
# 执行死循环确保窗口一直显示下去
while True:
    # 检查事件
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
