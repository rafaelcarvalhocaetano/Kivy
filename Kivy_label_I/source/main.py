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

def add_lb(**args):
    lb = Label(text="Estudando a classe Label", size_hint_y = None, height = 50, **args)

    glayout.add_widget(lb)
    return lb
#font_size determina o tamanho da font
add_lb().font_size = 10

#font-name determina a fonte do texto
x = add_lb()
x.font_name = "consola"

#bold termina negrito
add_lb().bold = True

#italic determina italico
add_lb().italic = True

#determina a cor do texto
add_lb(font_size = 60).color = .1, .2, .3, 1

#desativando um label
add_lb(font_size=30).disabled = True

div = """
-------------------------------------
"""
txt = \
"""1 - aaa bbb ccc ddd
2 - aaa bbb ccc ddd
3 - aaa bbb ccc ddd
4 - aaa bbb ccc ddd"""

x = add_lb()
x.text = txt

lb = add_lb()
lb.text = txt
lb.line_height = 2

d = add_lb()
d.text = div


lb = add_lb()
lb.text = txt
lb.color = .9,.9,.1,1
lb.max_lines = 3
