import PySimpleGUI as interface_sistema


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.componentes_tela()
        self.componentes_logados()

    def componentes_tela(self):
        interface_sistema.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_sistema.Text('Bem vindo ao Jogo!', font=("Helvica", 25))],
            [interface_sistema.Text('Escolha sua opção', font=("Helvica", 15))],
            [interface_sistema.Radio('Login de Usuário', "RD1", key='1')],
            [interface_sistema.Radio('Cadastro de Usuário', "RD1", key='2')],
            [interface_sistema.Radio('Sobre o jogo', "RD1", key='3')],
            [interface_sistema.Radio('Encerrar o jogo', "RD1", key='0')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Cancel('Cancelar')]
        ]
        self.__window = interface_sistema.Window('Sistema de livros').Layout(layout)

    def componentes_logados(self):
        interface_sistema.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_sistema.Text('Você está logado criador!', font=("Helvica", 25))],
            [interface_sistema.Text('Qual será a Aventura?', font=("Helvica", 15))],
            [interface_sistema.Radio('Acessar Hérois Criados', "RD1", key='1')],
            [interface_sistema.Radio('Criar Novo Herói', "RD1", key='2')],
            [interface_sistema.Radio('Opções da Conta', "RD1", key='3')],
            [interface_sistema.Radio('Retornar', "RD1", key='0')],
            [interface_sistema.Button('Confirmar'), interface_sistema.Cancel('Cancelar')]
        ]
        self.__window = interface_sistema.Window('Sistema de livros').Layout(layout)

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        interface_sistema.popup("", msg)

    def mensagem(self, texto):
        return print(texto)

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
        print("----------- Você está jogando com ", heroi.nome, heroi.titulo, " -----------")
        print("1 - Atacar monstro")
        print("2 - Abrir mochila")
        print("3 - Descansar")
        print("4 - Ver status do herói")
        print("5 - Selecionar título para o herói")
        print("0 - Retornar")
        opcao = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 3, 4, 5, 0])
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
