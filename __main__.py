import pygame
import numpy
import os
import time
import datetime
import http.client as httplib


# function to check internet connectivity, from https://www.geeksforgeeks.org/python/how-to-check-whether-users-internet-is-on-or-off-using-python/
def checkInternet(url="www.google.com", timeout=3):
    connection = httplib.HTTPConnection(url, timeout=timeout)
    try:
        # only header requested for fast operation
        connection.request("HEAD", "/")
        connection.close()  # connection closed
        return True
    except:
        return False
    

width, height = 320, 240
if pygame.IS_CE != 1: # AKA the current pygame module is NOT pygame-ce
    raise ModuleNotFoundError("Uh oh! This program expects pygame-ce, NOT regular pygame.")
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