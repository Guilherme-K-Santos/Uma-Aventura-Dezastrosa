import PySimpleGUI as interface_sistema


class TelaSistema:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        interface_sistema.popup(msg)

    def mensagem(self, texto):
        return print(texto)

    def componentes_tela(self):
        interface_sistema.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_sistema.Text('Bem vindo ao Jogo!', font=("Helvica", 25))],
            [interface_sistema.Text('Escolha sua opção', font=("Helvica", 15))],
            [interface_sistema.Radio('Login de Usuário', "componentes_tela", key='1')],
            [interface_sistema.Radio('Cadastro de Usuário', "componentes_tela", key='2')],
            [interface_sistema.Radio('Sobre o jogo', "componentes_tela", key='3')],
            [interface_sistema.Radio('Encerrar o jogo', "componentes_tela", key='0')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Cancel('Cancelar')]
        ]
        self.__window = interface_sistema.Window('Uma Aventura Dezastroza').Layout(layout)

    def componentes_logados(self):
        interface_sistema.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_sistema.Text('Você está logado criador!', font=("Helvica", 25))],
            [interface_sistema.Text('Qual será a Aventura?', font=("Helvica", 15))],
            [interface_sistema.Radio('Acessar Hérois Criados', "componentes_logados", key='1')],
            [interface_sistema.Radio('Criar Novo Herói', "componentes_logados", key='2')],
            [interface_sistema.Radio('Opções da Conta', "componentes_logados", key='3')],
            [interface_sistema.Radio('Retornar', "componentes_logados", key='0')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Cancel('Cancelar')]
        ]
        self.__window = interface_sistema.Window('Menu Usuário').Layout(layout)

    def tela_inicial(self):
        self.componentes_tela()
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

    def tela_logados(self):
        self.componentes_logados()
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

#         opções para o usuário escolher (ele agora está LOGADO, então pode prosseguir
#         para acessar ou criar heróis), essa tela pode ser colocada em tela sistema também,
#         conversamos depois

    def informacoes_jogo(self):
        interface_sistema.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_sistema.Text('--------------- Bem-vindo Jogador! ---------------', font=("Helvica", 20))],
            [interface_sistema.Text('Aqui será explicado um pouco sobre o nosso RPG!', font=("Helvica", 12))],
            [interface_sistema.Text('Para começo, você deve criar a sua conta e logar!')],
            [interface_sistema.Text('Após isso, crie um herói com o nome que você quiser e embarque')],
            [interface_sistema.Text('na sua jornada épica, tomara que ela não seja dezastrosa!')],
            [interface_sistema.Button('Retornar')]
        ]
        self.__window = interface_sistema.Window('Informações do Jogo').Layout(layout)

    def abrir_tela_informacoes(self):
        self.informacoes_jogo()
        botao = self.__window.Read()

        if botao is not None:
            self.close()

    def tela_opcoes_jogo(self, heroi):
        interface_sistema.ChangeLookAndFeel('DarkBlue9')

        layout = [
            [interface_sistema.Text('Você está jogando com ' + heroi.nome + ' ' + heroi.titulo)],
            [interface_sistema.Radio('Atacar Monstro', 'tela_opcoes_jogo', key='1')],
            [interface_sistema.Radio('Abrir mochila', 'tela_opcoes_jogo', key='2')],
            [interface_sistema.Radio('Descansar', 'tela_opcoes_jogo', key='3')],
            [interface_sistema.Radio('Ver status do herói', 'tela_opcoes_jogo', key='4')],
            [interface_sistema.Radio('Selecionar título para o herói', 'tela_opcoes_jogo', key='5')],
            [interface_sistema.Radio('Retornar', 'tela_opcoes_jogo', key='0')],
            [interface_sistema.Button('Confirmar')]
        ]

        self.__window = interface_sistema.Window('Menu Jogo').Layout(layout)

    def abrir_tela_opcoes_jogo(self, heroi):
        self.tela_opcoes_jogo(heroi)

        botao, valores = self.__window.Read()

        opcao = 0
        if valores['1']:
            opcao = 1
        if valores['2']:
            opcao = 2
        if valores['3']:
            opcao = 3
        if valores['4']:
            opcao = 4
        if valores['5']:
            opcao = 5
        if valores['0']:
            opcao = 0

        self.close()

        return opcao

    def opcoes_itens(self):
        print(" 1 - Equipar")
        print(" 2 - Deletar")
        print(" 3 - Desequipar")
        print(" 0 - Retornar")
        opcao = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 3, 0])
        return opcao

    def excecoes_escrita_numerica(self, mensagem: ""):
        while True:
            valor = input(mensagem)
            try:
                valor_comparativo = int(valor)
                return valor_comparativo
            except ValueError:
                print("Por favor, coloque um valor númerico!")

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
