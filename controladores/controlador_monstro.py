from telas.tela_monstro import TelaMonstro


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__monstros = []
        self.__controlador_sistema = controlador_sistema

    def listar(self):
        for monstro in self.__monstros:
            self.__tela_monstro.mensagem(monstro.nome)

    def atacar(self):
        pass
