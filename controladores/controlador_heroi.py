from telas.tela_heroi import TelaHeroi
from controladores.controlador_sistema import ControladorSistema
from controladores.controlador_mochila import ControladorMochila


class ControladorHeroi:
    def __init__(self, controle_sistema: ControladorSistema, controle_mochila: ControladorMochila):
        self.__herois = []
        self.__tela_heroi = TelaHeroi()
        self.__controle_sistema = controle_sistema
        self.__controle_mochila = controle_mochila

    def deletar_heroi(self):
        pass

    def abrir_tela_monstro(self):
        pass

    def abrir_mochila(self):
        pass

    def descansar(self):
        pass

    def escolher_titulo(self):
        pass
