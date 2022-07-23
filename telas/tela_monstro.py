import PySimpleGUI as interface_monstro

class TelaMonstro:

    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_mensagem(self, msg):
        interface_monstro.popup(msg)

    def mensagem(self, texto):
        return print(texto)

    def componentes_tela_monstro(self):
        interface_monstro.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_monstro.Text('Os monstros estão atacando o mundo!', font=("Helvica", 25))],
            [interface_monstro.Text('Qual o herói atacará primeiro?', font=("Helvica", 15))],
            [interface_monstro.Radio('Morbius', "componentes_tela_monstro", key='1')],
            [interface_monstro.Radio('Mihawk', "componentes_tela_monstro", key='2')],
            [interface_monstro.Radio('Lorde Demônio', "componentes_tela_monstro", key='3')],
            [interface_monstro.Radio('Retornar', "componentes_tela_monstro", key='0')],
            [interface_monstro.Button('Confirmar'), interface_monstro.Cancel('Cancelar')]
        ]
        self.__window = interface_monstro.Window('Monstro').Layout(layout)

    def escolher_monstro(self):
        self.componentes_tela_monstro()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3

        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0

        self.close()

        return opcao