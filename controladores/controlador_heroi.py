from telas.tela_heroi import TelaHeroi
from entidades.heroi import Heroi


class ControladorHeroi:

    def __init__(self, heroi):
        self.__heroi = Heroi(heroi)
        self.__tela_heroi = TelaHeroi()
        self.__manter_tela = True

    def abrir_tela_opcoes(self):
        switcher = {0: self.retornar, 1: self.atacar, 2: self.descansar, 3: self.abrir_mochila, \
                    4: self.escolher_titulo()}

        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_heroi.tela_opcoes_heroi()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()

    def atacar(self):
        pass

    def abrir_mochila(self):
        pass

    def descansar(self):
        pass

    def escolher_titulo(self):
        pass

    def retornar(self):
        self.__manter_tela = False
