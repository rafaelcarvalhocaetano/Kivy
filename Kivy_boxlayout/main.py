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
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 50
    Button:
        size_hint: 1., 1.
        text: "A"
    Button:
        size_hint: 1., 1.
        text:"B"
    Button:
        size_hint: 1., 1.
        text:"C"
"""

if(janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)
if(glayout.orientation == "vertical"):
    glayout.orientation = "horizontal"
else:
    glayout.add_widget(Button(text="X", size_hint=(1.,1.)))