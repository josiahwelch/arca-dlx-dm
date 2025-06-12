from kivy.uix.label import Label
from kivy.utils import rgba

class RGBA:
    def __init__(self, red, green, blue, alpha):
        self.rgba = rgba([red, green, blue, alpha])

    def __repr__(self):
        return self.rgba

    def set_color(self, red, green, blue, alpha):
        self.rgba = rgba([red, green, blue, alpha])

class Text:
    def __init__(self, text, color=None, font_size=None):
        self.text = text
        if color == 'red':
            self.rgba = RGBA(1, 0, 0, 1)
        elif color == 'green':
            self.rgba = RGBA(0, 1, 0, 1)
        elif color == 'blue':
            self.rgba = RGBA(0, 0, 1, 1)
