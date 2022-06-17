from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario


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
        switcher = {0: self.retornar, 1: self.excluir, 2:self.alterar}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_usuario.mostrar_opcoes_usuario()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__manter_tela = False

    def excluir(self):
        pass

    def alterar(self):
        pass

    def pega_usuario_por_heroi(self,nome_heroi):
        for usuario in self.__usuarios:
            if nome_heroi in usuario.lista_herois:
                return None
        else:
            return usuario

  #  def confirmar_credenciais(self):
  #      while True:
  #          login, senha = self.__tela_usuario.tela_login()
  #          for usuarios in self.__usuarios:
  #              if login == usuarios.login and senha == usuarios.senha:
  #                  self.__usuarios.remove(usuarios)
  #                  self.__tela_usuario.mensagem("Exclusão Concluída com Êxito!")
  #                  self.__tela_usuario.mensagem("-----------------------------")
  #                  self.__tela_usuario.mensagem("Você Será Redirecionado para o Menu Principal")
  #                  self.__controlador_sistema.abre_tela_nao_logados()
  #          else:
  #              self.__tela_usuario.mensagem("Credenciais Incorretas!")
  #              self.__controlador_sistema.abre_tela_logados()
  #              return None
