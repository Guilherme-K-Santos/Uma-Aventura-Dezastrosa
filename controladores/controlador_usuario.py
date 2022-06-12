from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = [Usuario()]

    def logar(self):
        pass

    def sair(self):
        pass

    def excluir(self):
        pass
