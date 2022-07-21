import PySimpleGUI as interface_usuario


class TelaUsuario:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def mostrar_mensagem(self, msg):
        interface_usuario.popup(msg)

    def mensagem(self, texto):
        return print(texto)

    #   -------------------------------------- OPÇÕES DO USUÁRIO --------------------------------------

    def tela_cadastro(self):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_usuario.Text('Cadastre-se para logar')],
            [interface_usuario.Text('Login', size=(15, 1)), interface_usuario.InputText('', key='login')],
            [interface_usuario.Text('Senha', size=(15, 1)), interface_usuario.InputText('',
                                                                                        key='senha')],
            [interface_usuario.Button('Confirmar'), interface_usuario.Cancel('Cancelar')]
        ]

        self.__window = interface_usuario.Window('Cadastro').Layout(layout)

    def abrir_cadastro(self):
        self.tela_cadastro()
        botao, values = self.__window.Read()

        if botao in (None, 'Cancelar'):
            self.close()
        else:
            login = values['login']
            self.close()
            senha = self.excecoes_escrita_numerica(values['senha'])
            return {"login": login, "senha": senha}

    def tela_login(self):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_usuario.Text('Login', size=(15, 1)), interface_usuario.InputText('', key='login')],
            [interface_usuario.Text('Senha', size=(15, 1)), interface_usuario.InputText('',
                                                                                        key='senha')],
            [interface_usuario.Button('Confirmar'), interface_usuario.Cancel('Cancelar')]
        ]

        self.__window = interface_usuario.Window('Login').Layout(layout)

    def abrir_login(self):
        self.tela_login()
        botao, values = self.__window.Read()

        if botao in (None, 'Cancelar'):
            self.close()
        else:
            login = values['login']
            self.close()
            senha = self.excecoes_escrita_numerica(values['senha'])
            return {"login": login, "senha": senha}

    def senha_certa(self):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')

        layout = [
            [interface_usuario.Text('Esperando uma senha válida (números inteiros):')],
            [interface_usuario.Text('Senha:', size=(15, 1)), interface_usuario.InputText(
                '', key='')],
            [interface_usuario.Button("Confirmar")]
        ]

        self.__window = interface_usuario.Window('Correção de senha').Layout(layout)

    def opcoes_usuario(self):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')

        layout = [
            [interface_usuario.Radio('Alterar Dados da Conta', "opcoes_usuario", key='1')],
            [interface_usuario.Radio('Excluir Conta', "opcoes_usuario", key='2')],
            [interface_usuario.Radio('Retornar', "opcoes_usuario", key='0')],
            [interface_usuario.Button('Confirmar'), [interface_usuario.Cancel('Cancelar')]]
        ]

        self.__window = interface_usuario.Window("Opções do Usuário").Layout(layout)

    def mostrar_opcoes_usuario(self):
        self.opcoes_usuario()
        botao, valores = self.__window.Read()

        opcao = 0
        if valores['1']:
            opcao = 1
        elif valores['2']:
            opcao = 2
        elif valores['0'] or botao in (None, 'Cancelar'):
            opcao = 0

        self.close()

        return opcao

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
        interface_usuario.ChangeLookAndFeel('DarkBlue9')

        layout = [
            [interface_usuario.Text('Tem certeza que deseja excluir sua conta com TODOS os seus heróis?')],
            [interface_usuario.Radio('Sim', 'tela_deletar_usuario', key='1'),
             interface_usuario.Radio('Não', 'tela_deletar_usuario', key='2')],
            [interface_usuario.Button('Confirmar')]
        ]

        self.__window = interface_usuario.Window('Exclusão de Conta').Layout(layout)

    def abrir_tela_deletar_usuario(self):
        self.tela_deletar_usuario()
        botao, valores = self.__window.Read()

        resposta = 2
        if valores['1']:
            resposta = 1
            self.close()
        elif valores['2']:
            resposta = 2
            self.close()

        return resposta

    #   -------------------------------------- OPÇÕES USUARIO X HEROI --------------------------------------

    def abrir_selecao_herois(self):
        print()
        print("--------------------------------------")
        print("Escreva abaixo o nome do herói que você deseja usar.")

        heroi_escolhido = input("Herói Escolhido: ")
        return heroi_escolhido

    def excecoes_escrita_numerica(self, mensagem: ""):
        try:
            valor_comparativo = int(mensagem)
            return valor_comparativo
        except ValueError:
            self.mostrar_mensagem("Por favor, coloque um valor númerico!")

        while True:
            self.senha_certa()
            botao, correcao = self.__window.Read()
            try:
                valor_comparativo = int(correcao[''])
                self.close()
                return valor_comparativo
            except ValueError:
                self.close()
                self.mostrar_mensagem("Por favor, coloque um valor númerico!")
