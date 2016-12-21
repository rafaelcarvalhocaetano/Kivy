"""
palavras reservadas

SELF - WIDGET(Aponta para o label editado)

ROOT - CLASSE(aponta para classe implementada)

APP - APLICAÇÃO(aponta para instancia da aplicação)

"""
#coding: utf-8
import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


def funcSelf(x):
    print("FUNC-SELF")

Button.funcSelf = funcSelf



class MinhaTela(BoxLayout):

    def funcRoot(self):
        print("FUNC-ROOT")



class Estudo5App(App):

    def funcApp(self):
        print("FUNC-APP")

janela = Estudo5App()
janela.run()