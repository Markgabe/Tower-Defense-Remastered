from menu import *
from config import *
from PPlay.mouse import *
from Components.OptionsMenu import OptionsScreen
import pygame

menu = MenuGame()
options = OptionsScreen()
while RUNNING:
    while MENU_STATE:
        menu.start(window)
        while OPTIONS_STATE:
            options.start(window)
    #For debuging purposes
    #print(MENU_STATE)
    #print(Mouse().get_position())
    #print(pygame.font.SysFont("Candara", 12, False, False).size("HEYHEYHEY"))
