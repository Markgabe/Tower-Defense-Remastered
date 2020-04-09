from menu import *
from config import Config
from PPlay.mouse import *
from Components.OptionsMenu import OptionsScreen
from Components.GameState import GameState
import pygame


menu = MenuGame()
options = OptionsScreen()
game_state = GameState()


while game_state.RUNNING:

    while game_state.MENU_STATE:
        menu.start(Config.window, game_state)

    while game_state.OPTIONS_STATE:
        options.start(Config.window, game_state)
