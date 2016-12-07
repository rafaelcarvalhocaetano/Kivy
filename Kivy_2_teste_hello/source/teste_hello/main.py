#conding: utf-8

from kivy.app import App
from kivy.uix.label import Label


def build():
    return Label(text = "Teste Hello World")

hello = App()
hello.build = build
hello.run()