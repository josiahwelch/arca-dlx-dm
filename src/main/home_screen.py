import sys
from functools import partial
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import importlib
class HomeScreen(Screen):
    def __init__(self, app, dlx_desktop, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.dlx_desktop = dlx_desktop
        self.mat_menu = BoxLayout()
        self.reload_mat()
        self.application_running = False

    def toolbar_button_pressed(self, button_text):
        print(f"{button_text} button pressed!")

    def run_program(self, app_name, *args):
        sys.path.append('/dlx/applications')
        program = importlib.import_module(app_name.replace(' ', '_').lower())
        if self.application_running == True:
            self.application_running = False
            self.application.kill()
            self.application = None
        else:
            self.application_running = True
            self.application = program.arca_application(self)
            self.application.run()

    def reload_mat(self):
        self.mat_menu = BoxLayout(orientation='vertical')
        for app in self.dlx_desktop.app_catalog:
            if app is not None:
                mat_entry = BoxLayout(orientation='horizontal', size_hint_y=None)
                mat_entry.add_widget(Label(text=app))
                mat_entry.add_widget(Button(text='RUN', on_release=partial(self.run_program, app)))
                self.mat_menu.add_widget(mat_entry)

    def open_close_mat(self):
        if self.mat_menu in self.ids.main_display.children:
            self.ids.main_display.remove_widget(self.mat_menu)
        else:
            self.reload_mat()
            self.ids.main_display.add_widget(self.mat_menu, index=len(self.children))
