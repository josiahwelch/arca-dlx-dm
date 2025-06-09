from kivy.core.text import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import importlib
class HomeScreen(Screen):
    def __init__(self, app, dlx_desktop):
        self.app = app
        self.dlx_desktop = dlx_desktop
        self.reload_mat(self.dlx_desktop)

    def toolbar_button_pressed(self, button_text):
        print(f"{button_text} button pressed!")

    def run_program(self, app_name):
        program = importlib.import_module('/dlx/applications/' + app_name.replace(' ', '_').lowercase() + '.py')
        program.main()

    def reload_mat(self, dlx_desktop):
        mat_menu = BoxLayout(orientation='vertical')
        for app in dlx_desktop.app_catalog:
            mat_entry = BoxLayout(orientation='horizontal')
            mat_entry.add_widget(Label(text=app))
            mat_entry.add_widget(Button(text='RUN', on_release=self.run_program(app)))

    def open_mat(self, app):