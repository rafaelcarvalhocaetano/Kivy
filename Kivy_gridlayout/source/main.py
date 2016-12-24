#coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder
from kivy.config import Config
Config.set("graphics", "fullscreen", "0")

janela = None
glayout = None

class JanelaApp(App):
    pass

janela = JanelaApp()
ji = InteractiveLauncher(janela)
ji.run()

kvcode = """
GridLayout:
    cols: None
    rows: 3

    row_default_height: 90
    row_force_default: True

    col_default_width: 50
    col_force_default: True

    Button:
        text: "A"
        size_hint: .1, None
    Button:
        text: "B"
    Button:
        text: "C"
    Button:
        text: "D"
        size_hint: .1, None
    Button:
        text: "E"
    Button:
        text: "F"
    Button:
        text: "G"
        size_hint: .1, None
"""

if(janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)

glayout.add_widget(Button(text="x"))