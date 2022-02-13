import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


# Defining a class
class DogCalendar(App):
    def build(self):
        return Label(text="Hello World !")


DogCalendar().run()
