#!/usr/bin/env python
"""
Credits:
Python Application written with the kivy framework
Kivy documentation: https://kivy.org/
Working with WindowManager: https://kivycoder.com/multiple-windows-with-screenmanager-python-kivy-gui-tutorial-31/
    - John Elder
Kivy Tutorials: https://www.youtube.com/watch?v=bMHK6NDVlCM&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn - Tech With Tim
https://kivycoder.com/kivymd-time-picker-python-kivy-gui-tutorial-52/
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
__Version__ = "0.5"
__status__ = "Development"

#               IMPORTS               #

from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import connect_db
import get_weather
import refreshtoken
import send_feedback

#              MAIN CODE              #
class WindowManager(ScreenManager):
    pass


class tutorial(Screen):
    def wipe_text_2(self):
        self.ids.confirm_options.text = ""

    def optionvars(self):
        global kilometers
        kilometers = self.ids.kilometers_default.text
        walks = self.ids.wandelingen_max.text
        self.ids.confirm_options.text = "Options saved"
        print(kilometers, walks)


class decidewalk(Screen):
    def verifyhour(self):
        global timez
        global default_kilometers
        global kilometers
        try:
            plannedhour = timez
            get_weather.weatherhourly(plannedhour)  # Find the weather for that hour
            confirmscreen(self)
        except NameError:
            popup = Popup(title="you haven't set your time!", size_hint=(.5, .1), background_color=[0, 0, 0, .8])
            popup.open()
            pass


class choicemenu(Screen):
    pass


class ConfirmsScreen(Screen):
    pass


class UserFeedback(Screen):
    def wipe_text(self):
        self.ids.confirm_feedback.text = ""

    def sendfeedback(self):
        try:
            feedback = self.ids.feedback_text.text
            self.ids.confirm_feedback.text = "Feedback sent"
            send_feedback.send_mail(feedback)
        except Exception:
            self.ids.confirm_feedback.text = "Something went wrong"



class PlanningScreen(Screen, GridLayout):
    def verifyinfo(self):  # verify if the values are correct
        km = self.ids.km.text
        wandelingen = self.ids.wandeling.text
        wandelingen_default = "5"
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
        elif wandelingen > wandelingen_default:
            popup = Popup(title='Too many walks - default is 3, check the settings', size_hint=(.5, .1),
                          background_color=[0, 0, 0, .6])
            popup.open()
            pass
        else:
            print(f"kilometers: {km} Wandelingen: {wandelingen}")
            changescreen(self)
            connect_db.insertkilometers(km)
            get_weather.getweatherrandomly(wandelingen)


def changescreen(self):  # Change screen if values are inputted correctly
    if self.manager.current == 'planner':
        self.manager.current = 'confirm'


def confirmscreen(self):
    if self.manager.current == 'decide':
        self.manager.current = 'confirm'


class StartScreen(Screen):
    def remove_text(self):
        self.ids.confirm_login.text = ""

    def gettoken(self):
        refreshtoken.refresh()
        self.ids.confirm_login.text = "Logged In"
    def logout(self):
        refreshtoken.logout()
        self.ids.confirm_login.text = "Logged Out"


class DogCalendar(MDApp):
    def build(self):
        self.title = 'Dog Calendar'
        return kv

    def get_time(self, instance, time):
        global timez
        timez = (str(time))
        return time

    def show_time_picker(self):
        try:
            time_dialog = MDTimePicker()
            time_dialog.bind(time=self.get_time)
            time_dialog.open()
        except Exception:
            pass


Window.size = (400, 650)
kv = Builder.load_file('dogcalendar.kv')


if __name__ == '__main__':
    DogCalendar().run()
