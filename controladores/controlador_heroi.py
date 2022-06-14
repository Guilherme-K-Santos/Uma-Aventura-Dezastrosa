from telas.tela_heroi import TelaHeroi
from entidades.heroi import Heroi


class ControladorHeroi:
    def __init__(self, controle_sistema):
        self.__herois = []
        self.__tela_heroi = TelaHeroi()
        self.__controle_sistema = controle_sistema

    # retirei o controle mochila do controlador heroi, vamos usar o controlador sistema para ligar ambos

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
