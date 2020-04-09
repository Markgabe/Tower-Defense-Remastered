from PPlay.gameimage import GameImage
from Components.Button import *
from config import GAME_WIDTH, GAME_HEIGHT

#-------------MENU--------------#
class MenuGame:
    def __init__(self):
        self.bgmenu = GameImage("Images/bgmenutd.png")
        self.buttonPlay = TextButton("Play", (200,200,200), Config.GAME_WIDTH/2, 400, True, False)
        self.buttonOptions = TextButton("Options", (200,200,200), Config.GAME_WIDTH/2, 440, True, False)
        self.buttonExit = TextButton("Exit", (200,200,200), Config.GAME_WIDTH/2, 480, True, False)

    def start(self, window, gs):
        self.draw(window)
        self.update(window, gs)
        window.set_title("Menu")

    def draw(self, window):
        self.bgmenu.draw()
        for button in self.buttons:
            button.draw(window)
        window.update()

    def update(self, run, menu, options):
        if (self.getButtonClicked(2)):
            run = False
            menu = False
        elif (self.getButtonClicked(1)):
            menu = False
            options = True

    def update(self, window, gs):
        if self.buttonExit.clicked():
            gs.exit_game()
            window.update()

        if self.buttonOptions.clicked():
            gs.enter_options()
            window.update()
