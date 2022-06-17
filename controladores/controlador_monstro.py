from telas.tela_monstro import TelaMonstro


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__monstros = []
        self.__controlador_sistema = controlador_sistema

    def atacar(self):
        pass
