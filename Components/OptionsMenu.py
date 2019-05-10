from PPlay.gameimage import GameImage

class OptionsScreen:
    def __init__(self, window):
        self.bg = GameImage("Images/bgmenutdorig.jpg")
        self.bg.resize(window.width, window.height)

    def start(self, window):
        self.draw(window)
        window.set_title("Options")
        window.update()

    def draw(self, window):
        self.bg.draw()
