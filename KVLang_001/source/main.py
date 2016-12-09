#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label

class Hello(App):

    def build(self):
        return Label(text="Ola Mundo")


Hello().run()