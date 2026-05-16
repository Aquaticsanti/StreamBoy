import pygame
import numpy
import os
import time
import datetime
import http.client as httplib
import threading


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
    

def DrawStatusBar():
    global screen, primaryColor, secondaryColor, font, font_smol
    # Draw status bar background
    pygame.draw.rect(surface=screen, color=primaryColor,
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
    batteryTextRect1.midright = (292.5, 22.5)
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

def DrawHomeMenu():
    global screen, primaryColor, secondaryColor, font, font_smol
    ## Load music button
    # Load music button background
    music_bg = pygame.draw.rect(surface=screen, color=primaryColor, rect=(97.5, 80, 150, 50), border_radius=60)
    # Load music logo
    music_logo = pygame.image.load_sized_svg("icons\\music_note_2.svg", (50, 50)).convert_alpha()
    musicRect1 = music_logo.get_rect()
    musicRect1.center = (107.5, 105)
    musicCircle2 = pygame.draw.circle(surface=screen, center=musicRect1.center, color=(0, 0, 0), radius=37.5)
    musicCircle1 = pygame.draw.circle(surface=screen, center=musicRect1.center, color=secondaryColor, radius=30)
    screen.blit(music_logo, musicRect1)
    # Load "Music" text
    musicText_render = font.render("Music", False, (255, 255, 255))
    musicTextRect1 = musicText_render.get_rect()
    musicTextRect1.center = (192.5, 107.5)
    screen.blit(musicText_render, musicTextRect1)

    ## Load settings button
    # Load settings button background
    settings_bg = pygame.draw.rect(surface=screen, color=secondaryColor, rect=(72.5, 145, 80, 50), border_radius=60)
    # Load settings logo
    settings_logo = pygame.image.load_sized_svg("icons\\settings.svg", (47.5, 47.5)).convert_alpha()
    settingsRect1 = settings_logo.get_rect()
    settingsRect1.center = (112.5, 170)
    screen.blit(settings_logo, settingsRect1)

    ## Load apps button
    # Load apps button background
    apps_bg = pygame.draw.rect(surface=screen, color=secondaryColor, rect=(167.5, 145, 80, 50), border_radius=60)
    # Load apps logo
    apps_logo = pygame.image.load_sized_svg("icons\\apps.svg", (47.5, 47.5)).convert_alpha()
    appsRect1 = apps_logo.get_rect()
    appsRect1.center = (207.5, 170)
    screen.blit(apps_logo, appsRect1)

def DrawSettingsMenu():
    global screen, primaryColor, secondaryColor, font, font_smol
    ## Draw go back option
    # Draw go back arrow
    goBack_logo = pygame.image.load_sized_svg("icons\\arrow_back_ios_new.svg", (30, 30)).convert_alpha()
    goBackRect1 = goBack_logo.get_rect()
    goBackRect1.center = (35, 60)
    screen.blit(goBack_logo, goBackRect1)
    # Draw go back text
    GoBackText_render = font.render("Go back", False, (255, 255, 255))
    GoBackTextRect1 = GoBackText_render.get_rect()
    GoBackTextRect1.center = (130, 64)
    screen.blit(GoBackText_render, GoBackTextRect1)

    ## Draw divider line
    divLine = pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, 85), end_pos=(width, 85))

    ## Draw wifi option
    # Draw wifi logo
    wifi_logo = pygame.image.load_sized_svg("icons\\wifi.svg", (45, 45)).convert_alpha()
    wifi_logo.fill(primaryColor, special_flags=pygame.BLEND_RGBA_MULT)
    wifiRect1 = wifi_logo.get_rect()
    wifiRect1.center = (35, 107.5)
    screen.blit(wifi_logo, wifiRect1)
    # Load "wifi" text
    wifiText_render = font.render("Wi-Fi", False, (255, 255, 255))
    wifiTextRect1 = wifiText_render.get_rect()
    wifiTextRect1.center = (110, 112.5)
    screen.blit(wifiText_render, wifiTextRect1)

    ## Draw (another) divider line
    divLine = pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, 132.5), end_pos=(width, 132.5))

    ## Draw bluetooth option
    # Draw bluetooth logo
    bluetooth_logo = pygame.image.load_sized_svg("icons\\bluetooth.svg", (45, 45)).convert_alpha()
    bluetooth_logo.fill(primaryColor, special_flags=pygame.BLEND_RGBA_MULT)
    bluetoothRect1 = bluetooth_logo.get_rect()
    bluetoothRect1.center = (35, 157.5)
    screen.blit(bluetooth_logo, bluetoothRect1)
    # Load "bluetooth" text
    bluetoothText_render = font.render("Bluetooth", False, (255, 255, 255))
    bluetoothTextRect1 = bluetoothText_render.get_rect()
    bluetoothTextRect1.center = (145, 160)
    screen.blit(bluetoothText_render, bluetoothTextRect1)

    ## Draw (yet another) divider line
    divLine = pygame.draw.line(surface=screen, color=(255, 255, 255), start_pos=(0, 185), end_pos=(width, 185))

    ## Draw bluetooth option
    # Draw bluetooth logo
    color_logo = pygame.image.load_sized_svg("icons\\format_paint.svg", (45, 45)).convert_alpha()
    color_logo.fill(primaryColor, special_flags=pygame.BLEND_RGBA_MULT)
    colorRect1 = color_logo.get_rect()
    colorRect1.center = (35, 212.5)
    screen.blit(color_logo, colorRect1)
    # Load "color" text
    colorText_render = font.render("Colors", False, (255, 255, 255))
    colorTextRect1 = colorText_render.get_rect()
    colorTextRect1.center = (120, 215)
    screen.blit(colorText_render, colorTextRect1)

