#coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
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

kvcode ="""
StackLayout:
    orientation: "tb-lr"
    padding: 50
"""
if(janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)

def add_lb(**args):
    lb = Label(size_hint_y=None,
               font_size=20,
               height=50,
               **args)
    glayout.add_widget(lb)
    return lb

add_lb(markup=True).text =\
    "[b]Estudando kivy com BBCODE[/b]"

add_lb(markup=True).text =\
    "[i]Estudando kivy com BBCODE -2[/i]"

add_lb(markup=True).text =\
    "[u]Estudando kivy com BBCODE -2[/u]"

add_lb(markup=True).text =\
    "[size=50]Estudando kivy com BBCODE -2[/size]"

add_lb(markup=True).text =\
    "[color=#ff3333]Estudando kivy com BBCODE -2[/color]"

add_lb(markup=True).text =\
    "[sup]Estudando kivy com BBCODE -2[/sup]"

add_lb(markup=True).text =\
    "[sub]Estudando kivy com BBCODE -2[/sub]"