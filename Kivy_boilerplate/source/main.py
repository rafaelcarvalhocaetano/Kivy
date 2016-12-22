#coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

#forçando a app a não iniciar em tela cheia

from kivy.config import Config
Config.set("graphics", "fullscreen", "0")

janele = None
glayout = None

class JanelaApp(App):
    pass

janele = JanelaApp()
ji = InteractiveLauncher(janele)
ji.run()

kvcode ="""

BoxLayout:
    Button:
        size_hint: .1, .1
        #pos_hint: {"x": .3, "top": 1.}
        text: "A"
    Button:
        size_hint: .1, .1
        #pos_hint: {"x": .3, "top": 1.}
        text: "A"
    Button:
        size_hint: .1, .1
        #pos_hint: {"x": .3, "top": 1.}
        text: "A"
"""

if(janele.root):
    janele.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None


janele.root = glayout = Builder.load_string( kvcode )
ji.root_window.add_widget(glayout)