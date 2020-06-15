from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.config import Config
from bs4 import BeautifulSoup
import requests


session = requests.Session()
session.get('https://lk.sut.ru/cabinet/')


def UserAuthorization(login, password):
    data = {'users': login,
            'parole': password}

    r = session.post("https://lk.sut.ru/cabinet/lib/autentificationok.php", data=data)
    return r.text


class LoginForm(BoxLayout):
    def getLoginData(self):
        auth = UserAuthorization(self.login.text, self.password.text)
        if auth == '1':
            print('Okey')
        elif auth == '0':
            print('Fuck')
            self.ids.password.error = True
        else:
            print("Well, shit.. here we go again. Bonch rip.")


class LoginApp(MDApp):
    tittle = 'lkBonchApp'
    Window.size = (480, 850)
    Config.set('kivy', 'keyboard_mode', 'systemanddock')

    def build(self):
        return LoginForm()

if __name__ == '__main__':
    LoginApp().run()