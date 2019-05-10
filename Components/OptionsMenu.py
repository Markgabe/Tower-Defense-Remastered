from PPlay.gameimage import GameImage

class OptionsScreen:
    def __init__(self):
        self.bg = GameImage("Images/bgmenutd.png")

    def start(self, window):
        self.draw(window)
        window.set_title("Options")
        window.update()

    def draw(self, window):
        self.bg.draw()
