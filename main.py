from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
import requests
from bs4 import BeautifulSoup
import re
import time




s = requests.Session()
s.get("https://lk.sut.ru/cabinet/")

def login_bonch(login, password):
    data = {'users': login,
            'parole': password}

    r = s.post("https://lk.sut.ru/cabinet/lib/autentificationok.php", data = data)

    logged = r.text
    if '1' == logged:
        print("Подключено через Email: %s.." % login)
    else:
        print("Не получилось подключиться..\nВозможно вы ввели неверный логин или пароль.")



from kivy.core.window import Window
Window.size = (480, 850)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

class LoginForm(BoxLayout):
    def page_auth_get_data(self):
        login_bonch(self.login.text, self.password.text)

class LoginApp(MDApp):
    tittle = 'lkBonchApp'

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return LoginForm()

if __name__ == '__main__':
    LoginApp().run()
