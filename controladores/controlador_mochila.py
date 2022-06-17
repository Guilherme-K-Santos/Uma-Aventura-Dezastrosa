from entidades.mochila import Mochila
from telas.tela_mochila import TelaMochila


class ControladorMochila:
    def __init__(self, controlador_sistema):
        self.__tela_mochila = TelaMochila()
        self.__mochila = Mochila()
        self.__itens = Mochila.itens
        self.__controlador_sistema = controlador_sistema

    def escolher_item(self):
        pass

    def remover_item(self):
        pass
