import PySimpleGUI as interface_heroi


class TelaHeroi:
    def __init__(self):
        self.__window = None

    def mensagem(self, texto):
        print(texto)
        input()

    def mostrar_mensagem(self, msg):
        interface_heroi.popup(msg)

    def close(self):
        self.__window.Close()

    def depois_matar_monstro(self):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_heroi.Text('Parabéns! Você matou o monstro!', font=("Helvica", 15))],
            [interface_heroi.Text('Um novo item apareceu em sua mochila, equipe-o para o próximo combate!')],
            [interface_heroi.Text('Você também ganhou um título do último monstro que você matou.')],
            [interface_heroi.Text('ATENÇÃO: Lembre-se de descansar de sua última batalha!')],
            [interface_heroi.Button('Ok')],
        ]

        self.__window = interface_heroi.Window('Parabéns').Layout(layout)

    def abrir_depois_matar_monstro(self):
        self.depois_matar_monstro()
        botao = self.__window.Read()
        self.close()
        return ''

    def depois_morrer(self):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_heroi.Text('Seu herói morreu', font=("Helvica", 15))],
            [interface_heroi.Text('Caso queira jogar novamente, crie outro herói!')],
            [interface_heroi.Text('Sua aventura foi dezastrosa :(')],
            [interface_heroi.Button('Ok')]
        ]

        self.__window = interface_heroi.Window('GAME OVER').Layout(layout)

    def abrir_depois_morrer(self):
        self.depois_morrer()
        botao = self.__window.Read()
        self.close()
        return ''

    def pegar_nome_heroi(self):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_heroi.Text('Nome do Herói'), interface_heroi.InputText('')],
            [interface_heroi.Button('Confirmar')]
        ]
        self.__window = interface_heroi.Window('Criação de Herói').Layout(layout)

    def abrir_pegar_nome_heroi(self):
        while True:
            self.pegar_nome_heroi()
            botao, nome = self.__window.Read()

            if nome[0] is None or nome[0] == '':
                self.close()
                self.mostrar_mensagem('Nome Inválido, Coloque um nome válido')
            else:
                self.close()
                return nome[0]

    def opcoes_itens(self):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_heroi.Text('O que deseja fazer com o item?', font=("Helvica", 15))],
            [interface_heroi.Radio('Equipar', "RD1", key='1')],
            [interface_heroi.Radio('Deletar', "RD1", key='2')],
            [interface_heroi.Radio('Desequipar', "RD1", key='3')],
            [interface_heroi.Radio('Retornar', "RD1", key='0')],
            [interface_heroi.Button('Confirmar'), interface_heroi.Cancel('Cancelar')]
        ]
        self.__window = interface_heroi.Window('Mochila').Layout(layout)

    def abrir_opcoes_itens(self):
        self.opcoes_itens()
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

    def janela_itens(self, tupla_itens):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')
        layout_mochila = [
            [interface_heroi.Text("Mochila", font=("Helvica", 15))],
            [interface_heroi.InputCombo(tupla_itens, size=(20,3), key='cb_opcoes')],
            [interface_heroi.Button('Escolher'), interface_heroi.Cancel('Retornar')]
        ]
        self.__window = interface_heroi.Window('Mochila').Layout(layout_mochila)

    def escolhe_item(self, tupla):
        self.janela_itens(tupla)
        button, values = self.__window.Read()
        indice = 0

        if values['cb_opcoes'] is not None:
            indice = values['cb_opcoes']

        if button in (None, 'Retornar'):
            indice = 0

        self.close()

        return indice


    def status_heroi(self, heroi):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')

        layout = [
            [interface_heroi.Text(heroi.nome, font=("Helvica", 20))],
            [interface_heroi.Text('Vida: {}'.format(heroi.hp_total))],
            [interface_heroi.Text('Ataque: {}'.format(heroi.ataque))],
            [interface_heroi.Text('Título atual: ' + heroi.titulo)],
            [interface_heroi.Text('Títulos disponíveis: {}'.format(heroi.lista_titulos))],
            [interface_heroi.Button('Ok')],
        ]

        self.__window = interface_heroi.Window('Status do Herói').Layout(layout)

    def abrir_status_heroi(self, heroi):
        self.status_heroi(heroi)
        botao = self.__window.Read()

        if botao is not None:
            self.close()

    def janela_titulos(self, tupla_titulos):
        interface_heroi.ChangeLookAndFeel('DarkBlue9')
        layout_titulos = [
            [interface_heroi.Text("Equipe um título para o herói")],
            [interface_heroi.InputCombo((tupla_titulos), size=(20,3), key='cb_opcoes')],
            [interface_heroi.Button('Confirmar'), interface_heroi.Cancel('Cancelar')]
        ]
        self.__window = interface_heroi.Window('Títulos').Layout(layout_titulos)

    def escolhe_titulo(self, tupla):
        self.janela_titulos(tupla)
        button, values = self.__window.Read()
        titulo = None

        if values['cb_opcoes'] is not None:
            titulo = values['cb_opcoes']

        if button in (None, 'Cancelar'):
            titulo = None

        self.close()

        return titulo

    def excecoes_escolha(self, mensagem: "", numeros_validos: [] = None):
        while True:
            resposta_usuario = input(mensagem)
            try:
                numero = int(resposta_usuario)
                if numero not in numeros_validos:
                    raise ValueError
                return numero
            except ValueError:
                print("Por favor, digite uma das opções:")
