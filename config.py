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
CLOCK = pygame.time.Clock()

OPTIONS_STATE = False
RUNNING = True
MENU_STATE = True


# INITIALIZES WINDOW ___________________________________________________
window = Window(GAME_WIDTH, GAME_HEIGHT, True)
pygame.display.set_icon(pygame.image.load('Images/icon.png'))

keyboard = window.get_keyboard()
