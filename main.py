from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window
Window.size = (480, 850)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

class LoginForm(BoxLayout):
    pass

class LoginApp(MDApp):
    tittle = 'lkBonchApp'

    def build(self):
        return LoginForm()

if __name__ == '__main__':
    LoginApp().run()
