from entidades.usuario import Usuario
from telas.tela_usuario import TelaUsuario


class ControladorUsuario:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []
        self.__manter_tela = True

    def cadastrar(self):
        dados_novos = self.__tela_usuario.tela_cadastro()

        for usuario in self.__usuarios:
            if (usuario.login == dados_novos["login"]) and \
                    usuario.senha == dados_novos["senha"]:
                self.__tela_usuario.mensagem("Usuário já existente! Faça o login para jogar")
                return None
        else:
            novo_usuario = Usuario(dados_novos["login"], dados_novos["senha"])
            self.__usuarios.append(novo_usuario)
            self.__tela_usuario.mensagem("Usuário Novo Criado! Faça o login para jogar")
            return novo_usuario

    def logar(self):
        dados = self.__tela_usuario.tela_login()

        for usuario in self.__usuarios:
            if (usuario.login == dados["login"]) and \
                    (usuario.senha == dados["senha"]):
                self.__tela_usuario.mensagem("Logado com Sucesso!")
                return usuario
        else:
            self.__tela_usuario.mensagem("Nome ou Senha invalidos!")
            return None

    def opcoes_usuario(self):
        switcher = {0: self.retornar, 1: self.alterar, 2: self.excluir}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_usuario.mostrar_opcoes_usuario()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__manter_tela = False

    def alterar(self):
        pass

    # aqui eu pego a lista de todos os usuarios atualmente cadastrados e exporto pro controlador sistema
    def pega_usuario_por_heroi(self):
        lista_usuarios = self.__usuarios

        return lista_usuarios

    def acessar_herois(self):
        pass

    def excluir(self):
        while self.__manter_tela:
            credenciais = self.__tela_usuario.tela_login()

            for usuario in self.__usuarios:
                if (usuario.login == credenciais["login"]) and \
                        usuario.senha == credenciais["senha"]:
                    resposta = self.__tela_usuario.tela_deletar_usuario()

                    if resposta == 1:
                        self.__usuarios.remove(usuario)
                        self.__tela_usuario.mensagem("Exclusão Concluída com Êxito!")
                        self.__tela_usuario.mensagem("-----------------------------")
                        self.__tela_usuario.mensagem("Você Será Redirecionado para o Menu Principal")
                        self.retornar()
                    else:
                        self.__tela_usuario.mensagem("Credenciais Incorretas!")
                        self.retornar()
                        return None
