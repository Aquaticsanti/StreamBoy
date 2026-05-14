import pygame
import numpy
import os
import time
import datetime

width, height = 320, 240

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("StreamBoy \"Emulator\"")
pygame.font.init()

pygame.draw.rect(surface=screen, color=(33, 95, 154),
                 rect=(0, 0, width, 40))

bold_font = pygame.font.SysFont("arial.ttf", 40, bold=False)
time_render = bold_font.render(f"{datetime.datetime.now().strftime("%H:%M")}", False, (255, 255, 255))
textRect1 = time_render.get_rect()
textRect1.topleft = (6, 6)

screen.blit(time_render, textRect1)

pygame.display.flip()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()