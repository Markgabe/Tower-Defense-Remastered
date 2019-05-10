from PPlay.mouse import *

class TextButton:
    font = "Candara"
    x = 0
    y = 0
    def __init__(self, text, color, x, y, aligned_x="false", aligned_y="false", size = 30):
        self.text = text
        self.color = color
        self.fontSize = size
        if aligned_x:
            self.x = x - self.get_size()[0]/2
        else:
            self.x = x
        if aligned_y:
            self.y = y - self.get_size()[1]/2
        else:
            self.y = y

    def draw(self, window):
        if (self.over()):
            self.set_color((0,0,0))
        else:
            self.set_color((200,200,200))
        window.draw_text(self.text, self.x, self.y, self.fontSize, self.color, self.font)

    def set_color(self, color):
        self.color = color

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def over(self):
        return Mouse().is_over_area((self.x, self.y), (self.x + self.get_size()[0], self.y + self.get_size()[1]))

    def clicked(self):
        return (self.over() and Mouse().is_button_pressed(1))

    def get_size(self):
        return pygame.font.SysFont(self.font, self.fontSize, False, False).size(self.text)

    def move_x(self, offset):
        self.x += offset
