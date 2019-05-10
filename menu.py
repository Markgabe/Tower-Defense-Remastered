from PPlay.gameimage import GameImage
from Components.Button import *
from config import GAME_WIDTH

#-------------MENU--------------#
class MenuGame:
    def __init__(self):
        self.bgmenu = GameImage("Images/bgmenutd.png")
        self.buttons = [TextButton("Play", (200,200,200), GAME_WIDTH/2, 400, True, False),
                        TextButton("Options", (200,200,200), GAME_WIDTH/2, 440, True, False),
                        TextButton("Exit", (200,200,200), GAME_WIDTH/2, 480, True, False)]

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
