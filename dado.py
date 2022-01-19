# simulador de dado
import random
import PySimpleGUI as sg
 
# oiiii

class SimuladorDeDado:
    
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Gostaria de jogar o dado novamente?'
        # layout
        self.layout = [
            [sg.Text('jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Nao')],
            ]
        
        
        
    def Iniciar(self):
        # criar janelas
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        # resposta = input(self.mensagem)
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos == 'Nao' or self.eventos == 'n':
                print('ok! obrigado por jogar!')
                return
            else:
                print('favor digitar sim (s) ou nao (n) ')
        except:
            print('ocorreu um erro ao receber sua resposta')    
        
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


start = SimuladorDeDado()
start.Iniciar()