primaryColor, secondaryColor = (33, 95, 154), (22, 62, 100)
width, height = 320, 240

if pygame.IS_CE != 1: # AKA the current pygame module is NOT pygame-ce
    raise ModuleNotFoundError("Uh oh! This program expects pygame-ce, NOT regular pygame.")

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("StreamBoy \"Emulator\"")

# Initialize fonts
pygame.font.init()
font = pygame.font.SysFont("freesansbold", 30)
font_smol = pygame.font.SysFont("freesansbold", 20)


menu = "home"
selected_option = 42
option_hasBeen_selected = False
def godFunc():
    """Yes, this will be deleted later. Please tell me you didn't actually believe this was permanent?"""
    global usrInput, running, selected_option, option_hasBeen_selected
    usrInput = input("What do you want to do? (h for help): ")
    if usrInput == "quit" or usrInput == "q":
        running = False
        os._exit(0)
    elif usrInput == "l" or usrInput == "left":
        selected_option -= 1
        print(f"selected_option = {selected_option}")
    elif usrInput == "r" or usrInput == "right":
        selected_option += 1
        print(f"selected_option = {selected_option}")
    elif usrInput == "e" or usrInput == "enter":
        option_hasBeen_selected = True
        print(f"selected_option = {selected_option}, menu = {menu}")
    elif usrInput == "help" or usrInput == "h":
        print("q/quit to exit")

thready = threading.Thread(target=godFunc)
selectRect = pygame.draw.rect(screen, (255, 255, 255), (400, 400, 2, 2), 5)

# Loop
pygame.display.flip()
running = True
while running:
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))
    DrawStatusBar()
    pygame.event.pump()
    if thready.is_alive() == False:
        thready = threading.Thread(target=godFunc)
        thready.start()
    if menu == "home":
        DrawHomeMenu()
        if selected_option > 2:
            if selected_option == 42:
                pass
            else:
                selected_option = 0
        elif selected_option < 0:
            selected_option = 2
        if option_hasBeen_selected == False:
            if selected_option == 0: # Music option
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5, 60)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (69, 70, 185, 70), 5, -1)
            if selected_option == 1: # Settings option.
                if selectRect.x == 69:
                    selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5)
                else:
                    selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5, 60)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (68, 140, 90, 60), 5, 60)
            if selected_option == 2: # Apps option
                if selectRect.x == 69:
                    selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5)
                else:
                    selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5, 60)
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (162.5, 140, 90, 60), 5, 60)
        else:
            if selectRect.x == 69:
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5)
            else:
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 5, 60)
            option_hasBeen_selected = False
            if selected_option == 0: # Music option
                raise Exception("Option not implemented yet")
            if selected_option == 1: # Settings option
                menu = "settings" 
            if selected_option == 2: # Apps option
                raise Exception("Option not implemented yet")
            selected_option = 42
    elif menu == "settings":
        DrawSettingsMenu()
        if selected_option > 3:
            if selected_option == 42:
                pass
            else:
                selected_option = 0
        elif selected_option < 0:
            selected_option = 3
        if option_hasBeen_selected == False:
            if selected_option == 0: # Go back option
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 3)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (0, 40, width, 45), 3)
            elif selected_option == 1: # Wifi option
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 3)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (0, 85, width, 50), 3)
            elif selected_option == 2: # Bluetooth option
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 3)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (0, 130, width, 55), 3)
            elif selected_option == 3: # Colors option
                selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 3)
                selectRect = pygame.draw.rect(screen, (255, 255, 255), (0, 185, width, 55), 3)
        else:
            selectRect = pygame.draw.rect(screen, (0, 0, 0), (selectRect.x, selectRect.y, selectRect.w, selectRect.h), 3)
            option_hasBeen_selected = False
            if selected_option == 0: # Go back option
                menu = "home"
            if selected_option == 1: # Wifi option
                raise Exception("Option not implemented yet") 
            if selected_option == 2: # Bluetooth option
                raise Exception("Option not implemented yet")
            if selected_option == 3: # Colors option
                raise Exception("Option not implemented yet")
            selected_option = 42
    pygame.display.flip()

# Quit Pygame
pygame.quit()