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
        nome = None
        while nome is None:
            self.listar()
            nome = self.__tela_monstro.escolher_monstro()
            for monstro in self.__monstros:
                if monstro.nome == nome:
                    break
                    return monstro
            else:
                self.__tela_monstro.mensagem("Monstro não existente")
                return None

    def atacar(self):
        pass
