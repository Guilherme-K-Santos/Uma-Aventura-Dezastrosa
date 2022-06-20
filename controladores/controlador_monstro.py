from telas.tela_monstro import TelaMonstro
from entidades.monstro import Monstro
from entidades.monstro import vampiro
from entidades.monstro import mihawk
from entidades.monstro import demon_lord


class ControladorMonstro:
    def __init__(self, controlador_sistema):
        self.__tela_monstro = TelaMonstro()
        self.__monstros = [vampiro,mihawk,demon_lord]
        self.__controlador_sistema = controlador_sistema

    def listar(self):
        for monstro in self.__monstros:
            self.__tela_monstro.mensagem(monstro.nome)

    def pega_monstro(self):
        self.listar()
        nome = self.__tela_monstro.escolher_monstro()
        for monstro in self.__monstros:
            if monstro.nome == nome:
                return monstro
                break
        else:
             self.__tela_monstro.mensagem("Monstro não existente")
             return self.pega_monstro()

    def remove(self, monstro):
        self.__monstros.remove(monstro)

