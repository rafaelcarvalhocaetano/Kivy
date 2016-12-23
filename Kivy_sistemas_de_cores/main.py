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
#: import C kivy.utils.get_color_from_hex
FloatLayout:
    Button:
        size_hint: .3, .3
        pos_hint:{"center_x": .5, "center_y": .5}
        background_color:C("#FFFFFF)
        background_normal: ""
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

from kivy.utils import get_color_from_hex