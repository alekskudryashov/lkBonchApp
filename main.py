from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from bs4 import BeautifulSoup
import requests

from kivy.core.window import Window
Window.size = (480, 850)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

session = requests.Session()
session.get('https://lk.sut.ru/cabinet/')

def UserAuthorization(login, password):
    data = {'users': login,
            'parple': password}

    response = session.post('https://lk.sut.ru/cabinet/lib/autentificationok.php', data = data)
    isLogged = response.text

    return isLogged

class LoginForm(BoxLayout):
    def getLoginData(self):
        if UserAuthorization(self.login.text, self.password.text) == '1':
            print('Okey')
        else:
            print('Fuck')
            self.ids.password.error = True



class LoginApp(MDApp):
    tittle = 'lkBonchApp'

    def build(self):
        return LoginForm()

if __name__ == '__main__':
    LoginApp().run()
