from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []

    def cadastrar(self):
        pass

    def logar(self):
        pass

    def sair(self):
        exit("Desligando o sistema.")

    def excluir(self):
        pass
