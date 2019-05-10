from config import *
from menu import *
from PPlay.mouse import *
from Components.OptionsMenu import OptionsScreen

menu = MenuGame(window)
options = OptionsScreen(window)

while RUNNING:
    while MENU_STATE:
        menu.start(window)
        clicked = menu.whichIsClicked()

        if menu.getButtonClicked(2) or keyboard.key_pressed("ESC"):
            RUNNING = False
            MENU_STATE = False
        if menu.getButtonClicked(1):
            MENU_STATE = False
            OPTIONS_STATE = True
        if menu.getButtonClicked(0):
            window.set_fullscreen()

    while OPTIONS_STATE:
        options.start(window)

        if keyboard.key_pressed("ESC"):
            OPTIONS_STATE = False
            MENU_STATE = True
    #For debuging purposes
    #print(MENU_STATE)
    #print(Mouse().get_position())
    #print(pygame.font.SysFont("Candara", 12, False, False).size("HEYHEYHEY"))
