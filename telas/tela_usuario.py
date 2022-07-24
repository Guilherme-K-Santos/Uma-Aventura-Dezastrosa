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

    def tela_alteracao(self, usuario):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')
        layout = [
            [interface_usuario.Text('Novo login', size=(15, 1)), interface_usuario.InputText(usuario.login,
                                                                                             key='login_novo')],
            [interface_usuario.Text('Nova senha', size=(15, 1)), interface_usuario.InputText(usuario.senha,
                                                                                             key='senha_novo')],
            [interface_usuario.Button('Confirmar'), interface_usuario.Cancel('Cancelar')]
        ]

        self.__window = interface_usuario.Window('Alteração').Layout(layout)

    def abrir_tela_alteracao(self, usuario):
        self.tela_alteracao(usuario)
        botao, values = self.__window.Read()

        if botao in (None, 'Cancelar'):
            self.close()
        else:
            login_novo = values['login_novo']
            self.close()
            senha_nova = self.excecoes_escrita_numerica(values['senha_novo'])

            return {"login_novo": login_novo, "senha_novo": senha_nova}

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
    def janela_herois(self, tupla_herois):
        interface_usuario.ChangeLookAndFeel('DarkBlue9')
        layout_mochila = [
            [interface_usuario.Text("Escolha um herói para a aventura!")],
            [interface_usuario.InputCombo((tupla_herois), size=(20,3), key='cb_opcoes')],
            [interface_usuario.Button('Confirmar'), interface_usuario.Cancel('Cancelar')]
        ]
        self.__window = interface_usuario.Window('Heróis').Layout(layout_mochila)

    def escolhe_heroi(self, tupla):
        self.janela_herois(tupla)
        button, values = self.__window.Read()
        heroi = 0

        if values['cb_opcoes'] is not None:
            heroi = values['cb_opcoes']

        if button in (None, 'Cancelar'):
            heroi = 0

        self.close()

        return heroi


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
