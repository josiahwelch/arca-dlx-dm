from kivy.app import App
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ArcaApp:
    def __init__(self, app):
        self.application = Label(text="No Application GUI Found!")
        self.app = app
        self.running = False

    def main(self):
        pass

    def run(self):
        self.main()
        self.app.ids.main_display.add_widget(self.application)

    def kill(self):
        self.app.ids.main_display.remove_widget(self.application)

    def create_layers(self, vertical=None, horizontal=None, padding=None):
        if padding is None:
            padding = 0
        else:
            padding = sp(padding)
        # sets verticality of the BoxLayout
        if vertical is None and horizontal is None:
            self.orientation = 'vertical'
            print("None!!!!!!!!!!!!!")
        elif vertical != False and horizontal != True:
            self.orientation = 'vertical'
        elif horizontal != False and vertical != True:
            vertical = False
            horizontal = True
        else:
            print('vertical and horizontal parameters cannot be the same!')
            if vertical is not type(bool) and horizontal is not type(bool):
                print('vertical and horizontal parameters must either be None, True, or False!')
            return
        self.application = BoxLayout(orientation=self.orientation, padding=padding)

    def add_layer(self, object):
        self.application.add_widget(object)