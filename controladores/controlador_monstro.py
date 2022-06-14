from telas.tela_monstro import TelaMonstro


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__monstros = []
        self.__controlador_sistema = controlador_sistema

    # alterei os parametros para o controle sistema possa acessar o controlador monstro

    def atacar(self):
        pass
