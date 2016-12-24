#coding: utf-8
from kivy.app import App
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.label import Label

Config.set("graphics", "fullscreen", "0")

janela = None
glayout = None

class JanelaApp(App):
    pass

janela = JanelaApp()
ji = InteractiveLauncher(janela)
ji.run()

kvcode = """
FloatLayout:
    TextInput:
        id: text_input
        size_hint: None, None
        width: root.width
        height: root.height
"""
if(janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)

ti = glayout.ids.text_input
ti.text = "Linha 1\nLinha 2\nLinha 3"

ti.readonly = False
ti.font_name = "consola"
ti.font_size = 25
ti.foreground_color = .2,.5,.1,1
ti.tab_width = 50
ti.write_tab = False
#ti.padding = 15
ti.padding_x = 10
ti.padding_y =