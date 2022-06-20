from entidades.mochila import Mochila
from telas.tela_mochila import TelaMochila

class ControladorMochila:
    def __init__(self, controlador_sistema):
        self.__tela_mochila = TelaMochila()
        self.__mochila = None
        self.__controlador_sistema = controlador_sistema
        self.__manter_tela = True


    def deleta(self,item):
        pass
    def equipa(self,item):
        pass