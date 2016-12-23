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
StackLayout:
    orientation: "bt-lr"
    Button:
        text:"A"
        size_hint: .33, .1
    Button:
        text:"B"
        size_hint: .33, .1
    Button:
        text:"C"
        size_hint: .33, .1

"""
if(janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)

glayout.add_widget(Button(text="X", size_hint=(.33, .1)))
#ALTERANDO A ORIENTAÇÂO
glayout.orientation = "rl-bt"