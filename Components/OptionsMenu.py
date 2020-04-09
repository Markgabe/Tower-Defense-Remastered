from PPlay.gameimage import GameImage
from Components.Button import *
from config import *

class OptionsScreen:
    def __init__(self, window):
        self.bg = GameImage("Images/bgmenutdorig.jpg")
        self.bg.resize(window.width, window.height)

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
