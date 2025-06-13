from kivy.uix.label import Label
from kivy.utils import rgba

class RGBA:
    def __init__(self, red, green, blue, alpha):
        self.rgba = color([red, green, blue, alpha])

    def __repr__(self):
        return self.rgba

    def set_color(self, red, green, blue, alpha):
        self.rgba = rgba([red, green, blue, alpha])

class Color:
    def __init__(self, color):
        self.rgba = None
        self.set_color(color)

    def __repr__(self):
        return self.rgba

    def set_color(self, color):
        if color == 'red':
            self.rgba = RGBA(1, 0, 0, 1)
        elif color == 'green':
            self.rgba = RGBA(0, 1, 0, 1)
        elif color == 'blue':
            self.rgba = RGBA(0, 0, 1, 1)
        elif color == 'white':
            self.rgba = RGBA(1, 1, 1, 1)
        elif color == 'black':
            self.rgba = RGBA(0, 0, 0, 1)
        else:
            print(f'unknown color: {color}')

class Text:
    def __init__(self, text, color=None, rgba=None, font_size=None):
        self.text = text
        if color is not None:
            self.rgba = Color(color)
        elif rgba is not None:
            self.rgba = rgba
        else:
            self.rgba = Color('white')
        self.label = Label(text=self.text, text_color=self.rgba)

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.text