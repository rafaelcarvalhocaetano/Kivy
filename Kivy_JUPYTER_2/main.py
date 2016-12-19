#importação dos pacotes
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.interactive import InteractiveLauncher

#alteração da exibição
from kivy.config import Config
Config.set('graphics', 'fullscreen','0')

#classe da aplicação
class EstudoApp(App):
    def build(self):
        return Widget()

#criando uma instancia de estudoApp()
e = EstudoApp()
ji = InteractiveLauncher( e )
ji.run()

#adicionando Button

bt = Button(text="Rafael")
ji.root.add_widget( bt )
bt.text = ""

def bt_click():
    print("Rafael")

bt.on_press = bt_click()