import pamela
from kivy.uix.screenmanager import Screen
class LoginScreen(Screen):
    def auth(self, username, password):
        """
        :param username: josiahwelch
        :param password: Josiah10
        :return: True
        """
        try:
            pamela.authenticate(username, password, service="login")
            print("PAM authentication success!")
            return True
        except pamela.PAMError as e:
            print("PAM authentication failed!")
            return False
    def login(self, app):
        if self.auth(self.ids.username.text, self.ids.password.text):
            app.root.current = "home"
            print("login success!")
            #clears password...
            self.ids.password.text = ""

        print("login failed!")
        return False