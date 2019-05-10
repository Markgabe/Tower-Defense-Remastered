from PPlay.window import *
import pygame

# OPENS FILE CONFIG ____________________________________________________
configFile = open("config.txt", "r")
config = configFile.readlines()
configFile.close()
res = config[0].split()


# SETS CONSTANTS _______________________________________________________
GAME_WIDTH = int(res[1])
GAME_HEIGHT = int(res[2])
MENU_STATE = True
OPTIONS_STATE = False
RUNNING = True
CLOCK = pygame.time.Clock()


# INITIALIZES WINDOW ___________________________________________________
window = Window(GAME_WIDTH, GAME_HEIGHT)
pygame.display.set_icon(pygame.image.load('Images/icon.png'))
