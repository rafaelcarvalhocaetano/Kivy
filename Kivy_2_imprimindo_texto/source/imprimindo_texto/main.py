#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text = "Rafael Carvalho"
    lb.italic = True
    lb.font_size=50
    return lb

app = App()
app.build = build
app.run()