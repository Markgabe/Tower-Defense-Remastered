from config import *
from menu import *
from PPlay.mouse import *
from Components.OptionsMenu import OptionsScreen

menu = MenuGame()
options = OptionsScreen()

while RUNNING:
    while MENU_STATE:
        menu.start(window)
        clicked = menu.whichIsClicked()

        if menu.getButtonClicked(2):
            RUNNING = False
            MENU_STATE = False
        if menu.getButtonClicked(1):
            MENU_STATE = False
            OPTIONS_STATE = True

    while OPTIONS_STATE:
        options.start(window)
    #For debuging purposes
    #print(MENU_STATE)
    #print(Mouse().get_position())
    #print(pygame.font.SysFont("Candara", 12, False, False).size("HEYHEYHEY"))
