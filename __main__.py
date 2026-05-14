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

# Initialize fonts
pygame.font.init()
font = pygame.font.SysFont("freesansbold", 30)
font_smol = pygame.font.SysFont("freesansbold", 20)

# Draw status bar background
# NOTE: Right now, the color is fixed at blue. 
# On actual hardware, you will be able to change this.
pygame.draw.rect(surface=screen, color=(33, 95, 154),
                 rect=(0, 0, width, 40))

# Load system time
time_render = font.render(f"{datetime.datetime.now().strftime("%H:%M")}", False, (255, 255, 255))
textRect1 = time_render.get_rect()
textRect1.center = (45, 22.5)
screen.blit(time_render, textRect1)

# Load battery percentage logo
# NOTE: On actual hardware, this logo will change acording to battery percentage.
battery_logo = pygame.image.load_sized_svg("icons\\battery_5_bar.svg", (35, 35)).convert_alpha()
batteryRect1 = battery_logo.get_rect()
batteryRect1.center = (305, 20)
screen.blit(battery_logo, batteryRect1)

# Load battery percentage text
# NOTE: Right now, this is a placeholder.
# When this is ported to actual hardware, this will change.
batteryText_render = font_smol.render("bat%", False, (255, 255, 255))
batteryTextRect1 = batteryText_render.get_rect()
batteryTextRect1.center = (265, 22.5)
screen.blit(batteryText_render, batteryTextRect1)

# Load Wifi logo
if checkInternet() == True:
    wifi_logo = pygame.image.load_sized_svg("icons\\wifi.svg", (35, 35)).convert_alpha()
else:
    wifi_logo = pygame.image.load_sized_svg("icons\\wifi_off.svg", (35, 35)).convert_alpha()
wifiRect1 = wifi_logo.get_rect()
wifiRect1.center = (217.5, 20)
screen.blit(wifi_logo, wifiRect1)

# Load audio logo
# NOTE: Right now, it assumes you have no audio plugged in. 
# When this is ported to actual hardware, this will change.
audio_logo = pygame.image.load_sized_svg("icons\\close.svg", (45, 45)).convert_alpha()
audioRect1 = audio_logo.get_rect()
audioRect1.center = (180, 22.5)
screen.blit(audio_logo, audioRect1)

# Loop
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()