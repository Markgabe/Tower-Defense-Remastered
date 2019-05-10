from PPlay.gameimage import GameImage
from Components.Button import *
from config import *

#-------------MENU--------------#
class MenuGame:
    def __init__(self):
        self.bgmenu = GameImage("Images/bgmenutd.png")
        self.buttonPlay = TextButton("Play", (200,200,200), GAME_WIDTH/2, 400, True, False)
        self.buttonOptions = TextButton("Options", (200,200,200), GAME_WIDTH/2, 440, True, False)
        self.buttonExit = TextButton("Exit", (200,200,200), GAME_WIDTH/2, 480, True, False)

    def start(self, window):
        self.draw(window)
        self.update(window)
        window.set_title("Menu")
        window.update()

    def draw(self, window):
        self.bgmenu.draw()
        self.buttonPlay.draw(window)
        self.buttonOptions.draw(window)
        self.buttonExit.draw(window)

    def update(self, window):
        if self.buttonExit.clicked():
            RUNNING = False
            window.update()

        if self.buttonOptions.clicked():
            OPTIONS_STATE = True
            window.update()
