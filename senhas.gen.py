import random
import pysimplegui as sg 
import os

class PassGen:
    def __init__(self):
        sg.theme('DarkGrey2')
        layout = [
            [sg.Text('Site', size=(10,1) ),
            sg.Input(key='site', size=(20,1))]
            [sg.Text('Usúario', size=(20,1) ),
            sg.Input(key='usuario', size=(20,1))],
            [sg.Text('Quantidade de caracteres'), 
            sg.Combo(values=list(range(30)), key='total_carcts', default_value=1,size=(3,1))],
            [sg.Output(size=(32,5))]
            [sg.Button('Gerar Senha')]       
        ]
        #Janela 
        self.janela = sg.Window('PassWord Generetor', layout)
        
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento ==sg.WINDOW_CLOSED:
                break
    def salvar_senha(self):
        pass

gen = PassGen()
gen.Iniciar()