from PPlay.gameimage import GameImage
from Components.Button import *
from config import *

class OptionsScreen:
    def __init__(self):
        self.bg = GameImage("Images/bgmenutd.png")
        self.buttonBack = TextButton("Back", (200,200,200), Config.GAME_WIDTH/2, 400, True, False)

    def start(self, window, gs):
        self.draw(window)
        self.update(window, gs)
        window.set_title("Options")
        window.update()

    def draw(self, window):
        self.bg.draw()
        self.buttonBack.draw(window)

    def update(self, window, gs):
        if self.buttonBack.clicked():
            gs.enter_menu()
            window.update()
