from entidades.mochila import Mochila
from telas.tela_mochila import TelaMochila


class ControladorMochila:
    def __init__(self, controlador_sistema, mochila: Mochila):
        self.__tela_mochila = TelaMochila()
        self.__mochila = mochila
        self.__itens = mochila.itens
        self.__controlador_sistema = controlador_sistema

    def escolher_item(self):
        pass

    def remover_item(self):
        pass
