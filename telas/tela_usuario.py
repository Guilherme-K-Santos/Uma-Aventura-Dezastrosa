import PySimpleGUI as interface_usuario


class TelaUsuario:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_mensagem(self, msg):
        interface_usuario.popup("", msg)

    def mensagem(self, texto):
        return print(texto)

    #   -------------------------------------- OPÇÕES DO USUÁRIO --------------------------------------

    def tela_cadastro(self):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_usuario.Text('------------- Cadastro -------------')],
            [interface_usuario.Text('Login', size=(15, 1)), interface_usuario.InputText('', key='login')],
            [interface_usuario.Text('Senha', size=(15, 1)), interface_usuario.InputText('',
                                                                                        key='senha')],
            [interface_usuario.Button('Confirmar'), interface_usuario.Cancel('Cancelar')]
        ]

        self.__window = interface_usuario.Window('Cadastro').Layout(layout)
        botao, values = self.__window.Read()

        login = values['login']
        senha = self.excecoes_escrita_numerica(values['senha'])

        if botao is (None, 'Cancelar'):
            self.close()
        else:
            self.close()
            return {"login": login, "senha": senha}

    def tela_login(self):
        print("--------------------------------------")
        print("Por favor, preencha com seus dados:")
        login = input("Login:")
        senha = self.excecoes_escrita_numerica("Senha:")

        return {"login": login, "senha": senha}

    def mostrar_opcoes_usuario(self):
        print("--------------------------------------")
        print("--------------Opções Do Usuário----------------")
        print("1 - Alterar Dados da Conta")
        print("2 - Excluir Conta")
        print("0 - Retornar")
        print("--------------------------------------")

        opcao_escolhida = self.excecoes_escolha("Escolha uma Opção ", [1, 2, 0])
        return opcao_escolhida

    def tela_confirmar_alteraracao(self):
        print("--------------------------------------")
        print("O que você deseja alterar em sua conta?")
        print("1 - Login")
        print("2 - Senha")

        resposta_alteracao = self.excecoes_escolha("Escolha uma Opção ", [1, 2])
        return resposta_alteracao

    # unificar alteraçao login e senha na tela grafica e fazer com que o usuario altere manualmente
    # a senha e o login ja existentes
    def tela_alteracao_login(self):
        print("--------------------------------------")
        print("Qual será o seu novo login?")
        login = input("Login:")

        return login

    def tela_alteracao_senha(self):
        print("--------------------------------------")
        print("Qual será sua nova senha?")
        senha = self.excecoes_escrita_numerica("Senha:")

        return senha

    def tela_deletar_usuario(self):
        print("--------------------------------------")
        print("Tem certeza que deseja apagar a conta?")
        print("1 - Sim")
        print("2 - Não")

        opcao_escolhida_deletar = self.excecoes_escolha("Escolha uma Opção ", [1, 2])
        return opcao_escolhida_deletar

    #   -------------------------------------- OPÇÕES USUARIO X HEROI --------------------------------------

    def abrir_selecao_herois(self):
        print()
        print("--------------------------------------")
        print("Escreva abaixo o nome do herói que você deseja usar.")

        heroi_escolhido = input("Herói Escolhido: ")
        return heroi_escolhido

    def excecoes_escrita_numerica(self, mensagem: ""):
        contador = 0
        while True:
            if contador > 0:
                self.close()
                self.tela_cadastro()
            try:
                contador += 1
                valor_comparativo = int(mensagem)
                return valor_comparativo
            except ValueError:
                self.mostrar_mensagem("Por favor, coloque um valor númerico!")

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
