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

def add_bt(**args):
    bt = Button(text="Estudando a classe Button",
                size_hint_y = None,
                height = 50,
                markup = True,
                **args)

    glayout.add_widget(bt)
    return bt
#font_size determina o tamanho da font
add_bt().font_size = 30

#font-name determina a fonte do texto
x = add_bt()
x.font_name = "consola"

add_bt(font_size=22).bold = True

add_bt(font_size=22).italic = True

add_bt().color = .9, .5, .3, 1

bt = add_bt()
bt.markup=True
bt.text = "Esse [b] texto [/b] possui formatação"

#event ON_PRESS

def click(bt):
    bt.text = "ON_PRESS"

def fim_click(bt):
    bt.text = "ON_RELEASE"

bt = add_bt()
#bind == ligar ou conectar
bt.bind(on_press=click)
bt.bind(on_release=fim_click)


