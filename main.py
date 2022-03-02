#!/usr/bin/env python
"""
Python Application written with the kivy framework
Kivy documentation: https://kivy.org/
Working with WindowManager: https://kivycoder.com/multiple-windows-with-screenmanager-python-kivy-gui-tutorial-31/ - John Elder
"""
#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "(Code version)"
__status__ = "Development"


#               IMPORTS               #
import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
import connect_db


#              MAIN CODE              #
class WindowManager(ScreenManager):
    pass


class ConfirmsScreen(Screen):
    pass


class PlanningScreen(Screen, GridLayout):
    def verifyinfo(self):   # verify if the values are correct
        km = self.ids.km.text
        wandelingen = self.ids.wandeling.text
        if km == "":
            popup = Popup(title='The ''km'' field is empty!', size_hint=(.5, .1), background_color=[0,0,0,.6])
            popup.open()
            pass
        elif wandelingen == "":
            popup = Popup(title='The ''walks'' field is empty', size_hint=(.5, .1), background_color=[0,0,0,.6])
            popup.open()
            pass
        elif not km.isdigit():
            popup = Popup(title='Not a valid value in the ''km'' field!', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif not wandelingen.isdigit():
            popup = Popup(title='Not a valid value in the ''walks'' field!', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif km == "0":
            popup = Popup(title='Lazy!', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
        elif wandelingen == "0":
            popup = Popup(title='Lazy!', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
        else:
            print(f"kilometers: {km} Wandelingen: {wandelingen}")
            connect_db.getkm(km)
            changescreen(self)


def changescreen(self): # Change screen if values are inputted correctly
    if self.manager.current == 'planner':
        self.manager.current = 'confirm'


class StartScreen(Screen):
    pass


Window.size = (400, 650)
kv = Builder.load_file('dogcalendar.kv')


class DogCalendar(App):
    def build(self):
        self.title = 'Dog Calendar'
        return kv


if __name__ == '__main__':
    DogCalendar().run()
