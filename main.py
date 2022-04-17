#!/usr/bin/env python
"""
Python Application written with the kivy framework
Kivy documentation: https://kivy.org/
Working with WindowManager: https://kivycoder.com/multiple-windows-with-screenmanager-python-kivy-gui-tutorial-31/ - John Elder
Kivy Tutorials: https://www.youtube.com/watch?v=bMHK6NDVlCM&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn - Tech With Tim
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

from kivy.app import App
#               IMPORTS               #
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

import connect_db
import get_weather

"""
TODO MAIN
- create a callback to the app when the code has run succesfully
- Optimse the code
"""

#              MAIN CODE              #
class WindowManager(ScreenManager):
    pass

class tutorial(Screen):
    pass

class decidewalk(Screen):
    def verifyhour(self):
        hour = self.ids.Hours.text
        mins = self.ids.Minutes.text
        sec = self.ids.Seconds.text

        # check hour fields
        if hour > "24":
            popup = Popup(title='Error in "Hours" field: Make sure your format is correct 00:00:00', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif hour == "":
            popup = Popup(title='empty field(s)', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif not hour.isdigit():
            popup = Popup(title='Invalid value in "Hours" field, please try again', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass

        # check min fields
        elif mins > "59":
            popup = Popup(title='Error in "Min" field: Make sure your format is correct 00:00:00', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif mins == "":
            popup = Popup(title='empty field(s)', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif not mins.isdigit():
            popup = Popup(title='Invalid value in "Min" field, please try again', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        # check sec fields
        elif sec > "59":
            popup = Popup(title='Error in "Sec" field: Make sure your format is correct 00:00:00', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif sec == "":
            popup = Popup(title='empty field(s)', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif not sec.isdigit():
            popup = Popup(title='Invalid value in "Sec" field, please try again', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        else:
            plannedhour = f'{hour}:{mins}:{sec}'
            get_weather.weatherhourly(plannedhour)  # Find the weather for that hour
            confirmscreen(self)


class choicemenu(Screen):
    pass


class ConfirmsScreen(Screen):
    pass


class PlanningScreen(Screen, GridLayout):
    def verifyinfo(self):  # verify if the values are correct
        km = self.ids.km.text
        wandelingen = self.ids.wandeling.text
        if km == "":
            popup = Popup(title='The ''km'' field is empty!', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif wandelingen == "":
            popup = Popup(title='The ''walks'' field is empty', size_hint=(.5, .1), background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif not km.isdigit():
            popup = Popup(title='Not a valid value in the ''km'' field!', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
            pass
        elif not wandelingen.isdigit():
            popup = Popup(title='Not a valid value in the ''walks'' field!', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
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
            connect_db.insertkilometers(km)
            get_weather.getweatherrandomly(wandelingen)
            changescreen(self)


def changescreen(self):  # Change screen if values are inputted correctly
    if self.manager.current == 'planner':
        self.manager.current = 'confirm'


def confirmscreen(self):
    if self.manager.current == 'decide':
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
