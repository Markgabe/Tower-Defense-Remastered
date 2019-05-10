from PPlay.gameimage import GameImage
from Components.Button import *
from config import GAME_WIDTH, GAME_HEIGHT

#-------------MENU--------------#
class MenuGame:
    def __init__(self, window):
        self.bgmenu = GameImage("Images/bgmenutdorig.jpg")
        self.bgmenu.resize(window.width, window.height)
        self.buttons = [TextButton("Play", (200,200,200), window.width/2, int(window.height*(0.65)), True, False, 40),
                        TextButton("Options", (200,200,200), window.width/2, int(window.height*(0.65)) + 50, True, False, 40),
                        TextButton("Exit", (200,200,200), window.width/2, int(window.height*(0.65)) + 100, True, False, 40)]

    def start(self, window):
        self.draw(window)
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

    def getButtonClicked(self, button):
        # 0 - Play | 1 - Options | 2 - Exit
        return self.buttons[button].clicked()

    def whichIsClicked(self):
        if self.buttons[0].clicked():
            return "play"
        elif self.buttons[1].clicked():
            return "options"
        elif self.buttons[2].clicked():
            return "exit"
        else:
            return "none"
