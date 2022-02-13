#!/usr/bin/env python

"""
Python App
"""

#               IMPORTS               #
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    _/__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "1.0"
__status__ = "Development"

#              MAIN CODE              #


class WindowManager(ScreenManager):
    pass


class CalendarScreen(Screen):
    pass


class StartScreen(Screen):
    pass

kv = Builder.load_file('dogcalendar.kv')


class DogCalendar(App):
    def build(self):
        return kv


if __name__ == '__main__':
    DogCalendar().run()
